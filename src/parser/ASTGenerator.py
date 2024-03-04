from src.antlr_files.Grammar_Project_1Visitor import Grammar_Project_1Visitor as Visitor

from src.parser.AST import *


class ASTGenerator(Visitor):
    def visitProgram(self, ctx):
        print("Start:", ctx.getText())
        root = AST("Start", ctx.start.line, ctx.start.column)
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                root.addNode(node)
        return root

    def visitExpression(self, ctx):
        print("Expression:", ctx.getText())

    def visitUnaryExpression(self, ctx):
        print("Operation:", ctx.getText())