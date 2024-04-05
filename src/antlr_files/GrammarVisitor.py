# Generated from grammars/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#main.
    def visitMain(self, ctx:GrammarParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#scope.
    def visitScope(self, ctx:GrammarParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#conditional.
    def visitConditional(self, ctx:GrammarParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ifStatement.
    def visitIfStatement(self, ctx:GrammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:GrammarParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#elseStatement.
    def visitElseStatement(self, ctx:GrammarParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#whileLoop.
    def visitWhileLoop(self, ctx:GrammarParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forLoop.
    def visitForLoop(self, ctx:GrammarParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forInit.
    def visitForInit(self, ctx:GrammarParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forCondition.
    def visitForCondition(self, ctx:GrammarParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forUpdate.
    def visitForUpdate(self, ctx:GrammarParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#break.
    def visitBreak(self, ctx:GrammarParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#continue.
    def visitContinue(self, ctx:GrammarParser.ContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#printfStatement.
    def visitPrintfStatement(self, ctx:GrammarParser.PrintfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#formatSpecifier.
    def visitFormatSpecifier(self, ctx:GrammarParser.FormatSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable.
    def visitVariable(self, ctx:GrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#lvalue.
    def visitLvalue(self, ctx:GrammarParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#rvalue.
    def visitRvalue(self, ctx:GrammarParser.RvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#unaryExpression.
    def visitUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#literal.
    def visitLiteral(self, ctx:GrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#explicitConversion.
    def visitExplicitConversion(self, ctx:GrammarParser.ExplicitConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#pointer.
    def visitPointer(self, ctx:GrammarParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#deref.
    def visitDeref(self, ctx:GrammarParser.DerefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#addr.
    def visitAddr(self, ctx:GrammarParser.AddrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#postFixIncrement.
    def visitPostFixIncrement(self, ctx:GrammarParser.PostFixIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#postFixDecrement.
    def visitPostFixDecrement(self, ctx:GrammarParser.PostFixDecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#preFixIncrement.
    def visitPreFixIncrement(self, ctx:GrammarParser.PreFixIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#preFixDecrement.
    def visitPreFixDecrement(self, ctx:GrammarParser.PreFixDecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#typedef.
    def visitTypedef(self, ctx:GrammarParser.TypedefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#type.
    def visitType(self, ctx:GrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#identifier.
    def visitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#comment.
    def visitComment(self, ctx:GrammarParser.CommentContext):
        return self.visitChildren(ctx)



del GrammarParser