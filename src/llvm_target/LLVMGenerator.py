import platform

from llvmlite import ir

from src.parser.AST import *
from src.parser.SymbolTable import *


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
            if isinstance(arg, CharNode):
                args.append(ir.Constant(ir.IntType(8), ord(arg.value)))
            elif isinstance(arg, IntNode):
                args.append(ir.Constant(ir.IntType(32), int(arg.value)))
            elif isinstance(arg, FloatNode):
                args.append(ir.Constant(ir.FloatType(), float(arg.value)))
            elif isinstance(arg, StringNode):
                c_string_type = ir.ArrayType(ir.IntType(8), len(arg.value) + 1)
                string_global = ir.GlobalVariable(self.module, c_string_type, name=f'printf_string_{self.printf_string}')
                string_global.global_constant = True
                string_global.initializer = ir.Constant(c_string_type, bytearray(arg.value + '\00', 'utf8'))
                args.append(self.builder.bitcast(string_global, ir.PointerType(ir.IntType(8))))
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

    def visit_AssignmentNode(self, node):
        var_name = node.lvalue.value
        var_ptr = self.symbol_table.get(var_name)
        value = self.visit(node.rvalue)

        self.builder.store(value, var_ptr)

    def visit_ReturnNode(self, node):
        if node.return_value is not None:
            value = self.visit(node.return_value)
            self.builder.ret(value)
        else:
            self.builder.ret_void()

    def visit_PlusNode(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[1])
        return self.builder.add(left, right)

    def visit_CharNode(self, node):
        return ir.Constant(ir.IntType(8), ord(node.value))

    def visit_IntNode(self, node):
        return ir.Constant(ir.IntType(32), int(node.value))

    def visit_FloatNode(self, node):
        return ir.Constant(ir.FloatType(), float(node.value))

    def visit_MinusNode(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[1])
        return self.builder.sub(left, right, name="tmp")

    def visit_DeclarationNode(self, node):
        # Get the type of the variable being declared
        var_type = self.visit(node.type)

        # Create an alloca instruction in the entry block of the function
        # This will reserve space for the declared variable
        alloca = self.create_entry_block_allocation(self.builder.function, node.lvalue.value)

        # Associate the variable name with its alloca instruction for future lookups
        self.symbol_table[node.lvalue.value] = alloca

        return alloca