# Generated from grammars/Grammar_Project_1.g4 by ANTLR 4.13.1
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
        4,1,25,118,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,29,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,85,8,2,10,2,12,2,88,9,2,
        1,3,3,3,91,8,3,1,3,1,3,1,3,4,3,96,8,3,11,3,12,3,97,1,3,3,3,101,8,
        3,1,3,1,3,1,3,4,3,106,8,3,11,3,12,3,107,1,3,3,3,111,8,3,1,3,3,3,
        114,8,3,1,4,1,4,1,4,0,1,4,5,0,2,4,6,8,0,1,1,0,3,4,141,0,13,1,0,0,
        0,2,16,1,0,0,0,4,28,1,0,0,0,6,113,1,0,0,0,8,115,1,0,0,0,10,12,3,
        2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,
        1,1,0,0,0,15,13,1,0,0,0,16,17,3,4,2,0,17,18,5,22,0,0,18,3,1,0,0,
        0,19,20,6,2,-1,0,20,29,3,6,3,0,21,22,5,21,0,0,22,29,3,4,2,3,23,24,
        5,1,0,0,24,25,3,4,2,0,25,26,5,2,0,0,26,29,1,0,0,0,27,29,5,23,0,0,
        28,19,1,0,0,0,28,21,1,0,0,0,28,23,1,0,0,0,28,27,1,0,0,0,29,86,1,
        0,0,0,30,31,10,21,0,0,31,32,5,6,0,0,32,85,3,4,2,22,33,34,10,20,0,
        0,34,35,5,7,0,0,35,85,3,4,2,21,36,37,10,19,0,0,37,38,5,5,0,0,38,
        85,3,4,2,20,39,40,10,18,0,0,40,41,5,4,0,0,41,85,3,4,2,19,42,43,10,
        17,0,0,43,44,5,3,0,0,44,85,3,4,2,18,45,46,10,16,0,0,46,47,5,8,0,
        0,47,85,3,4,2,17,48,49,10,15,0,0,49,50,5,9,0,0,50,85,3,4,2,16,51,
        52,10,14,0,0,52,53,5,10,0,0,53,85,3,4,2,15,54,55,10,13,0,0,55,56,
        5,11,0,0,56,85,3,4,2,14,57,58,10,12,0,0,58,59,5,12,0,0,59,85,3,4,
        2,13,60,61,10,11,0,0,61,62,5,13,0,0,62,85,3,4,2,12,63,64,10,10,0,
        0,64,65,5,14,0,0,65,85,3,4,2,11,66,67,10,9,0,0,67,68,5,15,0,0,68,
        85,3,4,2,10,69,70,10,8,0,0,70,71,5,16,0,0,71,85,3,4,2,9,72,73,10,
        7,0,0,73,74,5,17,0,0,74,85,3,4,2,8,75,76,10,6,0,0,76,77,5,18,0,0,
        77,85,3,4,2,7,78,79,10,5,0,0,79,80,5,19,0,0,80,85,3,4,2,6,81,82,
        10,4,0,0,82,83,5,20,0,0,83,85,3,4,2,5,84,30,1,0,0,0,84,33,1,0,0,
        0,84,36,1,0,0,0,84,39,1,0,0,0,84,42,1,0,0,0,84,45,1,0,0,0,84,48,
        1,0,0,0,84,51,1,0,0,0,84,54,1,0,0,0,84,57,1,0,0,0,84,60,1,0,0,0,
        84,63,1,0,0,0,84,66,1,0,0,0,84,69,1,0,0,0,84,72,1,0,0,0,84,75,1,
        0,0,0,84,78,1,0,0,0,84,81,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,
        87,1,0,0,0,87,5,1,0,0,0,88,86,1,0,0,0,89,91,7,0,0,0,90,89,1,0,0,
        0,90,91,1,0,0,0,91,92,1,0,0,0,92,114,3,8,4,0,93,94,5,3,0,0,94,96,
        5,4,0,0,95,93,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,
        98,100,1,0,0,0,99,101,5,3,0,0,100,99,1,0,0,0,100,101,1,0,0,0,101,
        102,1,0,0,0,102,114,3,8,4,0,103,104,5,4,0,0,104,106,5,3,0,0,105,
        103,1,0,0,0,106,107,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,
        110,1,0,0,0,109,111,5,4,0,0,110,109,1,0,0,0,110,111,1,0,0,0,111,
        112,1,0,0,0,112,114,3,8,4,0,113,90,1,0,0,0,113,95,1,0,0,0,113,105,
        1,0,0,0,114,7,1,0,0,0,115,116,5,23,0,0,116,9,1,0,0,0,10,13,28,84,
        86,90,97,100,107,110,113
    ]

