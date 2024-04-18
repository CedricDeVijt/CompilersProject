import src.parser.AST as AST
from llvmlite import ir


def generateLLVMcodePython(node, llvm_file, symbol_table):  # generate LLVM code using python
    if isinstance(node, AST.Node):
        if isinstance(node, AST.ProgramNode):
            for child in node.children:
                generateLLVMcodePython(child, llvm_file, symbol_table)
        elif isinstance(node, AST.MainNode):
            llvm_file.write("define i32 @main() {\n")
            llvm_file.write("entry:\n")
            for child in node.children:
                generateLLVMcodePython(child, llvm_file, symbol_table)
            llvm_file.write("    ret i32 0\n")
            llvm_file.write("}\n")
        elif isinstance(node, AST.DefinitionNode):
            pointer = False
            # Get variable name, value, and type from node
            var_name = f"%{node.lvalue.value}"
            value = node.rvalue.value
            c_type = ""  # type as in c code
            if node.type[0].value == "int":
                var_type = 'i32'
            elif node.type[0].value == "float":
                var_type = 'float'
            elif node.type[0].value == "char":
                var_type = 'i8'
                value = ord(value[1])
            else:
                # Handle pointers
                if isinstance(value, str):
                    var_type = symbol_table[f"%{value}"]
                else:
                    var_type = symbol_table[f"%{value.value}"]
                    c_type = var_type
                    if c_type == "i32":
                        c_type = "int"
                    elif c_type == "i8":
                        c_type = "char"
                for i in range(int(node.type[0].value)):
                    if i != 0:
                        var_type += '*'
                        c_type += '*'
                pointer = True
            if pointer == False and node.rvalue.value.isalpha():
                opeRation(node, llvm_file)
            else:
                # Write to output file
                if pointer:
                    llvm_file.write(f"    {var_name} = alloca {var_type}*")
                    llvm_file.write(f"  ; {c_type}* {node.lvalue.value} = &{value.value};\n")
                    llvm_file.write(f"    %addr_{value.value} = alloca {var_type}\n")
                    llvm_file.write(f"    store {var_type}* %{value.value}, {var_type}** %addr_{value.value}\n")
                    llvm_file.write(f"    %ptr_{value.value} = load {var_type}*, {var_type}** %addr_{value.value}\n")
                    llvm_file.write(f"    store {var_type}* %ptr_{value.value}, {var_type}** {var_name}\n\n")
                else:
                    llvm_file.write(f"    {var_name} = alloca {var_type}")
                    llvm_file.write(f"  ; {node.type[0].value} {node.lvalue.value} = {value};\n")
                    llvm_file.write(f"    store {var_type} {value}, {var_type}* {var_name}\n\n")
                symbol_table[var_name] = var_type

        elif isinstance(node, AST.AssignmentNode):
            # Get variable name, value, and type from node
            var_name = f"%{node.lvalue.value}"
            value = node.rvalue.value
            var_type = symbol_table[var_name]

            # Write to output file
            llvm_file.write(f"    store {var_type} {value}, {var_type}* {var_name}")
            llvm_file.write(f"  ; {node.lvalue.value} = {value};\n\n")
        elif isinstance(node, AST.PostFixNode) or isinstance(node, AST.PreFixNode):

            # Get variable name and type from node
            var_name = f"%{node.value}"
            var_type = symbol_table[var_name]

            # Write to output file
            llvm_file.write(f"    {var_name}_val = load {var_type}, {var_type}* {var_name}")
            if node.op == "inc":
                llvm_file.write(f"  ; {node.value}++\n")
                llvm_file.write(f"    {var_name}_inc = add {var_type} {var_name}_val, 1\n")
                llvm_file.write(f"    store {var_type} {var_name}_inc, {var_type}* {var_name}\n\n")
            else:
                llvm_file.write(f"  ; {node.value}--\n")
                llvm_file.write(f"    {var_name}_dec = sub {var_type} {var_name}_val, 1\n")
                llvm_file.write(f"    store {var_type} {var_name}_dec, {var_type}* {var_name}\n\n")
        elif isinstance(node, AST.CommentNode):
            # Multiline comments
            if node.value[1] == '*':
                comment = node.value[3:-6]
                c = ""
                for i in comment:
                    if i == '\n':
                        c = c[4:]
                        llvm_file.write(f"    ; {c}\n")
                        c = ""
                    else:
                        c += i
                llvm_file.write("\n")
            # Single line comments
            else:
                comment = node.value[2:]
                llvm_file.write(f"    ;{comment}\n")
        elif isinstance(node, AST.IdentifierNode):
            # No action needed for identifiers in LLVM code generation
            pass
        elif isinstance(node, AST.TypeNode):
            # No action needed for types in LLVM code generation
            pass


