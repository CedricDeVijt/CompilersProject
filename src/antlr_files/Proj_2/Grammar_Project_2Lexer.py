# Generated from grammars/Grammar_Project_2.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,38,214,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,
        1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,
        1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,
        1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,
        1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,5,30,
        164,8,30,10,30,12,30,167,9,30,1,31,4,31,170,8,31,11,31,12,31,171,
        1,31,1,31,4,31,176,8,31,11,31,12,31,177,3,31,180,8,31,1,32,1,32,
        1,32,1,32,1,33,4,33,187,8,33,11,33,12,33,188,1,33,1,33,1,34,1,34,
        5,34,195,8,34,10,34,12,34,198,9,34,1,35,1,35,1,35,1,36,1,36,1,36,
        1,37,1,37,1,37,1,37,5,37,210,8,37,10,37,12,37,213,9,37,0,0,38,1,
        1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,
        14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,
        25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,
        36,73,37,75,38,1,0,7,1,0,49,57,1,0,48,57,3,0,48,57,65,90,97,122,
        3,0,9,10,13,13,32,32,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,
        97,122,2,0,10,10,13,13,220,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,
        7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,
        1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,
        1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,
        1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,
        1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,
        1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,1,77,
        1,0,0,0,3,81,1,0,0,0,5,86,1,0,0,0,7,88,1,0,0,0,9,94,1,0,0,0,11,100,
        1,0,0,0,13,105,1,0,0,0,15,107,1,0,0,0,17,109,1,0,0,0,19,111,1,0,
        0,0,21,113,1,0,0,0,23,115,1,0,0,0,25,117,1,0,0,0,27,119,1,0,0,0,
        29,121,1,0,0,0,31,123,1,0,0,0,33,125,1,0,0,0,35,127,1,0,0,0,37,130,
        1,0,0,0,39,133,1,0,0,0,41,136,1,0,0,0,43,139,1,0,0,0,45,142,1,0,
        0,0,47,145,1,0,0,0,49,147,1,0,0,0,51,149,1,0,0,0,53,151,1,0,0,0,
        55,154,1,0,0,0,57,157,1,0,0,0,59,159,1,0,0,0,61,161,1,0,0,0,63,169,
        1,0,0,0,65,181,1,0,0,0,67,186,1,0,0,0,69,192,1,0,0,0,71,199,1,0,
        0,0,73,202,1,0,0,0,75,205,1,0,0,0,77,78,5,105,0,0,78,79,5,110,0,
        0,79,80,5,116,0,0,80,2,1,0,0,0,81,82,5,109,0,0,82,83,5,97,0,0,83,
        84,5,105,0,0,84,85,5,110,0,0,85,4,1,0,0,0,86,87,5,61,0,0,87,6,1,
        0,0,0,88,89,5,99,0,0,89,90,5,111,0,0,90,91,5,110,0,0,91,92,5,115,
        0,0,92,93,5,116,0,0,93,8,1,0,0,0,94,95,5,102,0,0,95,96,5,108,0,0,
        96,97,5,111,0,0,97,98,5,97,0,0,98,99,5,116,0,0,99,10,1,0,0,0,100,
        101,5,99,0,0,101,102,5,104,0,0,102,103,5,97,0,0,103,104,5,114,0,
        0,104,12,1,0,0,0,105,106,5,40,0,0,106,14,1,0,0,0,107,108,5,41,0,
        0,108,16,1,0,0,0,109,110,5,123,0,0,110,18,1,0,0,0,111,112,5,125,
        0,0,112,20,1,0,0,0,113,114,5,43,0,0,114,22,1,0,0,0,115,116,5,45,
        0,0,116,24,1,0,0,0,117,118,5,42,0,0,118,26,1,0,0,0,119,120,5,47,
        0,0,120,28,1,0,0,0,121,122,5,37,0,0,122,30,1,0,0,0,123,124,5,62,
        0,0,124,32,1,0,0,0,125,126,5,60,0,0,126,34,1,0,0,0,127,128,5,62,
        0,0,128,129,5,61,0,0,129,36,1,0,0,0,130,131,5,60,0,0,131,132,5,61,
        0,0,132,38,1,0,0,0,133,134,5,61,0,0,134,135,5,61,0,0,135,40,1,0,
        0,0,136,137,5,33,0,0,137,138,5,61,0,0,138,42,1,0,0,0,139,140,5,60,
        0,0,140,141,5,60,0,0,141,44,1,0,0,0,142,143,5,62,0,0,143,144,5,62,
        0,0,144,46,1,0,0,0,145,146,5,38,0,0,146,48,1,0,0,0,147,148,5,124,
        0,0,148,50,1,0,0,0,149,150,5,94,0,0,150,52,1,0,0,0,151,152,5,38,
        0,0,152,153,5,38,0,0,153,54,1,0,0,0,154,155,5,124,0,0,155,156,5,
        124,0,0,156,56,1,0,0,0,157,158,5,33,0,0,158,58,1,0,0,0,159,160,5,
        59,0,0,160,60,1,0,0,0,161,165,7,0,0,0,162,164,7,1,0,0,163,162,1,
        0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,62,1,0,
        0,0,167,165,1,0,0,0,168,170,7,1,0,0,169,168,1,0,0,0,170,171,1,0,
        0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,179,1,0,0,0,173,175,5,46,
        0,0,174,176,7,1,0,0,175,174,1,0,0,0,176,177,1,0,0,0,177,175,1,0,
        0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,173,1,0,0,0,179,180,1,0,
        0,0,180,64,1,0,0,0,181,182,5,39,0,0,182,183,7,2,0,0,183,184,5,39,
        0,0,184,66,1,0,0,0,185,187,7,3,0,0,186,185,1,0,0,0,187,188,1,0,0,
        0,188,186,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,191,6,33,0,
        0,191,68,1,0,0,0,192,196,7,4,0,0,193,195,7,5,0,0,194,193,1,0,0,0,
        195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,70,1,0,0,0,198,
        196,1,0,0,0,199,200,5,43,0,0,200,201,5,43,0,0,201,72,1,0,0,0,202,
        203,5,45,0,0,203,204,5,45,0,0,204,74,1,0,0,0,205,206,5,47,0,0,206,
        207,5,47,0,0,207,211,1,0,0,0,208,210,8,6,0,0,209,208,1,0,0,0,210,
        213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,76,1,0,0,0,213,211,
        1,0,0,0,8,0,165,171,177,179,188,196,211,1,6,0,0
    ]

