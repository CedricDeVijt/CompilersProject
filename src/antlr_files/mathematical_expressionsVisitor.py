# Generated from grammars/mathematical_expressions.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mathematical_expressionsParser import mathematical_expressionsParser
else:
    from mathematical_expressionsParser import mathematical_expressionsParser

# This class defines a complete generic visitor for a parse tree produced by mathematical_expressionsParser.

class mathematical_expressionsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mathematical_expressionsParser#program.
    def visitProgram(self, ctx:mathematical_expressionsParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematical_expressionsParser#expression.
    def visitExpression(self, ctx:mathematical_expressionsParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematical_expressionsParser#logicalExpression.
    def visitLogicalExpression(self, ctx:mathematical_expressionsParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematical_expressionsParser#equalityExpression.
    def visitEqualityExpression(self, ctx:mathematical_expressionsParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematical_expressionsParser#relationalExpression.
    def visitRelationalExpression(self, ctx:mathematical_expressionsParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematical_expressionsParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:mathematical_expressionsParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematical_expressionsParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:mathematical_expressionsParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematical_expressionsParser#unaryExpression.
    def visitUnaryExpression(self, ctx:mathematical_expressionsParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematical_expressionsParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:mathematical_expressionsParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)



del mathematical_expressionsParser