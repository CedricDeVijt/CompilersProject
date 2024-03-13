from src.antlr_files.Grammar_Project_1Parser import Grammar_Project_1Parser
from src.antlr_files.Grammar_Project_1Visitor import Grammar_Project_1Visitor as Visitor

from src.parser.AST import *


class ASTGenerator(Visitor):
    def visitProgram(self, ctx):
        children = []
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                children.append(node)
        return ProgramNode(ctx.start.line, ctx.start.column, children)

    def visitProgramLine(self, ctx):
        lines = []
        for line in ctx.getChildren():
            lines.append(line)
        node = self.visit(lines[0])
        return node

    def visitExpression(self, ctx):
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

    def visitUnaryExpression(self, ctx):
        node = UnaryExpressionNode(ctx.start.line, ctx.start.column)
        negatives = 0
        for child in ctx.getChildren():
            if child.getText() == "-":
                negatives += 1
        if negatives % 2 == 1:
            child = NegativeNode(ctx.start.line, ctx.start.column)
            node.children.append(child)
        for child in ctx.getChildren():
            if child.getText() != "-" and child.getText() != '+':
                node.children.append(child)
        return node

    def visitNumber(self, ctx):
        node = IntNode(ctx.getText(), ctx.start.line, ctx.start.column)
        return node
