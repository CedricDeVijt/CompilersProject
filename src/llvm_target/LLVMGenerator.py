import platform

from llvmlite import ir

from src.parser.AST import *
from src.parser.SymbolTable import *

unary_ops = {'LogicalNotNode', 'BitwiseNotNode'}
binary_ops = {'DivNode', 'ModNode', 'MultNode', 'MinusNode', 'PlusNode', 'GTNode', 'LTNode', 'GTEQNode', 'LTEQNode', 'EQNode', 'NEQNode', 'SLNode', 'SRNode', 'BitwiseAndNode', 'BitwiseOrNode', 'BitwiseXorNode', 'LogicalAndNode', 'LogicalOrNode'}

def get_highest_type(node1, node2):
    if node1.type == ir.FloatType() or node2.type == ir.FloatType():
        return ir.FloatType()
    if node1.type == ir.IntType(32) or node2.type == ir.IntType(32):
        return ir.IntType(32)
    if node1.type == ir.IntType(8) or node2.type == ir.IntType(8):
        return ir.IntType(8)

class LLVMVisitor:
    def __init__(self, stdio=False):
        self.builder = None
        self.scope = SymbolTableTree()
        self.module = ir.Module()
        self.module.triple = f"{platform.machine()}-pc-{platform.system().lower()}"
        self.printf_string = 0
        # Add printf and scanf function
        if stdio:
            function_type = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
            function = ir.Function(self.module, function_type, name='printf')

            self.builder = function

    def visit(self, node):
        if node.__class__.__name__ in unary_ops:
            return self.visit_UnaryOp(node)
        if node.__class__.__name__ in binary_ops:
            return self.visit_BinaryOp(node, f"visit_{node.__class__.__name__}")
        method_name = "visit_" + node.__class__.__name__
        _visitor = getattr(self, method_name, self.generic_visit)
        return _visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{node.__class__.__name__} method defined")

    @staticmethod
    def create_entry_block_allocation(function, var_name):
        builder = ir.IRBuilder(function.append_basic_block(name="entry"))
        return builder.alloca(ir.IntType(32), name=var_name)

    def visit_ProgramNode(self, node):
        for child in node.children:
            self.visit(child)

    def visit_PrintfNode(self, node):
        specifier = node.specifier
        specifier += '\00'
        j = 0
        while j < len(specifier) - 1:
            if specifier[j] == '\\':
                next_symbol = specifier[j + 1]
                if next_symbol == '\\':
                    specifier = specifier[:j] + '\\' + specifier[j + 2:]
                elif next_symbol == 'n':
                    specifier = specifier[:j] + '\n' + specifier[j + 2:]
                elif next_symbol == 't':
                    specifier = specifier[:j] + '\t' + specifier[j + 2:]
                elif next_symbol == '\'':
                    specifier = specifier[:j] + '\'' + specifier[j + 2:]
                elif next_symbol == '\"':
                    specifier = specifier[:j] + '\"' + specifier[j + 2:]
            j += 1
        # Create Global Variable For Format String.
        c_string_type = ir.ArrayType(ir.IntType(8), len(specifier))
        format_string_global = ir.GlobalVariable(self.module, c_string_type, name=f'printf_string_{self.printf_string}')
        format_string_global.global_constant = True
        format_string_global.initializer = ir.Constant(c_string_type, bytearray(specifier, 'utf8'))
        self.printf_string += 1

        # Call Printf Function.
        args = [self.builder.bitcast(format_string_global, ir.PointerType(ir.IntType(8)))]
        for arg in node.children:
            args.append(self.visit(arg))
            if isinstance(arg, StringNode):
                self.printf_string += 1
        self.builder.call(self.module.get_global('printf'), args)
        self.printf_string += 1

    def visit_FunctionNode(self, node):
        # Open new scope.
        self.scope.open_scope()
        # Add arguments to scope.
        # Add params
        for param in node.params:
            param_type = param[0]
            param_name = param[1]
            const = False
            # Get name
            if isinstance(param_name, IdentifierNode):
                param_name = param_name.value
            elif isinstance(param_name, AddrNode):
                param_name = param_name.value.value
            # Get type
            if isinstance(param_type, PointerNode):
                param_type = param_type.type
            if isinstance(param_type, list):
                const = True
                param_type = param_type[len(param_type) - 1]
            param_type = param_type.value
            symbol = Symbol(name=param_name, var_type=param_type, const=const, symbol_type='variable', defined=True,
                            params=None)
            #symbol.alloca =
            symbol = Symbol(name=param_name, var_type=param_type, const=const, symbol_type='variable', defined=True, params=None)
            symbols = self.scope.get_symbol(name=param_name)
            if not symbols:
                self.scope.add_symbol(symbol)
        # Arguments.
        args = []
        for param in node.params:
            if isinstance(param, list):
                param_type = param[len(param) - 2]
                if isinstance(param_type, TypeNode):
                    if param_type.value == 'char':
                        args.append(ir.IntType(8))
                    elif param_type.value == 'int':
                        args.append(ir.IntType(32))
                    elif param_type.value == 'float':
                        args.append(ir.FloatType())
                    elif param_type.value == 'void':
                        args.append(ir.VoidType())
                elif isinstance(param_type, PointerNode):
                    ...
        # Function type.
        function_type = ir.FunctionType(ir.VoidType(), args)
        func_type = node.type
        if isinstance(func_type, list):
            func_type = func_type[len(func_type) - 1]
        if isinstance(func_type, TypeNode):
            if func_type.value == 'char':
                function_type = ir.FunctionType(ir.IntType(8), args)
            elif func_type.value == 'int':
                function_type = ir.FunctionType(ir.IntType(32), args)
            elif func_type.value == 'float':
                function_type = ir.FunctionType(ir.FloatType(), args)
            elif func_type.value == 'void':
                function_type = ir.FunctionType(ir.VoidType(), args)
        elif isinstance(func_type, PointerNode):
            ...
        function = ir.Function(self.module, function_type, name=node.value)


        entry_block = function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        # Visit function body
        for statement in node.body:
            self.builder.comment(statement.original)
            self.visit(statement)

        # Close scope.
        self.scope.close_scope()

    def visit_FunctionCallNode(self, node):
        args = []
        for arg in node.arguments:
            args.append(self.visit(arg))
        return self.builder.call(self.module.get_global(node.value), args)

    def visit_ifStatementNode(self, node):
        # open scope
        self.scope.open_scope()

        # close scope
        self.scope.close_scope()

    def visit_DefinitionNode(self, node):
        # definition vars
        var_name = node.lvalue.value
        var_type = node.type[0].value
        value = self.convert(var_type, node)
        var_ptr = self.builder.alloca(value.type, name=var_name)
        # add to symbol table
        symbol = Symbol(name=var_name, var_type=var_type)
        symbol.alloca = var_ptr
        if self.scope.get_symbol(name=var_name) is None:
            self.scope.add_symbol(symbol)
        self.builder.store(value, var_ptr)

    def visit_AssignmentNode(self, node):
        var_name = node.lvalue.value
        var_type = self.scope.get_symbol(name=var_name).type
        value = self.convert(var_type, node)
        var_ptr = self.scope.get_symbol(name=var_name).alloca
        self.builder.store(value, var_ptr)

    def convert(self, var_type, node):    # var_type = cType in string: 'int'    value = value: 10)
        if var_type == "int":
            if isinstance(node.rvalue, IntNode):
                return ir.Constant(ir.IntType(32), node.rvalue.value)
            elif isinstance(node.rvalue, FloatNode):
                return ir.Constant(ir.IntType(32), int(float(node.rvalue.value)))
            elif isinstance(node.rvalue, CharNode):
                return ir.Constant(ir.IntType(32), node.rvalue.value)
        elif var_type == "float":
            if isinstance(node.rvalue, IntNode):
                return ir.Constant(ir.FloatType(), float(node.rvalue.value))
            elif isinstance(node.rvalue, FloatNode):
                print(node.rvalue.value)
                return ir.Constant(ir.FloatType(), float(node.rvalue.value))
            elif isinstance(node.rvalue, CharNode):
                return ir.Constant(ir.FloatType(), float(ord(node.rvalue.value)))
        elif var_type == "char":
            if isinstance(node.rvalue, IntNode):
                return ir.Constant(ir.IntType(8), node.rvalue.value)
            elif isinstance(node.rvalue, FloatNode):
                return ir.Constant(ir.IntType(8), int(node.rvalue.value))
            elif isinstance(node.rvalue, CharNode):
                return ir.Constant(ir.IntType(8), node.rvalue.value)

    def visit_ReturnNode(self, node):
        if node.return_value is not None:
            value = self.visit(node.return_value)
            self.builder.ret(value)
        else:
            self.builder.ret_void()

    # literals
    def visit_IntNode(self, node):
        return ir.Constant(ir.IntType(32), int(node.value))

    def visit_CharNode(self, node):
        return ir.Constant(ir.IntType(8), ord(int(node.value)))

    def visit_FloatNode(self, node):
        return ir.Constant(ir.FloatType(), float(node.value))

    def visit_StringNode(self, node):
        c_string_type = ir.ArrayType(ir.IntType(8), len(node.value))
        string_global = ir.GlobalVariable(self.module, c_string_type, name=f'string_{self.printf_string}')
        string_global.global_constant = True
        string_global.initializer = ir.Constant(c_string_type, bytearray(node.value, 'utf8'))
        self.printf_string += 1
        return self.builder.bitcast(string_global, ir.PointerType(ir.IntType(8)))

    # operations
    def visit_UnaryOp(self, node):
        if isinstance(node, BitwiseNotNode):
            return self.builder.not_(self.visit(node.children[0]))
        # TODO: FIX
        return self.builder.neg(self.visit(node.children[0]))

    def visit_BinaryOp(self, node, method):
        child1 = self.visit(node.children[0])
        child2 = self.visit(node.children[1])
        if child1.type != child2.type:
            child1.type = get_highest_type(child1, child2)
            child2.type = get_highest_type(child1, child2)
        _visitor = getattr(self, method, self.generic_visit)
        return _visitor(node, [child1, child2])

    def visit_PlusNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.add(left, right)

    def visit_MinusNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.sub(left, right, name="tmp")

    def visit_MultNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.mul(left, right)

    def visit_DivNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if children[0].type == ir.FloatType():
            return self.builder.fdiv(left, right)
        return self.builder.sdiv(left, right)

    def visit_ModNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.srem(left, right)

    def visit_BitwiseAndNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.and_(left, right)

    def visit_BitwiseOrNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.or_(left, right)

    def visit_BitwiseNotNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.xor(left, right)

    def visit_LogicalAndNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.and_(left, right)

    def visit_LogicalOrNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.or_(left, right)

    def visit_LogicalNotNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.shl(left, right)

    def visit_SRNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.ashr(left, right)

    def visit_LTNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.zext(self.builder.icmp_signed("<", left, right), ir.IntType(32))

    def visit_GTNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.zext(self.builder.icmp_signed(">", left, right), ir.IntType(32))

    def visit_LTEQNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.zext(self.builder.icmp_signed("<=", left, right), ir.IntType(32))

    def visit_GTEQNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.zext(self.builder.icmp_signed(">=", left, right), ir.IntType(32))

    def visit_EQNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.zext(self.builder.icmp_signed("==", left, right), ir.IntType(32))

    def visit_NEQNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.zext(self.builder.icmp_signed("!=", left, right), ir.IntType(32))

    def visit_DeclarationNode(self, node):
        # Get the type of the variable being declared
        var_type = self.visit(node.type)

        # Create an alloca instruction in the entry block of the function
        # This will reserve space for the declared variable
        alloca = self.create_entry_block_allocation(self.builder.function, node.lvalue.value)

        # Associate the variable name with its alloca instruction for future lookups
        self.symbol_table[node.lvalue.value] = alloca

        return alloca

    def visit_IdentifierNode(self, node):
        # Load the value from the alloca
        return self.builder.load(self.scope.get_symbol(name=node.value).alloca)
