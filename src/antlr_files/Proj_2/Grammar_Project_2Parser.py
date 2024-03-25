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
        4,1,38,271,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,4,0,42,8,0,11,0,12,0,43,1,0,5,0,47,8,0,10,0,12,0,50,9,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,60,8,2,10,2,12,2,63,9,2,1,2,1,2,1,
        3,1,3,4,3,69,8,3,11,3,12,3,70,1,3,1,3,4,3,75,8,3,11,3,12,3,76,1,
        3,1,3,1,3,1,3,4,3,83,8,3,11,3,12,3,84,1,3,1,3,1,3,1,3,4,3,91,8,3,
        11,3,12,3,92,1,3,1,3,1,3,1,3,4,3,99,8,3,11,3,12,3,100,1,3,1,3,4,
        3,105,8,3,11,3,12,3,106,1,3,1,3,4,3,111,8,3,11,3,12,3,112,1,3,3,
        3,116,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,126,8,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,139,8,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,5,5,195,8,5,10,5,12,5,198,9,5,1,6,1,6,1,6,1,6,1,6,1,7,3,7,
        206,8,7,1,7,1,7,1,7,4,7,211,8,7,11,7,12,7,212,1,7,3,7,216,8,7,1,
        7,1,7,1,7,4,7,221,8,7,11,7,12,7,222,1,7,3,7,226,8,7,1,7,3,7,229,
        8,7,1,8,1,8,1,9,1,9,4,9,235,8,9,11,9,12,9,236,1,10,4,10,240,8,10,
        11,10,12,10,241,1,10,1,10,1,11,4,11,247,8,11,11,11,12,11,248,1,11,
        1,11,1,12,5,12,254,8,12,10,12,12,12,257,9,12,1,12,1,12,1,13,1,13,
        1,13,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,0,1,10,17,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,0,3,1,0,11,12,1,0,31,33,2,0,
        1,1,5,6,308,0,37,1,0,0,0,2,51,1,0,0,0,4,57,1,0,0,0,6,115,1,0,0,0,
        8,125,1,0,0,0,10,138,1,0,0,0,12,199,1,0,0,0,14,228,1,0,0,0,16,230,
        1,0,0,0,18,232,1,0,0,0,20,239,1,0,0,0,22,246,1,0,0,0,24,255,1,0,
        0,0,26,260,1,0,0,0,28,263,1,0,0,0,30,266,1,0,0,0,32,268,1,0,0,0,
        34,36,3,32,16,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,
        42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,48,1,0,0,0,45,47,3,
        32,16,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,
        49,1,1,0,0,0,50,48,1,0,0,0,51,52,5,1,0,0,52,53,5,2,0,0,53,54,5,7,
        0,0,54,55,5,8,0,0,55,56,3,4,2,0,56,3,1,0,0,0,57,61,5,9,0,0,58,60,
        3,6,3,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,
        62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,10,0,0,65,5,1,0,0,0,66,68,3,
        10,5,0,67,69,5,30,0,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,
        70,71,1,0,0,0,71,116,1,0,0,0,72,74,3,8,4,0,73,75,5,30,0,0,74,73,
        1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,116,1,0,0,0,
        78,79,3,8,4,0,79,80,5,3,0,0,80,82,3,10,5,0,81,83,5,30,0,0,82,81,
        1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,116,1,0,0,0,
        86,87,3,8,4,0,87,88,5,3,0,0,88,90,3,12,6,0,89,91,5,30,0,0,90,89,
        1,0,0,0,91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,116,1,0,0,0,
        94,95,3,8,4,0,95,96,5,3,0,0,96,98,3,10,5,0,97,99,5,30,0,0,98,97,
        1,0,0,0,99,100,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,116,1,
        0,0,0,102,104,3,26,13,0,103,105,5,30,0,0,104,103,1,0,0,0,105,106,
        1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,116,1,0,0,0,108,110,
        3,28,14,0,109,111,5,30,0,0,110,109,1,0,0,0,111,112,1,0,0,0,112,110,
        1,0,0,0,112,113,1,0,0,0,113,116,1,0,0,0,114,116,3,32,16,0,115,66,
        1,0,0,0,115,72,1,0,0,0,115,78,1,0,0,0,115,86,1,0,0,0,115,94,1,0,
        0,0,115,102,1,0,0,0,115,108,1,0,0,0,115,114,1,0,0,0,116,7,1,0,0,
        0,117,126,3,30,15,0,118,119,3,24,12,0,119,120,3,30,15,0,120,126,
        1,0,0,0,121,122,3,18,9,0,122,123,3,30,15,0,123,126,1,0,0,0,124,126,
        3,20,10,0,125,117,1,0,0,0,125,118,1,0,0,0,125,121,1,0,0,0,125,124,
        1,0,0,0,126,9,1,0,0,0,127,128,6,5,-1,0,128,139,3,14,7,0,129,139,
        3,30,15,0,130,139,3,20,10,0,131,139,3,22,11,0,132,133,5,29,0,0,133,
        139,3,10,5,20,134,135,5,7,0,0,135,136,3,10,5,0,136,137,5,8,0,0,137,
        139,1,0,0,0,138,127,1,0,0,0,138,129,1,0,0,0,138,130,1,0,0,0,138,
        131,1,0,0,0,138,132,1,0,0,0,138,134,1,0,0,0,139,196,1,0,0,0,140,
        141,10,19,0,0,141,142,5,14,0,0,142,195,3,10,5,20,143,144,10,18,0,
        0,144,145,5,15,0,0,145,195,3,10,5,19,146,147,10,17,0,0,147,148,5,
        13,0,0,148,195,3,10,5,18,149,150,10,16,0,0,150,151,5,12,0,0,151,
        195,3,10,5,17,152,153,10,15,0,0,153,154,5,11,0,0,154,195,3,10,5,
        16,155,156,10,14,0,0,156,157,5,16,0,0,157,195,3,10,5,15,158,159,
        10,13,0,0,159,160,5,17,0,0,160,195,3,10,5,14,161,162,10,12,0,0,162,
        163,5,18,0,0,163,195,3,10,5,13,164,165,10,11,0,0,165,166,5,19,0,
        0,166,195,3,10,5,12,167,168,10,10,0,0,168,169,5,20,0,0,169,195,3,
        10,5,11,170,171,10,9,0,0,171,172,5,21,0,0,172,195,3,10,5,10,173,
        174,10,8,0,0,174,175,5,22,0,0,175,195,3,10,5,9,176,177,10,7,0,0,
        177,178,5,23,0,0,178,195,3,10,5,8,179,180,10,6,0,0,180,181,5,24,
        0,0,181,195,3,10,5,7,182,183,10,5,0,0,183,184,5,25,0,0,184,195,3,
        10,5,6,185,186,10,4,0,0,186,187,5,26,0,0,187,195,3,10,5,5,188,189,
        10,3,0,0,189,190,5,27,0,0,190,195,3,10,5,4,191,192,10,2,0,0,192,
        193,5,28,0,0,193,195,3,10,5,3,194,140,1,0,0,0,194,143,1,0,0,0,194,
        146,1,0,0,0,194,149,1,0,0,0,194,152,1,0,0,0,194,155,1,0,0,0,194,
        158,1,0,0,0,194,161,1,0,0,0,194,164,1,0,0,0,194,167,1,0,0,0,194,
        170,1,0,0,0,194,173,1,0,0,0,194,176,1,0,0,0,194,179,1,0,0,0,194,
        182,1,0,0,0,194,185,1,0,0,0,194,188,1,0,0,0,194,191,1,0,0,0,195,
        198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,11,1,0,0,0,198,196,
        1,0,0,0,199,200,5,7,0,0,200,201,3,24,12,0,201,202,5,8,0,0,202,203,
        3,10,5,0,203,13,1,0,0,0,204,206,7,0,0,0,205,204,1,0,0,0,205,206,
        1,0,0,0,206,207,1,0,0,0,207,229,3,16,8,0,208,209,5,11,0,0,209,211,
        5,12,0,0,210,208,1,0,0,0,211,212,1,0,0,0,212,210,1,0,0,0,212,213,
        1,0,0,0,213,215,1,0,0,0,214,216,5,11,0,0,215,214,1,0,0,0,215,216,
        1,0,0,0,216,217,1,0,0,0,217,229,3,16,8,0,218,219,5,12,0,0,219,221,
        5,11,0,0,220,218,1,0,0,0,221,222,1,0,0,0,222,220,1,0,0,0,222,223,
        1,0,0,0,223,225,1,0,0,0,224,226,5,12,0,0,225,224,1,0,0,0,225,226,
        1,0,0,0,226,227,1,0,0,0,227,229,3,16,8,0,228,205,1,0,0,0,228,210,
        1,0,0,0,228,220,1,0,0,0,229,15,1,0,0,0,230,231,7,1,0,0,231,17,1,
        0,0,0,232,234,3,24,12,0,233,235,5,13,0,0,234,233,1,0,0,0,235,236,
        1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,19,1,0,0,0,238,240,5,
        13,0,0,239,238,1,0,0,0,240,241,1,0,0,0,241,239,1,0,0,0,241,242,1,
        0,0,0,242,243,1,0,0,0,243,244,3,30,15,0,244,21,1,0,0,0,245,247,5,
        24,0,0,246,245,1,0,0,0,247,248,1,0,0,0,248,246,1,0,0,0,248,249,1,
        0,0,0,249,250,1,0,0,0,250,251,3,30,15,0,251,23,1,0,0,0,252,254,5,
        4,0,0,253,252,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,
        0,0,0,256,258,1,0,0,0,257,255,1,0,0,0,258,259,7,2,0,0,259,25,1,0,
        0,0,260,261,3,8,4,0,261,262,5,36,0,0,262,27,1,0,0,0,263,264,3,8,
        4,0,264,265,5,37,0,0,265,29,1,0,0,0,266,267,5,35,0,0,267,31,1,0,
        0,0,268,269,5,38,0,0,269,33,1,0,0,0,26,37,43,48,61,70,76,84,92,100,
        106,112,115,125,138,194,196,205,212,215,222,225,228,236,241,248,
        255
    ]

