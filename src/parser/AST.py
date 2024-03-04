class AST:
    def __init__(self, root, line, pos):
        self.root = root
        self.nodes = []
        self.line = line
        self.pos = pos

    def addNode(self, node):
        self.nodes.append(node)


class ASTOperation:

    def __init__(self, root, line, pos):
        self.root = root
        self.line = line
        self.pos = pos