class MIPSVisitor:
    def __init__(self, stdio=False):
        self.code = []

    def visit(self, node):
        method_name = "visit_" + node.__class__.__name__
        _visitor = getattr(self, method_name, self.generic_visit)
        return _visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{node.__class__.__name__} method")

    def visit_ProgramNode(self, node):
        for child in node.children:
            self.visit(child)

    def visit_FunctionNode(self, node):
        self.code.append(f"{node.value}:")
        for statement in node.body:
            self.visit(statement)

    def visit_ReturnNode(self, node):
        self.code.append(f"jr $ra")

    def visit_AssignmentNode(self, node):
        # Assuming only integer assignments for simplicity
        self.code.append(f"li $t0, {node.rvalue.value}")
        self.code.append(f"sw $t0, {node.lvalue.value}")

    def visit_PlusNode(self, node):
        # Assuming only integer addition for simplicity
        self.code.append(f"add $t0, {node.children[0].value}, {node.children[1].value}")

    # ... add more visit methods for other node types ...

    def generate(self):
        return "\n".join(self.code)