class Grammar_Project_2Parser ( Parser ):

    grammarFileName = "Grammar_Project_2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'='", "'const'", "'float'", 
                     "'char'", "'('", "')'", "'{'", "'}'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'<<'", "'>>'", "'&'", "'|'", "'^'", 
                     "'&&'", "'||'", "'!'", "';'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
                      "LESS_EQUAL", "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", 
                      "SHIFT_RIGHT", "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", 
                      "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", "SEMICOLON", 
                      "INT", "FLOAT", "CHAR", "WHITESPACE", "IDENTIFIER", 
                      "INCREMENT", "DECREMENT", "COMMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_scope = 2
    RULE_statement = 3
    RULE_lvalue = 4
    RULE_rvalue = 5
    RULE_rvalueCast = 6
    RULE_unaryExpression = 7
    RULE_literal = 8
    RULE_pointer = 9
    RULE_deref = 10
    RULE_addr = 11
    RULE_type = 12
    RULE_postfixIncrement = 13
    RULE_postfixDecrement = 14
    RULE_identifier = 15
    RULE_comment = 16

    ruleNames =  [ "program", "main", "scope", "statement", "lvalue", "rvalue", 
                   "rvalueCast", "unaryExpression", "literal", "pointer", 
                   "deref", "addr", "type", "postfixIncrement", "postfixDecrement", 
                   "identifier", "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
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
    IDENTIFIER=35
    INCREMENT=36
    DECREMENT=37
    COMMENT=38

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

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_2Parser.CommentContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_2Parser.CommentContext,i)


        def main(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_2Parser.MainContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_2Parser.MainContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 34
                self.comment()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.main()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 45
                self.comment()
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


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Grammar_Project_2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Grammar_Project_2Parser.RPAREN, 0)

        def scope(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.ScopeContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(Grammar_Project_2Parser.T__0)
            self.state = 52
            self.match(Grammar_Project_2Parser.T__1)
            self.state = 53
            self.match(Grammar_Project_2Parser.LPAREN)
            self.state = 54
            self.match(Grammar_Project_2Parser.RPAREN)
            self.state = 55
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return Grammar_Project_2Parser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScope" ):
                return visitor.visitScope(self)
            else:
                return visitor.visitChildren(self)




    def scope(self):

        localctx = Grammar_Project_2Parser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(Grammar_Project_2Parser.LBRACE)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 324823693554) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
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

        def rvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.RvalueContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_2Parser.SEMICOLON)
            else:
                return self.getToken(Grammar_Project_2Parser.SEMICOLON, i)

        def lvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.LvalueContext,0)


        def rvalueCast(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.RvalueCastContext,0)


        def postfixIncrement(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.PostfixIncrementContext,0)


        def postfixDecrement(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.PostfixDecrementContext,0)


        def comment(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.CommentContext,0)


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
        self.enterRule(localctx, 6, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.rvalue(0)
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 67
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 70 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.lvalue()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 73
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 76 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.lvalue()
                self.state = 79
                self.match(Grammar_Project_2Parser.T__2)
                self.state = 80
                self.rvalue(0)
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 81
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 84 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.lvalue()
                self.state = 87
                self.match(Grammar_Project_2Parser.T__2)
                self.state = 88
                self.rvalueCast()
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 89
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 92 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.lvalue()
                self.state = 95
                self.match(Grammar_Project_2Parser.T__2)
                self.state = 96
                self.rvalue(0)
                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 97
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 100 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 102
                self.postfixIncrement()
                self.state = 104 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 103
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 106 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 108
                self.postfixDecrement()
                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 109
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 112 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 114
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.IdentifierContext,0)


        def type_(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.TypeContext,0)


        def pointer(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.PointerContext,0)


        def deref(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.DerefContext,0)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvalue" ):
                return visitor.visitLvalue(self)
            else:
                return visitor.visitChildren(self)




    def lvalue(self):

        localctx = Grammar_Project_2Parser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lvalue)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.type_()
                self.state = 119
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.pointer()
                self.state = 122
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 124
                self.deref()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.UnaryExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.IdentifierContext,0)


        def deref(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.DerefContext,0)


        def addr(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.AddrContext,0)


        def LOGICAL_NOT(self):
            return self.getToken(Grammar_Project_2Parser.LOGICAL_NOT, 0)

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_2Parser.RvalueContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_2Parser.RvalueContext,i)


        def LPAREN(self):
            return self.getToken(Grammar_Project_2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Grammar_Project_2Parser.RPAREN, 0)

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
            return Grammar_Project_2Parser.RULE_rvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRvalue" ):
                listener.enterRvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRvalue" ):
                listener.exitRvalue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRvalue" ):
                return visitor.visitRvalue(self)
            else:
                return visitor.visitChildren(self)



    def rvalue(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Grammar_Project_2Parser.RvalueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 31, 32, 33]:
                self.state = 128
                self.unaryExpression()
                pass
            elif token in [35]:
                self.state = 129
                self.identifier()
                pass
            elif token in [13]:
                self.state = 130
                self.deref()
                pass
            elif token in [24]:
                self.state = 131
                self.addr()
                pass
            elif token in [29]:
                self.state = 132
                self.match(Grammar_Project_2Parser.LOGICAL_NOT)
                self.state = 133
                self.rvalue(20)
                pass
            elif token in [7]:
                self.state = 134
                self.match(Grammar_Project_2Parser.LPAREN)
                self.state = 135
                self.rvalue(0)
                self.state = 136
                self.match(Grammar_Project_2Parser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 194
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 140
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 141
                        self.match(Grammar_Project_2Parser.DIV)
                        self.state = 142
                        self.rvalue(20)
                        pass

                    elif la_ == 2:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 143
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 144
                        self.match(Grammar_Project_2Parser.MOD)
                        self.state = 145
                        self.rvalue(19)
                        pass

                    elif la_ == 3:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 146
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 147
                        self.match(Grammar_Project_2Parser.MULT)
                        self.state = 148
                        self.rvalue(18)
                        pass

                    elif la_ == 4:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 149
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 150
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 151
                        self.rvalue(17)
                        pass

                    elif la_ == 5:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 152
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 153
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 154
                        self.rvalue(16)
                        pass

                    elif la_ == 6:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 155
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 156
                        self.match(Grammar_Project_2Parser.GREATER_THAN)
                        self.state = 157
                        self.rvalue(15)
                        pass

                    elif la_ == 7:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 158
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 159
                        self.match(Grammar_Project_2Parser.LESS_THAN)
                        self.state = 160
                        self.rvalue(14)
                        pass

                    elif la_ == 8:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 161
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 162
                        self.match(Grammar_Project_2Parser.GREATER_EQUAL)
                        self.state = 163
                        self.rvalue(13)
                        pass

                    elif la_ == 9:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 164
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 165
                        self.match(Grammar_Project_2Parser.LESS_EQUAL)
                        self.state = 166
                        self.rvalue(12)
                        pass

                    elif la_ == 10:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 167
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 168
                        self.match(Grammar_Project_2Parser.EQUALS)
                        self.state = 169
                        self.rvalue(11)
                        pass

                    elif la_ == 11:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 170
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 171
                        self.match(Grammar_Project_2Parser.NOT_EQUAL)
                        self.state = 172
                        self.rvalue(10)
                        pass

                    elif la_ == 12:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 173
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 174
                        self.match(Grammar_Project_2Parser.SHIFT_LEFT)
                        self.state = 175
                        self.rvalue(9)
                        pass

                    elif la_ == 13:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 176
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 177
                        self.match(Grammar_Project_2Parser.SHIFT_RIGHT)
                        self.state = 178
                        self.rvalue(8)
                        pass

                    elif la_ == 14:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 179
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 180
                        self.match(Grammar_Project_2Parser.BITWISE_AND)
                        self.state = 181
                        self.rvalue(7)
                        pass

                    elif la_ == 15:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 182
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 183
                        self.match(Grammar_Project_2Parser.BITWISE_OR)
                        self.state = 184
                        self.rvalue(6)
                        pass

                    elif la_ == 16:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 185
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 186
                        self.match(Grammar_Project_2Parser.BITWISE_XOR)
                        self.state = 187
                        self.rvalue(5)
                        pass

                    elif la_ == 17:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 188
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 189
                        self.match(Grammar_Project_2Parser.LOGICAL_AND)
                        self.state = 190
                        self.rvalue(4)
                        pass

                    elif la_ == 18:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 191
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 192
                        self.match(Grammar_Project_2Parser.LOGICAL_OR)
                        self.state = 193
                        self.rvalue(3)
                        pass

             
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RvalueCastContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Grammar_Project_2Parser.LPAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.TypeContext,0)


        def RPAREN(self):
            return self.getToken(Grammar_Project_2Parser.RPAREN, 0)

        def rvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.RvalueContext,0)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_rvalueCast

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRvalueCast" ):
                listener.enterRvalueCast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRvalueCast" ):
                listener.exitRvalueCast(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRvalueCast" ):
                return visitor.visitRvalueCast(self)
            else:
                return visitor.visitChildren(self)




    def rvalueCast(self):

        localctx = Grammar_Project_2Parser.RvalueCastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rvalueCast)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(Grammar_Project_2Parser.LPAREN)
            self.state = 200
            self.type_()
            self.state = 201
            self.match(Grammar_Project_2Parser.RPAREN)
            self.state = 202
            self.rvalue(0)
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
        self.enterRule(localctx, 14, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11 or _la==12:
                    self.state = 204
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 207
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 208
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 209
                        self.match(Grammar_Project_2Parser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 212 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 214
                    self.match(Grammar_Project_2Parser.PLUS)


                self.state = 217
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 218
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 219
                        self.match(Grammar_Project_2Parser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 222 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 224
                    self.match(Grammar_Project_2Parser.MINUS)


                self.state = 227
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
        self.enterRule(localctx, 16, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
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
            self.state = 232
            self.type_()
            self.state = 234 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 233
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 236 
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

        def identifier(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.IdentifierContext,0)


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
            self.state = 239 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 238
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 241 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

            self.state = 243
            self.identifier()
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

        def identifier(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.IdentifierContext,0)


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
            self.state = 246 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 245
                self.match(Grammar_Project_2Parser.BITWISE_AND)
                self.state = 248 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

            self.state = 250
            self.identifier()
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
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 252
                self.match(Grammar_Project_2Parser.T__3)
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 98) != 0)):
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


    class PostfixIncrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.LvalueContext,0)


        def INCREMENT(self):
            return self.getToken(Grammar_Project_2Parser.INCREMENT, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_postfixIncrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixIncrement" ):
                listener.enterPostfixIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixIncrement" ):
                listener.exitPostfixIncrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixIncrement" ):
                return visitor.visitPostfixIncrement(self)
            else:
                return visitor.visitChildren(self)




    def postfixIncrement(self):

        localctx = Grammar_Project_2Parser.PostfixIncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_postfixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.lvalue()
            self.state = 261
            self.match(Grammar_Project_2Parser.INCREMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixDecrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.LvalueContext,0)


        def DECREMENT(self):
            return self.getToken(Grammar_Project_2Parser.DECREMENT, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_postfixDecrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixDecrement" ):
                listener.enterPostfixDecrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixDecrement" ):
                listener.exitPostfixDecrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixDecrement" ):
                return visitor.visitPostfixDecrement(self)
            else:
                return visitor.visitChildren(self)




    def postfixDecrement(self):

        localctx = Grammar_Project_2Parser.PostfixDecrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_postfixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.lvalue()
            self.state = 264
            self.match(Grammar_Project_2Parser.DECREMENT)
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
        self.enterRule(localctx, 30, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(Grammar_Project_2Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(Grammar_Project_2Parser.COMMENT, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = Grammar_Project_2Parser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(Grammar_Project_2Parser.COMMENT)
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
        self._predicates[5] = self.rvalue_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def rvalue_sempred(self, localctx:RvalueContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 2)
         




