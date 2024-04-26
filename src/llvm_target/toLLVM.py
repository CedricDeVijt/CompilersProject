import src.parser.AST as AST
from llvmlite import ir


# global vars
# store var names with their LLVM values: {var_name: value}  int a -> {a: %"a" = alloca i32}
definitions = {}
# store var names with their types: {var_name: [type, iterations]}  char a, int** b -> {a: [char, 0], b: [int, 2]}
types = {}
# all operations with two operands
ops = ["Plus", "Minus", "Mul", "Div", "Mod", "BitwiseAnd", "BitwiseOr", "BitwiseXor", "LogicalAnd", "LogicalOr", "SL", "SR", "LT", "GT", "LTEQ", "GTEQ", "EQ", "NEQ"]
# all operations with one operand
singleOps = ["PreFix", "BitwiseNot", "LogicalNot", "Deref"]
# typedefs
typedefs = {'int': 'int', 'float': 'float', 'char': 'char'}
# printf number
printfNumber = 0
# literal nodes
literalNodes = [AST.IntNode, AST.FloatNode, AST.CharNode]
# enumerations
enums = {}


def generateLLVMcodeLite(node, llvm_file):    # generate LLVM code using LLVM lite
    # Create module
    module = ir.Module()
    # Set the module ID
    module.module_id = ""
    # Set the target triple
    module.triple = "x86_64-pc-linux-gnu"
    # Set the target data layout
    module.data_layout = ""

    if isinstance(node, AST.Node):
        if isinstance(node, AST.ProgramNode):
            for child in node.children:
                generateLLVMcodeLiteBlock(child, module)

    # Write to output file
    output = str(module)
    llvm_file.write(str(module))


def generateLLVMcodeLiteBlock(node, module):
    if isinstance(node, AST.FunctionNode):
        function = ir.Function(module, ir.FunctionType(ir.IntType(32), []), name=node.value)
        block = function.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        for child in node.body:
            generateLLVMfunction(module, function, child, builder)
        builder.ret(ir.Constant(ir.IntType(32), 0))

    elif isinstance(node, AST.CommentNode):  # add comment outside of function if possible
        # add comment to the ir module
        module.add_named_metadata("llvm.module.flags", [ir.MetaDataString(module, node.value)])

    elif isinstance(node, AST.TypedefNode):
        typedefs[node.identifier] = node.type