def opeRation(node, llvm_file):
    # load variables for operation
    op = node.rvalue.value
    var_name = node.lvalue.value
    var_type = node.type[0].value
    c_type = node.type[0].value
    if var_type == "int":
        var_type = "i32"
    x = node.rvalue.children[0].value
    y = node.rvalue.children[1].value

    # check operation
    opSymbol = ""
    opText = ""
    if op == "Plus":
        opSymbol = '+'
        opText = "add"
    elif op == "Minus":
        opSymbol = '-'
        opText = "sub"
    elif op == "Mul":
        opSymbol = '*'
        opText = "mul"
    elif op == "Div":
        opSymbol = '/'
        opText = "div"

    # write to file
    llvm_file.write(f"    %{var_name} = alloca {var_type}")
    llvm_file.write(f"  ; {c_type} {var_name} = {x}{opSymbol}{y};\n")

    # differentiate between vars and literals
    if x.isalpha():
        llvm_file.write(f"    %{x}_val = load {var_type}, {var_type}* %{x}\n")
        x = f"%{x}_val"
    if y.isalpha():
        llvm_file.write(f"    %{y}_val = load {var_type}, {var_type}* %{y}\n")
        y = f"%{y}_val"
    llvm_file.write(f"    %{opText} = {opText} {var_type} {x}, {y}\n")
    llvm_file.write(f"    store {var_type} %{opText}, {var_type}* %{var_name}\n\n")


# global vars
done = True
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

def generateLLVMcodeLite(node, llvm_file):    # generate LLVM code using LLVM lite
    # Create module
    module = ir.Module()
    # Set the module ID
    module.module_id = ""
    # Set the target triple
    module.triple = "x86_64-pc-linux-gnu"
    # Set the target data layout
    module.data_layout = ""

    global done
    if isinstance(node, AST.Node):
        if isinstance(node, AST.ProgramNode):
            for child in node.children:
                generateLLVMcodeLiteBlock(child, module)
    if done:
        llvm_file.write(str(module))
        done = False


def generateLLVMcodeLiteBlock(node, module):
    if isinstance(node, AST.FunctionNode):
        function = ir.Function(module, ir.FunctionType(ir.IntType(32), []), name=node.value)
        block = function.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        for child in node.body:
            generateLLVMfunction(module, child, builder)
        builder.ret(ir.Constant(ir.IntType(32), 0))
    elif isinstance(node, AST.CommentNode):  # add comment outside of function if possible
        # add comment to the ir module
        module.add_named_metadata("llvm.module.flags", [ir.MetaDataString(module, node.value)])
    elif isinstance(node, AST.TypedefNode):
        typedefs[node.identifier] = node.type


def generateLLVMfunction(module, node, builder):
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
        builder.comment(node.original)
        printf_ty = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
        printf_func = ir.Function(module, printf_ty, name="printf" + str(printfNumber))
        printfNumber += 1
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
            d = definitions
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
            while ptr.type != definitions[lValue].type:
                ptr = builder.load(ptr)
            return builder.load(ptr)


def operationRecursive(node, builder, cType, lValue):
    # apply operation and update copy of AST
    if len(node.children) != 0:
        # if left node operation node -> recursive
        if node.children[0].value in ops:
            node.children[0] = operationRecursive(node.children[0], builder, cType, lValue)
        # if right node operation node -> recursive
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


# apply node operation on a
def applyOperation1operand(node, builder, cType):
    if isinstance(node, ir.Instruction):
        a = node
    elif str(node.children[0].value).isalpha():
        if definitions[node.children[0].value] not in loaded:
            loaded[node.children[0].value] = builder.load(definitions[node.children[0].value])
        a = convertVar(builder, cType, loaded[node.children[0].value])
    else:
        a = getLiteral(cType, node.children[0].value)
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
        return 'unknown'

# --target_llvm
# --render_ast_png
