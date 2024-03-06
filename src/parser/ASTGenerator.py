from src.antlr_files.Grammar_Project_1Parser import Grammar_Project_1Parser
from src.antlr_files.Grammar_Project_1Visitor import Grammar_Project_1Visitor as Visitor

from src.parser.AST import *


class ASTGenerator(Visitor):
    def visitProgram(self, ctx):
        root = AST("Program", ctx.start.line, ctx.start.column)
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                root.addNode(node)
        print("Program:", ctx.getText())
        return root

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
            node = ASTOperation(str(lines[1]), ctx.start.line, ctx.start.column)
            child1 = self.visit(lines[0])
            child2 = self.visit(lines[2])
            node.addNode(child1)
            node.addNode(child2)
            return node
        if len(lines) == 2:
            node = ASTOperation(str(lines[0]), ctx.start.line, ctx.start.column)
            child = self.visit(lines[1])
            node.addNode(child)
            return node
        print("Expression:", ctx.getText())
        node = self.visitChildren(ctx)
        return node

    def visitNumber(self, ctx):
        print("Number:", ctx.getText())
        node = ASTNumber(ctx.getText(), ctx.start.line, ctx.start.column)
        return node
