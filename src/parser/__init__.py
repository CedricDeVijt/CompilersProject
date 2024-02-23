class AST:
    def __init__(self):
        self.root = None

    def setRoot(self, node):
        self.root = node

class Node:
    def __init__(self):
        self.children = []

class ProgramNode (Node):
    def __init__(self):
        ...

class ExpressionNode (Node):
    def __init__(self):
        ...

class LogicalExpressionNode (Node):
    def __init__(self):
        ...

class EqualityExpressionNode (Node):
    def __init__(self):
        ...

class RelationalExpressionNode (Node):
    def __init__(self):
        ...

class AdditiveExpressionNode (Node):
    def __init__(self):
        ...

class MultiplicativeExpressionNode (Node):
    def __init__(self):
        ...

class UnaryExpressionNode (Node):
    def __init__(self):
        ...

class PrimaryExpressionNode (Node):
    def __init__(self):
        ...











