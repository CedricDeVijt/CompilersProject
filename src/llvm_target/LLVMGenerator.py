from llvmlite import ir

from src.parser.AST import *

# LLVM IR setup
module = ir.Module()


class LLVMVisitor:
    def __init__(self):
        self.builder = None
        self.symbol_table = {}

    def visit(self, node):
        method_name = "visit_" + node.__class__.__name__
        _visitor = getattr(self, method_name, self.generic_visit)
        return _visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{node.__class__.__name__} method defined")

    @staticmethod
    def create_entry_block_alloca(function, var_name):
        builder = ir.IRBuilder(function.append_basic_block(name="entry"))
        return builder.alloca(ir.IntType(32), name=var_name)

    def visit_ProgramNode(self, node):
        for child in node.children:
            self.visit(child)

    def visit_FunctionNode(self, node):
        function_type = ir.FunctionType(ir.VoidType(), [])
        function = ir.Function(module, function_type, name=node.value)

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

    def visit_IntNode(self, node):
        return ir.Constant(ir.IntType(32), int(node.value))

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.value == '+':
            return self.builder.add(left, right, name="addtmp")
        elif node.value == '-':
            return self.builder.sub(left, right, name="subtmp")
        elif node.value == '*':
            return self.builder.mul(left, right, name="multmp")
        elif node.value == '/':
            return self.builder.sdiv(left, right, name="divtmp")

    def visit_PrintNode(self, node):
        value = self.visit(node.expr)
        printf_arg = ir.Constant(ir.ArrayType(ir.IntType(8), len("%d\n")), bytearray(b"%d\0"))
        printf_format = self.builder.bitcast(printf_arg, ir.IntType(8).as_pointer())

        self.builder.call(
            module.get_or_insert_function("printf", ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer()])),
            [printf_format, value])


# Example AST
class BinOpNode:
    def __init__(self, left, value, right):
        self.left = left
        self.value = value
        self.right = right


class PrintNode:
    def __init__(self, expr):
        self.expr = expr


op = BinOpNode(left=IntNode(line=0, column=0, original=None, value="10"), value='+', right=IntNode(line=0, column=0, original=None, value="5"))

# Visiting the AST
visitor = LLVMVisitor()
# Create a FunctionNode
function_node = FunctionNode(line=0, column=0, original=None, return_type=None, value="main", params=[], body=[op])

# Visit the FunctionNode
visitor.visit(function_node)

print(module)
