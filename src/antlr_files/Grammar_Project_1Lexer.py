# Generated from grammars/Grammar_Project_1.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,25,128,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,1,
        1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,
        1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,
        13,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,
        19,1,19,1,19,1,20,1,20,1,21,1,21,1,22,4,22,105,8,22,11,22,12,22,
        106,1,23,4,23,110,8,23,11,23,12,23,111,1,23,1,23,4,23,116,8,23,11,
        23,12,23,117,3,23,120,8,23,1,24,4,24,123,8,24,11,24,12,24,124,1,
        24,1,24,0,0,25,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,
        11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,
        22,45,23,47,24,49,25,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,132,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,
        0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,
        0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,1,51,1,
        0,0,0,3,53,1,0,0,0,5,55,1,0,0,0,7,57,1,0,0,0,9,59,1,0,0,0,11,61,
        1,0,0,0,13,63,1,0,0,0,15,65,1,0,0,0,17,67,1,0,0,0,19,69,1,0,0,0,
        21,72,1,0,0,0,23,75,1,0,0,0,25,78,1,0,0,0,27,81,1,0,0,0,29,84,1,
        0,0,0,31,87,1,0,0,0,33,89,1,0,0,0,35,91,1,0,0,0,37,93,1,0,0,0,39,
        96,1,0,0,0,41,99,1,0,0,0,43,101,1,0,0,0,45,104,1,0,0,0,47,109,1,
        0,0,0,49,122,1,0,0,0,51,52,5,40,0,0,52,2,1,0,0,0,53,54,5,41,0,0,
        54,4,1,0,0,0,55,56,5,43,0,0,56,6,1,0,0,0,57,58,5,45,0,0,58,8,1,0,
        0,0,59,60,5,42,0,0,60,10,1,0,0,0,61,62,5,47,0,0,62,12,1,0,0,0,63,
        64,5,37,0,0,64,14,1,0,0,0,65,66,5,62,0,0,66,16,1,0,0,0,67,68,5,60,
        0,0,68,18,1,0,0,0,69,70,5,62,0,0,70,71,5,61,0,0,71,20,1,0,0,0,72,
        73,5,60,0,0,73,74,5,61,0,0,74,22,1,0,0,0,75,76,5,61,0,0,76,77,5,
        61,0,0,77,24,1,0,0,0,78,79,5,33,0,0,79,80,5,61,0,0,80,26,1,0,0,0,
        81,82,5,60,0,0,82,83,5,60,0,0,83,28,1,0,0,0,84,85,5,62,0,0,85,86,
        5,62,0,0,86,30,1,0,0,0,87,88,5,38,0,0,88,32,1,0,0,0,89,90,5,124,
        0,0,90,34,1,0,0,0,91,92,5,94,0,0,92,36,1,0,0,0,93,94,5,38,0,0,94,
        95,5,38,0,0,95,38,1,0,0,0,96,97,5,124,0,0,97,98,5,124,0,0,98,40,
        1,0,0,0,99,100,5,33,0,0,100,42,1,0,0,0,101,102,5,59,0,0,102,44,1,
        0,0,0,103,105,7,0,0,0,104,103,1,0,0,0,105,106,1,0,0,0,106,104,1,
        0,0,0,106,107,1,0,0,0,107,46,1,0,0,0,108,110,7,0,0,0,109,108,1,0,
        0,0,110,111,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,119,1,0,
        0,0,113,115,5,46,0,0,114,116,7,0,0,0,115,114,1,0,0,0,116,117,1,0,
        0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,1,0,0,0,119,113,1,0,
        0,0,119,120,1,0,0,0,120,48,1,0,0,0,121,123,7,1,0,0,122,121,1,0,0,
        0,123,124,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,
        0,126,127,6,24,0,0,127,50,1,0,0,0,6,0,106,111,117,119,124,1,6,0,
        0
    ]

class Grammar_Project_1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LPAREN = 1
    RPAREN = 2
    PLUS = 3
    MINUS = 4
    MULT = 5
    DIV = 6
    MOD = 7
    GREATER_THAN = 8
    LESS_THAN = 9
    GREATER_EQUAL = 10
    LESS_EQUAL = 11
    EQUALS = 12
    NOT_EQUAL = 13
    SHIFT_LEFT = 14
    SHIFT_RIGHT = 15
    BITWISE_AND = 16
    BITWISE_OR = 17
    BITWISE_XOR = 18
    LOGICAL_AND = 19
    LOGICAL_OR = 20
    LOGICAL_NOT = 21
    SEMICOLON = 22
    INT = 23
    FLOAT = 24
    WHITESPACE = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", 
            "'>='", "'<='", "'=='", "'!='", "'<<'", "'>>'", "'&'", "'|'", 
            "'^'", "'&&'", "'||'", "'!'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "PLUS", "MINUS", "MULT", "DIV", "MOD", "GREATER_THAN", 
            "LESS_THAN", "GREATER_EQUAL", "LESS_EQUAL", "EQUALS", "NOT_EQUAL", 
            "SHIFT_LEFT", "SHIFT_RIGHT", "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", 
            "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", "SEMICOLON", "INT", 
            "FLOAT", "WHITESPACE" ]

    ruleNames = [ "LPAREN", "RPAREN", "PLUS", "MINUS", "MULT", "DIV", "MOD", 
                  "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", "LESS_EQUAL", 
                  "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", "SHIFT_RIGHT", "BITWISE_AND", 
                  "BITWISE_OR", "BITWISE_XOR", "LOGICAL_AND", "LOGICAL_OR", 
                  "LOGICAL_NOT", "SEMICOLON", "INT", "FLOAT", "WHITESPACE" ]

    grammarFileName = "Grammar_Project_1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


