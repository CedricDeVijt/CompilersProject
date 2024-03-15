from src.antlr_files.Proj_2.Grammar_Project_2Parser import Grammar_Project_2Parser
from src.antlr_files.Proj_2.Grammar_Project_2Visitor import Grammar_Project_2Visitor as Visitor

from src.parser.AST import *

class ASTGenerator(Visitor):

    def __init__(self):
        self.scope = SymbolTable()

    def visitProgram(self, ctx):
        children = []
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                children.append(node)
        return ProgramNode(ctx.start.line, ctx.start.column, children)

    def visitMain(self, ctx):
        children = []
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                children.append(node)
        return MainNode(ctx.start.line, ctx.start.column, children)

    def visitStatement(self, ctx):
        children = []
        for line in ctx.getChildren():
            if line.getText() == ";":
                pass
            elif line.getText() == "=":
                children.append(line.getText())
            elif isinstance(self.visit(line), list):
                children.extend(self.visit(line))
            else:
                children.append(self.visit(line))
        if len(children) == 2:
            if isinstance(children[0], TypeNode) and isinstance(children[1], IdentifierNode):
                if self.scope.lookup(children[1].value) is not None:
                    raise Exception("Variable \'" + children[1].value + "\' not declared yet!")
        if children.__contains__("=") and (children.index("=") == 2):
            node = IdentifierNode(children[children.index("=")-1].value, children[0].line, children[0].pos)
            if self.scope.lookup(node.value) is None:
                self.scope.insert(node.value, children[(children.index("=")+1)].value, children[children.index("=")-2].value)
                return node
            else:
                raise Exception("Variable \'" + node.value + "\' already declared!")
        if children.__contains__("="):
            if self.scope.lookup(children[children.index("=")-1].value) is None:
                raise Exception("Variable \'" + children[children.index("=")-1].value + "\' not declared yet!")
        node = StatementNode(ctx.start.line, ctx.start.column, children)
        return node

    def visitLvalue(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(self.visit(line))
        return children

    def visitIdentifier(self, ctx):
        node = IdentifierNode(ctx.getText(), ctx.start.line, ctx.start.column)
        return node

    def visitType(self, ctx):
        node = TypeNode(ctx.getText(), ctx.start.line, ctx.start.column)
        return node

    def visitRvalue(self, ctx):
        lines = []
        for line in ctx.getChildren():
            lines.append(line)
        if len(lines) == 3:
            if str(lines[0]) == "(" and ")" == str(lines[2]):
                node = self.visit(lines[1])
                return node
            node = ProgramNode(0, 0)
            match str(lines[1]):
                case "/":
                    node = DivNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "%":
                    node = ModNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "*":
                    node = MultNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "-":
                    node = MinusNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "+":
                    node = PlusNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case ">":
                    node = GTNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "<":
                    node = LTNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case ">=":
                    node = GTEQNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "<=":
                    node = LTEQNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "!=":
                    node = NEQNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "<<":
                    node = SLNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case ">>":
                    node = SRNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "&":
                    node = BitwiseAndNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "|":
                    node = BitwiseOrNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "^":
                    node = BitwiseXorNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "&&":
                    node = LogicalAndNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "||":
                    node = LogicalOrNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
            return node
        if len(lines) == 2:
            if str(lines[0]) == "!":
                node = LogicalNotNode(ctx.start.line, ctx.start.column, [self.visit(lines[1])])
                return node
        node = self.visitChildren(ctx)
        return node

    def visitLiteral(self, ctx):
        literal = ctx.getText()
        if literal.startswith("\'"):
            for i in literal:
                if i.isalnum():
                    literal = ord(i)
        if float(literal) % 1 == 0:
            node = IntNode(ctx.getText(), ctx.start.line, ctx.start.column)
            return node
        node = FloatNode(ctx.getText(), ctx.start.line, ctx.start.column)
        return node
