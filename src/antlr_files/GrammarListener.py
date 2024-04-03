# Generated from grammars/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#programLine.
    def enterProgramLine(self, ctx:GrammarParser.ProgramLineContext):
        pass

    # Exit a parse tree produced by GrammarParser#programLine.
    def exitProgramLine(self, ctx:GrammarParser.ProgramLineContext):
        pass


    # Enter a parse tree produced by GrammarParser#main.
    def enterMain(self, ctx:GrammarParser.MainContext):
        pass

    # Exit a parse tree produced by GrammarParser#main.
    def exitMain(self, ctx:GrammarParser.MainContext):
        pass


    # Enter a parse tree produced by GrammarParser#scope.
    def enterScope(self, ctx:GrammarParser.ScopeContext):
        pass

    # Exit a parse tree produced by GrammarParser#scope.
    def exitScope(self, ctx:GrammarParser.ScopeContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#printfStatement.
    def enterPrintfStatement(self, ctx:GrammarParser.PrintfStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#printfStatement.
    def exitPrintfStatement(self, ctx:GrammarParser.PrintfStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#formatSpecifier.
    def enterFormatSpecifier(self, ctx:GrammarParser.FormatSpecifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#formatSpecifier.
    def exitFormatSpecifier(self, ctx:GrammarParser.FormatSpecifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#variables.
    def enterVariables(self, ctx:GrammarParser.VariablesContext):
        pass

    # Exit a parse tree produced by GrammarParser#variables.
    def exitVariables(self, ctx:GrammarParser.VariablesContext):
        pass


    # Enter a parse tree produced by GrammarParser#lvalue.
    def enterLvalue(self, ctx:GrammarParser.LvalueContext):
        pass

    # Exit a parse tree produced by GrammarParser#lvalue.
    def exitLvalue(self, ctx:GrammarParser.LvalueContext):
        pass


    # Enter a parse tree produced by GrammarParser#rvalue.
    def enterRvalue(self, ctx:GrammarParser.RvalueContext):
        pass

    # Exit a parse tree produced by GrammarParser#rvalue.
    def exitRvalue(self, ctx:GrammarParser.RvalueContext):
        pass


    # Enter a parse tree produced by GrammarParser#unaryExpression.
    def enterUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#unaryExpression.
    def exitUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#literal.
    def enterLiteral(self, ctx:GrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by GrammarParser#literal.
    def exitLiteral(self, ctx:GrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by GrammarParser#explicitConversion.
    def enterExplicitConversion(self, ctx:GrammarParser.ExplicitConversionContext):
        pass

    # Exit a parse tree produced by GrammarParser#explicitConversion.
    def exitExplicitConversion(self, ctx:GrammarParser.ExplicitConversionContext):
        pass


    # Enter a parse tree produced by GrammarParser#pointer.
    def enterPointer(self, ctx:GrammarParser.PointerContext):
        pass

    # Exit a parse tree produced by GrammarParser#pointer.
    def exitPointer(self, ctx:GrammarParser.PointerContext):
        pass


    # Enter a parse tree produced by GrammarParser#deref.
    def enterDeref(self, ctx:GrammarParser.DerefContext):
        pass

    # Exit a parse tree produced by GrammarParser#deref.
    def exitDeref(self, ctx:GrammarParser.DerefContext):
        pass


    # Enter a parse tree produced by GrammarParser#addr.
    def enterAddr(self, ctx:GrammarParser.AddrContext):
        pass

    # Exit a parse tree produced by GrammarParser#addr.
    def exitAddr(self, ctx:GrammarParser.AddrContext):
        pass


    # Enter a parse tree produced by GrammarParser#type.
    def enterType(self, ctx:GrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#type.
    def exitType(self, ctx:GrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#postFixIncrement.
    def enterPostFixIncrement(self, ctx:GrammarParser.PostFixIncrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#postFixIncrement.
    def exitPostFixIncrement(self, ctx:GrammarParser.PostFixIncrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#postFixDecrement.
    def enterPostFixDecrement(self, ctx:GrammarParser.PostFixDecrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#postFixDecrement.
    def exitPostFixDecrement(self, ctx:GrammarParser.PostFixDecrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#preFixIncrement.
    def enterPreFixIncrement(self, ctx:GrammarParser.PreFixIncrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#preFixIncrement.
    def exitPreFixIncrement(self, ctx:GrammarParser.PreFixIncrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#preFixDecrement.
    def enterPreFixDecrement(self, ctx:GrammarParser.PreFixDecrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#preFixDecrement.
    def exitPreFixDecrement(self, ctx:GrammarParser.PreFixDecrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#identifier.
    def enterIdentifier(self, ctx:GrammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#identifier.
    def exitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#comment.
    def enterComment(self, ctx:GrammarParser.CommentContext):
        pass

    # Exit a parse tree produced by GrammarParser#comment.
    def exitComment(self, ctx:GrammarParser.CommentContext):
        pass



del GrammarParser