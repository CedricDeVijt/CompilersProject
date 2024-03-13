# Generated from grammars/Grammar_Project_2.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,194,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,39,8,1,10,1,12,1,42,
        9,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,3,3,61,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,117,8,3,10,3,12,3,
        120,9,3,1,4,3,4,123,8,4,1,4,1,4,1,4,4,4,128,8,4,11,4,12,4,129,1,
        4,3,4,133,8,4,1,4,1,4,1,4,4,4,138,8,4,11,4,12,4,139,1,4,3,4,143,
        8,4,1,4,3,4,146,8,4,1,5,1,5,1,6,1,6,3,6,152,8,6,1,6,1,6,1,7,1,7,
        3,7,158,8,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,4,9,170,8,9,
        11,9,12,9,171,1,10,4,10,175,8,10,11,10,12,10,176,1,10,1,10,1,11,
        4,11,182,8,11,11,11,12,11,183,1,11,1,11,1,12,1,12,1,13,1,13,1,14,
        1,14,1,14,0,1,6,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,3,1,
        0,8,9,1,0,28,30,1,0,31,33,215,0,30,1,0,0,0,2,32,1,0,0,0,4,45,1,0,
        0,0,6,60,1,0,0,0,8,145,1,0,0,0,10,147,1,0,0,0,12,151,1,0,0,0,14,
        157,1,0,0,0,16,163,1,0,0,0,18,167,1,0,0,0,20,174,1,0,0,0,22,181,
        1,0,0,0,24,187,1,0,0,0,26,189,1,0,0,0,28,191,1,0,0,0,30,31,3,2,1,
        0,31,1,1,0,0,0,32,33,5,31,0,0,33,34,5,1,0,0,34,35,5,4,0,0,35,36,
        5,5,0,0,36,40,5,6,0,0,37,39,3,4,2,0,38,37,1,0,0,0,39,42,1,0,0,0,
        40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,44,5,
        7,0,0,44,3,1,0,0,0,45,46,3,6,3,0,46,47,5,27,0,0,47,5,1,0,0,0,48,
        49,6,3,-1,0,49,61,3,8,4,0,50,61,5,3,0,0,51,61,3,20,10,0,52,61,3,
        22,11,0,53,54,5,26,0,0,54,61,3,6,3,21,55,56,5,4,0,0,56,57,3,6,3,
        0,57,58,5,5,0,0,58,61,1,0,0,0,59,61,5,28,0,0,60,48,1,0,0,0,60,50,
        1,0,0,0,60,51,1,0,0,0,60,52,1,0,0,0,60,53,1,0,0,0,60,55,1,0,0,0,
        60,59,1,0,0,0,61,118,1,0,0,0,62,63,10,20,0,0,63,64,5,11,0,0,64,117,
        3,6,3,21,65,66,10,19,0,0,66,67,5,12,0,0,67,117,3,6,3,20,68,69,10,
        18,0,0,69,70,5,10,0,0,70,117,3,6,3,19,71,72,10,17,0,0,72,73,5,9,
        0,0,73,117,3,6,3,18,74,75,10,16,0,0,75,76,5,8,0,0,76,117,3,6,3,17,
        77,78,10,15,0,0,78,79,5,13,0,0,79,117,3,6,3,16,80,81,10,14,0,0,81,
        82,5,14,0,0,82,117,3,6,3,15,83,84,10,13,0,0,84,85,5,15,0,0,85,117,
        3,6,3,14,86,87,10,12,0,0,87,88,5,16,0,0,88,117,3,6,3,13,89,90,10,
        11,0,0,90,91,5,17,0,0,91,117,3,6,3,12,92,93,10,10,0,0,93,94,5,18,
        0,0,94,117,3,6,3,11,95,96,10,9,0,0,96,97,5,19,0,0,97,117,3,6,3,10,
        98,99,10,8,0,0,99,100,5,20,0,0,100,117,3,6,3,9,101,102,10,7,0,0,
        102,103,5,21,0,0,103,117,3,6,3,8,104,105,10,6,0,0,105,106,5,22,0,
        0,106,117,3,6,3,7,107,108,10,5,0,0,108,109,5,23,0,0,109,117,3,6,
        3,6,110,111,10,4,0,0,111,112,5,24,0,0,112,117,3,6,3,5,113,114,10,
        3,0,0,114,115,5,25,0,0,115,117,3,6,3,4,116,62,1,0,0,0,116,65,1,0,
        0,0,116,68,1,0,0,0,116,71,1,0,0,0,116,74,1,0,0,0,116,77,1,0,0,0,
        116,80,1,0,0,0,116,83,1,0,0,0,116,86,1,0,0,0,116,89,1,0,0,0,116,
        92,1,0,0,0,116,95,1,0,0,0,116,98,1,0,0,0,116,101,1,0,0,0,116,104,
        1,0,0,0,116,107,1,0,0,0,116,110,1,0,0,0,116,113,1,0,0,0,117,120,
        1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,7,1,0,0,0,120,118,1,
        0,0,0,121,123,7,0,0,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,
        0,0,0,124,146,3,10,5,0,125,126,5,8,0,0,126,128,5,9,0,0,127,125,1,
        0,0,0,128,129,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,1,
        0,0,0,131,133,5,8,0,0,132,131,1,0,0,0,132,133,1,0,0,0,133,134,1,
        0,0,0,134,146,3,10,5,0,135,136,5,9,0,0,136,138,5,8,0,0,137,135,1,
        0,0,0,138,139,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,
        0,0,0,141,143,5,9,0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,1,
        0,0,0,144,146,3,10,5,0,145,122,1,0,0,0,145,127,1,0,0,0,145,137,1,
        0,0,0,146,9,1,0,0,0,147,148,7,1,0,0,148,11,1,0,0,0,149,152,3,24,
        12,0,150,152,3,18,9,0,151,149,1,0,0,0,151,150,1,0,0,0,152,153,1,
        0,0,0,153,154,5,3,0,0,154,13,1,0,0,0,155,158,3,24,12,0,156,158,3,
        18,9,0,157,155,1,0,0,0,157,156,1,0,0,0,158,159,1,0,0,0,159,160,5,
        3,0,0,160,161,5,2,0,0,161,162,3,6,3,0,162,15,1,0,0,0,163,164,5,3,
        0,0,164,165,5,2,0,0,165,166,3,6,3,0,166,17,1,0,0,0,167,169,3,24,
        12,0,168,170,5,10,0,0,169,168,1,0,0,0,170,171,1,0,0,0,171,169,1,
        0,0,0,171,172,1,0,0,0,172,19,1,0,0,0,173,175,5,10,0,0,174,173,1,
        0,0,0,175,176,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,178,1,
        0,0,0,178,179,5,3,0,0,179,21,1,0,0,0,180,182,5,21,0,0,181,180,1,
        0,0,0,182,183,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,185,1,
        0,0,0,185,186,5,3,0,0,186,23,1,0,0,0,187,188,7,2,0,0,188,25,1,0,
        0,0,189,190,5,34,0,0,190,27,1,0,0,0,191,192,5,3,0,0,192,29,1,0,0,
        0,15,40,60,116,118,122,129,132,139,142,145,151,157,171,176,183
    ]

