# Generated from grammars/Grammar_Project_1.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Grammar_Project_1Parser import Grammar_Project_1Parser
else:
    from Grammar_Project_1Parser import Grammar_Project_1Parser

# This class defines a complete listener for a parse tree produced by Grammar_Project_1Parser.
class Grammar_Project_1Listener(ParseTreeListener):

    # Enter a parse tree produced by Grammar_Project_1Parser#program.
    def enterProgram(self, ctx:Grammar_Project_1Parser.ProgramContext):
        pass

    # Exit a parse tree produced by Grammar_Project_1Parser#program.
    def exitProgram(self, ctx:Grammar_Project_1Parser.ProgramContext):
        pass


    # Enter a parse tree produced by Grammar_Project_1Parser#programLine.
    def enterProgramLine(self, ctx:Grammar_Project_1Parser.ProgramLineContext):
        pass

    # Exit a parse tree produced by Grammar_Project_1Parser#programLine.
    def exitProgramLine(self, ctx:Grammar_Project_1Parser.ProgramLineContext):
        pass


    # Enter a parse tree produced by Grammar_Project_1Parser#expression.
    def enterExpression(self, ctx:Grammar_Project_1Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Grammar_Project_1Parser#expression.
    def exitExpression(self, ctx:Grammar_Project_1Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by Grammar_Project_1Parser#unaryExpression.
    def enterUnaryExpression(self, ctx:Grammar_Project_1Parser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by Grammar_Project_1Parser#unaryExpression.
    def exitUnaryExpression(self, ctx:Grammar_Project_1Parser.UnaryExpressionContext):
        pass



del Grammar_Project_1Parser