def generateLLVMfunction(module, function, node, builder):
    global printfNumber
    if isinstance(node, AST.DefinitionNode):
        operation(node, builder, True)

    elif isinstance(node, AST.AssignmentNode):
        operation(node, builder, False)

    elif isinstance(node, AST.PostFixNode):
        if node.op == "inc":
            originalExpression = f"{node.value}++"
            builder.comment(originalExpression)
            constant = builder.add(builder.load(definitions[node.value]), ir.Constant(ir.IntType(32), 1))
        else:
            originalExpression = f"{node.value}--"
            builder.comment(originalExpression)
            constant = builder.sub(builder.load(definitions[node.value]), ir.Constant(ir.IntType(32), 1))
        builder.store(constant, definitions[node.value])

    elif isinstance(node, AST.PreFixNode):
        if node.op == "inc":
            originalExpression = f"++{node.value}"
            builder.comment(originalExpression)
            constant = builder.add(builder.load(definitions[node.value]), ir.Constant(ir.IntType(32), 1))
        else:
            originalExpression = f"--{node.value}"
            builder.comment(originalExpression)
            constant = builder.sub(builder.load(definitions[node.value]), ir.Constant(ir.IntType(32), 1))
        builder.store(constant, definitions[node.value])

    elif isinstance(node, AST.CommentNode):
        # multi line comments
        if node.value[1] == '*':
            comment = node.value[2:-6]
            c = ""
            firstLine = True
            for i in range(len(comment)):
                if comment[i] == '\n':
                    # cut unnecessary spaces
                    if firstLine:
                        firstLine = False
                    else:
                        c = c[4:]
                    builder.comment(c)
                    c = ""
                else:
                    c += comment[i]
        else:
            # single line comments
            comment = node.value[2:]
            builder.comment(comment)

    elif isinstance(node, AST.PrintfNode):
        # printf
        builder.comment(node.original)
        printf_ty = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
        printf_func = ir.Function(module, printf_ty, name="printf" + str(printfNumber))
        if node.specifier[2] == 'd':
            cType = "int"
        elif node.specifier[2] == 'f':
            cType = "float"
        elif node.specifier[2] == 'c':
            cType = "char"
        if isinstance(node.node, AST.IdentifierNode):
            a = builder.load(definitions[node.node.value])
        else:
            a = getLiteral(cType, node.node.value)
        builder.call(printf_func, [ir.GlobalVariable(module, ir.ArrayType(ir.IntType(8), len(node.specifier)), name=".str" + str(printfNumber)).gep(
            (ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0))), a])
        printfNumber += 1

    elif isinstance(node, AST.IfStatementNode):
        # if else statement
        builder.comment(node.original)

        # define statement block
        ifThenBlock = function.append_basic_block(name="if.then")
        ifEndBlock = function.append_basic_block(name="if.end")

        # perform comparison
        comparisonResult = operationRecursive(node.condition, builder, "int", 0)

        # Conditional branch based on the result of the comparison
        builder.cbranch(comparisonResult, ifThenBlock, ifEndBlock)

        # Define the if-then block
        builder.position_at_start(ifThenBlock)

        # Perform statement content
        for child in node.body:
            generateLLVMfunction(module, function, child, builder)

        # Branch to the end of the if-else block
        builder.branch(ifEndBlock)

        # Define the if-end block
        builder.position_at_start(ifEndBlock)

    elif isinstance(node, AST.WhileLoopNode):
        # while loop
        builder.comment(node.original)

        # Define conditional branches
        loopBlock = function.append_basic_block(name="loop")
        exitBlock = function.append_basic_block(name="exit")

        # Branch to the loop block
        builder.branch(loopBlock)

        # Set the builder to the loop block
        builder.position_at_end(loopBlock)

        # Perform statement content
        for child in node.body:
            if isinstance(child, AST.BreakNode):
                builder.branch(exitBlock)
                continue
            elif isinstance(child, AST.ContinueNode):
                builder.branch(loopBlock)
                continue
            generateLLVMfunction(module, function, child, builder)

        # perform comparison
        comparisonResult = operationRecursive(node.condition, builder, "int", 0)

        # Conditional branch based on the comparison result
        builder.cbranch(comparisonResult, loopBlock, exitBlock)

        # Set the builder to the exit block
        builder.position_at_end(exitBlock)


def operation(node, builder, defOrAssigment):
    global definitions
    # original c comment
    builder.comment(node.original)
    # create LLVM variable
    if defOrAssigment:
        # create var for definition
        if node.type[0].value.isnumeric():
            var = builder.alloca(getLLVMtype(typedefs[types[node.rvalue.value.value][0]], int(node.type[0].value)), name=node.lvalue.value)
            types[node.lvalue.value] = [typedefs[types[node.rvalue.value.value][0]], node.type[0].value]
        else:
            var = builder.alloca(getLLVMtype(typedefs[node.type[0].value], 0), name=node.lvalue.value)
            types[node.lvalue.value] = [typedefs[node.type[0].value], 0]
    else:
        # create var for assigment
        var = definitions[node.lvalue.value]
    definitions[node.lvalue.value] = var
    # create LLVM value
    if node.rvalue.value in ops:
        AST2 = node
        value = operationRecursive(AST2.rvalue, builder, typedefs[types[node.lvalue.value][0]], node.lvalue.value)
    else:
        if types[node.lvalue.value][1] != 0:
            value = builder.bitcast(definitions[node.rvalue.value.value], getLLVMtype(typedefs[types[node.lvalue.value][0]], int(types[node.lvalue.value][1])))
        else:
            value = definition(node, builder, typedefs[types[node.lvalue.value][0]], 0, True)
    loaded[node.lvalue.value] = value
    builder.store(value, var)
    return False


# global var for checking if var is loaded in llvm
loaded = {}


# get LLVM value
def definition(node, builder, cType, lValue, varLit):
    if varLit:
        # get value
        if node.rvalue.value in singleOps:
            # apply single operand operation: !a, ~a, ++a, --a
            return applyOperation1operand(node.rvalue, builder, cType)
        elif isinstance(node.rvalue, AST.DerefNode):
            # dereference pointer: *a, **a
            ptr = builder.load(definitions[node.rvalue.identifier.value])
            while ptr.type != definitions[node.lvalue.value].type:
                ptr = builder.load(ptr)
            return builder.load(ptr)
        elif str(node.rvalue.value).isalpha():
            # load variable
            return convertVar(builder, cType, loaded[node.rvalue.value])
        else:
            # get literal value
            return getLiteral(cType, node.rvalue.value)
    else:
        # only perform operation and dereference pointer
        if node.value in singleOps:
            # apply single operand operation: !a, ~a, ++a, --a
            return applyOperation1operand(node, builder, cType)
        elif isinstance(node, AST.DerefNode):
            # dereference pointer
            ptr = builder.load(definitions[node.identifier.value])
            while ptr.type != ir.PointerType(ir.IntType(32)):
                ptr = builder.load(ptr)
            return builder.load(ptr)


