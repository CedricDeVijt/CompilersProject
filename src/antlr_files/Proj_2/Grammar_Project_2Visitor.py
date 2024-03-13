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


    # Visit a parse tree produced by Grammar_Project_2Parser#statement.
    def visitStatement(self, ctx:Grammar_Project_2Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#expression.
    def visitExpression(self, ctx:Grammar_Project_2Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:Grammar_Project_2Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#literal.
    def visitLiteral(self, ctx:Grammar_Project_2Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#decl.
    def visitDecl(self, ctx:Grammar_Project_2Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#def.
    def visitDef(self, ctx:Grammar_Project_2Parser.DefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Grammar_Project_2Parser#ass.
    def visitAss(self, ctx:Grammar_Project_2Parser.AssContext):
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



del Grammar_Project_2Parser