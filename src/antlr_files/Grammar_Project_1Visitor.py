# Generated from grammars/Grammar_Project_1.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Grammar_Project_1Parser import Grammar_Project_1Parser
else:
    from Grammar_Project_1Parser import Grammar_Project_1Parser

# This class defines a complete generic visitor for a parse tree produced by Grammar_Project_1Parser.

class Grammar_Project_1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Grammar_Project_1Parser#program.
    def visitProgram(self, ctx:Grammar_Project_1Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_1Parser#programLine.
    def visitProgramLine(self, ctx:Grammar_Project_1Parser.ProgramLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_1Parser#expression.
    def visitExpression(self, ctx:Grammar_Project_1Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_1Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:Grammar_Project_1Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_1Parser#number.
    def visitNumber(self, ctx:Grammar_Project_1Parser.NumberContext):
        return self.visitChildren(ctx)



del Grammar_Project_1Parser