class Grammar_Project_1Parser ( Parser ):

    grammarFileName = "Grammar_Project_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'<<'", "'>>'", "'&'", "'|'", "'^'", "'&&'", "'||'", 
                     "'!'", "';'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "PLUS", "MINUS", 
                      "MULT", "DIV", "MOD", "GREATER_THAN", "LESS_THAN", 
                      "GREATER_EQUAL", "LESS_EQUAL", "EQUALS", "NOT_EQUAL", 
                      "SHIFT_LEFT", "SHIFT_RIGHT", "BITWISE_AND", "BITWISE_OR", 
                      "BITWISE_XOR", "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", 
                      "SEMICOLON", "INT", "FLOAT", "WHITESPACE" ]

    RULE_program = 0
    RULE_programLine = 1
    RULE_expression = 2
    RULE_unaryExpression = 3
    RULE_number = 4

    ruleNames =  [ "program", "programLine", "expression", "unaryExpression", 
                   "number" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    PLUS=3
    MINUS=4
    MULT=5
    DIV=6
    MOD=7
    GREATER_THAN=8
    LESS_THAN=9
    GREATER_EQUAL=10
    LESS_EQUAL=11
    EQUALS=12
    NOT_EQUAL=13
    SHIFT_LEFT=14
    SHIFT_RIGHT=15
    BITWISE_AND=16
    BITWISE_OR=17
    BITWISE_XOR=18
    LOGICAL_AND=19
    LOGICAL_OR=20
    LOGICAL_NOT=21
    SEMICOLON=22
    INT=23
    FLOAT=24
    WHITESPACE=25

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

        def programLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_1Parser.ProgramLineContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_1Parser.ProgramLineContext,i)


        def getRuleIndex(self):
            return Grammar_Project_1Parser.RULE_program

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

        localctx = Grammar_Project_1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10485786) != 0):
                self.state = 10
                self.programLine()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Grammar_Project_1Parser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(Grammar_Project_1Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return Grammar_Project_1Parser.RULE_programLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramLine" ):
                listener.enterProgramLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramLine" ):
                listener.exitProgramLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramLine" ):
                return visitor.visitProgramLine(self)
            else:
                return visitor.visitChildren(self)




    def programLine(self):

        localctx = Grammar_Project_1Parser.ProgramLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.expression(0)
            self.state = 17
            self.match(Grammar_Project_1Parser.SEMICOLON)
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
            return self.getTypedRuleContext(Grammar_Project_1Parser.UnaryExpressionContext,0)


        def LOGICAL_NOT(self):
            return self.getToken(Grammar_Project_1Parser.LOGICAL_NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_1Parser.ExpressionContext,i)


        def LPAREN(self):
            return self.getToken(Grammar_Project_1Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Grammar_Project_1Parser.RPAREN, 0)

        def INT(self):
            return self.getToken(Grammar_Project_1Parser.INT, 0)

        def DIV(self):
            return self.getToken(Grammar_Project_1Parser.DIV, 0)

        def MOD(self):
            return self.getToken(Grammar_Project_1Parser.MOD, 0)

        def MULT(self):
            return self.getToken(Grammar_Project_1Parser.MULT, 0)

        def MINUS(self):
            return self.getToken(Grammar_Project_1Parser.MINUS, 0)

        def PLUS(self):
            return self.getToken(Grammar_Project_1Parser.PLUS, 0)

        def GREATER_THAN(self):
            return self.getToken(Grammar_Project_1Parser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(Grammar_Project_1Parser.LESS_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(Grammar_Project_1Parser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(Grammar_Project_1Parser.LESS_EQUAL, 0)

        def EQUALS(self):
            return self.getToken(Grammar_Project_1Parser.EQUALS, 0)

        def NOT_EQUAL(self):
            return self.getToken(Grammar_Project_1Parser.NOT_EQUAL, 0)

        def SHIFT_LEFT(self):
            return self.getToken(Grammar_Project_1Parser.SHIFT_LEFT, 0)

        def SHIFT_RIGHT(self):
            return self.getToken(Grammar_Project_1Parser.SHIFT_RIGHT, 0)

        def BITWISE_AND(self):
            return self.getToken(Grammar_Project_1Parser.BITWISE_AND, 0)

        def BITWISE_OR(self):
            return self.getToken(Grammar_Project_1Parser.BITWISE_OR, 0)

        def BITWISE_XOR(self):
            return self.getToken(Grammar_Project_1Parser.BITWISE_XOR, 0)

        def LOGICAL_AND(self):
            return self.getToken(Grammar_Project_1Parser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(Grammar_Project_1Parser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return Grammar_Project_1Parser.RULE_expression

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
        localctx = Grammar_Project_1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 20
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 21
                self.match(Grammar_Project_1Parser.LOGICAL_NOT)
                self.state = 22
                self.expression(3)
                pass

            elif la_ == 3:
                self.state = 23
                self.match(Grammar_Project_1Parser.LPAREN)
                self.state = 24
                self.expression(0)
                self.state = 25
                self.match(Grammar_Project_1Parser.RPAREN)
                pass

            elif la_ == 4:
                self.state = 27
                self.match(Grammar_Project_1Parser.INT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 30
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 31
                        self.match(Grammar_Project_1Parser.DIV)
                        self.state = 32
                        self.expression(22)
                        pass

                    elif la_ == 2:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 33
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 34
                        self.match(Grammar_Project_1Parser.MOD)
                        self.state = 35
                        self.expression(21)
                        pass

                    elif la_ == 3:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 36
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 37
                        self.match(Grammar_Project_1Parser.MULT)
                        self.state = 38
                        self.expression(20)
                        pass

                    elif la_ == 4:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 39
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 40
                        self.match(Grammar_Project_1Parser.MINUS)
                        self.state = 41
                        self.expression(19)
                        pass

                    elif la_ == 5:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 42
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 43
                        self.match(Grammar_Project_1Parser.PLUS)
                        self.state = 44
                        self.expression(18)
                        pass

                    elif la_ == 6:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 45
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 46
                        self.match(Grammar_Project_1Parser.GREATER_THAN)
                        self.state = 47
                        self.expression(17)
                        pass

                    elif la_ == 7:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 48
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 49
                        self.match(Grammar_Project_1Parser.LESS_THAN)
                        self.state = 50
                        self.expression(16)
                        pass

                    elif la_ == 8:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 51
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 52
                        self.match(Grammar_Project_1Parser.GREATER_EQUAL)
                        self.state = 53
                        self.expression(15)
                        pass

                    elif la_ == 9:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 55
                        self.match(Grammar_Project_1Parser.LESS_EQUAL)
                        self.state = 56
                        self.expression(14)
                        pass

                    elif la_ == 10:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 58
                        self.match(Grammar_Project_1Parser.EQUALS)
                        self.state = 59
                        self.expression(13)
                        pass

                    elif la_ == 11:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 60
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 61
                        self.match(Grammar_Project_1Parser.NOT_EQUAL)
                        self.state = 62
                        self.expression(12)
                        pass

                    elif la_ == 12:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 64
                        self.match(Grammar_Project_1Parser.SHIFT_LEFT)
                        self.state = 65
                        self.expression(11)
                        pass

                    elif la_ == 13:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 66
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 67
                        self.match(Grammar_Project_1Parser.SHIFT_RIGHT)
                        self.state = 68
                        self.expression(10)
                        pass

                    elif la_ == 14:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 69
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 70
                        self.match(Grammar_Project_1Parser.BITWISE_AND)
                        self.state = 71
                        self.expression(9)
                        pass

                    elif la_ == 15:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 72
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 73
                        self.match(Grammar_Project_1Parser.BITWISE_OR)
                        self.state = 74
                        self.expression(8)
                        pass

                    elif la_ == 16:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 75
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 76
                        self.match(Grammar_Project_1Parser.BITWISE_XOR)
                        self.state = 77
                        self.expression(7)
                        pass

                    elif la_ == 17:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 78
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 79
                        self.match(Grammar_Project_1Parser.LOGICAL_AND)
                        self.state = 80
                        self.expression(6)
                        pass

                    elif la_ == 18:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 81
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 82
                        self.match(Grammar_Project_1Parser.LOGICAL_OR)
                        self.state = 83
                        self.expression(5)
                        pass

             
                self.state = 88
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

        def number(self):
            return self.getTypedRuleContext(Grammar_Project_1Parser.NumberContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_1Parser.PLUS)
            else:
                return self.getToken(Grammar_Project_1Parser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_1Parser.MINUS)
            else:
                return self.getToken(Grammar_Project_1Parser.MINUS, i)

        def getRuleIndex(self):
            return Grammar_Project_1Parser.RULE_unaryExpression

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

        localctx = Grammar_Project_1Parser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3 or _la==4:
                    self.state = 89
                    _la = self._input.LA(1)
                    if not(_la==3 or _la==4):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 92
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 93
                        self.match(Grammar_Project_1Parser.PLUS)
                        self.state = 94
                        self.match(Grammar_Project_1Parser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 97 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 99
                    self.match(Grammar_Project_1Parser.PLUS)


                self.state = 102
                self.number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 103
                        self.match(Grammar_Project_1Parser.MINUS)
                        self.state = 104
                        self.match(Grammar_Project_1Parser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 107 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 109
                    self.match(Grammar_Project_1Parser.MINUS)


                self.state = 112
                self.number()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(Grammar_Project_1Parser.INT, 0)

        def getRuleIndex(self):
            return Grammar_Project_1Parser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = Grammar_Project_1Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(Grammar_Project_1Parser.INT)
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
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 4)
         




