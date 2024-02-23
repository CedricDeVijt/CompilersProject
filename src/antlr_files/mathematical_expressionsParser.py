# Generated from grammars/mathematical_expressions.g4 by ANTLR 4.13.1
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
        4,1,25,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,1,1,
        1,1,2,1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,3,1,3,1,3,5,3,40,8,3,
        10,3,12,3,43,9,3,1,4,1,4,1,4,5,4,48,8,4,10,4,12,4,51,9,4,1,5,1,5,
        1,5,5,5,56,8,5,10,5,12,5,59,9,5,1,6,1,6,1,6,5,6,64,8,6,10,6,12,6,
        67,9,6,1,7,1,7,1,7,3,7,72,8,7,1,8,1,8,1,8,1,8,1,8,3,8,79,8,8,1,8,
        0,0,9,0,2,4,6,8,10,12,14,16,0,6,1,0,13,14,1,0,9,12,1,0,7,8,1,0,2,
        3,1,0,4,6,3,0,2,3,15,15,20,20,79,0,23,1,0,0,0,2,26,1,0,0,0,4,28,
        1,0,0,0,6,36,1,0,0,0,8,44,1,0,0,0,10,52,1,0,0,0,12,60,1,0,0,0,14,
        71,1,0,0,0,16,78,1,0,0,0,18,19,3,2,1,0,19,20,5,24,0,0,20,22,1,0,
        0,0,21,18,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,1,
        1,0,0,0,25,23,1,0,0,0,26,27,3,4,2,0,27,3,1,0,0,0,28,33,3,6,3,0,29,
        30,7,0,0,0,30,32,3,6,3,0,31,29,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,
        0,33,34,1,0,0,0,34,5,1,0,0,0,35,33,1,0,0,0,36,41,3,8,4,0,37,38,7,
        1,0,0,38,40,3,8,4,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,
        42,1,0,0,0,42,7,1,0,0,0,43,41,1,0,0,0,44,49,3,10,5,0,45,46,7,2,0,
        0,46,48,3,10,5,0,47,45,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,
        1,0,0,0,50,9,1,0,0,0,51,49,1,0,0,0,52,57,3,12,6,0,53,54,7,3,0,0,
        54,56,3,12,6,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,
        0,0,0,58,11,1,0,0,0,59,57,1,0,0,0,60,65,3,14,7,0,61,62,7,4,0,0,62,
        64,3,14,7,0,63,61,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,
        0,0,66,13,1,0,0,0,67,65,1,0,0,0,68,69,7,5,0,0,69,72,3,14,7,0,70,
        72,3,16,8,0,71,68,1,0,0,0,71,70,1,0,0,0,72,15,1,0,0,0,73,79,5,1,
        0,0,74,75,5,22,0,0,75,76,3,2,1,0,76,77,5,23,0,0,77,79,1,0,0,0,78,
        73,1,0,0,0,78,74,1,0,0,0,79,17,1,0,0,0,8,23,33,41,49,57,65,71,78
    ]

