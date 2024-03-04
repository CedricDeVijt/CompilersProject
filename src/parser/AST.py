class AST:
    def __init__(self, root, line, pos):
        self.root = root
        self.nodes = []
        self.line = line
        self.pos = pos

    def addNode(self, node):
        self.nodes.append(node)


class ASTOperation(AST):

    def __init__(self, root, line, pos):
        super() .__init__(root, line, pos)


class ASTNumber(AST):

    def __init__(self, root, line, pos):
        super() .__init__(root, line, pos)