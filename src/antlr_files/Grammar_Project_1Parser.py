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
        4,1,24,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,27,
        8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,83,8,2,10,2,12,2,86,9,2,1,3,1,3,
        1,3,1,3,1,3,3,3,93,8,3,1,3,0,1,4,4,0,2,4,6,0,0,114,0,11,1,0,0,0,
        2,14,1,0,0,0,4,26,1,0,0,0,6,92,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,
        10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,11,1,0,
        0,0,14,15,3,4,2,0,15,16,5,22,0,0,16,3,1,0,0,0,17,18,6,2,-1,0,18,
        27,3,6,3,0,19,20,5,21,0,0,20,27,3,4,2,3,21,22,5,1,0,0,22,23,3,4,
        2,0,23,24,5,2,0,0,24,27,1,0,0,0,25,27,5,23,0,0,26,17,1,0,0,0,26,
        19,1,0,0,0,26,21,1,0,0,0,26,25,1,0,0,0,27,84,1,0,0,0,28,29,10,21,
        0,0,29,30,5,5,0,0,30,83,3,4,2,22,31,32,10,20,0,0,32,33,5,6,0,0,33,
        83,3,4,2,21,34,35,10,19,0,0,35,36,5,7,0,0,36,83,3,4,2,20,37,38,10,
        18,0,0,38,39,5,3,0,0,39,83,3,4,2,19,40,41,10,17,0,0,41,42,5,4,0,
        0,42,83,3,4,2,18,43,44,10,16,0,0,44,45,5,8,0,0,45,83,3,4,2,17,46,
        47,10,15,0,0,47,48,5,9,0,0,48,83,3,4,2,16,49,50,10,14,0,0,50,51,
        5,10,0,0,51,83,3,4,2,15,52,53,10,13,0,0,53,54,5,11,0,0,54,83,3,4,
        2,14,55,56,10,12,0,0,56,57,5,12,0,0,57,83,3,4,2,13,58,59,10,11,0,
        0,59,60,5,13,0,0,60,83,3,4,2,12,61,62,10,10,0,0,62,63,5,14,0,0,63,
        83,3,4,2,11,64,65,10,9,0,0,65,66,5,15,0,0,66,83,3,4,2,10,67,68,10,
        8,0,0,68,69,5,16,0,0,69,83,3,4,2,9,70,71,10,7,0,0,71,72,5,17,0,0,
        72,83,3,4,2,8,73,74,10,6,0,0,74,75,5,18,0,0,75,83,3,4,2,7,76,77,
        10,5,0,0,77,78,5,19,0,0,78,83,3,4,2,6,79,80,10,4,0,0,80,81,5,20,
        0,0,81,83,3,4,2,5,82,28,1,0,0,0,82,31,1,0,0,0,82,34,1,0,0,0,82,37,
        1,0,0,0,82,40,1,0,0,0,82,43,1,0,0,0,82,46,1,0,0,0,82,49,1,0,0,0,
        82,52,1,0,0,0,82,55,1,0,0,0,82,58,1,0,0,0,82,61,1,0,0,0,82,64,1,
        0,0,0,82,67,1,0,0,0,82,70,1,0,0,0,82,73,1,0,0,0,82,76,1,0,0,0,82,
        79,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,5,1,0,0,
        0,86,84,1,0,0,0,87,88,5,3,0,0,88,93,3,4,2,0,89,90,5,4,0,0,90,93,
        3,4,2,0,91,93,5,23,0,0,92,87,1,0,0,0,92,89,1,0,0,0,92,91,1,0,0,0,
        93,7,1,0,0,0,5,11,26,82,84,92
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
                      "SEMICOLON", "INT", "WHITESPACE" ]

    RULE_program = 0
    RULE_programLine = 1
    RULE_expression = 2
    RULE_unaryExpression = 3

    ruleNames =  [ "program", "programLine", "expression", "unaryExpression" ]

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
    WHITESPACE=24

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
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10485786) != 0):
                self.state = 8
                self.programLine()
                self.state = 13
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
            self.state = 14
            self.expression(0)
            self.state = 15
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

        def MULT(self):
            return self.getToken(Grammar_Project_1Parser.MULT, 0)

        def DIV(self):
            return self.getToken(Grammar_Project_1Parser.DIV, 0)

        def MOD(self):
            return self.getToken(Grammar_Project_1Parser.MOD, 0)

        def PLUS(self):
            return self.getToken(Grammar_Project_1Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(Grammar_Project_1Parser.MINUS, 0)

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
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 18
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 19
                self.match(Grammar_Project_1Parser.LOGICAL_NOT)
                self.state = 20
                self.expression(3)
                pass

            elif la_ == 3:
                self.state = 21
                self.match(Grammar_Project_1Parser.LPAREN)
                self.state = 22
                self.expression(0)
                self.state = 23
                self.match(Grammar_Project_1Parser.RPAREN)
                pass

            elif la_ == 4:
                self.state = 25
                self.match(Grammar_Project_1Parser.INT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 82
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 28
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 29
                        self.match(Grammar_Project_1Parser.MULT)
                        self.state = 30
                        self.expression(22)
                        pass

                    elif la_ == 2:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 31
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 32
                        self.match(Grammar_Project_1Parser.DIV)
                        self.state = 33
                        self.expression(21)
                        pass

                    elif la_ == 3:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 34
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 35
                        self.match(Grammar_Project_1Parser.MOD)
                        self.state = 36
                        self.expression(20)
                        pass

                    elif la_ == 4:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 37
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 38
                        self.match(Grammar_Project_1Parser.PLUS)
                        self.state = 39
                        self.expression(19)
                        pass

                    elif la_ == 5:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 40
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 41
                        self.match(Grammar_Project_1Parser.MINUS)
                        self.state = 42
                        self.expression(18)
                        pass

                    elif la_ == 6:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 43
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 44
                        self.match(Grammar_Project_1Parser.GREATER_THAN)
                        self.state = 45
                        self.expression(17)
                        pass

                    elif la_ == 7:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 46
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 47
                        self.match(Grammar_Project_1Parser.LESS_THAN)
                        self.state = 48
                        self.expression(16)
                        pass

                    elif la_ == 8:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 49
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 50
                        self.match(Grammar_Project_1Parser.GREATER_EQUAL)
                        self.state = 51
                        self.expression(15)
                        pass

                    elif la_ == 9:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 52
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 53
                        self.match(Grammar_Project_1Parser.LESS_EQUAL)
                        self.state = 54
                        self.expression(14)
                        pass

                    elif la_ == 10:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 55
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 56
                        self.match(Grammar_Project_1Parser.EQUALS)
                        self.state = 57
                        self.expression(13)
                        pass

                    elif la_ == 11:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 58
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 59
                        self.match(Grammar_Project_1Parser.NOT_EQUAL)
                        self.state = 60
                        self.expression(12)
                        pass

                    elif la_ == 12:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 61
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 62
                        self.match(Grammar_Project_1Parser.SHIFT_LEFT)
                        self.state = 63
                        self.expression(11)
                        pass

                    elif la_ == 13:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 64
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 65
                        self.match(Grammar_Project_1Parser.SHIFT_RIGHT)
                        self.state = 66
                        self.expression(10)
                        pass

                    elif la_ == 14:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 67
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 68
                        self.match(Grammar_Project_1Parser.BITWISE_AND)
                        self.state = 69
                        self.expression(9)
                        pass

                    elif la_ == 15:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 70
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 71
                        self.match(Grammar_Project_1Parser.BITWISE_OR)
                        self.state = 72
                        self.expression(8)
                        pass

                    elif la_ == 16:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 73
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 74
                        self.match(Grammar_Project_1Parser.BITWISE_XOR)
                        self.state = 75
                        self.expression(7)
                        pass

                    elif la_ == 17:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 76
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 77
                        self.match(Grammar_Project_1Parser.LOGICAL_AND)
                        self.state = 78
                        self.expression(6)
                        pass

                    elif la_ == 18:
                        localctx = Grammar_Project_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 79
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 80
                        self.match(Grammar_Project_1Parser.LOGICAL_OR)
                        self.state = 81
                        self.expression(5)
                        pass

             
                self.state = 86
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

        def PLUS(self):
            return self.getToken(Grammar_Project_1Parser.PLUS, 0)

        def expression(self):
            return self.getTypedRuleContext(Grammar_Project_1Parser.ExpressionContext,0)


        def MINUS(self):
            return self.getToken(Grammar_Project_1Parser.MINUS, 0)

        def INT(self):
            return self.getToken(Grammar_Project_1Parser.INT, 0)

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
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(Grammar_Project_1Parser.PLUS)
                self.state = 88
                self.expression(0)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(Grammar_Project_1Parser.MINUS)
                self.state = 90
                self.expression(0)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(Grammar_Project_1Parser.INT)
                pass
            else:
                raise NoViableAltException(self)

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
         




