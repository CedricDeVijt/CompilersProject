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
        4,1,40,314,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,5,0,47,8,0,10,0,12,0,50,9,0,1,0,1,0,1,0,5,
        0,55,8,0,10,0,12,0,58,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,66,8,1,1,1,
        1,1,5,1,70,8,1,10,1,12,1,73,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        5,3,83,8,3,10,3,12,3,86,9,3,1,3,1,3,1,4,1,4,4,4,92,8,4,11,4,12,4,
        93,1,4,1,4,1,4,4,4,99,8,4,11,4,12,4,100,1,4,1,4,4,4,105,8,4,11,4,
        12,4,106,1,4,1,4,4,4,111,8,4,11,4,12,4,112,1,4,1,4,4,4,117,8,4,11,
        4,12,4,118,1,4,3,4,122,8,4,1,5,1,5,1,5,1,5,4,5,128,8,5,11,5,12,5,
        129,1,5,1,5,4,5,134,8,5,11,5,12,5,135,3,5,138,8,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,148,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,164,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,220,
        8,7,10,7,12,7,223,9,7,1,8,1,8,1,8,1,8,1,8,1,9,3,9,231,8,9,1,9,1,
        9,1,9,4,9,236,8,9,11,9,12,9,237,1,9,3,9,241,8,9,1,9,1,9,1,9,4,9,
        246,8,9,11,9,12,9,247,1,9,3,9,251,8,9,1,9,3,9,254,8,9,1,10,1,10,
        1,11,4,11,259,8,11,11,11,12,11,260,1,11,4,11,264,8,11,11,11,12,11,
        265,1,11,1,11,1,12,1,12,4,12,272,8,12,11,12,12,12,273,1,13,4,13,
        277,8,13,11,13,12,13,278,1,13,1,13,1,14,4,14,284,8,14,11,14,12,14,
        285,1,14,1,14,1,15,5,15,291,8,15,10,15,12,15,294,9,15,1,15,1,15,
        1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,
        1,20,1,21,1,21,1,21,0,2,2,14,22,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,0,3,1,0,11,12,1,0,31,33,2,0,1,1,5,6,353,
        0,48,1,0,0,0,2,65,1,0,0,0,4,74,1,0,0,0,6,80,1,0,0,0,8,121,1,0,0,
        0,10,137,1,0,0,0,12,147,1,0,0,0,14,163,1,0,0,0,16,224,1,0,0,0,18,
        253,1,0,0,0,20,255,1,0,0,0,22,258,1,0,0,0,24,269,1,0,0,0,26,276,
        1,0,0,0,28,283,1,0,0,0,30,292,1,0,0,0,32,297,1,0,0,0,34,300,1,0,
        0,0,36,303,1,0,0,0,38,306,1,0,0,0,40,309,1,0,0,0,42,311,1,0,0,0,
        44,47,3,42,21,0,45,47,3,10,5,0,46,44,1,0,0,0,46,45,1,0,0,0,47,50,
        1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,
        51,56,3,4,2,0,52,55,3,42,21,0,53,55,3,10,5,0,54,52,1,0,0,0,54,53,
        1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,
        58,56,1,0,0,0,59,60,5,0,0,1,60,1,1,0,0,0,61,62,6,1,-1,0,62,66,3,
        42,21,0,63,66,3,4,2,0,64,66,3,10,5,0,65,61,1,0,0,0,65,63,1,0,0,0,
        65,64,1,0,0,0,66,71,1,0,0,0,67,68,10,4,0,0,68,70,3,2,1,5,69,67,1,
        0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,3,1,0,0,0,73,
        71,1,0,0,0,74,75,5,1,0,0,75,76,5,2,0,0,76,77,5,7,0,0,77,78,5,8,0,
        0,78,79,3,6,3,0,79,5,1,0,0,0,80,84,5,9,0,0,81,83,3,8,4,0,82,81,1,
        0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,
        84,1,0,0,0,87,88,5,10,0,0,88,7,1,0,0,0,89,91,3,14,7,0,90,92,5,30,
        0,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,122,
        1,0,0,0,95,122,3,10,5,0,96,98,3,32,16,0,97,99,5,30,0,0,98,97,1,0,
        0,0,99,100,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,122,1,0,0,
        0,102,104,3,34,17,0,103,105,5,30,0,0,104,103,1,0,0,0,105,106,1,0,
        0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,122,1,0,0,0,108,110,3,36,
        18,0,109,111,5,30,0,0,110,109,1,0,0,0,111,112,1,0,0,0,112,110,1,
        0,0,0,112,113,1,0,0,0,113,122,1,0,0,0,114,116,3,38,19,0,115,117,
        5,30,0,0,116,115,1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,0,118,119,
        1,0,0,0,119,122,1,0,0,0,120,122,3,42,21,0,121,89,1,0,0,0,121,95,
        1,0,0,0,121,96,1,0,0,0,121,102,1,0,0,0,121,108,1,0,0,0,121,114,1,
        0,0,0,121,120,1,0,0,0,122,9,1,0,0,0,123,124,3,12,6,0,124,125,5,3,
        0,0,125,127,3,14,7,0,126,128,5,30,0,0,127,126,1,0,0,0,128,129,1,
        0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,138,1,0,0,0,131,133,3,
        12,6,0,132,134,5,30,0,0,133,132,1,0,0,0,134,135,1,0,0,0,135,133,
        1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,123,1,0,0,0,137,131,
        1,0,0,0,138,11,1,0,0,0,139,148,3,40,20,0,140,141,3,30,15,0,141,142,
        3,40,20,0,142,148,1,0,0,0,143,144,3,24,12,0,144,145,3,40,20,0,145,
        148,1,0,0,0,146,148,3,26,13,0,147,139,1,0,0,0,147,140,1,0,0,0,147,
        143,1,0,0,0,147,146,1,0,0,0,148,13,1,0,0,0,149,150,6,7,-1,0,150,
        164,3,18,9,0,151,164,3,40,20,0,152,164,3,26,13,0,153,164,3,28,14,
        0,154,155,5,29,0,0,155,164,3,14,7,21,156,157,5,7,0,0,157,158,3,14,
        7,0,158,159,5,8,0,0,159,164,1,0,0,0,160,161,3,22,11,0,161,162,3,
        14,7,1,162,164,1,0,0,0,163,149,1,0,0,0,163,151,1,0,0,0,163,152,1,
        0,0,0,163,153,1,0,0,0,163,154,1,0,0,0,163,156,1,0,0,0,163,160,1,
        0,0,0,164,221,1,0,0,0,165,166,10,20,0,0,166,167,5,14,0,0,167,220,
        3,14,7,21,168,169,10,19,0,0,169,170,5,15,0,0,170,220,3,14,7,20,171,
        172,10,18,0,0,172,173,5,13,0,0,173,220,3,14,7,19,174,175,10,17,0,
        0,175,176,5,12,0,0,176,220,3,14,7,18,177,178,10,16,0,0,178,179,5,
        11,0,0,179,220,3,14,7,17,180,181,10,15,0,0,181,182,5,16,0,0,182,
        220,3,14,7,16,183,184,10,14,0,0,184,185,5,17,0,0,185,220,3,14,7,
        15,186,187,10,13,0,0,187,188,5,18,0,0,188,220,3,14,7,14,189,190,
        10,12,0,0,190,191,5,19,0,0,191,220,3,14,7,13,192,193,10,11,0,0,193,
        194,5,20,0,0,194,220,3,14,7,12,195,196,10,10,0,0,196,197,5,21,0,
        0,197,220,3,14,7,11,198,199,10,9,0,0,199,200,5,22,0,0,200,220,3,
        14,7,10,201,202,10,8,0,0,202,203,5,23,0,0,203,220,3,14,7,9,204,205,
        10,7,0,0,205,206,5,24,0,0,206,220,3,14,7,8,207,208,10,6,0,0,208,
        209,5,25,0,0,209,220,3,14,7,7,210,211,10,5,0,0,211,212,5,26,0,0,
        212,220,3,14,7,6,213,214,10,4,0,0,214,215,5,27,0,0,215,220,3,14,
        7,5,216,217,10,3,0,0,217,218,5,28,0,0,218,220,3,14,7,4,219,165,1,
        0,0,0,219,168,1,0,0,0,219,171,1,0,0,0,219,174,1,0,0,0,219,177,1,
        0,0,0,219,180,1,0,0,0,219,183,1,0,0,0,219,186,1,0,0,0,219,189,1,
        0,0,0,219,192,1,0,0,0,219,195,1,0,0,0,219,198,1,0,0,0,219,201,1,
        0,0,0,219,204,1,0,0,0,219,207,1,0,0,0,219,210,1,0,0,0,219,213,1,
        0,0,0,219,216,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,
        0,0,0,222,15,1,0,0,0,223,221,1,0,0,0,224,225,5,7,0,0,225,226,3,30,
        15,0,226,227,5,8,0,0,227,228,3,14,7,0,228,17,1,0,0,0,229,231,7,0,
        0,0,230,229,1,0,0,0,230,231,1,0,0,0,231,232,1,0,0,0,232,254,3,20,
        10,0,233,234,5,11,0,0,234,236,5,12,0,0,235,233,1,0,0,0,236,237,1,
        0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,241,5,
        11,0,0,240,239,1,0,0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,254,3,
        20,10,0,243,244,5,12,0,0,244,246,5,11,0,0,245,243,1,0,0,0,246,247,
        1,0,0,0,247,245,1,0,0,0,247,248,1,0,0,0,248,250,1,0,0,0,249,251,
        5,12,0,0,250,249,1,0,0,0,250,251,1,0,0,0,251,252,1,0,0,0,252,254,
        3,20,10,0,253,230,1,0,0,0,253,235,1,0,0,0,253,245,1,0,0,0,254,19,
        1,0,0,0,255,256,7,1,0,0,256,21,1,0,0,0,257,259,5,7,0,0,258,257,1,
        0,0,0,259,260,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,263,1,
        0,0,0,262,264,3,30,15,0,263,262,1,0,0,0,264,265,1,0,0,0,265,263,
        1,0,0,0,265,266,1,0,0,0,266,267,1,0,0,0,267,268,5,8,0,0,268,23,1,
        0,0,0,269,271,3,30,15,0,270,272,5,13,0,0,271,270,1,0,0,0,272,273,
        1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,25,1,0,0,0,275,277,5,
        13,0,0,276,275,1,0,0,0,277,278,1,0,0,0,278,276,1,0,0,0,278,279,1,
        0,0,0,279,280,1,0,0,0,280,281,3,40,20,0,281,27,1,0,0,0,282,284,5,
        24,0,0,283,282,1,0,0,0,284,285,1,0,0,0,285,283,1,0,0,0,285,286,1,
        0,0,0,286,287,1,0,0,0,287,288,3,40,20,0,288,29,1,0,0,0,289,291,5,
        4,0,0,290,289,1,0,0,0,291,294,1,0,0,0,292,290,1,0,0,0,292,293,1,
        0,0,0,293,295,1,0,0,0,294,292,1,0,0,0,295,296,7,2,0,0,296,31,1,0,
        0,0,297,298,3,12,6,0,298,299,5,36,0,0,299,33,1,0,0,0,300,301,3,12,
        6,0,301,302,5,37,0,0,302,35,1,0,0,0,303,304,5,36,0,0,304,305,3,12,
        6,0,305,37,1,0,0,0,306,307,5,37,0,0,307,308,3,12,6,0,308,39,1,0,
        0,0,309,310,5,35,0,0,310,41,1,0,0,0,311,312,5,38,0,0,312,43,1,0,
        0,0,32,46,48,54,56,65,71,84,93,100,106,112,118,121,129,135,137,147,
        163,219,221,230,237,240,247,250,253,260,265,273,278,285,292
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
                      "INCREMENT", "DECREMENT", "COMMENT", "BLOCKCOMMENT", 
                      "LINECOMMENT" ]

    RULE_program = 0
    RULE_programLine = 1
    RULE_main = 2
    RULE_scope = 3
    RULE_statement = 4
    RULE_variables = 5
    RULE_lvalue = 6
    RULE_rvalue = 7
    RULE_rvalueCast = 8
    RULE_unaryExpression = 9
    RULE_literal = 10
    RULE_explicitConversion = 11
    RULE_pointer = 12
    RULE_deref = 13
    RULE_addr = 14
    RULE_type = 15
    RULE_postFixIncrement = 16
    RULE_postFixDecrement = 17
    RULE_preFixIncrement = 18
    RULE_preFixDecrement = 19
    RULE_identifier = 20
    RULE_comment = 21

    ruleNames =  [ "program", "programLine", "main", "scope", "statement", 
                   "variables", "lvalue", "rvalue", "rvalueCast", "unaryExpression", 
                   "literal", "explicitConversion", "pointer", "deref", 
                   "addr", "type", "postFixIncrement", "postFixDecrement", 
                   "preFixIncrement", "preFixDecrement", "identifier", "comment" ]

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
    BLOCKCOMMENT=39
    LINECOMMENT=40

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


        def EOF(self):
            return self.getToken(Grammar_Project_2Parser.EOF, 0)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_2Parser.CommentContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_2Parser.CommentContext,i)


        def variables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_2Parser.VariablesContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_2Parser.VariablesContext,i)


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
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 46
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [38]:
                        self.state = 44
                        self.comment()
                        pass
                    elif token in [1, 4, 5, 6, 13, 35]:
                        self.state = 45
                        self.variables()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 51
            self.main()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 309237653618) != 0):
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [38]:
                    self.state = 52
                    self.comment()
                    pass
                elif token in [1, 4, 5, 6, 13, 35]:
                    self.state = 53
                    self.variables()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(Grammar_Project_2Parser.EOF)
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

        def comment(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.CommentContext,0)


        def main(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.MainContext,0)


        def variables(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.VariablesContext,0)


        def programLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_Project_2Parser.ProgramLineContext)
            else:
                return self.getTypedRuleContext(Grammar_Project_2Parser.ProgramLineContext,i)


        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_programLine

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



    def programLine(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Grammar_Project_2Parser.ProgramLineContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_programLine, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 62
                self.comment()
                pass

            elif la_ == 2:
                self.state = 63
                self.main()
                pass

            elif la_ == 3:
                self.state = 64
                self.variables()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Grammar_Project_2Parser.ProgramLineContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_programLine)
                    self.state = 67
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 68
                    self.programLine(5) 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 4, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(Grammar_Project_2Parser.T__0)
            self.state = 75
            self.match(Grammar_Project_2Parser.T__1)
            self.state = 76
            self.match(Grammar_Project_2Parser.LPAREN)
            self.state = 77
            self.match(Grammar_Project_2Parser.RPAREN)
            self.state = 78
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
        self.enterRule(localctx, 6, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(Grammar_Project_2Parser.LBRACE)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 530982123762) != 0):
                self.state = 81
                self.statement()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
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

        def variables(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.VariablesContext,0)


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
        self.enterRule(localctx, 8, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.rvalue(0)
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 90
                    self.match(Grammar_Project_2Parser.SEMICOLON)
                    self.state = 93 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.variables()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.postFixIncrement()
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

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.postFixDecrement()
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

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 108
                self.preFixIncrement()
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

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 114
                self.preFixDecrement()
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

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 120
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.LvalueContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.RvalueContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_Project_2Parser.SEMICOLON)
            else:
                return self.getToken(Grammar_Project_2Parser.SEMICOLON, i)

        def getRuleIndex(self):
            return Grammar_Project_2Parser.RULE_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables" ):
                listener.enterVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables" ):
                listener.exitVariables(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = Grammar_Project_2Parser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variables)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.lvalue()
                self.state = 124
                self.match(Grammar_Project_2Parser.T__2)
                self.state = 125
                self.rvalue(0)
                self.state = 127 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 126
                        self.match(Grammar_Project_2Parser.SEMICOLON)

                    else:
                        raise NoViableAltException(self)
                    self.state = 129 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.lvalue()
                self.state = 133 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 132
                        self.match(Grammar_Project_2Parser.SEMICOLON)

                    else:
                        raise NoViableAltException(self)
                    self.state = 135 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_lvalue)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.type_()
                self.state = 141
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.pointer()
                self.state = 144
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
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

        def explicitConversion(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.ExplicitConversionContext,0)


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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 150
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 151
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 152
                self.deref()
                pass

            elif la_ == 4:
                self.state = 153
                self.addr()
                pass

            elif la_ == 5:
                self.state = 154
                self.match(Grammar_Project_2Parser.LOGICAL_NOT)
                self.state = 155
                self.rvalue(21)
                pass

            elif la_ == 6:
                self.state = 156
                self.match(Grammar_Project_2Parser.LPAREN)
                self.state = 157
                self.rvalue(0)
                self.state = 158
                self.match(Grammar_Project_2Parser.RPAREN)
                pass

            elif la_ == 7:
                self.state = 160
                self.explicitConversion()
                self.state = 161
                self.rvalue(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 219
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 165
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 166
                        self.match(Grammar_Project_2Parser.DIV)
                        self.state = 167
                        self.rvalue(21)
                        pass

                    elif la_ == 2:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 168
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 169
                        self.match(Grammar_Project_2Parser.MOD)
                        self.state = 170
                        self.rvalue(20)
                        pass

                    elif la_ == 3:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 171
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 172
                        self.match(Grammar_Project_2Parser.MULT)
                        self.state = 173
                        self.rvalue(19)
                        pass

                    elif la_ == 4:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 174
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 175
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 176
                        self.rvalue(18)
                        pass

                    elif la_ == 5:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 177
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 178
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 179
                        self.rvalue(17)
                        pass

                    elif la_ == 6:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 180
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 181
                        self.match(Grammar_Project_2Parser.GREATER_THAN)
                        self.state = 182
                        self.rvalue(16)
                        pass

                    elif la_ == 7:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 183
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 184
                        self.match(Grammar_Project_2Parser.LESS_THAN)
                        self.state = 185
                        self.rvalue(15)
                        pass

                    elif la_ == 8:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 186
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 187
                        self.match(Grammar_Project_2Parser.GREATER_EQUAL)
                        self.state = 188
                        self.rvalue(14)
                        pass

                    elif la_ == 9:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 189
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 190
                        self.match(Grammar_Project_2Parser.LESS_EQUAL)
                        self.state = 191
                        self.rvalue(13)
                        pass

                    elif la_ == 10:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 192
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 193
                        self.match(Grammar_Project_2Parser.EQUALS)
                        self.state = 194
                        self.rvalue(12)
                        pass

                    elif la_ == 11:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 195
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 196
                        self.match(Grammar_Project_2Parser.NOT_EQUAL)
                        self.state = 197
                        self.rvalue(11)
                        pass

                    elif la_ == 12:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 198
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 199
                        self.match(Grammar_Project_2Parser.SHIFT_LEFT)
                        self.state = 200
                        self.rvalue(10)
                        pass

                    elif la_ == 13:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 201
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 202
                        self.match(Grammar_Project_2Parser.SHIFT_RIGHT)
                        self.state = 203
                        self.rvalue(9)
                        pass

                    elif la_ == 14:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 204
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 205
                        self.match(Grammar_Project_2Parser.BITWISE_AND)
                        self.state = 206
                        self.rvalue(8)
                        pass

                    elif la_ == 15:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 207
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 208
                        self.match(Grammar_Project_2Parser.BITWISE_OR)
                        self.state = 209
                        self.rvalue(7)
                        pass

                    elif la_ == 16:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 210
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 211
                        self.match(Grammar_Project_2Parser.BITWISE_XOR)
                        self.state = 212
                        self.rvalue(6)
                        pass

                    elif la_ == 17:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 213
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 214
                        self.match(Grammar_Project_2Parser.LOGICAL_AND)
                        self.state = 215
                        self.rvalue(5)
                        pass

                    elif la_ == 18:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 216
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 217
                        self.match(Grammar_Project_2Parser.LOGICAL_OR)
                        self.state = 218
                        self.rvalue(4)
                        pass

             
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_rvalueCast)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(Grammar_Project_2Parser.LPAREN)
            self.state = 225
            self.type_()
            self.state = 226
            self.match(Grammar_Project_2Parser.RPAREN)
            self.state = 227
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
        self.enterRule(localctx, 18, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11 or _la==12:
                    self.state = 229
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 232
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 233
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 234
                        self.match(Grammar_Project_2Parser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 237 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 239
                    self.match(Grammar_Project_2Parser.PLUS)


                self.state = 242
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 245 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 243
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 244
                        self.match(Grammar_Project_2Parser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 247 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 249
                    self.match(Grammar_Project_2Parser.MINUS)


                self.state = 252
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
        self.enterRule(localctx, 20, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
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


    class ExplicitConversionContext(ParserRuleContext):
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
            return Grammar_Project_2Parser.RULE_explicitConversion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicitConversion" ):
                listener.enterExplicitConversion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicitConversion" ):
                listener.exitExplicitConversion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicitConversion" ):
                return visitor.visitExplicitConversion(self)
            else:
                return visitor.visitChildren(self)




    def explicitConversion(self):

        localctx = Grammar_Project_2Parser.ExplicitConversionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 257
                self.match(Grammar_Project_2Parser.LPAREN)
                self.state = 260 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 263 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 262
                self.type_()
                self.state = 265 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 114) != 0)):
                    break

            self.state = 267
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
        self.enterRule(localctx, 24, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.type_()
            self.state = 271 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 270
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 273 
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
        self.enterRule(localctx, 26, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 275
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 278 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

            self.state = 280
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
        self.enterRule(localctx, 28, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 282
                self.match(Grammar_Project_2Parser.BITWISE_AND)
                self.state = 285 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

            self.state = 287
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
        self.enterRule(localctx, 30, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 289
                self.match(Grammar_Project_2Parser.T__3)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
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
        self.enterRule(localctx, 32, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.lvalue()
            self.state = 298
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
        self.enterRule(localctx, 34, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.lvalue()
            self.state = 301
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
        self.enterRule(localctx, 36, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(Grammar_Project_2Parser.INCREMENT)
            self.state = 304
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
        self.enterRule(localctx, 38, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(Grammar_Project_2Parser.DECREMENT)
            self.state = 307
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
        self.enterRule(localctx, 40, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
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
        self.enterRule(localctx, 42, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
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
        self._predicates[1] = self.programLine_sempred
        self._predicates[7] = self.rvalue_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def programLine_sempred(self, localctx:ProgramLineContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

    def rvalue_sempred(self, localctx:RvalueContext, predIndex:int):
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
         

            if predIndex == 18:
                return self.precpred(self._ctx, 3)
         




