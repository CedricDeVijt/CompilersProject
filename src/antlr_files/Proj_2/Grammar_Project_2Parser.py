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
        4,1,38,310,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,4,0,48,8,0,11,0,12,0,49,1,0,5,0,
        53,8,0,10,0,12,0,56,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,66,8,
        2,10,2,12,2,69,9,2,1,2,1,2,1,3,1,3,4,3,75,8,3,11,3,12,3,76,1,3,1,
        3,4,3,81,8,3,11,3,12,3,82,1,3,1,3,1,3,1,3,4,3,89,8,3,11,3,12,3,90,
        1,3,1,3,1,3,1,3,4,3,97,8,3,11,3,12,3,98,1,3,1,3,1,3,1,3,4,3,105,
        8,3,11,3,12,3,106,1,3,1,3,4,3,111,8,3,11,3,12,3,112,1,3,1,3,4,3,
        117,8,3,11,3,12,3,118,1,3,1,3,4,3,123,8,3,11,3,12,3,124,1,3,1,3,
        4,3,129,8,3,11,3,12,3,130,1,3,3,3,134,8,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,144,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,3,5,160,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,216,8,5,10,
        5,12,5,219,9,5,1,6,1,6,1,6,1,6,1,6,1,7,3,7,227,8,7,1,7,1,7,1,7,4,
        7,232,8,7,11,7,12,7,233,1,7,3,7,237,8,7,1,7,1,7,1,7,4,7,242,8,7,
        11,7,12,7,243,1,7,3,7,247,8,7,1,7,3,7,250,8,7,1,8,1,8,1,9,4,9,255,
        8,9,11,9,12,9,256,1,9,4,9,260,8,9,11,9,12,9,261,1,9,1,9,1,10,1,10,
        4,10,268,8,10,11,10,12,10,269,1,11,4,11,273,8,11,11,11,12,11,274,
        1,11,1,11,1,12,4,12,280,8,12,11,12,12,12,281,1,12,1,12,1,13,5,13,
        287,8,13,10,13,12,13,290,9,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,
        1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,19,0,1,
        10,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,3,
        1,0,11,12,1,0,31,33,2,0,1,1,5,6,351,0,43,1,0,0,0,2,57,1,0,0,0,4,
        63,1,0,0,0,6,133,1,0,0,0,8,143,1,0,0,0,10,159,1,0,0,0,12,220,1,0,
        0,0,14,249,1,0,0,0,16,251,1,0,0,0,18,254,1,0,0,0,20,265,1,0,0,0,
        22,272,1,0,0,0,24,279,1,0,0,0,26,288,1,0,0,0,28,293,1,0,0,0,30,296,
        1,0,0,0,32,299,1,0,0,0,34,302,1,0,0,0,36,305,1,0,0,0,38,307,1,0,
        0,0,40,42,3,38,19,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,
        44,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,
        0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,54,1,0,0,0,51,53,
        3,38,19,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,
        0,55,1,1,0,0,0,56,54,1,0,0,0,57,58,5,1,0,0,58,59,5,2,0,0,59,60,5,
        7,0,0,60,61,5,8,0,0,61,62,3,4,2,0,62,3,1,0,0,0,63,67,5,9,0,0,64,
        66,3,6,3,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,
        0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,10,0,0,71,5,1,0,0,0,72,74,
        3,10,5,0,73,75,5,30,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,
        0,76,77,1,0,0,0,77,134,1,0,0,0,78,80,3,8,4,0,79,81,5,30,0,0,80,79,
        1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,134,1,0,0,0,
        84,85,3,8,4,0,85,86,5,3,0,0,86,88,3,10,5,0,87,89,5,30,0,0,88,87,
        1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,134,1,0,0,0,
        92,93,3,8,4,0,93,94,5,3,0,0,94,96,3,12,6,0,95,97,5,30,0,0,96,95,
        1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,134,1,0,0,0,
        100,101,3,8,4,0,101,102,5,3,0,0,102,104,3,10,5,0,103,105,5,30,0,
        0,104,103,1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,
        0,107,134,1,0,0,0,108,110,3,28,14,0,109,111,5,30,0,0,110,109,1,0,
        0,0,111,112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,134,1,0,
        0,0,114,116,3,30,15,0,115,117,5,30,0,0,116,115,1,0,0,0,117,118,1,
        0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,134,1,0,0,0,120,122,3,
        32,16,0,121,123,5,30,0,0,122,121,1,0,0,0,123,124,1,0,0,0,124,122,
        1,0,0,0,124,125,1,0,0,0,125,134,1,0,0,0,126,128,3,34,17,0,127,129,
        5,30,0,0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,134,1,0,0,0,132,134,3,38,19,0,133,72,1,0,0,0,133,78,
        1,0,0,0,133,84,1,0,0,0,133,92,1,0,0,0,133,100,1,0,0,0,133,108,1,
        0,0,0,133,114,1,0,0,0,133,120,1,0,0,0,133,126,1,0,0,0,133,132,1,
        0,0,0,134,7,1,0,0,0,135,144,3,36,18,0,136,137,3,26,13,0,137,138,
        3,36,18,0,138,144,1,0,0,0,139,140,3,20,10,0,140,141,3,36,18,0,141,
        144,1,0,0,0,142,144,3,22,11,0,143,135,1,0,0,0,143,136,1,0,0,0,143,
        139,1,0,0,0,143,142,1,0,0,0,144,9,1,0,0,0,145,146,6,5,-1,0,146,160,
        3,14,7,0,147,160,3,36,18,0,148,160,3,22,11,0,149,160,3,24,12,0,150,
        151,5,29,0,0,151,160,3,10,5,21,152,153,5,7,0,0,153,154,3,10,5,0,
        154,155,5,8,0,0,155,160,1,0,0,0,156,157,3,18,9,0,157,158,3,10,5,
        1,158,160,1,0,0,0,159,145,1,0,0,0,159,147,1,0,0,0,159,148,1,0,0,
        0,159,149,1,0,0,0,159,150,1,0,0,0,159,152,1,0,0,0,159,156,1,0,0,
        0,160,217,1,0,0,0,161,162,10,20,0,0,162,163,5,14,0,0,163,216,3,10,
        5,21,164,165,10,19,0,0,165,166,5,15,0,0,166,216,3,10,5,20,167,168,
        10,18,0,0,168,169,5,13,0,0,169,216,3,10,5,19,170,171,10,17,0,0,171,
        172,5,12,0,0,172,216,3,10,5,18,173,174,10,16,0,0,174,175,5,11,0,
        0,175,216,3,10,5,17,176,177,10,15,0,0,177,178,5,16,0,0,178,216,3,
        10,5,16,179,180,10,14,0,0,180,181,5,17,0,0,181,216,3,10,5,15,182,
        183,10,13,0,0,183,184,5,18,0,0,184,216,3,10,5,14,185,186,10,12,0,
        0,186,187,5,19,0,0,187,216,3,10,5,13,188,189,10,11,0,0,189,190,5,
        20,0,0,190,216,3,10,5,12,191,192,10,10,0,0,192,193,5,21,0,0,193,
        216,3,10,5,11,194,195,10,9,0,0,195,196,5,22,0,0,196,216,3,10,5,10,
        197,198,10,8,0,0,198,199,5,23,0,0,199,216,3,10,5,9,200,201,10,7,
        0,0,201,202,5,24,0,0,202,216,3,10,5,8,203,204,10,6,0,0,204,205,5,
        25,0,0,205,216,3,10,5,7,206,207,10,5,0,0,207,208,5,26,0,0,208,216,
        3,10,5,6,209,210,10,4,0,0,210,211,5,27,0,0,211,216,3,10,5,5,212,
        213,10,3,0,0,213,214,5,28,0,0,214,216,3,10,5,4,215,161,1,0,0,0,215,
        164,1,0,0,0,215,167,1,0,0,0,215,170,1,0,0,0,215,173,1,0,0,0,215,
        176,1,0,0,0,215,179,1,0,0,0,215,182,1,0,0,0,215,185,1,0,0,0,215,
        188,1,0,0,0,215,191,1,0,0,0,215,194,1,0,0,0,215,197,1,0,0,0,215,
        200,1,0,0,0,215,203,1,0,0,0,215,206,1,0,0,0,215,209,1,0,0,0,215,
        212,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,
        11,1,0,0,0,219,217,1,0,0,0,220,221,5,7,0,0,221,222,3,26,13,0,222,
        223,5,8,0,0,223,224,3,10,5,0,224,13,1,0,0,0,225,227,7,0,0,0,226,
        225,1,0,0,0,226,227,1,0,0,0,227,228,1,0,0,0,228,250,3,16,8,0,229,
        230,5,11,0,0,230,232,5,12,0,0,231,229,1,0,0,0,232,233,1,0,0,0,233,
        231,1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,237,5,11,0,0,236,
        235,1,0,0,0,236,237,1,0,0,0,237,238,1,0,0,0,238,250,3,16,8,0,239,
        240,5,12,0,0,240,242,5,11,0,0,241,239,1,0,0,0,242,243,1,0,0,0,243,
        241,1,0,0,0,243,244,1,0,0,0,244,246,1,0,0,0,245,247,5,12,0,0,246,
        245,1,0,0,0,246,247,1,0,0,0,247,248,1,0,0,0,248,250,3,16,8,0,249,
        226,1,0,0,0,249,231,1,0,0,0,249,241,1,0,0,0,250,15,1,0,0,0,251,252,
        7,1,0,0,252,17,1,0,0,0,253,255,5,7,0,0,254,253,1,0,0,0,255,256,1,
        0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,259,1,0,0,0,258,260,3,
        26,13,0,259,258,1,0,0,0,260,261,1,0,0,0,261,259,1,0,0,0,261,262,
        1,0,0,0,262,263,1,0,0,0,263,264,5,8,0,0,264,19,1,0,0,0,265,267,3,
        26,13,0,266,268,5,13,0,0,267,266,1,0,0,0,268,269,1,0,0,0,269,267,
        1,0,0,0,269,270,1,0,0,0,270,21,1,0,0,0,271,273,5,13,0,0,272,271,
        1,0,0,0,273,274,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,276,
        1,0,0,0,276,277,3,36,18,0,277,23,1,0,0,0,278,280,5,24,0,0,279,278,
        1,0,0,0,280,281,1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,283,
        1,0,0,0,283,284,3,36,18,0,284,25,1,0,0,0,285,287,5,4,0,0,286,285,
        1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,291,
        1,0,0,0,290,288,1,0,0,0,291,292,7,2,0,0,292,27,1,0,0,0,293,294,3,
        8,4,0,294,295,5,36,0,0,295,29,1,0,0,0,296,297,3,8,4,0,297,298,5,
        37,0,0,298,31,1,0,0,0,299,300,5,36,0,0,300,301,3,8,4,0,301,33,1,
        0,0,0,302,303,5,37,0,0,303,304,3,8,4,0,304,35,1,0,0,0,305,306,5,
        35,0,0,306,37,1,0,0,0,307,308,5,38,0,0,308,39,1,0,0,0,30,43,49,54,
        67,76,82,90,98,106,112,118,124,130,133,143,159,215,217,226,233,236,
        243,246,249,256,261,269,274,281,288
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
    RULE_implicitConversion = 9
    RULE_pointer = 10
    RULE_deref = 11
    RULE_addr = 12
    RULE_type = 13
    RULE_postFixIncrement = 14
    RULE_postFixDecrement = 15
    RULE_preFixIncrement = 16
    RULE_preFixDecrement = 17
    RULE_identifier = 18
    RULE_comment = 19

    ruleNames =  [ "program", "main", "scope", "statement", "lvalue", "rvalue", 
                   "rvalueCast", "unaryExpression", "literal", "implicitConversion", 
                   "pointer", "deref", "addr", "type", "postFixIncrement", 
                   "postFixDecrement", "preFixIncrement", "preFixDecrement", 
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
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 40
                self.comment()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.main()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 51
                self.comment()
                self.state = 56
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
            self.state = 57
            self.match(Grammar_Project_2Parser.T__0)
            self.state = 58
            self.match(Grammar_Project_2Parser.T__1)
            self.state = 59
            self.match(Grammar_Project_2Parser.LPAREN)
            self.state = 60
            self.match(Grammar_Project_2Parser.RPAREN)
            self.state = 61
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
            self.state = 63
            self.match(Grammar_Project_2Parser.LBRACE)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 530982123762) != 0):
                self.state = 64
                self.statement()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
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


        def postFixIncrement(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.PostFixIncrementContext,0)


        def postFixDecrement(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.PostFixDecrementContext,0)


        def preFixIncrement(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.PreFixIncrementContext,0)


        def preFixDecrement(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.PreFixDecrementContext,0)


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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.rvalue(0)
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

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.lvalue()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 79
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 82 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.lvalue()
                self.state = 85
                self.match(Grammar_Project_2Parser.T__2)
                self.state = 86
                self.rvalue(0)
                self.state = 88 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 87
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 90 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.lvalue()
                self.state = 93
                self.match(Grammar_Project_2Parser.T__2)
                self.state = 94
                self.rvalueCast()
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 95
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 98 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.lvalue()
                self.state = 101
                self.match(Grammar_Project_2Parser.T__2)
                self.state = 102
                self.rvalue(0)
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

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.postFixIncrement()
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

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.postFixDecrement()
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 115
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 118 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 120
                self.preFixIncrement()
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 121
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 124 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 126
                self.preFixDecrement()
                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 127
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 130 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 132
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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.type_()
                self.state = 137
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.pointer()
                self.state = 140
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
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

        def implicitConversion(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.ImplicitConversionContext,0)


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
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 146
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 147
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 148
                self.deref()
                pass

            elif la_ == 4:
                self.state = 149
                self.addr()
                pass

            elif la_ == 5:
                self.state = 150
                self.match(Grammar_Project_2Parser.LOGICAL_NOT)
                self.state = 151
                self.rvalue(21)
                pass

            elif la_ == 6:
                self.state = 152
                self.match(Grammar_Project_2Parser.LPAREN)
                self.state = 153
                self.rvalue(0)
                self.state = 154
                self.match(Grammar_Project_2Parser.RPAREN)
                pass

            elif la_ == 7:
                self.state = 156
                self.implicitConversion()
                self.state = 157
                self.rvalue(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 215
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 161
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 162
                        self.match(Grammar_Project_2Parser.DIV)
                        self.state = 163
                        self.rvalue(21)
                        pass

                    elif la_ == 2:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 164
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 165
                        self.match(Grammar_Project_2Parser.MOD)
                        self.state = 166
                        self.rvalue(20)
                        pass

                    elif la_ == 3:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 167
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 168
                        self.match(Grammar_Project_2Parser.MULT)
                        self.state = 169
                        self.rvalue(19)
                        pass

                    elif la_ == 4:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 170
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 171
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 172
                        self.rvalue(18)
                        pass

                    elif la_ == 5:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 173
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 174
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 175
                        self.rvalue(17)
                        pass

                    elif la_ == 6:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 176
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 177
                        self.match(Grammar_Project_2Parser.GREATER_THAN)
                        self.state = 178
                        self.rvalue(16)
                        pass

                    elif la_ == 7:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 179
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 180
                        self.match(Grammar_Project_2Parser.LESS_THAN)
                        self.state = 181
                        self.rvalue(15)
                        pass

                    elif la_ == 8:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 182
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 183
                        self.match(Grammar_Project_2Parser.GREATER_EQUAL)
                        self.state = 184
                        self.rvalue(14)
                        pass

                    elif la_ == 9:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 185
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 186
                        self.match(Grammar_Project_2Parser.LESS_EQUAL)
                        self.state = 187
                        self.rvalue(13)
                        pass

                    elif la_ == 10:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 188
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 189
                        self.match(Grammar_Project_2Parser.EQUALS)
                        self.state = 190
                        self.rvalue(12)
                        pass

                    elif la_ == 11:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 191
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 192
                        self.match(Grammar_Project_2Parser.NOT_EQUAL)
                        self.state = 193
                        self.rvalue(11)
                        pass

                    elif la_ == 12:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 194
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 195
                        self.match(Grammar_Project_2Parser.SHIFT_LEFT)
                        self.state = 196
                        self.rvalue(10)
                        pass

                    elif la_ == 13:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 197
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 198
                        self.match(Grammar_Project_2Parser.SHIFT_RIGHT)
                        self.state = 199
                        self.rvalue(9)
                        pass

                    elif la_ == 14:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 200
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 201
                        self.match(Grammar_Project_2Parser.BITWISE_AND)
                        self.state = 202
                        self.rvalue(8)
                        pass

                    elif la_ == 15:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 203
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 204
                        self.match(Grammar_Project_2Parser.BITWISE_OR)
                        self.state = 205
                        self.rvalue(7)
                        pass

                    elif la_ == 16:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 206
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 207
                        self.match(Grammar_Project_2Parser.BITWISE_XOR)
                        self.state = 208
                        self.rvalue(6)
                        pass

                    elif la_ == 17:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 209
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 210
                        self.match(Grammar_Project_2Parser.LOGICAL_AND)
                        self.state = 211
                        self.rvalue(5)
                        pass

                    elif la_ == 18:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 212
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 213
                        self.match(Grammar_Project_2Parser.LOGICAL_OR)
                        self.state = 214
                        self.rvalue(4)
                        pass

             
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.state = 220
            self.match(Grammar_Project_2Parser.LPAREN)
            self.state = 221
            self.type_()
            self.state = 222
            self.match(Grammar_Project_2Parser.RPAREN)
            self.state = 223
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
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11 or _la==12:
                    self.state = 225
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 228
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 229
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 230
                        self.match(Grammar_Project_2Parser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 233 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 235
                    self.match(Grammar_Project_2Parser.PLUS)


                self.state = 238
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 241 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 239
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 240
                        self.match(Grammar_Project_2Parser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 243 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 245
                    self.match(Grammar_Project_2Parser.MINUS)


                self.state = 248
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
            self.state = 251
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


    class ImplicitConversionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAREN(self):
            return self.getToken(Grammar_Project_2Parser.RPAREN, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_2Parser.LPAREN)
            else:
                return self.getToken(Grammar_Project_2Parser.LPAREN, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_2Parser.TypeContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_2Parser.TypeContext,i)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_implicitConversion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicitConversion" ):
                listener.enterImplicitConversion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicitConversion" ):
                listener.exitImplicitConversion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicitConversion" ):
                return visitor.visitImplicitConversion(self)
            else:
                return visitor.visitChildren(self)




    def implicitConversion(self):

        localctx = Grammar_Project_2Parser.ImplicitConversionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_implicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 253
                self.match(Grammar_Project_2Parser.LPAREN)
                self.state = 256 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 259 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 258
                self.type_()
                self.state = 261 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 114) != 0)):
                    break

            self.state = 263
            self.match(Grammar_Project_2Parser.RPAREN)
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
        self.enterRule(localctx, 20, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.type_()
            self.state = 267 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 266
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 269 
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
        self.enterRule(localctx, 22, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 271
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 274 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

            self.state = 276
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
        self.enterRule(localctx, 24, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 278
                self.match(Grammar_Project_2Parser.BITWISE_AND)
                self.state = 281 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

            self.state = 283
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
        self.enterRule(localctx, 26, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 285
                self.match(Grammar_Project_2Parser.T__3)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
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


    class PostFixIncrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.LvalueContext,0)


        def INCREMENT(self):
            return self.getToken(Grammar_Project_2Parser.INCREMENT, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_postFixIncrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostFixIncrement" ):
                listener.enterPostFixIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostFixIncrement" ):
                listener.exitPostFixIncrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostFixIncrement" ):
                return visitor.visitPostFixIncrement(self)
            else:
                return visitor.visitChildren(self)




    def postFixIncrement(self):

        localctx = Grammar_Project_2Parser.PostFixIncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.lvalue()
            self.state = 294
            self.match(Grammar_Project_2Parser.INCREMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostFixDecrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.LvalueContext,0)


        def DECREMENT(self):
            return self.getToken(Grammar_Project_2Parser.DECREMENT, 0)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_postFixDecrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostFixDecrement" ):
                listener.enterPostFixDecrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostFixDecrement" ):
                listener.exitPostFixDecrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostFixDecrement" ):
                return visitor.visitPostFixDecrement(self)
            else:
                return visitor.visitChildren(self)




    def postFixDecrement(self):

        localctx = Grammar_Project_2Parser.PostFixDecrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.lvalue()
            self.state = 297
            self.match(Grammar_Project_2Parser.DECREMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreFixIncrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENT(self):
            return self.getToken(Grammar_Project_2Parser.INCREMENT, 0)

        def lvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.LvalueContext,0)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_preFixIncrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreFixIncrement" ):
                listener.enterPreFixIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreFixIncrement" ):
                listener.exitPreFixIncrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreFixIncrement" ):
                return visitor.visitPreFixIncrement(self)
            else:
                return visitor.visitChildren(self)




    def preFixIncrement(self):

        localctx = Grammar_Project_2Parser.PreFixIncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(Grammar_Project_2Parser.INCREMENT)
            self.state = 300
            self.lvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreFixDecrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECREMENT(self):
            return self.getToken(Grammar_Project_2Parser.DECREMENT, 0)

        def lvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.LvalueContext,0)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_preFixDecrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreFixDecrement" ):
                listener.enterPreFixDecrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreFixDecrement" ):
                listener.exitPreFixDecrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreFixDecrement" ):
                return visitor.visitPreFixDecrement(self)
            else:
                return visitor.visitChildren(self)




    def preFixDecrement(self):

        localctx = Grammar_Project_2Parser.PreFixDecrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(Grammar_Project_2Parser.DECREMENT)
            self.state = 303
            self.lvalue()
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
        self.enterRule(localctx, 36, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
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
        self.enterRule(localctx, 38, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
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
         