class mathematical_expressionsParser ( Parser ):

    grammarFileName = "mathematical_expressions.g4"

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

    RULE_program = 0
    RULE_expression = 1
    RULE_logicalExpression = 2
    RULE_equalityExpression = 3
    RULE_relationalExpression = 4
    RULE_additiveExpression = 5
    RULE_multiplicativeExpression = 6
    RULE_unaryExpression = 7
    RULE_primaryExpression = 8

    ruleNames =  [ "program", "expression", "logicalExpression", "equalityExpression", 
                   "relationalExpression", "additiveExpression", "multiplicativeExpression", 
                   "unaryExpression", "primaryExpression" ]

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




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematical_expressionsParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(mathematical_expressionsParser.ExpressionContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.SEMICOLON)
            else:
                return self.getToken(mathematical_expressionsParser.SEMICOLON, i)

        def getRuleIndex(self):
            return mathematical_expressionsParser.RULE_program

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

        localctx = mathematical_expressionsParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5275662) != 0):
                self.state = 18
                self.expression()
                self.state = 19
                self.match(mathematical_expressionsParser.SEMICOLON)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def logicalExpression(self):
            return self.getTypedRuleContext(mathematical_expressionsParser.LogicalExpressionContext,0)


        def getRuleIndex(self):
            return mathematical_expressionsParser.RULE_expression

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




    def expression(self):

        localctx = mathematical_expressionsParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.logicalExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematical_expressionsParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(mathematical_expressionsParser.EqualityExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.AND)
            else:
                return self.getToken(mathematical_expressionsParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.OR)
            else:
                return self.getToken(mathematical_expressionsParser.OR, i)

        def getRuleIndex(self):
            return mathematical_expressionsParser.RULE_logicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpression" ):
                return visitor.visitLogicalExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalExpression(self):

        localctx = mathematical_expressionsParser.LogicalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.equalityExpression()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 29
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.equalityExpression()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematical_expressionsParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(mathematical_expressionsParser.RelationalExpressionContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.EQ)
            else:
                return self.getToken(mathematical_expressionsParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.NEQ)
            else:
                return self.getToken(mathematical_expressionsParser.NEQ, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.GTE)
            else:
                return self.getToken(mathematical_expressionsParser.GTE, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.LTE)
            else:
                return self.getToken(mathematical_expressionsParser.LTE, i)

        def getRuleIndex(self):
            return mathematical_expressionsParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = mathematical_expressionsParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.relationalExpression()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                self.state = 37
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 38
                self.relationalExpression()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematical_expressionsParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(mathematical_expressionsParser.AdditiveExpressionContext,i)


        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.GT)
            else:
                return self.getToken(mathematical_expressionsParser.GT, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.LT)
            else:
                return self.getToken(mathematical_expressionsParser.LT, i)

        def getRuleIndex(self):
            return mathematical_expressionsParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = mathematical_expressionsParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.additiveExpression()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 45
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 46
                self.additiveExpression()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematical_expressionsParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(mathematical_expressionsParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.PLUS)
            else:
                return self.getToken(mathematical_expressionsParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.MINUS)
            else:
                return self.getToken(mathematical_expressionsParser.MINUS, i)

        def getRuleIndex(self):
            return mathematical_expressionsParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = mathematical_expressionsParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.multiplicativeExpression()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 53
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54
                self.multiplicativeExpression()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematical_expressionsParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(mathematical_expressionsParser.UnaryExpressionContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.MULTIPLY)
            else:
                return self.getToken(mathematical_expressionsParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.DIVIDE)
            else:
                return self.getToken(mathematical_expressionsParser.DIVIDE, i)

        def MODULO(self, i:int=None):
            if i is None:
                return self.getTokens(mathematical_expressionsParser.MODULO)
            else:
                return self.getToken(mathematical_expressionsParser.MODULO, i)

        def getRuleIndex(self):
            return mathematical_expressionsParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = mathematical_expressionsParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.unaryExpression()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                self.state = 61
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 62
                self.unaryExpression()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(mathematical_expressionsParser.UnaryExpressionContext,0)


        def PLUS(self):
            return self.getToken(mathematical_expressionsParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(mathematical_expressionsParser.MINUS, 0)

        def NOT(self):
            return self.getToken(mathematical_expressionsParser.NOT, 0)

        def BIT_NOT(self):
            return self.getToken(mathematical_expressionsParser.BIT_NOT, 0)

        def primaryExpression(self):
            return self.getTypedRuleContext(mathematical_expressionsParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return mathematical_expressionsParser.RULE_unaryExpression

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

        localctx = mathematical_expressionsParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 15, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1081356) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 69
                self.unaryExpression()
                pass
            elif token in [1, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.primaryExpression()
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


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(mathematical_expressionsParser.INTEGER, 0)

        def LPAREN(self):
            return self.getToken(mathematical_expressionsParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(mathematical_expressionsParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(mathematical_expressionsParser.RPAREN, 0)

        def getRuleIndex(self):
            return mathematical_expressionsParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = mathematical_expressionsParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primaryExpression)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(mathematical_expressionsParser.INTEGER)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(mathematical_expressionsParser.LPAREN)
                self.state = 75
                self.expression()
                self.state = 76
                self.match(mathematical_expressionsParser.RPAREN)
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