def operationRecursive(node, builder, cType, lValue):
    # apply operation and update copy of AST
    if len(node.children) == 2:
        # if left node operation node -> recursive
        if not isinstance(node.children[0], ir.Instruction):
            if node.children[0].value in ops:
                node.children[0] = operationRecursive(node.children[0], builder, cType, lValue)
        # if right node operation node -> recursive
        if not isinstance(node.children[1], ir.Instruction):
            if node.children[1].value in ops:
                node.children[1] = operationRecursive(node.children[1], builder, cType, lValue)

        # apply all single operand operations first
        if not isinstance(node.children[0], ir.Instruction):
            if node.children[0].value in singleOps or isinstance(node.children[0], AST.DerefNode):
                node.children[0] = definition(node.children[0], builder, cType, lValue, False)
        if not isinstance(node.children[1], ir.Instruction):
            if node.children[1].value in singleOps or isinstance(node.children[1], AST.DerefNode):
                node.children[1] = definition(node.children[1], builder, cType, lValue, False)

        # apply the operation
        return applyOperation2operands(node, builder, cType)
    else:
        if node.value in singleOps:
            # apply single operand operation: !a, ~a, ++a, --a
            return applyOperation1operand(node, builder, cType)
        else:
            # get value
            if isinstance(node, AST.DefinitionNode):
                loaded[node.children[0].value] = builder.load(definitions[node.children[0].value])
                a = convertVar(builder, cType, loaded[node.value])
            else:
                a = getLiteral(cType, node.value)
            return a


# apply node operation on a
def applyOperation1operand(node, builder, cType):
    if isinstance(node, ir.Instruction):
        a = node
    elif isinstance(node.children[0], AST.IdentifierNode):
        if definitions[node.children[0].value] not in loaded:
            loaded[node.children[0].value] = builder.load(definitions[node.children[0].value])
        a = convertVar(builder, cType, loaded[node.children[0].value])
    elif type(node.children[0]) in literalNodes:
        a = getLiteral(cType, node.children[0].value)
    else:
        a = operationRecursive(node.children[0], builder, cType, node.value)
    if isinstance(node, AST.BitwiseNotNode):
        return builder.not_(a)
    elif isinstance(node, AST.LogicalNotNode):
        return builder.not_(a)
    elif isinstance(node, AST.PreFixNode):
        if node.op == "inc":
            return builder.add(a, ir.Constant(ir.IntType(32), 1))
        elif node.op == "dec":
            return builder.sub(a, ir.Constant(ir.IntType(32), 1))
    elif isinstance(node, AST.DerefNode):
        return builder.load(a)


