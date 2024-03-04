from src.antlr_files.Grammar_Project_1Visitor import Grammar_Project_1Visitor as Visitor

from src.parser.AST import *


class ASTGenerator(Visitor):
    def visitProgram(self, ctx):
        print("Program:", ctx.getText())
        root = AST("Program", ctx.start.line, ctx.start.column)
        for line in ctx.getChildren():
            node = self.visitExpression(line)
            if node is not None:
                root.addNode(node)
        return root

    def visitExpression(self, ctx):
        print("Expression:", ctx.getText())
        lines = []
        for line in ctx.getChildren():
            self.visit(line)


    def visitNumber(self, ctx):
        print("Number:", ctx.getText())
        return ASTNumber(ctx.getText(), ctx.start.line, ctx.start.column)
