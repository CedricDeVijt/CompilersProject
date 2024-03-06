class AST:
    def __init__(self, value, line, pos):
        self.value = value
        self.children = []
        self.line = line
        self.pos = pos

    def addChildren(self, node):
        self.children.append(node)


class ASTOperation(AST):

    def __init__(self, value, line, pos):
        super().__init__(value, line, pos)


class ASTNumber(AST):

    def __init__(self, value, line, pos):
        super().__init__(value, line, pos)