# apply node operation on a and b
def applyOperation2operands(node, builder, cType):
    if isinstance(node.children[0], ir.Instruction):
        a = node.children[0]
    elif str(node.children[0].value).isalpha():
        if definitions[node.children[0].value] not in loaded:
            loaded[node.children[0].value] = builder.load(definitions[node.children[0].value])
        a = convertVar(builder, cType, loaded[node.children[0].value])
    else:
        a = getLiteral(cType, node.children[0].value)
    if isinstance(node.children[1], ir.Instruction):
        b = node.children[1]
    elif str(node.children[1].value).isalpha():
        if definitions[node.children[1].value] not in loaded:
            loaded[node.children[1].value] = builder.load(definitions[node.children[1].value])
        b = convertVar(builder, cType, loaded[node.children[1].value])
    else:
        b = getLiteral(cType, node.children[1].value)

    # apply operation
    if isinstance(node, AST.PlusNode):
        return builder.add(a, b)
    elif isinstance(node, AST.MinusNode):
        return builder.sub(a, b)
    elif isinstance(node, AST.MultNode):
        return builder.mul(a, b)
    elif isinstance(node, AST.DivNode):
        return builder.sdiv(a, b)
    elif isinstance(node, AST.ModNode):
        return builder.srem(a, b)
    elif isinstance(node, AST.BitwiseAndNode):
        return builder.and_(a, b)
    elif isinstance(node, AST.BitwiseOrNode):
        return builder.or_(a, b)
    elif isinstance(node, AST.BitwiseNotNode):
        return builder.not_(a, b)
    elif isinstance(node, AST.BitwiseXorNode):
        return builder.xor(a, b)
    elif isinstance(node, AST.LogicalAndNode):
        return builder.and_(a, b)
    elif isinstance(node, AST.LogicalOrNode):
        return builder.or_(a, b)
    elif isinstance(node, AST.LogicalNotNode):
        return builder.not_(a, b)
    elif isinstance(node, AST.SLNode):
        return builder.shl(a, b)
    elif isinstance(node, AST.SRNode):
        return builder.ashr(a, b)
    elif isinstance(node, AST.LTNode):
        return builder.zext(builder.icmp_signed("<", a, b), ir.IntType(32))
    elif isinstance(node, AST.GTNode):
        return builder.zext(builder.icmp_signed(">", a, b), ir.IntType(32))
    elif isinstance(node, AST.LTEQNode):
        return builder.zext(builder.icmp_signed("<=", a, b), ir.IntType(32))
    elif isinstance(node, AST.GTEQNode):
        return builder.zext(builder.icmp_signed(">=", a, b), ir.IntType(32))
    elif isinstance(node, AST.EQNode):
        return builder.zext(builder.icmp_signed("==", a, b), ir.IntType(32))
    elif isinstance(node, AST.NEQNode):
        return builder.zext(builder.icmp_signed("!=", a, b), ir.IntType(32))


# get llvm literal using cType and literal value
def getLiteral(cType, value):
    valueType = checkDataType(value)
    if cType == "int":
        if valueType == "int":
            return ir.Constant(ir.IntType(32), value)
        elif valueType == "float":
            return ir.Constant(ir.IntType(32), int(float(value)))
        elif valueType == "char":
            return ir.Constant(ir.IntType(32), ord(value))
    elif cType == "float":
        if valueType == "int":
            return ir.Constant(ir.FloatType(), float(value))
        elif valueType == "float":
            return ir.Constant(ir.FloatType(), float(value))
        elif valueType == "char":
            return ir.Constant(ir.FloatType(), float(ord(value)))
    elif cType == "char":
        if valueType == "int":
            return ir.Constant(ir.IntType(8), value)
        elif valueType == "float":
            return ir.Constant(ir.IntType(8), int(value))
        elif valueType == "char":
            return ir.Constant(ir.IntType(8), value)


# convert variable to operation lvalue type
def convertVar(builder, cType, value):
    if cType == "int":
        if value.type == ir.IntType(32):
            return value
        elif value.type == ir.FloatType():
            return builder.fptosi(value, ir.IntType(32))
        elif value.type == ir.IntType(8):
            return builder.zext(value, ir.IntType(32))
    elif cType == "float":
        if value.type == ir.IntType(32):
            return builder.sitofp(value, ir.FloatType())
        elif value.type == ir.FloatType():
            return value
        elif value.type == ir.IntType(8):
            return builder.uitofp(value, ir.FloatType())
    elif cType == "char":
        if value.type == ir.IntType(32):
            return builder.trunc(value, ir.IntType(8))
        elif value.type == ir.FloatType():
            return builder.trunc(builder.fptosi(value, ir.IntType(32)), ir.IntType(8))
        elif value.type == ir.IntType(8):
            return value


# get llvm type from cType
def getLLVMtype(cType, iterations):
    if iterations == 0:
        if cType == "int":
            return ir.IntType(32)
        elif cType == "float":
            return ir.FloatType()
        elif cType == "char":
            return ir.IntType(8)
    else:
        return getIRpointerType(getLLVMtype(cType, 0), iterations)


# get llvm pointer type from cType and iterations
def getIRpointerType(type, iterations):
    if iterations > 0:
        return ir.PointerType(getIRpointerType(type, iterations-1))
    else:
        return type


def checkDataType(x):
    def is_integer(x):
        try:
            int(x)
            return True
        except ValueError:
            return False

    def is_float(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def is_char(x):
        return len(x) == 1

    if is_integer(x):
        return 'int'
    elif is_float(x):
        return 'float'
    elif is_char(x):
        return 'char'
    else:
        return 'string'

# --target_llvm
# --render_ast_png
