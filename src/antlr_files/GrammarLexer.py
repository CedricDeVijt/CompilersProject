# Generated from grammars/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,59,381,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,
        13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,
        16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,
        18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,
        21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,
        28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,
        33,1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,
        38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,
        43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,48,5,48,297,
        8,48,10,48,12,48,300,9,48,3,48,302,8,48,1,49,4,49,305,8,49,11,49,
        12,49,306,1,49,1,49,4,49,311,8,49,11,49,12,49,312,3,49,315,8,49,
        1,50,1,50,3,50,319,8,50,1,50,1,50,1,50,1,51,1,51,5,51,326,8,51,10,
        51,12,51,329,9,51,1,51,1,51,1,52,4,52,334,8,52,11,52,12,52,335,1,
        52,1,52,1,53,1,53,5,53,342,8,53,10,53,12,53,345,9,53,1,54,1,54,1,
        54,1,55,1,55,1,55,1,56,1,56,3,56,355,8,56,1,57,1,57,1,57,1,57,5,
        57,361,8,57,10,57,12,57,364,9,57,1,57,1,57,1,57,1,57,1,57,1,58,1,
        58,1,58,1,58,5,58,375,8,58,10,58,12,58,378,9,58,1,58,1,58,1,362,
        0,59,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,
        24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,
        35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,
        46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,
        56,113,57,115,58,117,59,1,0,8,1,0,49,57,1,0,48,57,3,0,48,57,65,90,
        97,122,3,0,9,10,13,13,34,34,3,0,9,10,13,13,32,32,3,0,65,90,95,95,
        97,122,4,0,48,57,65,90,95,95,97,122,2,0,10,10,13,13,392,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,
        0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,
        0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,
        0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,
        0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,
        0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,
        0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,
        0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,
        0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,
        0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,
        1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,1,119,1,0,0,0,
        3,126,1,0,0,0,5,131,1,0,0,0,7,139,1,0,0,0,9,142,1,0,0,0,11,147,1,
        0,0,0,13,153,1,0,0,0,15,157,1,0,0,0,17,164,1,0,0,0,19,166,1,0,0,
        0,21,172,1,0,0,0,23,181,1,0,0,0,25,188,1,0,0,0,27,193,1,0,0,0,29,
        195,1,0,0,0,31,197,1,0,0,0,33,205,1,0,0,0,35,211,1,0,0,0,37,215,
        1,0,0,0,39,221,1,0,0,0,41,226,1,0,0,0,43,231,1,0,0,0,45,233,1,0,
        0,0,47,235,1,0,0,0,49,237,1,0,0,0,51,239,1,0,0,0,53,241,1,0,0,0,
        55,243,1,0,0,0,57,245,1,0,0,0,59,247,1,0,0,0,61,249,1,0,0,0,63,251,
        1,0,0,0,65,253,1,0,0,0,67,256,1,0,0,0,69,259,1,0,0,0,71,262,1,0,
        0,0,73,265,1,0,0,0,75,268,1,0,0,0,77,271,1,0,0,0,79,273,1,0,0,0,
        81,275,1,0,0,0,83,277,1,0,0,0,85,279,1,0,0,0,87,282,1,0,0,0,89,285,
        1,0,0,0,91,287,1,0,0,0,93,289,1,0,0,0,95,291,1,0,0,0,97,301,1,0,
        0,0,99,304,1,0,0,0,101,316,1,0,0,0,103,323,1,0,0,0,105,333,1,0,0,
        0,107,339,1,0,0,0,109,346,1,0,0,0,111,349,1,0,0,0,113,354,1,0,0,
        0,115,356,1,0,0,0,117,370,1,0,0,0,119,120,5,115,0,0,120,121,5,119,
        0,0,121,122,5,105,0,0,122,123,5,116,0,0,123,124,5,99,0,0,124,125,
        5,104,0,0,125,2,1,0,0,0,126,127,5,99,0,0,127,128,5,97,0,0,128,129,
        5,115,0,0,129,130,5,101,0,0,130,4,1,0,0,0,131,132,5,100,0,0,132,
        133,5,101,0,0,133,134,5,102,0,0,134,135,5,97,0,0,135,136,5,117,0,
        0,136,137,5,108,0,0,137,138,5,116,0,0,138,6,1,0,0,0,139,140,5,105,
        0,0,140,141,5,102,0,0,141,8,1,0,0,0,142,143,5,101,0,0,143,144,5,
        108,0,0,144,145,5,115,0,0,145,146,5,101,0,0,146,10,1,0,0,0,147,148,
        5,119,0,0,148,149,5,104,0,0,149,150,5,105,0,0,150,151,5,108,0,0,
        151,152,5,101,0,0,152,12,1,0,0,0,153,154,5,102,0,0,154,155,5,111,
        0,0,155,156,5,114,0,0,156,14,1,0,0,0,157,158,5,112,0,0,158,159,5,
        114,0,0,159,160,5,105,0,0,160,161,5,110,0,0,161,162,5,116,0,0,162,
        163,5,102,0,0,163,16,1,0,0,0,164,165,5,61,0,0,165,18,1,0,0,0,166,
        167,5,98,0,0,167,168,5,114,0,0,168,169,5,101,0,0,169,170,5,97,0,
        0,170,171,5,107,0,0,171,20,1,0,0,0,172,173,5,99,0,0,173,174,5,111,
        0,0,174,175,5,110,0,0,175,176,5,116,0,0,176,177,5,105,0,0,177,178,
        5,110,0,0,178,179,5,117,0,0,179,180,5,101,0,0,180,22,1,0,0,0,181,
        182,5,114,0,0,182,183,5,101,0,0,183,184,5,116,0,0,184,185,5,117,
        0,0,185,186,5,114,0,0,186,187,5,110,0,0,187,24,1,0,0,0,188,189,5,
        101,0,0,189,190,5,110,0,0,190,191,5,117,0,0,191,192,5,109,0,0,192,
        26,1,0,0,0,193,194,5,91,0,0,194,28,1,0,0,0,195,196,5,93,0,0,196,
        30,1,0,0,0,197,198,5,116,0,0,198,199,5,121,0,0,199,200,5,112,0,0,
        200,201,5,101,0,0,201,202,5,100,0,0,202,203,5,101,0,0,203,204,5,
        102,0,0,204,32,1,0,0,0,205,206,5,99,0,0,206,207,5,111,0,0,207,208,
        5,110,0,0,208,209,5,115,0,0,209,210,5,116,0,0,210,34,1,0,0,0,211,
        212,5,105,0,0,212,213,5,110,0,0,213,214,5,116,0,0,214,36,1,0,0,0,
        215,216,5,102,0,0,216,217,5,108,0,0,217,218,5,111,0,0,218,219,5,
        97,0,0,219,220,5,116,0,0,220,38,1,0,0,0,221,222,5,99,0,0,222,223,
        5,104,0,0,223,224,5,97,0,0,224,225,5,114,0,0,225,40,1,0,0,0,226,
        227,5,118,0,0,227,228,5,111,0,0,228,229,5,105,0,0,229,230,5,100,
        0,0,230,42,1,0,0,0,231,232,5,40,0,0,232,44,1,0,0,0,233,234,5,41,
        0,0,234,46,1,0,0,0,235,236,5,123,0,0,236,48,1,0,0,0,237,238,5,125,
        0,0,238,50,1,0,0,0,239,240,5,43,0,0,240,52,1,0,0,0,241,242,5,45,
        0,0,242,54,1,0,0,0,243,244,5,42,0,0,244,56,1,0,0,0,245,246,5,47,
        0,0,246,58,1,0,0,0,247,248,5,37,0,0,248,60,1,0,0,0,249,250,5,62,
        0,0,250,62,1,0,0,0,251,252,5,60,0,0,252,64,1,0,0,0,253,254,5,62,
        0,0,254,255,5,61,0,0,255,66,1,0,0,0,256,257,5,60,0,0,257,258,5,61,
        0,0,258,68,1,0,0,0,259,260,5,61,0,0,260,261,5,61,0,0,261,70,1,0,
        0,0,262,263,5,33,0,0,263,264,5,61,0,0,264,72,1,0,0,0,265,266,5,60,
        0,0,266,267,5,60,0,0,267,74,1,0,0,0,268,269,5,62,0,0,269,270,5,62,
        0,0,270,76,1,0,0,0,271,272,5,38,0,0,272,78,1,0,0,0,273,274,5,124,
        0,0,274,80,1,0,0,0,275,276,5,94,0,0,276,82,1,0,0,0,277,278,5,126,
        0,0,278,84,1,0,0,0,279,280,5,38,0,0,280,281,5,38,0,0,281,86,1,0,
        0,0,282,283,5,124,0,0,283,284,5,124,0,0,284,88,1,0,0,0,285,286,5,
        33,0,0,286,90,1,0,0,0,287,288,5,58,0,0,288,92,1,0,0,0,289,290,5,
        59,0,0,290,94,1,0,0,0,291,292,5,44,0,0,292,96,1,0,0,0,293,302,5,
        48,0,0,294,298,7,0,0,0,295,297,7,1,0,0,296,295,1,0,0,0,297,300,1,
        0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,302,1,0,0,0,300,298,1,
        0,0,0,301,293,1,0,0,0,301,294,1,0,0,0,302,98,1,0,0,0,303,305,7,1,
        0,0,304,303,1,0,0,0,305,306,1,0,0,0,306,304,1,0,0,0,306,307,1,0,
        0,0,307,314,1,0,0,0,308,310,5,46,0,0,309,311,7,1,0,0,310,309,1,0,
        0,0,311,312,1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,315,1,0,
        0,0,314,308,1,0,0,0,314,315,1,0,0,0,315,100,1,0,0,0,316,318,5,39,
        0,0,317,319,5,92,0,0,318,317,1,0,0,0,318,319,1,0,0,0,319,320,1,0,
        0,0,320,321,7,2,0,0,321,322,5,39,0,0,322,102,1,0,0,0,323,327,5,34,
        0,0,324,326,8,3,0,0,325,324,1,0,0,0,326,329,1,0,0,0,327,325,1,0,
        0,0,327,328,1,0,0,0,328,330,1,0,0,0,329,327,1,0,0,0,330,331,5,34,
        0,0,331,104,1,0,0,0,332,334,7,4,0,0,333,332,1,0,0,0,334,335,1,0,
        0,0,335,333,1,0,0,0,335,336,1,0,0,0,336,337,1,0,0,0,337,338,6,52,
        0,0,338,106,1,0,0,0,339,343,7,5,0,0,340,342,7,6,0,0,341,340,1,0,
        0,0,342,345,1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,108,1,0,
        0,0,345,343,1,0,0,0,346,347,5,43,0,0,347,348,5,43,0,0,348,110,1,
        0,0,0,349,350,5,45,0,0,350,351,5,45,0,0,351,112,1,0,0,0,352,355,
        3,117,58,0,353,355,3,115,57,0,354,352,1,0,0,0,354,353,1,0,0,0,355,
        114,1,0,0,0,356,357,5,47,0,0,357,358,5,42,0,0,358,362,1,0,0,0,359,
        361,9,0,0,0,360,359,1,0,0,0,361,364,1,0,0,0,362,363,1,0,0,0,362,
        360,1,0,0,0,363,365,1,0,0,0,364,362,1,0,0,0,365,366,5,42,0,0,366,
        367,5,47,0,0,367,368,1,0,0,0,368,369,6,57,0,0,369,116,1,0,0,0,370,
        371,5,47,0,0,371,372,5,47,0,0,372,376,1,0,0,0,373,375,8,7,0,0,374,
        373,1,0,0,0,375,378,1,0,0,0,376,374,1,0,0,0,376,377,1,0,0,0,377,
        379,1,0,0,0,378,376,1,0,0,0,379,380,6,58,0,0,380,118,1,0,0,0,13,
        0,298,301,306,312,314,318,327,335,343,354,362,376,1,6,0,0
    ]

