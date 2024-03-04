# Generated from ../../grammars/grammarC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .grammarCParser import grammarCParser
else:
    from grammarCParser import grammarCParser

# This class defines a complete listener for a parse tree produced by grammarCParser.
class grammarCListener(ParseTreeListener):

    # Enter a parse tree produced by grammarCParser#start.
    def enterStart(self, ctx:grammarCParser.StartContext):
        pass

    # Exit a parse tree produced by grammarCParser#start.
    def exitStart(self, ctx:grammarCParser.StartContext):
        pass


    # Enter a parse tree produced by grammarCParser#programLine.
    def enterProgramLine(self, ctx:grammarCParser.ProgramLineContext):
        pass

    # Exit a parse tree produced by grammarCParser#programLine.
    def exitProgramLine(self, ctx:grammarCParser.ProgramLineContext):
        pass


    # Enter a parse tree produced by grammarCParser#expression.
    def enterExpression(self, ctx:grammarCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammarCParser#expression.
    def exitExpression(self, ctx:grammarCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by grammarCParser#operation.
    def enterOperation(self, ctx:grammarCParser.OperationContext):
        pass

    # Exit a parse tree produced by grammarCParser#operation.
    def exitOperation(self, ctx:grammarCParser.OperationContext):
        pass


    # Enter a parse tree produced by grammarCParser#term.
    def enterTerm(self, ctx:grammarCParser.TermContext):
        pass

    # Exit a parse tree produced by grammarCParser#term.
    def exitTerm(self, ctx:grammarCParser.TermContext):
        pass



del grammarCParser