class Grammar_Project_2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    LPAREN = 7
    RPAREN = 8
    LBRACE = 9
    RBRACE = 10
    PLUS = 11
    MINUS = 12
    MULT = 13
    DIV = 14
    MOD = 15
    GREATER_THAN = 16
    LESS_THAN = 17
    GREATER_EQUAL = 18
    LESS_EQUAL = 19
    EQUALS = 20
    NOT_EQUAL = 21
    SHIFT_LEFT = 22
    SHIFT_RIGHT = 23
    BITWISE_AND = 24
    BITWISE_OR = 25
    BITWISE_XOR = 26
    LOGICAL_AND = 27
    LOGICAL_OR = 28
    LOGICAL_NOT = 29
    SEMICOLON = 30
    INT = 31
    FLOAT = 32
    CHAR = 33
    WHITESPACE = 34
    IDENTIFIER = 35
    INCREMENT = 36
    DECREMENT = 37
    COMMENT = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'main'", "'='", "'const'", "'float'", "'char'", "'('", 
            "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", 
            "'<'", "'>='", "'<='", "'=='", "'!='", "'<<'", "'>>'", "'&'", 
            "'|'", "'^'", "'&&'", "'||'", "'!'", "';'", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT", 
            "DIV", "MOD", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
            "LESS_EQUAL", "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", "SHIFT_RIGHT", 
            "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", "LOGICAL_AND", "LOGICAL_OR", 
            "LOGICAL_NOT", "SEMICOLON", "INT", "FLOAT", "CHAR", "WHITESPACE", 
            "IDENTIFIER", "INCREMENT", "DECREMENT", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT", 
                  "DIV", "MOD", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
                  "LESS_EQUAL", "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", "SHIFT_RIGHT", 
                  "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", "LOGICAL_AND", 
                  "LOGICAL_OR", "LOGICAL_NOT", "SEMICOLON", "INT", "FLOAT", 
                  "CHAR", "WHITESPACE", "IDENTIFIER", "INCREMENT", "DECREMENT", 
                  "COMMENT" ]

    grammarFileName = "Grammar_Project_2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


