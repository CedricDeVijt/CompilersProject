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
        4,1,49,323,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,5,0,50,8,0,10,0,12,0,53,9,0,
        1,0,1,0,1,0,1,0,5,0,59,8,0,10,0,12,0,62,9,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,5,2,74,8,2,10,2,12,2,77,9,2,1,2,1,2,1,3,1,3,
        4,3,83,8,3,11,3,12,3,84,1,3,1,3,1,3,4,3,90,8,3,11,3,12,3,91,1,3,
        1,3,4,3,96,8,3,11,3,12,3,97,1,3,1,3,4,3,102,8,3,11,3,12,3,103,1,
        3,1,3,4,3,108,8,3,11,3,12,3,109,1,3,1,3,1,3,1,3,3,3,116,8,3,1,4,
        1,4,1,4,1,4,1,4,1,4,3,4,124,8,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,
        1,6,4,6,135,8,6,11,6,12,6,136,1,6,1,6,4,6,141,8,6,11,6,12,6,142,
        3,6,145,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,155,8,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,173,
        8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,229,8,8,10,8,12,8,232,9,8,1,9,3,
        9,235,8,9,1,9,1,9,1,9,4,9,240,8,9,11,9,12,9,241,1,9,3,9,245,8,9,
        1,9,1,9,1,9,4,9,250,8,9,11,9,12,9,251,1,9,3,9,255,8,9,1,9,3,9,258,
        8,9,1,10,1,10,1,11,4,11,263,8,11,11,11,12,11,264,1,11,4,11,268,8,
        11,11,11,12,11,269,1,11,1,11,1,12,1,12,4,12,276,8,12,11,12,12,12,
        277,1,13,4,13,281,8,13,11,13,12,13,282,1,13,1,13,1,14,4,14,288,8,
        14,11,14,12,14,289,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,
        1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,5,20,312,
        8,20,10,20,12,20,315,9,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,0,1,
        16,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,0,4,1,0,5,9,1,0,19,20,1,0,40,42,3,0,1,1,13,14,44,44,365,0,
        51,1,0,0,0,2,65,1,0,0,0,4,71,1,0,0,0,6,115,1,0,0,0,8,117,1,0,0,0,
        10,128,1,0,0,0,12,144,1,0,0,0,14,154,1,0,0,0,16,172,1,0,0,0,18,257,
        1,0,0,0,20,259,1,0,0,0,22,262,1,0,0,0,24,273,1,0,0,0,26,280,1,0,
        0,0,28,287,1,0,0,0,30,293,1,0,0,0,32,296,1,0,0,0,34,299,1,0,0,0,
        36,302,1,0,0,0,38,305,1,0,0,0,40,313,1,0,0,0,42,318,1,0,0,0,44,320,
        1,0,0,0,46,50,3,44,22,0,47,50,3,12,6,0,48,50,3,38,19,0,49,46,1,0,
        0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,60,3,2,1,0,55,59,3,44,22,
        0,56,59,3,12,6,0,57,59,3,38,19,0,58,55,1,0,0,0,58,56,1,0,0,0,58,
        57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,
        0,62,60,1,0,0,0,63,64,5,0,0,1,64,1,1,0,0,0,65,66,5,1,0,0,66,67,5,
        2,0,0,67,68,5,15,0,0,68,69,5,16,0,0,69,70,3,4,2,0,70,3,1,0,0,0,71,
        75,5,17,0,0,72,74,3,6,3,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,
        0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,18,0,0,79,
        5,1,0,0,0,80,82,3,16,8,0,81,83,5,39,0,0,82,81,1,0,0,0,83,84,1,0,
        0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,116,1,0,0,0,86,116,3,12,6,0,87,
        89,3,30,15,0,88,90,5,39,0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,89,1,
        0,0,0,91,92,1,0,0,0,92,116,1,0,0,0,93,95,3,32,16,0,94,96,5,39,0,
        0,95,94,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,116,
        1,0,0,0,99,101,3,34,17,0,100,102,5,39,0,0,101,100,1,0,0,0,102,103,
        1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,116,1,0,0,0,105,107,
        3,36,18,0,106,108,5,39,0,0,107,106,1,0,0,0,108,109,1,0,0,0,109,107,
        1,0,0,0,109,110,1,0,0,0,110,116,1,0,0,0,111,116,3,44,22,0,112,116,
        3,8,4,0,113,116,3,4,2,0,114,116,3,38,19,0,115,80,1,0,0,0,115,86,
        1,0,0,0,115,87,1,0,0,0,115,93,1,0,0,0,115,99,1,0,0,0,115,105,1,0,
        0,0,115,111,1,0,0,0,115,112,1,0,0,0,115,113,1,0,0,0,115,114,1,0,
        0,0,116,7,1,0,0,0,117,118,5,3,0,0,118,119,5,15,0,0,119,120,3,10,
        5,0,120,123,5,4,0,0,121,124,3,42,21,0,122,124,3,20,10,0,123,121,
        1,0,0,0,123,122,1,0,0,0,124,125,1,0,0,0,125,126,5,16,0,0,126,127,
        5,39,0,0,127,9,1,0,0,0,128,129,7,0,0,0,129,11,1,0,0,0,130,131,3,
        14,7,0,131,132,5,10,0,0,132,134,3,16,8,0,133,135,5,39,0,0,134,133,
        1,0,0,0,135,136,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,145,
        1,0,0,0,138,140,3,14,7,0,139,141,5,39,0,0,140,139,1,0,0,0,141,142,
        1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,130,
        1,0,0,0,144,138,1,0,0,0,145,13,1,0,0,0,146,155,3,42,21,0,147,148,
        3,40,20,0,148,149,3,42,21,0,149,155,1,0,0,0,150,151,3,24,12,0,151,
        152,3,42,21,0,152,155,1,0,0,0,153,155,3,26,13,0,154,146,1,0,0,0,
        154,147,1,0,0,0,154,150,1,0,0,0,154,153,1,0,0,0,155,15,1,0,0,0,156,
        157,6,8,-1,0,157,173,3,18,9,0,158,173,3,42,21,0,159,173,3,26,13,
        0,160,173,3,28,14,0,161,162,5,38,0,0,162,173,3,16,8,22,163,164,5,
        35,0,0,164,173,3,16,8,21,165,166,5,15,0,0,166,167,3,16,8,0,167,168,
        5,16,0,0,168,173,1,0,0,0,169,170,3,22,11,0,170,171,3,16,8,1,171,
        173,1,0,0,0,172,156,1,0,0,0,172,158,1,0,0,0,172,159,1,0,0,0,172,
        160,1,0,0,0,172,161,1,0,0,0,172,163,1,0,0,0,172,165,1,0,0,0,172,
        169,1,0,0,0,173,230,1,0,0,0,174,175,10,20,0,0,175,176,5,22,0,0,176,
        229,3,16,8,21,177,178,10,19,0,0,178,179,5,23,0,0,179,229,3,16,8,
        20,180,181,10,18,0,0,181,182,5,21,0,0,182,229,3,16,8,19,183,184,
        10,17,0,0,184,185,5,20,0,0,185,229,3,16,8,18,186,187,10,16,0,0,187,
        188,5,19,0,0,188,229,3,16,8,17,189,190,10,15,0,0,190,191,5,24,0,
        0,191,229,3,16,8,16,192,193,10,14,0,0,193,194,5,25,0,0,194,229,3,
        16,8,15,195,196,10,13,0,0,196,197,5,26,0,0,197,229,3,16,8,14,198,
        199,10,12,0,0,199,200,5,27,0,0,200,229,3,16,8,13,201,202,10,11,0,
        0,202,203,5,28,0,0,203,229,3,16,8,12,204,205,10,10,0,0,205,206,5,
        29,0,0,206,229,3,16,8,11,207,208,10,9,0,0,208,209,5,30,0,0,209,229,
        3,16,8,10,210,211,10,8,0,0,211,212,5,31,0,0,212,229,3,16,8,9,213,
        214,10,7,0,0,214,215,5,32,0,0,215,229,3,16,8,8,216,217,10,6,0,0,
        217,218,5,33,0,0,218,229,3,16,8,7,219,220,10,5,0,0,220,221,5,34,
        0,0,221,229,3,16,8,6,222,223,10,4,0,0,223,224,5,36,0,0,224,229,3,
        16,8,5,225,226,10,3,0,0,226,227,5,37,0,0,227,229,3,16,8,4,228,174,
        1,0,0,0,228,177,1,0,0,0,228,180,1,0,0,0,228,183,1,0,0,0,228,186,
        1,0,0,0,228,189,1,0,0,0,228,192,1,0,0,0,228,195,1,0,0,0,228,198,
        1,0,0,0,228,201,1,0,0,0,228,204,1,0,0,0,228,207,1,0,0,0,228,210,
        1,0,0,0,228,213,1,0,0,0,228,216,1,0,0,0,228,219,1,0,0,0,228,222,
        1,0,0,0,228,225,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,
        1,0,0,0,231,17,1,0,0,0,232,230,1,0,0,0,233,235,7,1,0,0,234,233,1,
        0,0,0,234,235,1,0,0,0,235,236,1,0,0,0,236,258,3,20,10,0,237,238,
        5,19,0,0,238,240,5,20,0,0,239,237,1,0,0,0,240,241,1,0,0,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,244,1,0,0,0,243,245,5,19,0,0,244,243,
        1,0,0,0,244,245,1,0,0,0,245,246,1,0,0,0,246,258,3,20,10,0,247,248,
        5,20,0,0,248,250,5,19,0,0,249,247,1,0,0,0,250,251,1,0,0,0,251,249,
        1,0,0,0,251,252,1,0,0,0,252,254,1,0,0,0,253,255,5,20,0,0,254,253,
        1,0,0,0,254,255,1,0,0,0,255,256,1,0,0,0,256,258,3,20,10,0,257,234,
        1,0,0,0,257,239,1,0,0,0,257,249,1,0,0,0,258,19,1,0,0,0,259,260,7,
        2,0,0,260,21,1,0,0,0,261,263,5,15,0,0,262,261,1,0,0,0,263,264,1,
        0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,267,1,0,0,0,266,268,3,
        40,20,0,267,266,1,0,0,0,268,269,1,0,0,0,269,267,1,0,0,0,269,270,
        1,0,0,0,270,271,1,0,0,0,271,272,5,16,0,0,272,23,1,0,0,0,273,275,
        3,40,20,0,274,276,5,21,0,0,275,274,1,0,0,0,276,277,1,0,0,0,277,275,
        1,0,0,0,277,278,1,0,0,0,278,25,1,0,0,0,279,281,5,21,0,0,280,279,
        1,0,0,0,281,282,1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,284,
        1,0,0,0,284,285,3,42,21,0,285,27,1,0,0,0,286,288,5,32,0,0,287,286,
        1,0,0,0,288,289,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,291,
        1,0,0,0,291,292,3,42,21,0,292,29,1,0,0,0,293,294,3,14,7,0,294,295,
        5,45,0,0,295,31,1,0,0,0,296,297,3,14,7,0,297,298,5,46,0,0,298,33,
        1,0,0,0,299,300,5,45,0,0,300,301,3,14,7,0,301,35,1,0,0,0,302,303,
        5,46,0,0,303,304,3,14,7,0,304,37,1,0,0,0,305,306,5,11,0,0,306,307,
        3,40,20,0,307,308,5,44,0,0,308,309,5,39,0,0,309,39,1,0,0,0,310,312,
        5,12,0,0,311,310,1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,314,
        1,0,0,0,314,316,1,0,0,0,315,313,1,0,0,0,316,317,7,3,0,0,317,41,1,
        0,0,0,318,319,5,44,0,0,319,43,1,0,0,0,320,321,5,47,0,0,321,45,1,
        0,0,0,31,49,51,58,60,75,84,91,97,103,109,115,123,136,142,144,154,
        172,228,230,234,241,244,251,254,257,264,269,277,282,289,313
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'printf'", "','", 
                     "'\"%s\"'", "'\"%d\"'", "'\"%x\"'", "'\"%f\"'", "'\"%c\"'", 
                     "'='", "'typedef'", "'const'", "'float'", "'char'", 
                     "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'<<'", "'>>'", "'&'", "'|'", "'^'", "'~'", "'&&'", 
                     "'||'", "'!'", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
                      "LESS_EQUAL", "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", 
                      "SHIFT_RIGHT", "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", 
                      "BITWISE_NOT", "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", 
                      "SEMICOLON", "INT", "FLOAT", "CHAR", "WHITESPACE", 
                      "IDENTIFIER", "INCREMENT", "DECREMENT", "COMMENT", 
                      "BLOCKCOMMENT", "LINECOMMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_scope = 2
    RULE_statement = 3
    RULE_printfStatement = 4
    RULE_formatSpecifier = 5
    RULE_variables = 6
    RULE_lvalue = 7
    RULE_rvalue = 8
    RULE_unaryExpression = 9
    RULE_literal = 10
    RULE_explicitConversion = 11
    RULE_pointer = 12
    RULE_deref = 13
    RULE_addr = 14
    RULE_postFixIncrement = 15
    RULE_postFixDecrement = 16
    RULE_preFixIncrement = 17
    RULE_preFixDecrement = 18
    RULE_typedef = 19
    RULE_type = 20
    RULE_identifier = 21
    RULE_comment = 22

    ruleNames =  [ "program", "main", "scope", "statement", "printfStatement", 
                   "formatSpecifier", "variables", "lvalue", "rvalue", "unaryExpression", 
                   "literal", "explicitConversion", "pointer", "deref", 
                   "addr", "postFixIncrement", "postFixDecrement", "preFixIncrement", 
                   "preFixDecrement", "typedef", "type", "identifier", "comment" ]

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
    BITWISE_NOT=35
    LOGICAL_AND=36
    LOGICAL_OR=37
    LOGICAL_NOT=38
    SEMICOLON=39
    INT=40
    FLOAT=41
    CHAR=42
    WHITESPACE=43
    IDENTIFIER=44
    INCREMENT=45
    DECREMENT=46
    COMMENT=47
    BLOCKCOMMENT=48
    LINECOMMENT=49

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


        def typedef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.TypedefContext)
            else:
                return self.getTypedRuleContext(GrammarParser.TypedefContext,i)


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
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [47]:
                        self.state = 46
                        self.comment()
                        pass
                    elif token in [1, 12, 13, 14, 21, 44]:
                        self.state = 47
                        self.variables()
                        pass
                    elif token in [11]:
                        self.state = 48
                        self.typedef()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 54
            self.main()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 158329676527618) != 0):
                self.state = 58
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [47]:
                    self.state = 55
                    self.comment()
                    pass
                elif token in [1, 12, 13, 14, 21, 44]:
                    self.state = 56
                    self.variables()
                    pass
                elif token in [11]:
                    self.state = 57
                    self.typedef()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(GrammarParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(GrammarParser.T__0)
            self.state = 66
            self.match(GrammarParser.T__1)
            self.state = 67
            self.match(GrammarParser.LPAREN)
            self.state = 68
            self.match(GrammarParser.RPAREN)
            self.state = 69
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
        self.enterRule(localctx, 4, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(GrammarParser.LBRACE)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 271892908537866) != 0):
                self.state = 72
                self.statement()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
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


        def typedef(self):
            return self.getTypedRuleContext(GrammarParser.TypedefContext,0)


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
        self.enterRule(localctx, 6, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.rvalue(0)
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 81
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 84 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.variables()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.postFixIncrement()
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 88
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 91 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.postFixDecrement()
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 94
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 97 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.preFixIncrement()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 100
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 103 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.preFixDecrement()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 106
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 109 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 111
                self.comment()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 112
                self.printfStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 113
                self.scope()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 114
                self.typedef()
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

        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


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
        self.enterRule(localctx, 8, self.RULE_printfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(GrammarParser.T__2)
            self.state = 118
            self.match(GrammarParser.LPAREN)
            self.state = 119
            self.formatSpecifier()
            self.state = 120
            self.match(GrammarParser.T__3)
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.state = 121
                self.identifier()
                pass
            elif token in [40, 41, 42]:
                self.state = 122
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 125
            self.match(GrammarParser.RPAREN)
            self.state = 126
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
        self.enterRule(localctx, 10, self.RULE_formatSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.lvalue()
                self.state = 131
                self.match(GrammarParser.T__9)
                self.state = 132
                self.rvalue(0)
                self.state = 134 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 133
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 136 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.lvalue()
                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 139
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 142 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

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
        self.enterRule(localctx, 14, self.RULE_lvalue)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.type_()
                self.state = 148
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.pointer()
                self.state = 151
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
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


        def BITWISE_NOT(self):
            return self.getToken(GrammarParser.BITWISE_NOT, 0)

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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 157
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 158
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 159
                self.deref()
                pass

            elif la_ == 4:
                self.state = 160
                self.addr()
                pass

            elif la_ == 5:
                self.state = 161
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 162
                self.rvalue(22)
                pass

            elif la_ == 6:
                self.state = 163
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 164
                self.rvalue(21)
                pass

            elif la_ == 7:
                self.state = 165
                self.match(GrammarParser.LPAREN)
                self.state = 166
                self.rvalue(0)
                self.state = 167
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 169
                self.explicitConversion()
                self.state = 170
                self.rvalue(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 228
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 174
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 175
                        self.match(GrammarParser.DIV)
                        self.state = 176
                        self.rvalue(21)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 177
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 178
                        self.match(GrammarParser.MOD)
                        self.state = 179
                        self.rvalue(20)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 180
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 181
                        self.match(GrammarParser.MULT)
                        self.state = 182
                        self.rvalue(19)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 183
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 184
                        self.match(GrammarParser.MINUS)
                        self.state = 185
                        self.rvalue(18)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 186
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 187
                        self.match(GrammarParser.PLUS)
                        self.state = 188
                        self.rvalue(17)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 189
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 190
                        self.match(GrammarParser.GREATER_THAN)
                        self.state = 191
                        self.rvalue(16)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 192
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 193
                        self.match(GrammarParser.LESS_THAN)
                        self.state = 194
                        self.rvalue(15)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 195
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 196
                        self.match(GrammarParser.GREATER_EQUAL)
                        self.state = 197
                        self.rvalue(14)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 198
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 199
                        self.match(GrammarParser.LESS_EQUAL)
                        self.state = 200
                        self.rvalue(13)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 201
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 202
                        self.match(GrammarParser.EQUALS)
                        self.state = 203
                        self.rvalue(12)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 204
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 205
                        self.match(GrammarParser.NOT_EQUAL)
                        self.state = 206
                        self.rvalue(11)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 207
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 208
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 209
                        self.rvalue(10)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 210
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 211
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 212
                        self.rvalue(9)
                        pass

                    elif la_ == 14:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 213
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 214
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 215
                        self.rvalue(8)
                        pass

                    elif la_ == 15:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 216
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 217
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 218
                        self.rvalue(7)
                        pass

                    elif la_ == 16:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 219
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 220
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 221
                        self.rvalue(6)
                        pass

                    elif la_ == 17:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 222
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 223
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 224
                        self.rvalue(5)
                        pass

                    elif la_ == 18:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 225
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 226
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 227
                        self.rvalue(4)
                        pass

             
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19 or _la==20:
                    self.state = 233
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 236
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 237
                        self.match(GrammarParser.PLUS)
                        self.state = 238
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 241 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 243
                    self.match(GrammarParser.PLUS)


                self.state = 246
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 247
                        self.match(GrammarParser.MINUS)
                        self.state = 248
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 251 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 253
                    self.match(GrammarParser.MINUS)


                self.state = 256
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
        self.enterRule(localctx, 20, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0)):
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
        self.enterRule(localctx, 22, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 261
                self.match(GrammarParser.LPAREN)
                self.state = 264 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

            self.state = 267 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 266
                self.type_()
                self.state = 269 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17592186073090) != 0)):
                    break

            self.state = 271
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
        self.enterRule(localctx, 24, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.type_()
            self.state = 275 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 274
                self.match(GrammarParser.MULT)
                self.state = 277 
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
        self.enterRule(localctx, 26, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 279
                self.match(GrammarParser.MULT)
                self.state = 282 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 284
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
        self.enterRule(localctx, 28, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 286
                self.match(GrammarParser.BITWISE_AND)
                self.state = 289 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 291
            self.identifier()
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
        self.enterRule(localctx, 30, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.lvalue()
            self.state = 294
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
        self.enterRule(localctx, 32, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.lvalue()
            self.state = 297
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
        self.enterRule(localctx, 34, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(GrammarParser.INCREMENT)
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
        self.enterRule(localctx, 36, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(GrammarParser.DECREMENT)
            self.state = 303
            self.lvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_typedef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedef" ):
                listener.enterTypedef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedef" ):
                listener.exitTypedef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedef" ):
                return visitor.visitTypedef(self)
            else:
                return visitor.visitChildren(self)




    def typedef(self):

        localctx = GrammarParser.TypedefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(GrammarParser.T__10)
            self.state = 306
            self.type_()
            self.state = 307
            self.match(GrammarParser.IDENTIFIER)
            self.state = 308
            self.match(GrammarParser.SEMICOLON)
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

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 40, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 310
                self.match(GrammarParser.T__11)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 316
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17592186068994) != 0)):
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
            self.state = 318
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
            self.state = 320
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
        self._predicates[8] = self.rvalue_sempred
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
         




