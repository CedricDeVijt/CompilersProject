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
        4,1,34,182,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,1,1,1,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,55,8,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,5,3,111,8,3,10,3,12,3,114,9,3,1,4,3,4,117,8,4,1,
        4,1,4,1,4,4,4,122,8,4,11,4,12,4,123,1,4,3,4,127,8,4,1,4,1,4,1,4,
        4,4,132,8,4,11,4,12,4,133,1,4,3,4,137,8,4,1,4,3,4,140,8,4,1,5,1,
        5,1,6,1,6,3,6,146,8,6,1,6,1,6,1,7,1,7,3,7,152,8,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,9,1,9,4,9,164,8,9,11,9,12,9,165,1,10,4,10,169,
        8,10,11,10,12,10,170,1,10,1,10,1,11,4,11,176,8,11,11,11,12,11,177,
        1,11,1,11,1,11,0,1,6,12,0,2,4,6,8,10,12,14,16,18,20,22,0,2,1,0,11,
        12,1,0,31,33,206,0,24,1,0,0,0,2,26,1,0,0,0,4,39,1,0,0,0,6,54,1,0,
        0,0,8,139,1,0,0,0,10,141,1,0,0,0,12,145,1,0,0,0,14,151,1,0,0,0,16,
        157,1,0,0,0,18,161,1,0,0,0,20,168,1,0,0,0,22,175,1,0,0,0,24,25,3,
        2,1,0,25,1,1,0,0,0,26,27,5,1,0,0,27,28,5,2,0,0,28,29,5,7,0,0,29,
        30,5,8,0,0,30,34,5,9,0,0,31,33,3,4,2,0,32,31,1,0,0,0,33,36,1,0,0,
        0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,
        5,10,0,0,38,3,1,0,0,0,39,40,3,6,3,0,40,41,5,30,0,0,41,5,1,0,0,0,
        42,43,6,3,-1,0,43,55,3,8,4,0,44,55,5,6,0,0,45,55,3,20,10,0,46,55,
        3,22,11,0,47,48,5,29,0,0,48,55,3,6,3,21,49,50,5,7,0,0,50,51,3,6,
        3,0,51,52,5,8,0,0,52,55,1,0,0,0,53,55,5,31,0,0,54,42,1,0,0,0,54,
        44,1,0,0,0,54,45,1,0,0,0,54,46,1,0,0,0,54,47,1,0,0,0,54,49,1,0,0,
        0,54,53,1,0,0,0,55,112,1,0,0,0,56,57,10,20,0,0,57,58,5,14,0,0,58,
        111,3,6,3,21,59,60,10,19,0,0,60,61,5,15,0,0,61,111,3,6,3,20,62,63,
        10,18,0,0,63,64,5,13,0,0,64,111,3,6,3,19,65,66,10,17,0,0,66,67,5,
        12,0,0,67,111,3,6,3,18,68,69,10,16,0,0,69,70,5,11,0,0,70,111,3,6,
        3,17,71,72,10,15,0,0,72,73,5,16,0,0,73,111,3,6,3,16,74,75,10,14,
        0,0,75,76,5,17,0,0,76,111,3,6,3,15,77,78,10,13,0,0,78,79,5,18,0,
        0,79,111,3,6,3,14,80,81,10,12,0,0,81,82,5,19,0,0,82,111,3,6,3,13,
        83,84,10,11,0,0,84,85,5,20,0,0,85,111,3,6,3,12,86,87,10,10,0,0,87,
        88,5,21,0,0,88,111,3,6,3,11,89,90,10,9,0,0,90,91,5,22,0,0,91,111,
        3,6,3,10,92,93,10,8,0,0,93,94,5,23,0,0,94,111,3,6,3,9,95,96,10,7,
        0,0,96,97,5,24,0,0,97,111,3,6,3,8,98,99,10,6,0,0,99,100,5,25,0,0,
        100,111,3,6,3,7,101,102,10,5,0,0,102,103,5,26,0,0,103,111,3,6,3,
        6,104,105,10,4,0,0,105,106,5,27,0,0,106,111,3,6,3,5,107,108,10,3,
        0,0,108,109,5,28,0,0,109,111,3,6,3,4,110,56,1,0,0,0,110,59,1,0,0,
        0,110,62,1,0,0,0,110,65,1,0,0,0,110,68,1,0,0,0,110,71,1,0,0,0,110,
        74,1,0,0,0,110,77,1,0,0,0,110,80,1,0,0,0,110,83,1,0,0,0,110,86,1,
        0,0,0,110,89,1,0,0,0,110,92,1,0,0,0,110,95,1,0,0,0,110,98,1,0,0,
        0,110,101,1,0,0,0,110,104,1,0,0,0,110,107,1,0,0,0,111,114,1,0,0,
        0,112,110,1,0,0,0,112,113,1,0,0,0,113,7,1,0,0,0,114,112,1,0,0,0,
        115,117,7,0,0,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,
        118,140,3,10,5,0,119,120,5,11,0,0,120,122,5,12,0,0,121,119,1,0,0,
        0,122,123,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,
        0,125,127,5,11,0,0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,
        0,128,140,3,10,5,0,129,130,5,12,0,0,130,132,5,11,0,0,131,129,1,0,
        0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,
        0,0,135,137,5,12,0,0,136,135,1,0,0,0,136,137,1,0,0,0,137,138,1,0,
        0,0,138,140,3,10,5,0,139,116,1,0,0,0,139,121,1,0,0,0,139,131,1,0,
        0,0,140,9,1,0,0,0,141,142,7,1,0,0,142,11,1,0,0,0,143,146,5,4,0,0,
        144,146,3,18,9,0,145,143,1,0,0,0,145,144,1,0,0,0,146,147,1,0,0,0,
        147,148,5,6,0,0,148,13,1,0,0,0,149,152,5,4,0,0,150,152,3,18,9,0,
        151,149,1,0,0,0,151,150,1,0,0,0,152,153,1,0,0,0,153,154,5,6,0,0,
        154,155,5,3,0,0,155,156,3,6,3,0,156,15,1,0,0,0,157,158,5,6,0,0,158,
        159,5,3,0,0,159,160,3,6,3,0,160,17,1,0,0,0,161,163,5,4,0,0,162,164,
        5,13,0,0,163,162,1,0,0,0,164,165,1,0,0,0,165,163,1,0,0,0,165,166,
        1,0,0,0,166,19,1,0,0,0,167,169,5,13,0,0,168,167,1,0,0,0,169,170,
        1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,
        5,6,0,0,173,21,1,0,0,0,174,176,5,24,0,0,175,174,1,0,0,0,176,177,
        1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,180,
        5,6,0,0,180,23,1,0,0,0,15,34,54,110,112,116,123,126,133,136,139,
        145,151,165,170,177
    ]

