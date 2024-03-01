class AST:
    def __init__(self):
        self.root = None

    def setRoot(self, node):
        self.root = node


class Node:
    def __init__(self):
        self.children = []


class ProgramNode(Node):
    def __init__(self):
        super().__init__()
        ...


class ExpressionNode(Node):
    def __init__(self):
        super().__init__()
        ...


class LogicalExpressionNode(Node):
    def __init__(self):
        super().__init__()
        ...


class EqualityExpressionNode(Node):
    def __init__(self):
        super().__init__()
        ...


class RelationalExpressionNode(Node):
    def __init__(self):
        super().__init__()
        ...


class AdditiveExpressionNode(Node):
    def __init__(self):
        super().__init__()
        ...


class MultiplicativeExpressionNode(Node):
    def __init__(self):
        super().__init__()
        ...


class UnaryExpressionNode(Node):
    def __init__(self):
        super().__init__()
        ...


class PrimaryExpressionNode(Node):
    def __init__(self):
        super().__init__()
        ...
