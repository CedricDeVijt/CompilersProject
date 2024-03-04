# Generated from ../../grammars/grammarC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .grammarCParser import grammarCParser
else:
    from grammarCParser import grammarCParser

# This class defines a complete generic visitor for a parse tree produced by grammarCParser.

class grammarCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammarCParser#start.
    def visitStart(self, ctx:grammarCParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#programLine.
    def visitProgramLine(self, ctx:grammarCParser.ProgramLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#expression.
    def visitExpression(self, ctx:grammarCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#operation.
    def visitOperation(self, ctx:grammarCParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#term.
    def visitTerm(self, ctx:grammarCParser.TermContext):
        return self.visitChildren(ctx)



del grammarCParser