class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    LPAREN = 22
    RPAREN = 23
    LBRACE = 24
    RBRACE = 25
    PLUS = 26
    MINUS = 27
    MULT = 28
    DIV = 29
    MOD = 30
    GREATER_THAN = 31
    LESS_THAN = 32
    GREATER_EQUAL = 33
    LESS_EQUAL = 34
    EQUALS = 35
    NOT_EQUAL = 36
    SHIFT_LEFT = 37
    SHIFT_RIGHT = 38
    BITWISE_AND = 39
    BITWISE_OR = 40
    BITWISE_XOR = 41
    BITWISE_NOT = 42
    LOGICAL_AND = 43
    LOGICAL_OR = 44
    LOGICAL_NOT = 45
    COLON = 46
    SEMICOLON = 47
    COMMA = 48
    INT = 49
    FLOAT = 50
    CHAR = 51
    STRING = 52
    WHITESPACE = 53
    IDENTIFIER = 54
    INCREMENT = 55
    DECREMENT = 56
    COMMENT = 57
    BLOCKCOMMENT = 58
    LINECOMMENT = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'switch'", "'case'", "'default'", "'if'", "'else'", "'while'", 
            "'for'", "'printf'", "'='", "'break'", "'continue'", "'return'", 
            "'enum'", "'['", "']'", "'typedef'", "'const'", "'int'", "'float'", 
            "'char'", "'void'", "'('", "')'", "'{'", "'}'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
            "'<<'", "'>>'", "'&'", "'|'", "'^'", "'~'", "'&&'", "'||'", 
            "'!'", "':'", "';'", "','", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT", 
            "DIV", "MOD", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
            "LESS_EQUAL", "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", "SHIFT_RIGHT", 
            "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", "BITWISE_NOT", "LOGICAL_AND", 
            "LOGICAL_OR", "LOGICAL_NOT", "COLON", "SEMICOLON", "COMMA", 
            "INT", "FLOAT", "CHAR", "STRING", "WHITESPACE", "IDENTIFIER", 
            "INCREMENT", "DECREMENT", "COMMENT", "BLOCKCOMMENT", "LINECOMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", 
                  "MINUS", "MULT", "DIV", "MOD", "GREATER_THAN", "LESS_THAN", 
                  "GREATER_EQUAL", "LESS_EQUAL", "EQUALS", "NOT_EQUAL", 
                  "SHIFT_LEFT", "SHIFT_RIGHT", "BITWISE_AND", "BITWISE_OR", 
                  "BITWISE_XOR", "BITWISE_NOT", "LOGICAL_AND", "LOGICAL_OR", 
                  "LOGICAL_NOT", "COLON", "SEMICOLON", "COMMA", "INT", "FLOAT", 
                  "CHAR", "STRING", "WHITESPACE", "IDENTIFIER", "INCREMENT", 
                  "DECREMENT", "COMMENT", "BLOCKCOMMENT", "LINECOMMENT" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