class Grammar_Project_2Parser ( Parser ):

    grammarFileName = "Grammar_Project_2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'='", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "'<<'", "'>>'", 
                     "'&'", "'|'", "'^'", "'&&'", "'||'", "'!'", "';'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'float'", 
                     "'char'", "'const'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", 
                      "MULT", "DIV", "MOD", "GREATER_THAN", "LESS_THAN", 
                      "GREATER_EQUAL", "LESS_EQUAL", "EQUALS", "NOT_EQUAL", 
                      "SHIFT_LEFT", "SHIFT_RIGHT", "BITWISE_AND", "BITWISE_OR", 
                      "BITWISE_XOR", "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", 
                      "SEMICOLON", "INT", "FLOAT", "CHAR", "INTTYPE", "FLOATTYPE", 
                      "CHARTYPE", "CONST", "WHITESPACE" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_expression = 3
    RULE_unaryExpression = 4
    RULE_literal = 5
    RULE_decl = 6
    RULE_def = 7
    RULE_ass = 8
    RULE_pointer = 9
    RULE_deref = 10
    RULE_addr = 11
    RULE_type = 12
    RULE_const = 13
    RULE_identifier = 14

    ruleNames =  [ "program", "main", "statement", "expression", "unaryExpression", 
                   "literal", "decl", "def", "ass", "pointer", "deref", 
                   "addr", "type", "const", "identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IDENTIFIER=3
    LPAREN=4
    RPAREN=5
    LBRACE=6
    RBRACE=7
    PLUS=8
    MINUS=9
    MULT=10
    DIV=11
    MOD=12
    GREATER_THAN=13
    LESS_THAN=14
    GREATER_EQUAL=15
    LESS_EQUAL=16
    EQUALS=17
    NOT_EQUAL=18
    SHIFT_LEFT=19
    SHIFT_RIGHT=20
    BITWISE_AND=21
    BITWISE_OR=22
    BITWISE_XOR=23
    LOGICAL_AND=24
    LOGICAL_OR=25
    LOGICAL_NOT=26
    SEMICOLON=27
    INT=28
    FLOAT=29
    CHAR=30
    INTTYPE=31
    FLOATTYPE=32
    CHARTYPE=33
    CONST=34
    WHITESPACE=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.MainContext,0)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Grammar_Project_2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(Grammar_Project_2Parser.INTTYPE, 0)

        def LPAREN(self):
            return self.getToken(Grammar_Project_2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Grammar_Project_2Parser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(Grammar_Project_2Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Grammar_Project_2Parser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = Grammar_Project_2Parser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(Grammar_Project_2Parser.INTTYPE)
            self.state = 33
            self.match(Grammar_Project_2Parser.T__0)
            self.state = 34
            self.match(Grammar_Project_2Parser.LPAREN)
            self.state = 35
            self.match(Grammar_Project_2Parser.RPAREN)
            self.state = 36
            self.match(Grammar_Project_2Parser.LBRACE)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1948256024) != 0):
                self.state = 37
                self.statement()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(Grammar_Project_2Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(Grammar_Project_2Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Grammar_Project_2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.expression(0)
            self.state = 46
            self.match(Grammar_Project_2Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.UnaryExpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(Grammar_Project_2Parser.IDENTIFIER, 0)

        def deref(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.DerefContext,0)


        def addr(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.AddrContext,0)


        def LOGICAL_NOT(self):
            return self.getToken(Grammar_Project_2Parser.LOGICAL_NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_2Parser.ExpressionContext,i)


        def LPAREN(self):
            return self.getToken(Grammar_Project_2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Grammar_Project_2Parser.RPAREN, 0)

        def INT(self):
            return self.getToken(Grammar_Project_2Parser.INT, 0)

        def DIV(self):
            return self.getToken(Grammar_Project_2Parser.DIV, 0)

        def MOD(self):
            return self.getToken(Grammar_Project_2Parser.MOD, 0)

        def MULT(self):
            return self.getToken(Grammar_Project_2Parser.MULT, 0)

        def MINUS(self):
            return self.getToken(Grammar_Project_2Parser.MINUS, 0)

        def PLUS(self):
            return self.getToken(Grammar_Project_2Parser.PLUS, 0)

        def GREATER_THAN(self):
            return self.getToken(Grammar_Project_2Parser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(Grammar_Project_2Parser.LESS_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(Grammar_Project_2Parser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(Grammar_Project_2Parser.LESS_EQUAL, 0)

        def EQUALS(self):
            return self.getToken(Grammar_Project_2Parser.EQUALS, 0)

        def NOT_EQUAL(self):
            return self.getToken(Grammar_Project_2Parser.NOT_EQUAL, 0)

        def SHIFT_LEFT(self):
            return self.getToken(Grammar_Project_2Parser.SHIFT_LEFT, 0)

        def SHIFT_RIGHT(self):
            return self.getToken(Grammar_Project_2Parser.SHIFT_RIGHT, 0)

        def BITWISE_AND(self):
            return self.getToken(Grammar_Project_2Parser.BITWISE_AND, 0)

        def BITWISE_OR(self):
            return self.getToken(Grammar_Project_2Parser.BITWISE_OR, 0)

        def BITWISE_XOR(self):
            return self.getToken(Grammar_Project_2Parser.BITWISE_XOR, 0)

        def LOGICAL_AND(self):
            return self.getToken(Grammar_Project_2Parser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(Grammar_Project_2Parser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Grammar_Project_2Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 49
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 50
                self.match(Grammar_Project_2Parser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 51
                self.deref()
                pass

            elif la_ == 4:
                self.state = 52
                self.addr()
                pass

            elif la_ == 5:
                self.state = 53
                self.match(Grammar_Project_2Parser.LOGICAL_NOT)
                self.state = 54
                self.expression(21)
                pass

            elif la_ == 6:
                self.state = 55
                self.match(Grammar_Project_2Parser.LPAREN)
                self.state = 56
                self.expression(0)
                self.state = 57
                self.match(Grammar_Project_2Parser.RPAREN)
                pass

            elif la_ == 7:
                self.state = 59
                self.match(Grammar_Project_2Parser.INT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 116
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 62
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 63
                        self.match(Grammar_Project_2Parser.DIV)
                        self.state = 64
                        self.expression(21)
                        pass

                    elif la_ == 2:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 65
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 66
                        self.match(Grammar_Project_2Parser.MOD)
                        self.state = 67
                        self.expression(20)
                        pass

                    elif la_ == 3:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 68
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 69
                        self.match(Grammar_Project_2Parser.MULT)
                        self.state = 70
                        self.expression(19)
                        pass

                    elif la_ == 4:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 71
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 72
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 73
                        self.expression(18)
                        pass

                    elif la_ == 5:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 74
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 75
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 76
                        self.expression(17)
                        pass

                    elif la_ == 6:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 77
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 78
                        self.match(Grammar_Project_2Parser.GREATER_THAN)
                        self.state = 79
                        self.expression(16)
                        pass

                    elif la_ == 7:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 80
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 81
                        self.match(Grammar_Project_2Parser.LESS_THAN)
                        self.state = 82
                        self.expression(15)
                        pass

                    elif la_ == 8:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 83
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 84
                        self.match(Grammar_Project_2Parser.GREATER_EQUAL)
                        self.state = 85
                        self.expression(14)
                        pass

                    elif la_ == 9:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 86
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 87
                        self.match(Grammar_Project_2Parser.LESS_EQUAL)
                        self.state = 88
                        self.expression(13)
                        pass

                    elif la_ == 10:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 89
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 90
                        self.match(Grammar_Project_2Parser.EQUALS)
                        self.state = 91
                        self.expression(12)
                        pass

                    elif la_ == 11:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 93
                        self.match(Grammar_Project_2Parser.NOT_EQUAL)
                        self.state = 94
                        self.expression(11)
                        pass

                    elif la_ == 12:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 95
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 96
                        self.match(Grammar_Project_2Parser.SHIFT_LEFT)
                        self.state = 97
                        self.expression(10)
                        pass

                    elif la_ == 13:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 98
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 99
                        self.match(Grammar_Project_2Parser.SHIFT_RIGHT)
                        self.state = 100
                        self.expression(9)
                        pass

                    elif la_ == 14:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 101
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 102
                        self.match(Grammar_Project_2Parser.BITWISE_AND)
                        self.state = 103
                        self.expression(8)
                        pass

                    elif la_ == 15:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 105
                        self.match(Grammar_Project_2Parser.BITWISE_OR)
                        self.state = 106
                        self.expression(7)
                        pass

                    elif la_ == 16:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 108
                        self.match(Grammar_Project_2Parser.BITWISE_XOR)
                        self.state = 109
                        self.expression(6)
                        pass

                    elif la_ == 17:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 110
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 111
                        self.match(Grammar_Project_2Parser.LOGICAL_AND)
                        self.state = 112
                        self.expression(5)
                        pass

                    elif la_ == 18:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 113
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 114
                        self.match(Grammar_Project_2Parser.LOGICAL_OR)
                        self.state = 115
                        self.expression(4)
                        pass

             
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.LiteralContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_2Parser.PLUS)
            else:
                return self.getToken(Grammar_Project_2Parser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_2Parser.MINUS)
            else:
                return self.getToken(Grammar_Project_2Parser.MINUS, i)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = Grammar_Project_2Parser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8 or _la==9:
                    self.state = 121
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 124
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 125
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 126
                        self.match(Grammar_Project_2Parser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 129 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 131
                    self.match(Grammar_Project_2Parser.PLUS)


                self.state = 134
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 135
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 136
                        self.match(Grammar_Project_2Parser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 139 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 141
                    self.match(Grammar_Project_2Parser.MINUS)


                self.state = 144
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(Grammar_Project_2Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(Grammar_Project_2Parser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(Grammar_Project_2Parser.CHAR, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = Grammar_Project_2Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Grammar_Project_2Parser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.TypeContext,0)


        def pointer(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.PointerContext,0)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = Grammar_Project_2Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 149
                self.type_()
                pass

            elif la_ == 2:
                self.state = 150
                self.pointer()
                pass


            self.state = 153
            self.match(Grammar_Project_2Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Grammar_Project_2Parser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.ExpressionContext,0)


        def type_(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.TypeContext,0)


        def pointer(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.PointerContext,0)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDef" ):
                listener.enterDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDef" ):
                listener.exitDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDef" ):
                return visitor.visitDef(self)
            else:
                return visitor.visitChildren(self)




    def def_(self):

        localctx = Grammar_Project_2Parser.DefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 155
                self.type_()
                pass

            elif la_ == 2:
                self.state = 156
                self.pointer()
                pass


            self.state = 159
            self.match(Grammar_Project_2Parser.IDENTIFIER)
            self.state = 160
            self.match(Grammar_Project_2Parser.T__1)
            self.state = 161
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Grammar_Project_2Parser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_ass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAss" ):
                listener.enterAss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAss" ):
                listener.exitAss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss" ):
                return visitor.visitAss(self)
            else:
                return visitor.visitChildren(self)




    def ass(self):

        localctx = Grammar_Project_2Parser.AssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(Grammar_Project_2Parser.IDENTIFIER)
            self.state = 164
            self.match(Grammar_Project_2Parser.T__1)
            self.state = 165
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.TypeContext,0)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_2Parser.MULT)
            else:
                return self.getToken(Grammar_Project_2Parser.MULT, i)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_pointer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer" ):
                listener.enterPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer" ):
                listener.exitPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer" ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)




    def pointer(self):

        localctx = Grammar_Project_2Parser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.type_()
            self.state = 169 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 168
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 171 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DerefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Grammar_Project_2Parser.IDENTIFIER, 0)

        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_2Parser.MULT)
            else:
                return self.getToken(Grammar_Project_2Parser.MULT, i)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_deref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeref" ):
                listener.enterDeref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeref" ):
                listener.exitDeref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeref" ):
                return visitor.visitDeref(self)
            else:
                return visitor.visitChildren(self)




    def deref(self):

        localctx = Grammar_Project_2Parser.DerefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 173
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 176 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

            self.state = 178
            self.match(Grammar_Project_2Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Grammar_Project_2Parser.IDENTIFIER, 0)

        def BITWISE_AND(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_2Parser.BITWISE_AND)
            else:
                return self.getToken(Grammar_Project_2Parser.BITWISE_AND, i)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_addr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddr" ):
                listener.enterAddr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddr" ):
                listener.exitAddr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddr" ):
                return visitor.visitAddr(self)
            else:
                return visitor.visitChildren(self)




    def addr(self):

        localctx = Grammar_Project_2Parser.AddrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 180
                self.match(Grammar_Project_2Parser.BITWISE_AND)
                self.state = 183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 185
            self.match(Grammar_Project_2Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(Grammar_Project_2Parser.INTTYPE, 0)

        def CHARTYPE(self):
            return self.getToken(Grammar_Project_2Parser.CHARTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(Grammar_Project_2Parser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = Grammar_Project_2Parser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(Grammar_Project_2Parser.CONST, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = Grammar_Project_2Parser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(Grammar_Project_2Parser.CONST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Grammar_Project_2Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = Grammar_Project_2Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(Grammar_Project_2Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 3)
         




