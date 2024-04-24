import platform

from llvmlite import ir

from src.llvm_target.toLLVM import definitions
from src.parser.AST import *


class LLVMVisitor:
    def __init__(self, symbol_table):
        self.builder = None
        self.symbol_table = symbol_table
        self.module = ir.Module()
        self.module.triple = f"{platform.machine()}-pc-{platform.system().lower()}"
        self.ops = ["Plus", "Minus", "Mul", "Div", "Mod", "BitwiseAnd", "BitwiseOr", "BitwiseXor", "LogicalAnd",
                    "LogicalOr", "SL", "SR", "LT", "GT", "LTEQ", "GTEQ", "EQ", "NEQ"]
        self.singleOps = ["PreFix", "BitwiseNot", "LogicalNot", "Deref"]
        self.literalNodes = [IntNode, FloatNode, CharNode]



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
        function_type = ir.FunctionType(ir.VoidType(), [])
        func_type = node.type
        if isinstance(func_type, list):
            func_type = func_type[len(func_type) - 1]
        if isinstance(func_type, TypeNode):
            if func_type.value == 'char':
                function_type = ir.FunctionType(ir.IntType(8), [])
            elif func_type.value == 'int':
                function_type = ir.FunctionType(ir.IntType(32), [])
            elif func_type.value == 'float':
                function_type = ir.FunctionType(ir.FloatType(), [])
            elif func_type.value == 'void':
                function_type = ir.FunctionType(ir.VoidType(), [])
        elif isinstance(func_type, PointerNode):
            ...
        function = ir.Function(self.module, function_type, name=node.value)

        entry_block = function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        # Allocate space for function parameters
        for param in node.params:
            alloca = self.create_entry_block_alloca(function, param.lvalue.value)
            self.symbol_table[param.lvalue.value] = alloca

        # Visit function body
        for statement in node.body:
            self.visit(statement)

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

    def visit_MinusNode(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[1])
        return self.builder.sub(left, right, name="tmp")

    @staticmethod
    def visit_IntNode(node):
        return ir.Constant(ir.IntType(32), int(node.value))

    @staticmethod
    def visit_CharNode(node):
        return ir.Constant(ir.IntType(8), ord(node.value))

    @staticmethod
    def visit_FloatNode(node):
        # Convert the node's value to a float and then to an LLVM float constant
        return ir.Constant(ir.FloatType(), float(node.value))

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
        # Retrieve the LLVM value associated with the variable from the symbol table
        var_value = definitions.get(node.value)
        if var_value is None:
            raise Exception(f"Undefined variable '{node.value}' used before assignment")
        return var_value