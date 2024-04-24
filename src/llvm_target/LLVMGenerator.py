import platform

from llvmlite import ir

from src.parser.AST import *


class LLVMVisitor:
    def __init__(self):
        self.builder = None
        self.symbol_table = {}
        self.module = ir.Module()
        self.module.triple = f"{platform.machine()}-pc-{platform.system().lower()}"

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

    def visit_FunctionNode(self, node):
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

    def visit_FunctionCallNode(self, node):
        args = []
        for arg in node.arguments:
            args.append(self.visit(arg))
        return self.builder.call(self.module.get_global(node.value), args)

    def visit_IdentifierNode(self, node):
        return self.symbol_table.get(node.value)

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
        return self.builder.add(left, right, name="tmp")

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
