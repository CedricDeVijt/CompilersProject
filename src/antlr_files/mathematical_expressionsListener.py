# Generated from /Users/cedric/Library/Mobile Documents/com~apple~CloudDocs/School/Informatica 2/2 Compilers/Project/grammars/mathematical_expressions.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mathematical_expressionsParser import mathematical_expressionsParser
else:
    from mathematical_expressionsParser import mathematical_expressionsParser

# This class defines a complete listener for a parse tree produced by mathematical_expressionsParser.
class mathematical_expressionsListener(ParseTreeListener):

    # Enter a parse tree produced by mathematical_expressionsParser#expression.
    def enterExpression(self, ctx:mathematical_expressionsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by mathematical_expressionsParser#expression.
    def exitExpression(self, ctx:mathematical_expressionsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by mathematical_expressionsParser#logicalExpression.
    def enterLogicalExpression(self, ctx:mathematical_expressionsParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by mathematical_expressionsParser#logicalExpression.
    def exitLogicalExpression(self, ctx:mathematical_expressionsParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by mathematical_expressionsParser#equalityExpression.
    def enterEqualityExpression(self, ctx:mathematical_expressionsParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by mathematical_expressionsParser#equalityExpression.
    def exitEqualityExpression(self, ctx:mathematical_expressionsParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by mathematical_expressionsParser#relationalExpression.
    def enterRelationalExpression(self, ctx:mathematical_expressionsParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by mathematical_expressionsParser#relationalExpression.
    def exitRelationalExpression(self, ctx:mathematical_expressionsParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by mathematical_expressionsParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:mathematical_expressionsParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by mathematical_expressionsParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:mathematical_expressionsParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by mathematical_expressionsParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:mathematical_expressionsParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by mathematical_expressionsParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:mathematical_expressionsParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by mathematical_expressionsParser#unaryExpression.
    def enterUnaryExpression(self, ctx:mathematical_expressionsParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by mathematical_expressionsParser#unaryExpression.
    def exitUnaryExpression(self, ctx:mathematical_expressionsParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by mathematical_expressionsParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:mathematical_expressionsParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by mathematical_expressionsParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:mathematical_expressionsParser.PrimaryExpressionContext):
        pass



del mathematical_expressionsParser