class Grammar_Project_2Parser ( Parser ):

    grammarFileName = "Grammar_Project_2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'='", "<INVALID>", 
                     "'const'", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", 
                     "'<='", "'=='", "'!='", "'<<'", "'>>'", "'&'", "'|'", 
                     "'^'", "'&&'", "'||'", "'!'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TYPE", "CONST", "IDENTIFIER", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
                      "LESS_EQUAL", "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", 
                      "SHIFT_RIGHT", "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", 
                      "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", "SEMICOLON", 
                      "INT", "FLOAT", "CHAR", "WHITESPACE" ]

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

    ruleNames =  [ "program", "main", "statement", "expression", "unaryExpression", 
                   "literal", "decl", "def", "ass", "pointer", "deref", 
                   "addr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TYPE=4
    CONST=5
    IDENTIFIER=6
    LPAREN=7
    RPAREN=8
    LBRACE=9
    RBRACE=10
    PLUS=11
    MINUS=12
    MULT=13
    DIV=14
    MOD=15
    GREATER_THAN=16
    LESS_THAN=17
    GREATER_EQUAL=18
    LESS_EQUAL=19
    EQUALS=20
    NOT_EQUAL=21
    SHIFT_LEFT=22
    SHIFT_RIGHT=23
    BITWISE_AND=24
    BITWISE_OR=25
    BITWISE_XOR=26
    LOGICAL_AND=27
    LOGICAL_OR=28
    LOGICAL_NOT=29
    SEMICOLON=30
    INT=31
    FLOAT=32
    CHAR=33
    WHITESPACE=34

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
            self.state = 24
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
            self.state = 26
            self.match(Grammar_Project_2Parser.T__0)
            self.state = 27
            self.match(Grammar_Project_2Parser.T__1)
            self.state = 28
            self.match(Grammar_Project_2Parser.LPAREN)
            self.state = 29
            self.match(Grammar_Project_2Parser.RPAREN)
            self.state = 30
            self.match(Grammar_Project_2Parser.LBRACE)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15586048192) != 0):
                self.state = 31
                self.statement()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
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
            self.state = 39
            self.expression(0)
            self.state = 40
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
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 43
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 44
                self.match(Grammar_Project_2Parser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 45
                self.deref()
                pass

            elif la_ == 4:
                self.state = 46
                self.addr()
                pass

            elif la_ == 5:
                self.state = 47
                self.match(Grammar_Project_2Parser.LOGICAL_NOT)
                self.state = 48
                self.expression(21)
                pass

            elif la_ == 6:
                self.state = 49
                self.match(Grammar_Project_2Parser.LPAREN)
                self.state = 50
                self.expression(0)
                self.state = 51
                self.match(Grammar_Project_2Parser.RPAREN)
                pass

            elif la_ == 7:
                self.state = 53
                self.match(Grammar_Project_2Parser.INT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 56
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 57
                        self.match(Grammar_Project_2Parser.DIV)
                        self.state = 58
                        self.expression(21)
                        pass

                    elif la_ == 2:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 59
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 60
                        self.match(Grammar_Project_2Parser.MOD)
                        self.state = 61
                        self.expression(20)
                        pass

                    elif la_ == 3:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 62
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 63
                        self.match(Grammar_Project_2Parser.MULT)
                        self.state = 64
                        self.expression(19)
                        pass

                    elif la_ == 4:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 65
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 66
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 67
                        self.expression(18)
                        pass

                    elif la_ == 5:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 68
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 69
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 70
                        self.expression(17)
                        pass

                    elif la_ == 6:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 71
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 72
                        self.match(Grammar_Project_2Parser.GREATER_THAN)
                        self.state = 73
                        self.expression(16)
                        pass

                    elif la_ == 7:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 74
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 75
                        self.match(Grammar_Project_2Parser.LESS_THAN)
                        self.state = 76
                        self.expression(15)
                        pass

                    elif la_ == 8:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 77
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 78
                        self.match(Grammar_Project_2Parser.GREATER_EQUAL)
                        self.state = 79
                        self.expression(14)
                        pass

                    elif la_ == 9:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 80
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 81
                        self.match(Grammar_Project_2Parser.LESS_EQUAL)
                        self.state = 82
                        self.expression(13)
                        pass

                    elif la_ == 10:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 83
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 84
                        self.match(Grammar_Project_2Parser.EQUALS)
                        self.state = 85
                        self.expression(12)
                        pass

                    elif la_ == 11:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 86
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 87
                        self.match(Grammar_Project_2Parser.NOT_EQUAL)
                        self.state = 88
                        self.expression(11)
                        pass

                    elif la_ == 12:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 89
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 90
                        self.match(Grammar_Project_2Parser.SHIFT_LEFT)
                        self.state = 91
                        self.expression(10)
                        pass

                    elif la_ == 13:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 93
                        self.match(Grammar_Project_2Parser.SHIFT_RIGHT)
                        self.state = 94
                        self.expression(9)
                        pass

                    elif la_ == 14:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 95
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 96
                        self.match(Grammar_Project_2Parser.BITWISE_AND)
                        self.state = 97
                        self.expression(8)
                        pass

                    elif la_ == 15:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 98
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 99
                        self.match(Grammar_Project_2Parser.BITWISE_OR)
                        self.state = 100
                        self.expression(7)
                        pass

                    elif la_ == 16:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 101
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 102
                        self.match(Grammar_Project_2Parser.BITWISE_XOR)
                        self.state = 103
                        self.expression(6)
                        pass

                    elif la_ == 17:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 105
                        self.match(Grammar_Project_2Parser.LOGICAL_AND)
                        self.state = 106
                        self.expression(5)
                        pass

                    elif la_ == 18:
                        localctx = Grammar_Project_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 108
                        self.match(Grammar_Project_2Parser.LOGICAL_OR)
                        self.state = 109
                        self.expression(4)
                        pass

             
                self.state = 114
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11 or _la==12:
                    self.state = 115
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 118
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 119
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 120
                        self.match(Grammar_Project_2Parser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 123 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 125
                    self.match(Grammar_Project_2Parser.PLUS)


                self.state = 128
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 129
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 130
                        self.match(Grammar_Project_2Parser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 133 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 135
                    self.match(Grammar_Project_2Parser.MINUS)


                self.state = 138
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
            self.state = 141
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


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Grammar_Project_2Parser.IDENTIFIER, 0)

        def TYPE(self):
            return self.getToken(Grammar_Project_2Parser.TYPE, 0)

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
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 143
                self.match(Grammar_Project_2Parser.TYPE)
                pass

            elif la_ == 2:
                self.state = 144
                self.pointer()
                pass


            self.state = 147
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


        def TYPE(self):
            return self.getToken(Grammar_Project_2Parser.TYPE, 0)

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
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 149
                self.match(Grammar_Project_2Parser.TYPE)
                pass

            elif la_ == 2:
                self.state = 150
                self.pointer()
                pass


            self.state = 153
            self.match(Grammar_Project_2Parser.IDENTIFIER)
            self.state = 154
            self.match(Grammar_Project_2Parser.T__2)
            self.state = 155
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
            self.state = 157
            self.match(Grammar_Project_2Parser.IDENTIFIER)
            self.state = 158
            self.match(Grammar_Project_2Parser.T__2)
            self.state = 159
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

        def TYPE(self):
            return self.getToken(Grammar_Project_2Parser.TYPE, 0)

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
            self.state = 161
            self.match(Grammar_Project_2Parser.TYPE)
            self.state = 163 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 162
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
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
            self.state = 168 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 167
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

            self.state = 172
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
            self.state = 175 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 174
                self.match(Grammar_Project_2Parser.BITWISE_AND)
                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

            self.state = 179
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
         




