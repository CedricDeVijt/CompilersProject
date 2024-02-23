# Generated from /Users/cedric/Library/Mobile Documents/com~apple~CloudDocs/School/Informatica 2/2 Compilers/Project/grammars/mathematical_expressions.g4 by ANTLR 4.13.1
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
        4,1,24,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,
        2,1,2,1,2,5,2,31,8,2,10,2,12,2,34,9,2,1,3,1,3,1,3,5,3,39,8,3,10,
        3,12,3,42,9,3,1,4,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,1,5,1,5,1,
        5,5,5,55,8,5,10,5,12,5,58,9,5,1,6,1,6,1,6,3,6,63,8,6,1,7,1,7,1,7,
        1,7,1,7,3,7,70,8,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,6,1,0,13,14,1,
        0,9,12,1,0,7,8,1,0,2,3,1,0,4,6,3,0,2,3,15,15,20,20,70,0,16,1,0,0,
        0,2,19,1,0,0,0,4,27,1,0,0,0,6,35,1,0,0,0,8,43,1,0,0,0,10,51,1,0,
        0,0,12,62,1,0,0,0,14,69,1,0,0,0,16,17,3,2,1,0,17,18,5,24,0,0,18,
        1,1,0,0,0,19,24,3,4,2,0,20,21,7,0,0,0,21,23,3,4,2,0,22,20,1,0,0,
        0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,0,26,24,1,
        0,0,0,27,32,3,6,3,0,28,29,7,1,0,0,29,31,3,6,3,0,30,28,1,0,0,0,31,
        34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,5,1,0,0,0,34,32,1,0,0,
        0,35,40,3,8,4,0,36,37,7,2,0,0,37,39,3,8,4,0,38,36,1,0,0,0,39,42,
        1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,7,1,0,0,0,42,40,1,0,0,0,43,
        48,3,10,5,0,44,45,7,3,0,0,45,47,3,10,5,0,46,44,1,0,0,0,47,50,1,0,
        0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,9,1,0,0,0,50,48,1,0,0,0,51,56,
        3,12,6,0,52,53,7,4,0,0,53,55,3,12,6,0,54,52,1,0,0,0,55,58,1,0,0,
        0,56,54,1,0,0,0,56,57,1,0,0,0,57,11,1,0,0,0,58,56,1,0,0,0,59,60,
        7,5,0,0,60,63,3,12,6,0,61,63,3,14,7,0,62,59,1,0,0,0,62,61,1,0,0,
        0,63,13,1,0,0,0,64,70,5,1,0,0,65,66,5,22,0,0,66,67,3,0,0,0,67,68,
        5,23,0,0,68,70,1,0,0,0,69,64,1,0,0,0,69,65,1,0,0,0,70,15,1,0,0,0,
        7,24,32,40,48,56,62,69
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
                      "SEMICOLON" ]

    RULE_expression = 0
    RULE_logicalExpression = 1
    RULE_equalityExpression = 2
    RULE_relationalExpression = 3
    RULE_additiveExpression = 4
    RULE_multiplicativeExpression = 5
    RULE_unaryExpression = 6
    RULE_primaryExpression = 7

    ruleNames =  [ "expression", "logicalExpression", "equalityExpression", 
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

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpression(self):
            return self.getTypedRuleContext(mathematical_expressionsParser.LogicalExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(mathematical_expressionsParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 0, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.logicalExpression()
            self.state = 17
            self.match(mathematical_expressionsParser.SEMICOLON)
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
        self.enterRule(localctx, 2, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.equalityExpression()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 20
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
                self.equalityExpression()
                self.state = 26
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
        self.enterRule(localctx, 4, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.relationalExpression()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                self.state = 28
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29
                self.relationalExpression()
                self.state = 34
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
        self.enterRule(localctx, 6, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.additiveExpression()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 36
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 37
                self.additiveExpression()
                self.state = 42
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
        self.enterRule(localctx, 8, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.multiplicativeExpression()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 44
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 45
                self.multiplicativeExpression()
                self.state = 50
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
        self.enterRule(localctx, 10, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.unaryExpression()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                self.state = 52
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 53
                self.unaryExpression()
                self.state = 58
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
        self.enterRule(localctx, 12, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 15, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1081356) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60
                self.unaryExpression()
                pass
            elif token in [1, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
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
        self.enterRule(localctx, 14, self.RULE_primaryExpression)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(mathematical_expressionsParser.INTEGER)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(mathematical_expressionsParser.LPAREN)
                self.state = 66
                self.expression()
                self.state = 67
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





