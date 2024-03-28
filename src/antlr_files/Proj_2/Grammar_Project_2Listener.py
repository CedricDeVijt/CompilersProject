# Generated from grammars/Grammar_Project_2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Grammar_Project_2Parser import Grammar_Project_2Parser
else:
    from Grammar_Project_2Parser import Grammar_Project_2Parser

# This class defines a complete listener for a parse tree produced by Grammar_Project_2Parser.
class Grammar_Project_2Listener(ParseTreeListener):

    # Enter a parse tree produced by Grammar_Project_2Parser#program.
    def enterProgram(self, ctx:Grammar_Project_2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#program.
    def exitProgram(self, ctx:Grammar_Project_2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#main.
    def enterMain(self, ctx:Grammar_Project_2Parser.MainContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#main.
    def exitMain(self, ctx:Grammar_Project_2Parser.MainContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#scope.
    def enterScope(self, ctx:Grammar_Project_2Parser.ScopeContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#scope.
    def exitScope(self, ctx:Grammar_Project_2Parser.ScopeContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#statement.
    def enterStatement(self, ctx:Grammar_Project_2Parser.StatementContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#statement.
    def exitStatement(self, ctx:Grammar_Project_2Parser.StatementContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#lvalue.
    def enterLvalue(self, ctx:Grammar_Project_2Parser.LvalueContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#lvalue.
    def exitLvalue(self, ctx:Grammar_Project_2Parser.LvalueContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#rvalue.
    def enterRvalue(self, ctx:Grammar_Project_2Parser.RvalueContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#rvalue.
    def exitRvalue(self, ctx:Grammar_Project_2Parser.RvalueContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#rvalueCast.
    def enterRvalueCast(self, ctx:Grammar_Project_2Parser.RvalueCastContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#rvalueCast.
    def exitRvalueCast(self, ctx:Grammar_Project_2Parser.RvalueCastContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#unaryExpression.
    def enterUnaryExpression(self, ctx:Grammar_Project_2Parser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#unaryExpression.
    def exitUnaryExpression(self, ctx:Grammar_Project_2Parser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#literal.
    def enterLiteral(self, ctx:Grammar_Project_2Parser.LiteralContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#literal.
    def exitLiteral(self, ctx:Grammar_Project_2Parser.LiteralContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#pointer.
    def enterPointer(self, ctx:Grammar_Project_2Parser.PointerContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#pointer.
    def exitPointer(self, ctx:Grammar_Project_2Parser.PointerContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#deref.
    def enterDeref(self, ctx:Grammar_Project_2Parser.DerefContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#deref.
    def exitDeref(self, ctx:Grammar_Project_2Parser.DerefContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#addr.
    def enterAddr(self, ctx:Grammar_Project_2Parser.AddrContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#addr.
    def exitAddr(self, ctx:Grammar_Project_2Parser.AddrContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#type.
    def enterType(self, ctx:Grammar_Project_2Parser.TypeContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#type.
    def exitType(self, ctx:Grammar_Project_2Parser.TypeContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#postFixIncrement.
    def enterPostFixIncrement(self, ctx:Grammar_Project_2Parser.PostFixIncrementContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#postFixIncrement.
    def exitPostFixIncrement(self, ctx:Grammar_Project_2Parser.PostFixIncrementContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#postFixDecrement.
    def enterPostFixDecrement(self, ctx:Grammar_Project_2Parser.PostFixDecrementContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#postFixDecrement.
    def exitPostFixDecrement(self, ctx:Grammar_Project_2Parser.PostFixDecrementContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#preFixIncrement.
    def enterPreFixIncrement(self, ctx:Grammar_Project_2Parser.PreFixIncrementContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#preFixIncrement.
    def exitPreFixIncrement(self, ctx:Grammar_Project_2Parser.PreFixIncrementContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#preFixDecrement.
    def enterPreFixDecrement(self, ctx:Grammar_Project_2Parser.PreFixDecrementContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#preFixDecrement.
    def exitPreFixDecrement(self, ctx:Grammar_Project_2Parser.PreFixDecrementContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#identifier.
    def enterIdentifier(self, ctx:Grammar_Project_2Parser.IdentifierContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#identifier.
    def exitIdentifier(self, ctx:Grammar_Project_2Parser.IdentifierContext):
        pass


    # Enter a parse tree produced by Grammar_Project_2Parser#comment.
    def enterComment(self, ctx:Grammar_Project_2Parser.CommentContext):
        pass

    # Exit a parse tree produced by Grammar_Project_2Parser#comment.
    def exitComment(self, ctx:Grammar_Project_2Parser.CommentContext):
        pass



del Grammar_Project_2Parser