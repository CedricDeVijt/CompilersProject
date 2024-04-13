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


done = True
definitions = {}
types = {}
# all operations with two operands
ops = ["Plus", "Minus", "Mul", "Div", "Mod", "BitwiseAnd", "BitwiseOr", "BitwiseXor", "LogicalAnd", "LogicalOr", "SL", "SR"]
# all operations with one operand
singleOps = ["PreFix", "BitwiseNot", "LogicalNot"]


def generateLLVMcodeLite(node, llvm_file, symbol_table):    # generate LLVM code using LLVM lite
    # Create module
    module = ir.Module()
    # Set the module ID
    module.module_id = ""
    # Set the target triple
    module.triple = "x86_64-pc-linux-gnu"
    # Set the target data layout
    module.data_layout = ""

    builder = None
    global done
    if isinstance(node, AST.Node):
        if isinstance(node, AST.ProgramNode):
            for child in node.children:
                generateLLVMcodeLite(child, llvm_file, symbol_table)
        elif isinstance(node, AST.MainNode):
            function = ir.Function(module, ir.FunctionType(ir.IntType(32), []), name="main")
            block = function.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            for child in node.children:
                generateLLVMfunction(child, builder)
            builder.ret(ir.Constant(ir.IntType(32), 0))
        # elif isinstance(node, AST.CommentNode):   add comment outside of function if possible

    if done:
        llvm_file.write(str(module))
        done = False


def generateLLVMfunction(node, builder):
    global definitions
    global types
    global ops

    if isinstance(node, AST.DefinitionNode):
        constant = None
        var = None
        operation(node, builder)
        """
        # check if definition is on an operation
        if node.rvalue.value in ops and len(node.rvalue.children) != 0:
            operation(node, builder)
        else:
            # add original c code as comment
            originalExpression = f"{node.type[0].value} {node.lvalue.value} = {node.rvalue.value};"
    
            # generate code
            if node.type[0].value == "int":
                builder.comment(originalExpression)
                constant = ir.Constant(ir.IntType(32), node.rvalue.value)
                var = builder.alloca(ir.IntType(32), name=node.lvalue.value)
                definitions[node.lvalue.value] = var
            elif node.type[0].value == "float":
                builder.comment(originalExpression)
                constant = ir.Constant(ir.FloatType(), float(node.rvalue.value))
                var = builder.alloca(ir.FloatType(), name=node.lvalue.value)
                definitions[node.lvalue.value] = var
            elif node.type[0].value == "char":
                originalExpression = f"{node.type[0].value} {node.lvalue.value} = {node.rvalue.value};"
                builder.comment(originalExpression)
                constant = ir.Constant(ir.IntType(8), node.rvalue.value)
                var = builder.alloca(ir.IntType(8), name=node.lvalue.value)
                definitions[node.lvalue.value] = var
            elif node.type[0].value.isnumeric():
                # handle pointers
                stars = ""
                for i in range(int(node.type[0].value)):
                    stars += "*"
                originalExpression = f"{node.type[0].type[0].value}{stars} {node.lvalue.value} = &{node.rvalue.value.value};"
                builder.comment(originalExpression)
                constant = builder.bitcast(definitions[node.rvalue.value.value], getIRpointerType(getIRtype(node.type[0].type[0].value), int(node.type[0].value)))
                var = builder.alloca(getIRpointerType(getIRtype(node.type[0].type[0].value), int(node.type[0].value)), name=node.lvalue.value)
                definitions[node.lvalue.value] = var
            types[node.lvalue.value] = node.type[0].value
            builder.store(constant, var)
        """

    elif isinstance(node, AST.AssignmentNode):
        originalExpression = f"{node.lvalue.value} = {node.rvalue.value};"
        builder.comment(originalExpression)
        builder.store(ir.Constant(getIRtype(types[node.lvalue.value]), node.rvalue.value), definitions[node.lvalue.value])

    elif isinstance(node, AST.PostFixNode):
        if node.op == "inc":
            originalExpression = f"{node.value}++;"
            builder.comment(originalExpression)
            constant = builder.add(builder.load(definitions[node.value]), ir.Constant(ir.IntType(32), 1))
        else:
            originalExpression = f"{node.value}--;"
            builder.comment(originalExpression)
            constant = builder.sub(builder.load(definitions[node.value]), ir.Constant(ir.IntType(32), 1))
        builder.store(constant, definitions[node.value])

    elif isinstance(node, AST.PreFixNode):
        if node.op == "inc":
            originalExpression = f"++{node.value};"
            builder.comment(originalExpression)
            constant = builder.add(builder.load(definitions[node.value]), ir.Constant(ir.IntType(32), 1))
        else:
            originalExpression = f"--{node.value};"
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


def operation(node, builder):
    global definitions
    builder.comment(node.original)
    var = builder.alloca(getIRtype(node.type[0].value), name=node.lvalue.value)
    definitions[node.lvalue.value] = var
    AST2 = node
    value = operationRecursive(AST2.rvalue, builder, node.type[0].value)
    builder.store(value, var)
    return False


# global var for checking if var is loaded in llvm
loaded = {}


def operationRecursive(node, builder, cType):
    # apply operation and update copy of AST
    if len(node.children) != 0:
        # if left node operation node -> recursive
        if node.children[0].value in ops:
            node.children[0] = operationRecursive(node.children[0], builder, cType)
        # if right node operation node -> recursive
        if node.children[1].value in ops:
            node.children[1] = operationRecursive(node.children[1], builder, cType)

        # apply all single operand operations first
        if node.children[0].value in singleOps:
            node.children[0] = applyOperation1operand(node.children[0], builder, cType)
        if node.children[1].value in singleOps:
            node.children[1] = applyOperation1operand(node.children[1], builder, cType)

        # apply the operation
        return applyOperation2operands(node, builder, cType)
    else:
        if node.value in singleOps:
            return applyOperation1operand(node, builder, cType)
        elif str(node.value).isalpha():
            return convertVar(builder, cType, loaded[node.value])
        else:
            return getLiteral(cType, node.value)


# apply node operation on a
def applyOperation1operand(node, builder, cType):
    if isinstance(node, ir.Instruction):
        a = node
    elif str(node.children[0].value).isalpha() and definitions[node.children[0].value] not in loaded:
        # if not loaded in llvm load it
        loaded[node.children[0].value] = builder.load(definitions[node.children[0].value])
        a = convertVar(builder, cType, loaded[node.children[0].value])
    else:
        a = getLiteral(cType, node.children[0].value)
    if isinstance(node, AST.BitwiseNotNode):
        return builder.not_(a)
    elif isinstance(node, AST.LogicalNotNode):
        return builder.not_(a)


# apply node operation on a and b
def applyOperation2operands(node, builder, cType):
    if isinstance(node.children[0], ir.Instruction):
        a = node.children[0]
    elif str(node.children[0].value).isalpha() and definitions[node.children[0].value] not in loaded:
        # if not loaded in llvm load it
        loaded[node.children[0].value] = builder.load(definitions[node.children[0].value])
        a = convertVar(builder, cType, loaded[node.children[0].value])
    else:
        a = getLiteral(cType, node.children[0].value)
    if isinstance(node.children[1], ir.Instruction):
        b = node.children[1]
    elif str(node.children[1].value).isalpha() and definitions[node.children[1].value] not in loaded:
        # if not loaded in llvm load it
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
            return ir.Constant(ir.FloatType(), value)
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
def getIRtype(Ctype):
    if Ctype == "int":
        return ir.IntType(32)
    elif Ctype == "float":
        return ir.FloatType()
    elif Ctype == "char":
        return ir.IntType(8)


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
