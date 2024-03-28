# Generated from grammars/Grammar_Project_2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Grammar_Project_2Parser import Grammar_Project_2Parser
else:
    from Grammar_Project_2Parser import Grammar_Project_2Parser

# This class defines a complete generic visitor for a parse tree produced by Grammar_Project_2Parser.

class Grammar_Project_2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Grammar_Project_2Parser#program.
    def visitProgram(self, ctx:Grammar_Project_2Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#main.
    def visitMain(self, ctx:Grammar_Project_2Parser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#scope.
    def visitScope(self, ctx:Grammar_Project_2Parser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#statement.
    def visitStatement(self, ctx:Grammar_Project_2Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#lvalue.
    def visitLvalue(self, ctx:Grammar_Project_2Parser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#rvalue.
    def visitRvalue(self, ctx:Grammar_Project_2Parser.RvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#rvalueCast.
    def visitRvalueCast(self, ctx:Grammar_Project_2Parser.RvalueCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:Grammar_Project_2Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#literal.
    def visitLiteral(self, ctx:Grammar_Project_2Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#implicitConversion.
    def visitImplicitConversion(self, ctx:Grammar_Project_2Parser.ImplicitConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#pointer.
    def visitPointer(self, ctx:Grammar_Project_2Parser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#deref.
    def visitDeref(self, ctx:Grammar_Project_2Parser.DerefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#addr.
    def visitAddr(self, ctx:Grammar_Project_2Parser.AddrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#type.
    def visitType(self, ctx:Grammar_Project_2Parser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#postFixIncrement.
    def visitPostFixIncrement(self, ctx:Grammar_Project_2Parser.PostFixIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#postFixDecrement.
    def visitPostFixDecrement(self, ctx:Grammar_Project_2Parser.PostFixDecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#preFixIncrement.
    def visitPreFixIncrement(self, ctx:Grammar_Project_2Parser.PreFixIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#preFixDecrement.
    def visitPreFixDecrement(self, ctx:Grammar_Project_2Parser.PreFixDecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#identifier.
    def visitIdentifier(self, ctx:Grammar_Project_2Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#comment.
    def visitComment(self, ctx:Grammar_Project_2Parser.CommentContext):
        return self.visitChildren(ctx)



del Grammar_Project_2Parser