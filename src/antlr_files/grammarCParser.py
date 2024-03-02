# Generated from ../../grammars/grammarC.g4 by ANTLR 4.13.1
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
        4,1,25,111,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,26,8,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,67,8,2,10,2,12,2,70,9,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,81,8,3,10,3,12,3,84,9,3,1,4,1,
        4,1,4,1,4,1,4,1,4,3,4,92,8,4,1,4,3,4,95,8,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,5,4,106,8,4,10,4,12,4,109,9,4,1,4,0,3,4,6,8,5,0,
        2,4,6,8,0,0,128,0,13,1,0,0,0,2,16,1,0,0,0,4,25,1,0,0,0,6,71,1,0,
        0,0,8,94,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,
        1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,13,1,0,0,0,16,17,3,4,2,0,17,
        18,5,24,0,0,18,3,1,0,0,0,19,20,6,2,-1,0,20,21,5,15,0,0,21,26,3,4,
        2,8,22,23,5,20,0,0,23,26,3,4,2,2,24,26,3,6,3,0,25,19,1,0,0,0,25,
        22,1,0,0,0,25,24,1,0,0,0,26,68,1,0,0,0,27,28,10,16,0,0,28,29,5,7,
        0,0,29,67,3,4,2,17,30,31,10,15,0,0,31,32,5,8,0,0,32,67,3,4,2,16,
        33,34,10,14,0,0,34,35,5,9,0,0,35,67,3,4,2,15,36,37,10,13,0,0,37,
        38,5,10,0,0,38,67,3,4,2,14,39,40,10,12,0,0,40,41,5,11,0,0,41,67,
        3,4,2,13,42,43,10,11,0,0,43,44,5,12,0,0,44,67,3,4,2,12,45,46,10,
        10,0,0,46,47,5,13,0,0,47,67,3,4,2,11,48,49,10,9,0,0,49,50,5,14,0,
        0,50,67,3,4,2,10,51,52,10,7,0,0,52,53,5,16,0,0,53,67,3,4,2,8,54,
        55,10,6,0,0,55,56,5,17,0,0,56,67,3,4,2,7,57,58,10,5,0,0,58,59,5,
        18,0,0,59,67,3,4,2,6,60,61,10,4,0,0,61,62,5,19,0,0,62,67,3,4,2,5,
        63,64,10,3,0,0,64,65,5,21,0,0,65,67,3,4,2,4,66,27,1,0,0,0,66,30,
        1,0,0,0,66,33,1,0,0,0,66,36,1,0,0,0,66,39,1,0,0,0,66,42,1,0,0,0,
        66,45,1,0,0,0,66,48,1,0,0,0,66,51,1,0,0,0,66,54,1,0,0,0,66,57,1,
        0,0,0,66,60,1,0,0,0,66,63,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,
        69,1,0,0,0,69,5,1,0,0,0,70,68,1,0,0,0,71,72,6,3,-1,0,72,73,3,8,4,
        0,73,82,1,0,0,0,74,75,10,3,0,0,75,76,5,2,0,0,76,81,3,6,3,4,77,78,
        10,2,0,0,78,79,5,3,0,0,79,81,3,6,3,3,80,74,1,0,0,0,80,77,1,0,0,0,
        81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,7,1,0,0,0,84,82,1,0,
        0,0,85,86,6,4,-1,0,86,87,5,22,0,0,87,88,3,4,2,0,88,89,5,23,0,0,89,
        95,1,0,0,0,90,92,5,3,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,93,1,0,0,
        0,93,95,5,1,0,0,94,85,1,0,0,0,94,91,1,0,0,0,95,107,1,0,0,0,96,97,
        10,4,0,0,97,98,5,4,0,0,98,106,3,8,4,5,99,100,10,3,0,0,100,101,5,
        5,0,0,101,106,3,8,4,4,102,103,10,2,0,0,103,104,5,6,0,0,104,106,3,
        8,4,3,105,96,1,0,0,0,105,99,1,0,0,0,105,102,1,0,0,0,106,109,1,0,
        0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,9,1,0,0,0,109,107,1,0,0,
        0,10,13,25,66,68,80,82,91,94,105,107
    ]

