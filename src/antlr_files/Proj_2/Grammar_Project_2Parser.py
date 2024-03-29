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
        4,1,40,315,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,5,0,47,8,0,10,0,12,0,50,9,0,1,0,1,0,1,0,5,
        0,55,8,0,10,0,12,0,58,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,66,8,1,1,1,
        1,1,5,1,70,8,1,10,1,12,1,73,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        5,3,83,8,3,10,3,12,3,86,9,3,1,3,1,3,1,4,1,4,4,4,92,8,4,11,4,12,4,
        93,1,4,1,4,1,4,4,4,99,8,4,11,4,12,4,100,1,4,1,4,4,4,105,8,4,11,4,
        12,4,106,1,4,1,4,4,4,111,8,4,11,4,12,4,112,1,4,1,4,4,4,117,8,4,11,
        4,12,4,118,1,4,1,4,3,4,123,8,4,1,5,1,5,1,5,1,5,4,5,129,8,5,11,5,
        12,5,130,1,5,1,5,4,5,135,8,5,11,5,12,5,136,3,5,139,8,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,149,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,165,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,
        7,221,8,7,10,7,12,7,224,9,7,1,8,1,8,1,8,1,8,1,8,1,9,3,9,232,8,9,
        1,9,1,9,1,9,4,9,237,8,9,11,9,12,9,238,1,9,3,9,242,8,9,1,9,1,9,1,
        9,4,9,247,8,9,11,9,12,9,248,1,9,3,9,252,8,9,1,9,3,9,255,8,9,1,10,
        1,10,1,11,4,11,260,8,11,11,11,12,11,261,1,11,4,11,265,8,11,11,11,
        12,11,266,1,11,1,11,1,12,1,12,4,12,273,8,12,11,12,12,12,274,1,13,
        4,13,278,8,13,11,13,12,13,279,1,13,1,13,1,14,4,14,285,8,14,11,14,
        12,14,286,1,14,1,14,1,15,5,15,292,8,15,10,15,12,15,295,9,15,1,15,
        1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,
        1,20,1,20,1,21,1,21,1,21,0,2,2,14,22,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,0,3,1,0,11,12,1,0,31,33,2,0,1,1,
        5,6,355,0,48,1,0,0,0,2,65,1,0,0,0,4,74,1,0,0,0,6,80,1,0,0,0,8,122,
        1,0,0,0,10,138,1,0,0,0,12,148,1,0,0,0,14,164,1,0,0,0,16,225,1,0,
        0,0,18,254,1,0,0,0,20,256,1,0,0,0,22,259,1,0,0,0,24,270,1,0,0,0,
        26,277,1,0,0,0,28,284,1,0,0,0,30,293,1,0,0,0,32,298,1,0,0,0,34,301,
        1,0,0,0,36,304,1,0,0,0,38,307,1,0,0,0,40,310,1,0,0,0,42,312,1,0,
        0,0,44,47,3,42,21,0,45,47,3,10,5,0,46,44,1,0,0,0,46,45,1,0,0,0,47,
        50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,
        0,51,56,3,4,2,0,52,55,3,42,21,0,53,55,3,10,5,0,54,52,1,0,0,0,54,
        53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,
        0,58,56,1,0,0,0,59,60,5,0,0,1,60,1,1,0,0,0,61,62,6,1,-1,0,62,66,
        3,42,21,0,63,66,3,4,2,0,64,66,3,10,5,0,65,61,1,0,0,0,65,63,1,0,0,
        0,65,64,1,0,0,0,66,71,1,0,0,0,67,68,10,4,0,0,68,70,3,2,1,5,69,67,
        1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,3,1,0,0,0,73,
        71,1,0,0,0,74,75,5,1,0,0,75,76,5,2,0,0,76,77,5,7,0,0,77,78,5,8,0,
        0,78,79,3,6,3,0,79,5,1,0,0,0,80,84,5,9,0,0,81,83,3,8,4,0,82,81,1,
        0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,
        84,1,0,0,0,87,88,5,10,0,0,88,7,1,0,0,0,89,91,3,14,7,0,90,92,5,30,
        0,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,123,
        1,0,0,0,95,123,3,10,5,0,96,98,3,32,16,0,97,99,5,30,0,0,98,97,1,0,
        0,0,99,100,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,123,1,0,0,
        0,102,104,3,34,17,0,103,105,5,30,0,0,104,103,1,0,0,0,105,106,1,0,
        0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,123,1,0,0,0,108,110,3,36,
        18,0,109,111,5,30,0,0,110,109,1,0,0,0,111,112,1,0,0,0,112,110,1,
        0,0,0,112,113,1,0,0,0,113,123,1,0,0,0,114,116,3,38,19,0,115,117,
        5,30,0,0,116,115,1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,0,118,119,
        1,0,0,0,119,123,1,0,0,0,120,123,3,42,21,0,121,123,3,6,3,0,122,89,
        1,0,0,0,122,95,1,0,0,0,122,96,1,0,0,0,122,102,1,0,0,0,122,108,1,
        0,0,0,122,114,1,0,0,0,122,120,1,0,0,0,122,121,1,0,0,0,123,9,1,0,
        0,0,124,125,3,12,6,0,125,126,5,3,0,0,126,128,3,14,7,0,127,129,5,
        30,0,0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,1,
        0,0,0,131,139,1,0,0,0,132,134,3,12,6,0,133,135,5,30,0,0,134,133,
        1,0,0,0,135,136,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,139,
        1,0,0,0,138,124,1,0,0,0,138,132,1,0,0,0,139,11,1,0,0,0,140,149,3,
        40,20,0,141,142,3,30,15,0,142,143,3,40,20,0,143,149,1,0,0,0,144,
        145,3,24,12,0,145,146,3,40,20,0,146,149,1,0,0,0,147,149,3,26,13,
        0,148,140,1,0,0,0,148,141,1,0,0,0,148,144,1,0,0,0,148,147,1,0,0,
        0,149,13,1,0,0,0,150,151,6,7,-1,0,151,165,3,18,9,0,152,165,3,40,
        20,0,153,165,3,26,13,0,154,165,3,28,14,0,155,156,5,29,0,0,156,165,
        3,14,7,21,157,158,5,7,0,0,158,159,3,14,7,0,159,160,5,8,0,0,160,165,
        1,0,0,0,161,162,3,22,11,0,162,163,3,14,7,1,163,165,1,0,0,0,164,150,
        1,0,0,0,164,152,1,0,0,0,164,153,1,0,0,0,164,154,1,0,0,0,164,155,
        1,0,0,0,164,157,1,0,0,0,164,161,1,0,0,0,165,222,1,0,0,0,166,167,
        10,20,0,0,167,168,5,14,0,0,168,221,3,14,7,21,169,170,10,19,0,0,170,
        171,5,15,0,0,171,221,3,14,7,20,172,173,10,18,0,0,173,174,5,13,0,
        0,174,221,3,14,7,19,175,176,10,17,0,0,176,177,5,12,0,0,177,221,3,
        14,7,18,178,179,10,16,0,0,179,180,5,11,0,0,180,221,3,14,7,17,181,
        182,10,15,0,0,182,183,5,16,0,0,183,221,3,14,7,16,184,185,10,14,0,
        0,185,186,5,17,0,0,186,221,3,14,7,15,187,188,10,13,0,0,188,189,5,
        18,0,0,189,221,3,14,7,14,190,191,10,12,0,0,191,192,5,19,0,0,192,
        221,3,14,7,13,193,194,10,11,0,0,194,195,5,20,0,0,195,221,3,14,7,
        12,196,197,10,10,0,0,197,198,5,21,0,0,198,221,3,14,7,11,199,200,
        10,9,0,0,200,201,5,22,0,0,201,221,3,14,7,10,202,203,10,8,0,0,203,
        204,5,23,0,0,204,221,3,14,7,9,205,206,10,7,0,0,206,207,5,24,0,0,
        207,221,3,14,7,8,208,209,10,6,0,0,209,210,5,25,0,0,210,221,3,14,
        7,7,211,212,10,5,0,0,212,213,5,26,0,0,213,221,3,14,7,6,214,215,10,
        4,0,0,215,216,5,27,0,0,216,221,3,14,7,5,217,218,10,3,0,0,218,219,
        5,28,0,0,219,221,3,14,7,4,220,166,1,0,0,0,220,169,1,0,0,0,220,172,
        1,0,0,0,220,175,1,0,0,0,220,178,1,0,0,0,220,181,1,0,0,0,220,184,
        1,0,0,0,220,187,1,0,0,0,220,190,1,0,0,0,220,193,1,0,0,0,220,196,
        1,0,0,0,220,199,1,0,0,0,220,202,1,0,0,0,220,205,1,0,0,0,220,208,
        1,0,0,0,220,211,1,0,0,0,220,214,1,0,0,0,220,217,1,0,0,0,221,224,
        1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,15,1,0,0,0,224,222,1,
        0,0,0,225,226,5,7,0,0,226,227,3,30,15,0,227,228,5,8,0,0,228,229,
        3,14,7,0,229,17,1,0,0,0,230,232,7,0,0,0,231,230,1,0,0,0,231,232,
        1,0,0,0,232,233,1,0,0,0,233,255,3,20,10,0,234,235,5,11,0,0,235,237,
        5,12,0,0,236,234,1,0,0,0,237,238,1,0,0,0,238,236,1,0,0,0,238,239,
        1,0,0,0,239,241,1,0,0,0,240,242,5,11,0,0,241,240,1,0,0,0,241,242,
        1,0,0,0,242,243,1,0,0,0,243,255,3,20,10,0,244,245,5,12,0,0,245,247,
        5,11,0,0,246,244,1,0,0,0,247,248,1,0,0,0,248,246,1,0,0,0,248,249,
        1,0,0,0,249,251,1,0,0,0,250,252,5,12,0,0,251,250,1,0,0,0,251,252,
        1,0,0,0,252,253,1,0,0,0,253,255,3,20,10,0,254,231,1,0,0,0,254,236,
        1,0,0,0,254,246,1,0,0,0,255,19,1,0,0,0,256,257,7,1,0,0,257,21,1,
        0,0,0,258,260,5,7,0,0,259,258,1,0,0,0,260,261,1,0,0,0,261,259,1,
        0,0,0,261,262,1,0,0,0,262,264,1,0,0,0,263,265,3,30,15,0,264,263,
        1,0,0,0,265,266,1,0,0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,268,
        1,0,0,0,268,269,5,8,0,0,269,23,1,0,0,0,270,272,3,30,15,0,271,273,
        5,13,0,0,272,271,1,0,0,0,273,274,1,0,0,0,274,272,1,0,0,0,274,275,
        1,0,0,0,275,25,1,0,0,0,276,278,5,13,0,0,277,276,1,0,0,0,278,279,
        1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,282,
        3,40,20,0,282,27,1,0,0,0,283,285,5,24,0,0,284,283,1,0,0,0,285,286,
        1,0,0,0,286,284,1,0,0,0,286,287,1,0,0,0,287,288,1,0,0,0,288,289,
        3,40,20,0,289,29,1,0,0,0,290,292,5,4,0,0,291,290,1,0,0,0,292,295,
        1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,296,1,0,0,0,295,293,
        1,0,0,0,296,297,7,2,0,0,297,31,1,0,0,0,298,299,3,12,6,0,299,300,
        5,36,0,0,300,33,1,0,0,0,301,302,3,12,6,0,302,303,5,37,0,0,303,35,
        1,0,0,0,304,305,5,36,0,0,305,306,3,12,6,0,306,37,1,0,0,0,307,308,
        5,37,0,0,308,309,3,12,6,0,309,39,1,0,0,0,310,311,5,35,0,0,311,41,
        1,0,0,0,312,313,5,38,0,0,313,43,1,0,0,0,32,46,48,54,56,65,71,84,
        93,100,106,112,118,122,130,136,138,148,164,220,222,231,238,241,248,
        251,254,261,266,274,279,286,293
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 530982124274) != 0):
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


        def scope(self):
            return self.getTypedRuleContext(Grammar_Project_2Parser.ScopeContext,0)


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
            self.state = 122
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

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 121
                self.scope()
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
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.lvalue()
                self.state = 125
                self.match(Grammar_Project_2Parser.T__2)
                self.state = 126
                self.rvalue(0)
                self.state = 128 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 127
                        self.match(Grammar_Project_2Parser.SEMICOLON)

                    else:
                        raise NoViableAltException(self)
                    self.state = 130 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.lvalue()
                self.state = 134 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 133
                        self.match(Grammar_Project_2Parser.SEMICOLON)

                    else:
                        raise NoViableAltException(self)
                    self.state = 136 
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
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.type_()
                self.state = 142
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.pointer()
                self.state = 145
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 151
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 152
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 153
                self.deref()
                pass

            elif la_ == 4:
                self.state = 154
                self.addr()
                pass

            elif la_ == 5:
                self.state = 155
                self.match(Grammar_Project_2Parser.LOGICAL_NOT)
                self.state = 156
                self.rvalue(21)
                pass

            elif la_ == 6:
                self.state = 157
                self.match(Grammar_Project_2Parser.LPAREN)
                self.state = 158
                self.rvalue(0)
                self.state = 159
                self.match(Grammar_Project_2Parser.RPAREN)
                pass

            elif la_ == 7:
                self.state = 161
                self.explicitConversion()
                self.state = 162
                self.rvalue(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 220
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 166
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 167
                        self.match(Grammar_Project_2Parser.DIV)
                        self.state = 168
                        self.rvalue(21)
                        pass

                    elif la_ == 2:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 169
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 170
                        self.match(Grammar_Project_2Parser.MOD)
                        self.state = 171
                        self.rvalue(20)
                        pass

                    elif la_ == 3:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 172
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 173
                        self.match(Grammar_Project_2Parser.MULT)
                        self.state = 174
                        self.rvalue(19)
                        pass

                    elif la_ == 4:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 175
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 176
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 177
                        self.rvalue(18)
                        pass

                    elif la_ == 5:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 178
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 179
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 180
                        self.rvalue(17)
                        pass

                    elif la_ == 6:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 181
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 182
                        self.match(Grammar_Project_2Parser.GREATER_THAN)
                        self.state = 183
                        self.rvalue(16)
                        pass

                    elif la_ == 7:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 184
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 185
                        self.match(Grammar_Project_2Parser.LESS_THAN)
                        self.state = 186
                        self.rvalue(15)
                        pass

                    elif la_ == 8:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 187
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 188
                        self.match(Grammar_Project_2Parser.GREATER_EQUAL)
                        self.state = 189
                        self.rvalue(14)
                        pass

                    elif la_ == 9:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 190
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 191
                        self.match(Grammar_Project_2Parser.LESS_EQUAL)
                        self.state = 192
                        self.rvalue(13)
                        pass

                    elif la_ == 10:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 193
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 194
                        self.match(Grammar_Project_2Parser.EQUALS)
                        self.state = 195
                        self.rvalue(12)
                        pass

                    elif la_ == 11:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 196
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 197
                        self.match(Grammar_Project_2Parser.NOT_EQUAL)
                        self.state = 198
                        self.rvalue(11)
                        pass

                    elif la_ == 12:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 199
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 200
                        self.match(Grammar_Project_2Parser.SHIFT_LEFT)
                        self.state = 201
                        self.rvalue(10)
                        pass

                    elif la_ == 13:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 202
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 203
                        self.match(Grammar_Project_2Parser.SHIFT_RIGHT)
                        self.state = 204
                        self.rvalue(9)
                        pass

                    elif la_ == 14:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 205
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 206
                        self.match(Grammar_Project_2Parser.BITWISE_AND)
                        self.state = 207
                        self.rvalue(8)
                        pass

                    elif la_ == 15:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 208
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 209
                        self.match(Grammar_Project_2Parser.BITWISE_OR)
                        self.state = 210
                        self.rvalue(7)
                        pass

                    elif la_ == 16:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 211
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 212
                        self.match(Grammar_Project_2Parser.BITWISE_XOR)
                        self.state = 213
                        self.rvalue(6)
                        pass

                    elif la_ == 17:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 214
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 215
                        self.match(Grammar_Project_2Parser.LOGICAL_AND)
                        self.state = 216
                        self.rvalue(5)
                        pass

                    elif la_ == 18:
                        localctx = Grammar_Project_2Parser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 217
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 218
                        self.match(Grammar_Project_2Parser.LOGICAL_OR)
                        self.state = 219
                        self.rvalue(4)
                        pass

             
                self.state = 224
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
            self.state = 225
            self.match(Grammar_Project_2Parser.LPAREN)
            self.state = 226
            self.type_()
            self.state = 227
            self.match(Grammar_Project_2Parser.RPAREN)
            self.state = 228
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
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11 or _la==12:
                    self.state = 230
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 233
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 234
                        self.match(Grammar_Project_2Parser.PLUS)
                        self.state = 235
                        self.match(Grammar_Project_2Parser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 238 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 240
                    self.match(Grammar_Project_2Parser.PLUS)


                self.state = 243
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 244
                        self.match(Grammar_Project_2Parser.MINUS)
                        self.state = 245
                        self.match(Grammar_Project_2Parser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 248 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 250
                    self.match(Grammar_Project_2Parser.MINUS)


                self.state = 253
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
            self.state = 256
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
            self.state = 259 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 258
                self.match(Grammar_Project_2Parser.LPAREN)
                self.state = 261 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 264 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 263
                self.type_()
                self.state = 266 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 114) != 0)):
                    break

            self.state = 268
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
            self.state = 270
            self.type_()
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
            self.state = 277 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 276
                self.match(Grammar_Project_2Parser.MULT)
                self.state = 279 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

            self.state = 281
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
            self.state = 284 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 283
                self.match(Grammar_Project_2Parser.BITWISE_AND)
                self.state = 286 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

            self.state = 288
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
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 290
                self.match(Grammar_Project_2Parser.T__3)
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
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
            self.state = 298
            self.lvalue()
            self.state = 299
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
            self.state = 301
            self.lvalue()
            self.state = 302
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
            self.state = 304
            self.match(Grammar_Project_2Parser.INCREMENT)
            self.state = 305
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
            self.state = 307
            self.match(Grammar_Project_2Parser.DECREMENT)
            self.state = 308
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
            self.state = 310
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
            self.state = 312
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
         




