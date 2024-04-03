# Generated from grammars/Grammar.g4 by ANTLR 4.13.1
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
        4,1,48,326,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,1,0,
        1,0,1,0,5,0,57,8,0,10,0,12,0,60,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,
        68,8,1,1,1,1,1,5,1,72,8,1,10,1,12,1,75,9,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,5,3,85,8,3,10,3,12,3,88,9,3,1,3,1,3,1,4,1,4,4,4,94,8,4,
        11,4,12,4,95,1,4,1,4,1,4,4,4,101,8,4,11,4,12,4,102,1,4,1,4,4,4,107,
        8,4,11,4,12,4,108,1,4,1,4,4,4,113,8,4,11,4,12,4,114,1,4,1,4,4,4,
        119,8,4,11,4,12,4,120,1,4,1,4,1,4,3,4,126,8,4,1,5,1,5,1,5,1,5,1,
        5,1,5,3,5,134,8,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,4,7,145,8,
        7,11,7,12,7,146,1,7,1,7,4,7,151,8,7,11,7,12,7,152,3,7,155,8,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,165,8,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,181,8,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,5,9,237,8,9,10,9,12,9,240,9,9,1,10,3,10,243,8,10,1,10,1,10,
        1,10,4,10,248,8,10,11,10,12,10,249,1,10,3,10,253,8,10,1,10,1,10,
        1,10,4,10,258,8,10,11,10,12,10,259,1,10,3,10,263,8,10,1,10,3,10,
        266,8,10,1,11,1,11,1,12,4,12,271,8,12,11,12,12,12,272,1,12,4,12,
        276,8,12,11,12,12,12,277,1,12,1,12,1,13,1,13,4,13,284,8,13,11,13,
        12,13,285,1,14,4,14,289,8,14,11,14,12,14,290,1,14,1,14,1,15,4,15,
        296,8,15,11,15,12,15,297,1,15,1,15,1,16,5,16,303,8,16,10,16,12,16,
        306,9,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,
        1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,0,2,2,18,23,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,4,1,0,6,10,
        1,0,19,20,1,0,39,41,2,0,1,1,13,14,367,0,50,1,0,0,0,2,67,1,0,0,0,
        4,76,1,0,0,0,6,82,1,0,0,0,8,125,1,0,0,0,10,127,1,0,0,0,12,138,1,
        0,0,0,14,154,1,0,0,0,16,164,1,0,0,0,18,180,1,0,0,0,20,265,1,0,0,
        0,22,267,1,0,0,0,24,270,1,0,0,0,26,281,1,0,0,0,28,288,1,0,0,0,30,
        295,1,0,0,0,32,304,1,0,0,0,34,309,1,0,0,0,36,312,1,0,0,0,38,315,
        1,0,0,0,40,318,1,0,0,0,42,321,1,0,0,0,44,323,1,0,0,0,46,49,3,44,
        22,0,47,49,3,14,7,0,48,46,1,0,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,
        48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,58,3,4,2,
        0,54,57,3,44,22,0,55,57,3,14,7,0,56,54,1,0,0,0,56,55,1,0,0,0,57,
        60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,
        0,61,62,5,0,0,1,62,1,1,0,0,0,63,64,6,1,-1,0,64,68,3,44,22,0,65,68,
        3,4,2,0,66,68,3,14,7,0,67,63,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,
        68,73,1,0,0,0,69,70,10,4,0,0,70,72,3,2,1,5,71,69,1,0,0,0,72,75,1,
        0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,3,1,0,0,0,75,73,1,0,0,0,76,
        77,5,1,0,0,77,78,5,2,0,0,78,79,5,15,0,0,79,80,5,16,0,0,80,81,3,6,
        3,0,81,5,1,0,0,0,82,86,5,17,0,0,83,85,3,8,4,0,84,83,1,0,0,0,85,88,
        1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,
        89,90,5,18,0,0,90,7,1,0,0,0,91,93,3,18,9,0,92,94,5,38,0,0,93,92,
        1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,126,1,0,0,0,
        97,126,3,14,7,0,98,100,3,34,17,0,99,101,5,38,0,0,100,99,1,0,0,0,
        101,102,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,126,1,0,0,0,
        104,106,3,36,18,0,105,107,5,38,0,0,106,105,1,0,0,0,107,108,1,0,0,
        0,108,106,1,0,0,0,108,109,1,0,0,0,109,126,1,0,0,0,110,112,3,38,19,
        0,111,113,5,38,0,0,112,111,1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,
        0,114,115,1,0,0,0,115,126,1,0,0,0,116,118,3,40,20,0,117,119,5,38,
        0,0,118,117,1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,
        0,0,121,126,1,0,0,0,122,126,3,44,22,0,123,126,3,10,5,0,124,126,3,
        6,3,0,125,91,1,0,0,0,125,97,1,0,0,0,125,98,1,0,0,0,125,104,1,0,0,
        0,125,110,1,0,0,0,125,116,1,0,0,0,125,122,1,0,0,0,125,123,1,0,0,
        0,125,124,1,0,0,0,126,9,1,0,0,0,127,128,5,3,0,0,128,129,5,15,0,0,
        129,130,3,12,6,0,130,133,5,4,0,0,131,134,5,5,0,0,132,134,3,22,11,
        0,133,131,1,0,0,0,133,132,1,0,0,0,134,135,1,0,0,0,135,136,5,16,0,
        0,136,137,5,38,0,0,137,11,1,0,0,0,138,139,7,0,0,0,139,13,1,0,0,0,
        140,141,3,16,8,0,141,142,5,11,0,0,142,144,3,18,9,0,143,145,5,38,
        0,0,144,143,1,0,0,0,145,146,1,0,0,0,146,144,1,0,0,0,146,147,1,0,
        0,0,147,155,1,0,0,0,148,150,3,16,8,0,149,151,5,38,0,0,150,149,1,
        0,0,0,151,152,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,155,1,
        0,0,0,154,140,1,0,0,0,154,148,1,0,0,0,155,15,1,0,0,0,156,165,3,42,
        21,0,157,158,3,32,16,0,158,159,3,42,21,0,159,165,1,0,0,0,160,161,
        3,26,13,0,161,162,3,42,21,0,162,165,1,0,0,0,163,165,3,28,14,0,164,
        156,1,0,0,0,164,157,1,0,0,0,164,160,1,0,0,0,164,163,1,0,0,0,165,
        17,1,0,0,0,166,167,6,9,-1,0,167,181,3,20,10,0,168,181,3,42,21,0,
        169,181,3,28,14,0,170,181,3,30,15,0,171,172,5,37,0,0,172,181,3,18,
        9,21,173,174,5,15,0,0,174,175,3,18,9,0,175,176,5,16,0,0,176,181,
        1,0,0,0,177,178,3,24,12,0,178,179,3,18,9,1,179,181,1,0,0,0,180,166,
        1,0,0,0,180,168,1,0,0,0,180,169,1,0,0,0,180,170,1,0,0,0,180,171,
        1,0,0,0,180,173,1,0,0,0,180,177,1,0,0,0,181,238,1,0,0,0,182,183,
        10,20,0,0,183,184,5,22,0,0,184,237,3,18,9,21,185,186,10,19,0,0,186,
        187,5,23,0,0,187,237,3,18,9,20,188,189,10,18,0,0,189,190,5,21,0,
        0,190,237,3,18,9,19,191,192,10,17,0,0,192,193,5,20,0,0,193,237,3,
        18,9,18,194,195,10,16,0,0,195,196,5,19,0,0,196,237,3,18,9,17,197,
        198,10,15,0,0,198,199,5,24,0,0,199,237,3,18,9,16,200,201,10,14,0,
        0,201,202,5,25,0,0,202,237,3,18,9,15,203,204,10,13,0,0,204,205,5,
        26,0,0,205,237,3,18,9,14,206,207,10,12,0,0,207,208,5,27,0,0,208,
        237,3,18,9,13,209,210,10,11,0,0,210,211,5,28,0,0,211,237,3,18,9,
        12,212,213,10,10,0,0,213,214,5,29,0,0,214,237,3,18,9,11,215,216,
        10,9,0,0,216,217,5,30,0,0,217,237,3,18,9,10,218,219,10,8,0,0,219,
        220,5,31,0,0,220,237,3,18,9,9,221,222,10,7,0,0,222,223,5,32,0,0,
        223,237,3,18,9,8,224,225,10,6,0,0,225,226,5,33,0,0,226,237,3,18,
        9,7,227,228,10,5,0,0,228,229,5,34,0,0,229,237,3,18,9,6,230,231,10,
        4,0,0,231,232,5,35,0,0,232,237,3,18,9,5,233,234,10,3,0,0,234,235,
        5,36,0,0,235,237,3,18,9,4,236,182,1,0,0,0,236,185,1,0,0,0,236,188,
        1,0,0,0,236,191,1,0,0,0,236,194,1,0,0,0,236,197,1,0,0,0,236,200,
        1,0,0,0,236,203,1,0,0,0,236,206,1,0,0,0,236,209,1,0,0,0,236,212,
        1,0,0,0,236,215,1,0,0,0,236,218,1,0,0,0,236,221,1,0,0,0,236,224,
        1,0,0,0,236,227,1,0,0,0,236,230,1,0,0,0,236,233,1,0,0,0,237,240,
        1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,19,1,0,0,0,240,238,1,
        0,0,0,241,243,7,1,0,0,242,241,1,0,0,0,242,243,1,0,0,0,243,244,1,
        0,0,0,244,266,3,22,11,0,245,246,5,19,0,0,246,248,5,20,0,0,247,245,
        1,0,0,0,248,249,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,252,
        1,0,0,0,251,253,5,19,0,0,252,251,1,0,0,0,252,253,1,0,0,0,253,254,
        1,0,0,0,254,266,3,22,11,0,255,256,5,20,0,0,256,258,5,19,0,0,257,
        255,1,0,0,0,258,259,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,
        262,1,0,0,0,261,263,5,20,0,0,262,261,1,0,0,0,262,263,1,0,0,0,263,
        264,1,0,0,0,264,266,3,22,11,0,265,242,1,0,0,0,265,247,1,0,0,0,265,
        257,1,0,0,0,266,21,1,0,0,0,267,268,7,2,0,0,268,23,1,0,0,0,269,271,
        5,15,0,0,270,269,1,0,0,0,271,272,1,0,0,0,272,270,1,0,0,0,272,273,
        1,0,0,0,273,275,1,0,0,0,274,276,3,32,16,0,275,274,1,0,0,0,276,277,
        1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,280,
        5,16,0,0,280,25,1,0,0,0,281,283,3,32,16,0,282,284,5,21,0,0,283,282,
        1,0,0,0,284,285,1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,27,1,
        0,0,0,287,289,5,21,0,0,288,287,1,0,0,0,289,290,1,0,0,0,290,288,1,
        0,0,0,290,291,1,0,0,0,291,292,1,0,0,0,292,293,3,42,21,0,293,29,1,
        0,0,0,294,296,5,32,0,0,295,294,1,0,0,0,296,297,1,0,0,0,297,295,1,
        0,0,0,297,298,1,0,0,0,298,299,1,0,0,0,299,300,3,42,21,0,300,31,1,
        0,0,0,301,303,5,12,0,0,302,301,1,0,0,0,303,306,1,0,0,0,304,302,1,
        0,0,0,304,305,1,0,0,0,305,307,1,0,0,0,306,304,1,0,0,0,307,308,7,
        3,0,0,308,33,1,0,0,0,309,310,3,16,8,0,310,311,5,44,0,0,311,35,1,
        0,0,0,312,313,3,16,8,0,313,314,5,45,0,0,314,37,1,0,0,0,315,316,5,
        44,0,0,316,317,3,16,8,0,317,39,1,0,0,0,318,319,5,45,0,0,319,320,
        3,16,8,0,320,41,1,0,0,0,321,322,5,43,0,0,322,43,1,0,0,0,323,324,
        5,46,0,0,324,45,1,0,0,0,33,48,50,56,58,67,73,86,95,102,108,114,120,
        125,133,146,152,154,164,180,236,238,242,249,252,259,262,265,272,
        277,285,290,297,304
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'printf'", "','", 
                     "'var'", "'\"%s\"'", "'\"%d\"'", "'\"%x\"'", "'\"%f\"'", 
                     "'\"%c\"'", "'='", "'const'", "'float'", "'char'", 
                     "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'<<'", "'>>'", "'&'", "'|'", "'^'", "'&&'", "'||'", 
                     "'!'", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_printfStatement = 5
    RULE_formatSpecifier = 6
    RULE_variables = 7
    RULE_lvalue = 8
    RULE_rvalue = 9
    RULE_unaryExpression = 10
    RULE_literal = 11
    RULE_explicitConversion = 12
    RULE_pointer = 13
    RULE_deref = 14
    RULE_addr = 15
    RULE_type = 16
    RULE_postFixIncrement = 17
    RULE_postFixDecrement = 18
    RULE_preFixIncrement = 19
    RULE_preFixDecrement = 20
    RULE_identifier = 21
    RULE_comment = 22

    ruleNames =  [ "program", "programLine", "main", "scope", "statement", 
                   "printfStatement", "formatSpecifier", "variables", "lvalue", 
                   "rvalue", "unaryExpression", "literal", "explicitConversion", 
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
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    LPAREN=15
    RPAREN=16
    LBRACE=17
    RBRACE=18
    PLUS=19
    MINUS=20
    MULT=21
    DIV=22
    MOD=23
    GREATER_THAN=24
    LESS_THAN=25
    GREATER_EQUAL=26
    LESS_EQUAL=27
    EQUALS=28
    NOT_EQUAL=29
    SHIFT_LEFT=30
    SHIFT_RIGHT=31
    BITWISE_AND=32
    BITWISE_OR=33
    BITWISE_XOR=34
    LOGICAL_AND=35
    LOGICAL_OR=36
    LOGICAL_NOT=37
    SEMICOLON=38
    INT=39
    FLOAT=40
    CHAR=41
    WHITESPACE=42
    IDENTIFIER=43
    INCREMENT=44
    DECREMENT=45
    COMMENT=46
    BLOCKCOMMENT=47
    LINECOMMENT=48

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
            return self.getTypedRuleContext(GrammarParser.MainContext,0)


        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.CommentContext)
            else:
                return self.getTypedRuleContext(GrammarParser.CommentContext,i)


        def variables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.VariablesContext)
            else:
                return self.getTypedRuleContext(GrammarParser.VariablesContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_program

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

        localctx = GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 48
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [46]:
                        self.state = 46
                        self.comment()
                        pass
                    elif token in [1, 12, 13, 14, 21, 43]:
                        self.state = 47
                        self.variables()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 53
            self.main()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 79164839325698) != 0):
                self.state = 56
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [46]:
                    self.state = 54
                    self.comment()
                    pass
                elif token in [1, 12, 13, 14, 21, 43]:
                    self.state = 55
                    self.variables()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(GrammarParser.EOF)
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
            return self.getTypedRuleContext(GrammarParser.CommentContext,0)


        def main(self):
            return self.getTypedRuleContext(GrammarParser.MainContext,0)


        def variables(self):
            return self.getTypedRuleContext(GrammarParser.VariablesContext,0)


        def programLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ProgramLineContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ProgramLineContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_programLine

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
        localctx = GrammarParser.ProgramLineContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_programLine, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 64
                self.comment()
                pass

            elif la_ == 2:
                self.state = 65
                self.main()
                pass

            elif la_ == 3:
                self.state = 66
                self.variables()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ProgramLineContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_programLine)
                    self.state = 69
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 70
                    self.programLine(5) 
                self.state = 75
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
            return self.getToken(GrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def scope(self):
            return self.getTypedRuleContext(GrammarParser.ScopeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_main

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

        localctx = GrammarParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(GrammarParser.T__0)
            self.state = 77
            self.match(GrammarParser.T__1)
            self.state = 78
            self.match(GrammarParser.LPAREN)
            self.state = 79
            self.match(GrammarParser.RPAREN)
            self.state = 80
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
            return self.getToken(GrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GrammarParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_scope

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

        localctx = GrammarParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(GrammarParser.LBRACE)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 135931423813642) != 0):
                self.state = 83
                self.statement()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(GrammarParser.RBRACE)
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
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def variables(self):
            return self.getTypedRuleContext(GrammarParser.VariablesContext,0)


        def postFixIncrement(self):
            return self.getTypedRuleContext(GrammarParser.PostFixIncrementContext,0)


        def postFixDecrement(self):
            return self.getTypedRuleContext(GrammarParser.PostFixDecrementContext,0)


        def preFixIncrement(self):
            return self.getTypedRuleContext(GrammarParser.PreFixIncrementContext,0)


        def preFixDecrement(self):
            return self.getTypedRuleContext(GrammarParser.PreFixDecrementContext,0)


        def comment(self):
            return self.getTypedRuleContext(GrammarParser.CommentContext,0)


        def printfStatement(self):
            return self.getTypedRuleContext(GrammarParser.PrintfStatementContext,0)


        def scope(self):
            return self.getTypedRuleContext(GrammarParser.ScopeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

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

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.rvalue(0)
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 92
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 95 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==38):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.variables()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.postFixIncrement()
                self.state = 100 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 99
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 102 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==38):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.postFixDecrement()
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 105
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 108 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==38):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 110
                self.preFixIncrement()
                self.state = 112 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 111
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 114 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==38):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 116
                self.preFixDecrement()
                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 117
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 120 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==38):
                        break

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 122
                self.comment()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 123
                self.printfStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 124
                self.scope()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def formatSpecifier(self):
            return self.getTypedRuleContext(GrammarParser.FormatSpecifierContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def literal(self):
            return self.getTypedRuleContext(GrammarParser.LiteralContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_printfStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintfStatement" ):
                listener.enterPrintfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintfStatement" ):
                listener.exitPrintfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintfStatement" ):
                return visitor.visitPrintfStatement(self)
            else:
                return visitor.visitChildren(self)




    def printfStatement(self):

        localctx = GrammarParser.PrintfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(GrammarParser.T__2)
            self.state = 128
            self.match(GrammarParser.LPAREN)
            self.state = 129
            self.formatSpecifier()
            self.state = 130
            self.match(GrammarParser.T__3)
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 131
                self.match(GrammarParser.T__4)
                pass
            elif token in [39, 40, 41]:
                self.state = 132
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 135
            self.match(GrammarParser.RPAREN)
            self.state = 136
            self.match(GrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_formatSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormatSpecifier" ):
                listener.enterFormatSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormatSpecifier" ):
                listener.exitFormatSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormatSpecifier" ):
                return visitor.visitFormatSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def formatSpecifier(self):

        localctx = GrammarParser.FormatSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_formatSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0)):
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


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(GrammarParser.LvalueContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_variables

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

        localctx = GrammarParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variables)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.lvalue()
                self.state = 141
                self.match(GrammarParser.T__10)
                self.state = 142
                self.rvalue(0)
                self.state = 144 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 143
                        self.match(GrammarParser.SEMICOLON)

                    else:
                        raise NoViableAltException(self)
                    self.state = 146 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.lvalue()
                self.state = 150 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 149
                        self.match(GrammarParser.SEMICOLON)

                    else:
                        raise NoViableAltException(self)
                    self.state = 152 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def pointer(self):
            return self.getTypedRuleContext(GrammarParser.PointerContext,0)


        def deref(self):
            return self.getTypedRuleContext(GrammarParser.DerefContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_lvalue

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

        localctx = GrammarParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lvalue)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.type_()
                self.state = 158
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.pointer()
                self.state = 161
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
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
            return self.getTypedRuleContext(GrammarParser.UnaryExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def deref(self):
            return self.getTypedRuleContext(GrammarParser.DerefContext,0)


        def addr(self):
            return self.getTypedRuleContext(GrammarParser.AddrContext,0)


        def LOGICAL_NOT(self):
            return self.getToken(GrammarParser.LOGICAL_NOT, 0)

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def explicitConversion(self):
            return self.getTypedRuleContext(GrammarParser.ExplicitConversionContext,0)


        def DIV(self):
            return self.getToken(GrammarParser.DIV, 0)

        def MOD(self):
            return self.getToken(GrammarParser.MOD, 0)

        def MULT(self):
            return self.getToken(GrammarParser.MULT, 0)

        def MINUS(self):
            return self.getToken(GrammarParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(GrammarParser.PLUS, 0)

        def GREATER_THAN(self):
            return self.getToken(GrammarParser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(GrammarParser.LESS_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(GrammarParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(GrammarParser.LESS_EQUAL, 0)

        def EQUALS(self):
            return self.getToken(GrammarParser.EQUALS, 0)

        def NOT_EQUAL(self):
            return self.getToken(GrammarParser.NOT_EQUAL, 0)

        def SHIFT_LEFT(self):
            return self.getToken(GrammarParser.SHIFT_LEFT, 0)

        def SHIFT_RIGHT(self):
            return self.getToken(GrammarParser.SHIFT_RIGHT, 0)

        def BITWISE_AND(self):
            return self.getToken(GrammarParser.BITWISE_AND, 0)

        def BITWISE_OR(self):
            return self.getToken(GrammarParser.BITWISE_OR, 0)

        def BITWISE_XOR(self):
            return self.getToken(GrammarParser.BITWISE_XOR, 0)

        def LOGICAL_AND(self):
            return self.getToken(GrammarParser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(GrammarParser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_rvalue

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
        localctx = GrammarParser.RvalueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 167
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 168
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 169
                self.deref()
                pass

            elif la_ == 4:
                self.state = 170
                self.addr()
                pass

            elif la_ == 5:
                self.state = 171
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 172
                self.rvalue(21)
                pass

            elif la_ == 6:
                self.state = 173
                self.match(GrammarParser.LPAREN)
                self.state = 174
                self.rvalue(0)
                self.state = 175
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 7:
                self.state = 177
                self.explicitConversion()
                self.state = 178
                self.rvalue(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 236
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 182
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 183
                        self.match(GrammarParser.DIV)
                        self.state = 184
                        self.rvalue(21)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 185
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 186
                        self.match(GrammarParser.MOD)
                        self.state = 187
                        self.rvalue(20)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 188
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 189
                        self.match(GrammarParser.MULT)
                        self.state = 190
                        self.rvalue(19)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 191
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 192
                        self.match(GrammarParser.MINUS)
                        self.state = 193
                        self.rvalue(18)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 194
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 195
                        self.match(GrammarParser.PLUS)
                        self.state = 196
                        self.rvalue(17)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 197
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 198
                        self.match(GrammarParser.GREATER_THAN)
                        self.state = 199
                        self.rvalue(16)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 200
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 201
                        self.match(GrammarParser.LESS_THAN)
                        self.state = 202
                        self.rvalue(15)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 203
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 204
                        self.match(GrammarParser.GREATER_EQUAL)
                        self.state = 205
                        self.rvalue(14)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 206
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 207
                        self.match(GrammarParser.LESS_EQUAL)
                        self.state = 208
                        self.rvalue(13)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 209
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 210
                        self.match(GrammarParser.EQUALS)
                        self.state = 211
                        self.rvalue(12)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 212
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 213
                        self.match(GrammarParser.NOT_EQUAL)
                        self.state = 214
                        self.rvalue(11)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 215
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 216
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 217
                        self.rvalue(10)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 218
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 219
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 220
                        self.rvalue(9)
                        pass

                    elif la_ == 14:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 221
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 222
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 223
                        self.rvalue(8)
                        pass

                    elif la_ == 15:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 224
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 225
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 226
                        self.rvalue(7)
                        pass

                    elif la_ == 16:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 227
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 228
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 229
                        self.rvalue(6)
                        pass

                    elif la_ == 17:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 230
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 231
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 232
                        self.rvalue(5)
                        pass

                    elif la_ == 18:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 233
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 234
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 235
                        self.rvalue(4)
                        pass

             
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            return self.getTypedRuleContext(GrammarParser.LiteralContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.PLUS)
            else:
                return self.getToken(GrammarParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.MINUS)
            else:
                return self.getToken(GrammarParser.MINUS, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_unaryExpression

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

        localctx = GrammarParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19 or _la==20:
                    self.state = 241
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 244
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 245
                        self.match(GrammarParser.PLUS)
                        self.state = 246
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 249 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 251
                    self.match(GrammarParser.PLUS)


                self.state = 254
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 255
                        self.match(GrammarParser.MINUS)
                        self.state = 256
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 259 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 261
                    self.match(GrammarParser.MINUS)


                self.state = 264
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
            return self.getToken(GrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(GrammarParser.CHAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_literal

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

        localctx = GrammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0)):
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
            return self.getToken(GrammarParser.RPAREN, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.LPAREN)
            else:
                return self.getToken(GrammarParser.LPAREN, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.TypeContext)
            else:
                return self.getTypedRuleContext(GrammarParser.TypeContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_explicitConversion

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

        localctx = GrammarParser.ExplicitConversionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 269
                self.match(GrammarParser.LPAREN)
                self.state = 272 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

            self.state = 275 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 274
                self.type_()
                self.state = 277 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28674) != 0)):
                    break

            self.state = 279
            self.match(GrammarParser.RPAREN)
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
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.MULT)
            else:
                return self.getToken(GrammarParser.MULT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_pointer

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

        localctx = GrammarParser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.type_()
            self.state = 283 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 282
                self.match(GrammarParser.MULT)
                self.state = 285 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
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
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.MULT)
            else:
                return self.getToken(GrammarParser.MULT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_deref

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

        localctx = GrammarParser.DerefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 287
                self.match(GrammarParser.MULT)
                self.state = 290 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 292
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
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def BITWISE_AND(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.BITWISE_AND)
            else:
                return self.getToken(GrammarParser.BITWISE_AND, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_addr

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

        localctx = GrammarParser.AddrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 294
                self.match(GrammarParser.BITWISE_AND)
                self.state = 297 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 299
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
            return GrammarParser.RULE_type

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

        localctx = GrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 301
                self.match(GrammarParser.T__11)
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24578) != 0)):
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
            return self.getTypedRuleContext(GrammarParser.LvalueContext,0)


        def INCREMENT(self):
            return self.getToken(GrammarParser.INCREMENT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_postFixIncrement

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

        localctx = GrammarParser.PostFixIncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.lvalue()
            self.state = 310
            self.match(GrammarParser.INCREMENT)
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
            return self.getTypedRuleContext(GrammarParser.LvalueContext,0)


        def DECREMENT(self):
            return self.getToken(GrammarParser.DECREMENT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_postFixDecrement

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

        localctx = GrammarParser.PostFixDecrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.lvalue()
            self.state = 313
            self.match(GrammarParser.DECREMENT)
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
            return self.getToken(GrammarParser.INCREMENT, 0)

        def lvalue(self):
            return self.getTypedRuleContext(GrammarParser.LvalueContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_preFixIncrement

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

        localctx = GrammarParser.PreFixIncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(GrammarParser.INCREMENT)
            self.state = 316
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
            return self.getToken(GrammarParser.DECREMENT, 0)

        def lvalue(self):
            return self.getTypedRuleContext(GrammarParser.LvalueContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_preFixDecrement

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

        localctx = GrammarParser.PreFixDecrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(GrammarParser.DECREMENT)
            self.state = 319
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
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_identifier

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

        localctx = GrammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(GrammarParser.IDENTIFIER)
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
            return self.getToken(GrammarParser.COMMENT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_comment

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

        localctx = GrammarParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(GrammarParser.COMMENT)
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
        self._predicates[9] = self.rvalue_sempred
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
         