class grammarCParser ( Parser ):

    grammarFileName = "grammarC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'>'", "'<'", "'=='", "'>='", "'<='", "'!='", 
                     "'&&'", "'||'", "'!'", "'<<'", "'>>'", "'&'", "'|'", 
                     "'~'", "'^'", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULO", "GT", "LT", "EQ", "GTE", "LTE", 
                      "NEQ", "AND", "OR", "NOT", "LSHIFT", "RSHIFT", "BIT_AND", 
                      "BIT_OR", "BIT_NOT", "BIT_XOR", "LPAREN", "RPAREN", 
                      "SEMICOLON", "WS" ]

    RULE_start = 0
    RULE_programLine = 1
    RULE_expression = 2
    RULE_operation = 3
    RULE_term = 4

    ruleNames =  [ "start", "programLine", "expression", "operation", "term" ]

    EOF = Token.EOF
    INTEGER=1
    PLUS=2
    MINUS=3
    MULTIPLY=4
    DIVIDE=5
    MODULO=6
    GT=7
    LT=8
    EQ=9
    GTE=10
    LTE=11
    NEQ=12
    AND=13
    OR=14
    NOT=15
    LSHIFT=16
    RSHIFT=17
    BIT_AND=18
    BIT_OR=19
    BIT_NOT=20
    BIT_XOR=21
    LPAREN=22
    RPAREN=23
    SEMICOLON=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.ProgramLineContext)
            else:
                return self.getTypedRuleContext(grammarCParser.ProgramLineContext,i)


        def getRuleIndex(self):
            return grammarCParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = grammarCParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5275658) != 0):
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
            return self.getTypedRuleContext(grammarCParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(grammarCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return grammarCParser.RULE_programLine

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

        localctx = grammarCParser.ProgramLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.expression(0)
            self.state = 17
            self.match(grammarCParser.SEMICOLON)
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

        def NOT(self):
            return self.getToken(grammarCParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grammarCParser.ExpressionContext,i)


        def BIT_NOT(self):
            return self.getToken(grammarCParser.BIT_NOT, 0)

        def operation(self):
            return self.getTypedRuleContext(grammarCParser.OperationContext,0)


        def GT(self):
            return self.getToken(grammarCParser.GT, 0)

        def LT(self):
            return self.getToken(grammarCParser.LT, 0)

        def EQ(self):
            return self.getToken(grammarCParser.EQ, 0)

        def GTE(self):
            return self.getToken(grammarCParser.GTE, 0)

        def LTE(self):
            return self.getToken(grammarCParser.LTE, 0)

        def NEQ(self):
            return self.getToken(grammarCParser.NEQ, 0)

        def AND(self):
            return self.getToken(grammarCParser.AND, 0)

        def OR(self):
            return self.getToken(grammarCParser.OR, 0)

        def LSHIFT(self):
            return self.getToken(grammarCParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(grammarCParser.RSHIFT, 0)

        def BIT_AND(self):
            return self.getToken(grammarCParser.BIT_AND, 0)

        def BIT_OR(self):
            return self.getToken(grammarCParser.BIT_OR, 0)

        def BIT_XOR(self):
            return self.getToken(grammarCParser.BIT_XOR, 0)

        def getRuleIndex(self):
            return grammarCParser.RULE_expression

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
        localctx = grammarCParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 20
                self.match(grammarCParser.NOT)
                self.state = 21
                self.expression(8)
                pass
            elif token in [20]:
                self.state = 22
                self.match(grammarCParser.BIT_NOT)
                self.state = 23
                self.expression(2)
                pass
            elif token in [1, 3, 22]:
                self.state = 24
                self.operation(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 27
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 28
                        self.match(grammarCParser.GT)
                        self.state = 29
                        self.expression(17)
                        pass

                    elif la_ == 2:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 30
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 31
                        self.match(grammarCParser.LT)
                        self.state = 32
                        self.expression(16)
                        pass

                    elif la_ == 3:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 33
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 34
                        self.match(grammarCParser.EQ)
                        self.state = 35
                        self.expression(15)
                        pass

                    elif la_ == 4:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 36
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 37
                        self.match(grammarCParser.GTE)
                        self.state = 38
                        self.expression(14)
                        pass

                    elif la_ == 5:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 39
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 40
                        self.match(grammarCParser.LTE)
                        self.state = 41
                        self.expression(13)
                        pass

                    elif la_ == 6:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 42
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 43
                        self.match(grammarCParser.NEQ)
                        self.state = 44
                        self.expression(12)
                        pass

                    elif la_ == 7:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 45
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 46
                        self.match(grammarCParser.AND)
                        self.state = 47
                        self.expression(11)
                        pass

                    elif la_ == 8:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 48
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 49
                        self.match(grammarCParser.OR)
                        self.state = 50
                        self.expression(10)
                        pass

                    elif la_ == 9:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 51
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 52
                        self.match(grammarCParser.LSHIFT)
                        self.state = 53
                        self.expression(8)
                        pass

                    elif la_ == 10:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        self.match(grammarCParser.RSHIFT)
                        self.state = 56
                        self.expression(7)
                        pass

                    elif la_ == 11:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 58
                        self.match(grammarCParser.BIT_AND)
                        self.state = 59
                        self.expression(6)
                        pass

                    elif la_ == 12:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 60
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 61
                        self.match(grammarCParser.BIT_OR)
                        self.state = 62
                        self.expression(5)
                        pass

                    elif la_ == 13:
                        localctx = grammarCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 64
                        self.match(grammarCParser.BIT_XOR)
                        self.state = 65
                        self.expression(4)
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(grammarCParser.TermContext,0)


        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.OperationContext)
            else:
                return self.getTypedRuleContext(grammarCParser.OperationContext,i)


        def PLUS(self):
            return self.getToken(grammarCParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(grammarCParser.MINUS, 0)

        def getRuleIndex(self):
            return grammarCParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)



    def operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grammarCParser.OperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_operation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = grammarCParser.OperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 74
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 75
                        self.match(grammarCParser.PLUS)
                        self.state = 76
                        self.operation(4)
                        pass

                    elif la_ == 2:
                        localctx = grammarCParser.OperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 77
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 78
                        self.match(grammarCParser.MINUS)
                        self.state = 79
                        self.operation(3)
                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(grammarCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarCParser.RPAREN, 0)

        def INTEGER(self):
            return self.getToken(grammarCParser.INTEGER, 0)

        def MINUS(self):
            return self.getToken(grammarCParser.MINUS, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.TermContext)
            else:
                return self.getTypedRuleContext(grammarCParser.TermContext,i)


        def MULTIPLY(self):
            return self.getToken(grammarCParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(grammarCParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(grammarCParser.MODULO, 0)

        def getRuleIndex(self):
            return grammarCParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grammarCParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 86
                self.match(grammarCParser.LPAREN)
                self.state = 87
                self.expression(0)
                self.state = 88
                self.match(grammarCParser.RPAREN)
                pass
            elif token in [1, 3]:
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 90
                    self.match(grammarCParser.MINUS)


                self.state = 93
                self.match(grammarCParser.INTEGER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 105
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = grammarCParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 96
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 97
                        self.match(grammarCParser.MULTIPLY)
                        self.state = 98
                        self.term(5)
                        pass

                    elif la_ == 2:
                        localctx = grammarCParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 99
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 100
                        self.match(grammarCParser.DIVIDE)
                        self.state = 101
                        self.term(4)
                        pass

                    elif la_ == 3:
                        localctx = grammarCParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 102
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 103
                        self.match(grammarCParser.MODULO)
                        self.state = 104
                        self.term(3)
                        pass

             
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        self._predicates[3] = self.operation_sempred
        self._predicates[4] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

    def operation_sempred(self, localctx:OperationContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 2)
         




