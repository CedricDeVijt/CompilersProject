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
        4,0,63,405,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,
        1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,36,
        1,36,1,37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,
        1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,
        1,46,1,47,1,47,1,47,1,48,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,
        1,52,1,52,1,53,1,53,1,53,5,53,330,8,53,10,53,12,53,333,9,53,3,53,
        335,8,53,1,54,4,54,338,8,54,11,54,12,54,339,1,54,1,54,4,54,344,8,
        54,11,54,12,54,345,3,54,348,8,54,1,55,1,55,3,55,352,8,55,1,55,1,
        55,1,55,1,56,4,56,358,8,56,11,56,12,56,359,1,56,1,56,1,57,1,57,5,
        57,366,8,57,10,57,12,57,369,9,57,1,58,1,58,1,58,1,59,1,59,1,59,1,
        60,1,60,3,60,379,8,60,1,61,1,61,1,61,1,61,5,61,385,8,61,10,61,12,
        61,388,9,61,1,61,1,61,1,61,1,61,1,61,1,62,1,62,1,62,1,62,5,62,399,
        8,62,10,62,12,62,402,9,62,1,62,1,62,1,386,0,63,1,1,3,2,5,3,7,4,9,
        5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,
        33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,
        55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,
        77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,
        99,50,101,51,103,52,105,53,107,54,109,55,111,56,113,57,115,58,117,
        59,119,60,121,61,123,62,125,63,1,0,7,1,0,49,57,1,0,48,57,3,0,48,
        57,65,90,97,122,3,0,9,10,13,13,32,32,3,0,65,90,95,95,97,122,4,0,
        48,57,65,90,95,95,97,122,2,0,10,10,13,13,415,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,
        0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,
        0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,
        0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,
        0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,
        0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,
        0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,
        0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,
        0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,
        0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,
        1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,
        0,123,1,0,0,0,0,125,1,0,0,0,1,127,1,0,0,0,3,134,1,0,0,0,5,139,1,
        0,0,0,7,147,1,0,0,0,9,150,1,0,0,0,11,155,1,0,0,0,13,161,1,0,0,0,
        15,165,1,0,0,0,17,172,1,0,0,0,19,177,1,0,0,0,21,182,1,0,0,0,23,187,
        1,0,0,0,25,192,1,0,0,0,27,197,1,0,0,0,29,199,1,0,0,0,31,205,1,0,
        0,0,33,214,1,0,0,0,35,221,1,0,0,0,37,226,1,0,0,0,39,234,1,0,0,0,
        41,240,1,0,0,0,43,244,1,0,0,0,45,250,1,0,0,0,47,255,1,0,0,0,49,260,
        1,0,0,0,51,262,1,0,0,0,53,264,1,0,0,0,55,266,1,0,0,0,57,268,1,0,
        0,0,59,270,1,0,0,0,61,272,1,0,0,0,63,274,1,0,0,0,65,276,1,0,0,0,
        67,278,1,0,0,0,69,280,1,0,0,0,71,282,1,0,0,0,73,284,1,0,0,0,75,286,
        1,0,0,0,77,289,1,0,0,0,79,292,1,0,0,0,81,295,1,0,0,0,83,298,1,0,
        0,0,85,301,1,0,0,0,87,304,1,0,0,0,89,306,1,0,0,0,91,308,1,0,0,0,
        93,310,1,0,0,0,95,312,1,0,0,0,97,315,1,0,0,0,99,318,1,0,0,0,101,
        320,1,0,0,0,103,322,1,0,0,0,105,324,1,0,0,0,107,334,1,0,0,0,109,
        337,1,0,0,0,111,349,1,0,0,0,113,357,1,0,0,0,115,363,1,0,0,0,117,
        370,1,0,0,0,119,373,1,0,0,0,121,378,1,0,0,0,123,380,1,0,0,0,125,
        394,1,0,0,0,127,128,5,115,0,0,128,129,5,119,0,0,129,130,5,105,0,
        0,130,131,5,116,0,0,131,132,5,99,0,0,132,133,5,104,0,0,133,2,1,0,
        0,0,134,135,5,99,0,0,135,136,5,97,0,0,136,137,5,115,0,0,137,138,
        5,101,0,0,138,4,1,0,0,0,139,140,5,100,0,0,140,141,5,101,0,0,141,
        142,5,102,0,0,142,143,5,97,0,0,143,144,5,117,0,0,144,145,5,108,0,
        0,145,146,5,116,0,0,146,6,1,0,0,0,147,148,5,105,0,0,148,149,5,102,
        0,0,149,8,1,0,0,0,150,151,5,101,0,0,151,152,5,108,0,0,152,153,5,
        115,0,0,153,154,5,101,0,0,154,10,1,0,0,0,155,156,5,119,0,0,156,157,
        5,104,0,0,157,158,5,105,0,0,158,159,5,108,0,0,159,160,5,101,0,0,
        160,12,1,0,0,0,161,162,5,102,0,0,162,163,5,111,0,0,163,164,5,114,
        0,0,164,14,1,0,0,0,165,166,5,112,0,0,166,167,5,114,0,0,167,168,5,
        105,0,0,168,169,5,110,0,0,169,170,5,116,0,0,170,171,5,102,0,0,171,
        16,1,0,0,0,172,173,5,34,0,0,173,174,5,37,0,0,174,175,5,115,0,0,175,
        176,5,34,0,0,176,18,1,0,0,0,177,178,5,34,0,0,178,179,5,37,0,0,179,
        180,5,100,0,0,180,181,5,34,0,0,181,20,1,0,0,0,182,183,5,34,0,0,183,
        184,5,37,0,0,184,185,5,120,0,0,185,186,5,34,0,0,186,22,1,0,0,0,187,
        188,5,34,0,0,188,189,5,37,0,0,189,190,5,102,0,0,190,191,5,34,0,0,
        191,24,1,0,0,0,192,193,5,34,0,0,193,194,5,37,0,0,194,195,5,99,0,
        0,195,196,5,34,0,0,196,26,1,0,0,0,197,198,5,61,0,0,198,28,1,0,0,
        0,199,200,5,98,0,0,200,201,5,114,0,0,201,202,5,101,0,0,202,203,5,
        97,0,0,203,204,5,107,0,0,204,30,1,0,0,0,205,206,5,99,0,0,206,207,
        5,111,0,0,207,208,5,110,0,0,208,209,5,116,0,0,209,210,5,105,0,0,
        210,211,5,110,0,0,211,212,5,117,0,0,212,213,5,101,0,0,213,32,1,0,
        0,0,214,215,5,114,0,0,215,216,5,101,0,0,216,217,5,116,0,0,217,218,
        5,117,0,0,218,219,5,114,0,0,219,220,5,110,0,0,220,34,1,0,0,0,221,
        222,5,101,0,0,222,223,5,110,0,0,223,224,5,117,0,0,224,225,5,109,
        0,0,225,36,1,0,0,0,226,227,5,116,0,0,227,228,5,121,0,0,228,229,5,
        112,0,0,229,230,5,101,0,0,230,231,5,100,0,0,231,232,5,101,0,0,232,
        233,5,102,0,0,233,38,1,0,0,0,234,235,5,99,0,0,235,236,5,111,0,0,
        236,237,5,110,0,0,237,238,5,115,0,0,238,239,5,116,0,0,239,40,1,0,
        0,0,240,241,5,105,0,0,241,242,5,110,0,0,242,243,5,116,0,0,243,42,
        1,0,0,0,244,245,5,102,0,0,245,246,5,108,0,0,246,247,5,111,0,0,247,
        248,5,97,0,0,248,249,5,116,0,0,249,44,1,0,0,0,250,251,5,99,0,0,251,
        252,5,104,0,0,252,253,5,97,0,0,253,254,5,114,0,0,254,46,1,0,0,0,
        255,256,5,118,0,0,256,257,5,111,0,0,257,258,5,105,0,0,258,259,5,
        100,0,0,259,48,1,0,0,0,260,261,5,91,0,0,261,50,1,0,0,0,262,263,5,
        93,0,0,263,52,1,0,0,0,264,265,5,40,0,0,265,54,1,0,0,0,266,267,5,
        41,0,0,267,56,1,0,0,0,268,269,5,123,0,0,269,58,1,0,0,0,270,271,5,
        125,0,0,271,60,1,0,0,0,272,273,5,43,0,0,273,62,1,0,0,0,274,275,5,
        45,0,0,275,64,1,0,0,0,276,277,5,42,0,0,277,66,1,0,0,0,278,279,5,
        47,0,0,279,68,1,0,0,0,280,281,5,37,0,0,281,70,1,0,0,0,282,283,5,
        62,0,0,283,72,1,0,0,0,284,285,5,60,0,0,285,74,1,0,0,0,286,287,5,
        62,0,0,287,288,5,61,0,0,288,76,1,0,0,0,289,290,5,60,0,0,290,291,
        5,61,0,0,291,78,1,0,0,0,292,293,5,61,0,0,293,294,5,61,0,0,294,80,
        1,0,0,0,295,296,5,33,0,0,296,297,5,61,0,0,297,82,1,0,0,0,298,299,
        5,60,0,0,299,300,5,60,0,0,300,84,1,0,0,0,301,302,5,62,0,0,302,303,
        5,62,0,0,303,86,1,0,0,0,304,305,5,38,0,0,305,88,1,0,0,0,306,307,
        5,124,0,0,307,90,1,0,0,0,308,309,5,94,0,0,309,92,1,0,0,0,310,311,
        5,126,0,0,311,94,1,0,0,0,312,313,5,38,0,0,313,314,5,38,0,0,314,96,
        1,0,0,0,315,316,5,124,0,0,316,317,5,124,0,0,317,98,1,0,0,0,318,319,
        5,33,0,0,319,100,1,0,0,0,320,321,5,58,0,0,321,102,1,0,0,0,322,323,
        5,59,0,0,323,104,1,0,0,0,324,325,5,44,0,0,325,106,1,0,0,0,326,335,
        5,48,0,0,327,331,7,0,0,0,328,330,7,1,0,0,329,328,1,0,0,0,330,333,
        1,0,0,0,331,329,1,0,0,0,331,332,1,0,0,0,332,335,1,0,0,0,333,331,
        1,0,0,0,334,326,1,0,0,0,334,327,1,0,0,0,335,108,1,0,0,0,336,338,
        7,1,0,0,337,336,1,0,0,0,338,339,1,0,0,0,339,337,1,0,0,0,339,340,
        1,0,0,0,340,347,1,0,0,0,341,343,5,46,0,0,342,344,7,1,0,0,343,342,
        1,0,0,0,344,345,1,0,0,0,345,343,1,0,0,0,345,346,1,0,0,0,346,348,
        1,0,0,0,347,341,1,0,0,0,347,348,1,0,0,0,348,110,1,0,0,0,349,351,
        5,39,0,0,350,352,5,92,0,0,351,350,1,0,0,0,351,352,1,0,0,0,352,353,
        1,0,0,0,353,354,7,2,0,0,354,355,5,39,0,0,355,112,1,0,0,0,356,358,
        7,3,0,0,357,356,1,0,0,0,358,359,1,0,0,0,359,357,1,0,0,0,359,360,
        1,0,0,0,360,361,1,0,0,0,361,362,6,56,0,0,362,114,1,0,0,0,363,367,
        7,4,0,0,364,366,7,5,0,0,365,364,1,0,0,0,366,369,1,0,0,0,367,365,
        1,0,0,0,367,368,1,0,0,0,368,116,1,0,0,0,369,367,1,0,0,0,370,371,
        5,43,0,0,371,372,5,43,0,0,372,118,1,0,0,0,373,374,5,45,0,0,374,375,
        5,45,0,0,375,120,1,0,0,0,376,379,3,125,62,0,377,379,3,123,61,0,378,
        376,1,0,0,0,378,377,1,0,0,0,379,122,1,0,0,0,380,381,5,47,0,0,381,
        382,5,42,0,0,382,386,1,0,0,0,383,385,9,0,0,0,384,383,1,0,0,0,385,
        388,1,0,0,0,386,387,1,0,0,0,386,384,1,0,0,0,387,389,1,0,0,0,388,
        386,1,0,0,0,389,390,5,42,0,0,390,391,5,47,0,0,391,392,1,0,0,0,392,
        393,6,61,0,0,393,124,1,0,0,0,394,395,5,47,0,0,395,396,5,47,0,0,396,
        400,1,0,0,0,397,399,8,6,0,0,398,397,1,0,0,0,399,402,1,0,0,0,400,
        398,1,0,0,0,400,401,1,0,0,0,401,403,1,0,0,0,402,400,1,0,0,0,403,
        404,6,62,0,0,404,126,1,0,0,0,12,0,331,334,339,345,347,351,359,367,
        378,386,400,1,6,0,0
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
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    LPAREN = 27
    RPAREN = 28
    LBRACE = 29
    RBRACE = 30
    PLUS = 31
    MINUS = 32
    MULT = 33
    DIV = 34
    MOD = 35
    GREATER_THAN = 36
    LESS_THAN = 37
    GREATER_EQUAL = 38
    LESS_EQUAL = 39
    EQUALS = 40
    NOT_EQUAL = 41
    SHIFT_LEFT = 42
    SHIFT_RIGHT = 43
    BITWISE_AND = 44
    BITWISE_OR = 45
    BITWISE_XOR = 46
    BITWISE_NOT = 47
    LOGICAL_AND = 48
    LOGICAL_OR = 49
    LOGICAL_NOT = 50
    COLON = 51
    SEMICOLON = 52
    COMMA = 53
    INT = 54
    FLOAT = 55
    CHAR = 56
    WHITESPACE = 57
    IDENTIFIER = 58
    INCREMENT = 59
    DECREMENT = 60
    COMMENT = 61
    BLOCKCOMMENT = 62
    LINECOMMENT = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'switch'", "'case'", "'default'", "'if'", "'else'", "'while'", 
            "'for'", "'printf'", "'\"%s\"'", "'\"%d\"'", "'\"%x\"'", "'\"%f\"'", 
            "'\"%c\"'", "'='", "'break'", "'continue'", "'return'", "'enum'", 
            "'typedef'", "'const'", "'int'", "'float'", "'char'", "'void'", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
            "'<<'", "'>>'", "'&'", "'|'", "'^'", "'~'", "'&&'", "'||'", 
            "'!'", "':'", "';'", "','", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT", 
            "DIV", "MOD", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
            "LESS_EQUAL", "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", "SHIFT_RIGHT", 
            "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", "BITWISE_NOT", "LOGICAL_AND", 
            "LOGICAL_OR", "LOGICAL_NOT", "COLON", "SEMICOLON", "COMMA", 
            "INT", "FLOAT", "CHAR", "WHITESPACE", "IDENTIFIER", "INCREMENT", 
            "DECREMENT", "COMMENT", "BLOCKCOMMENT", "LINECOMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", 
                  "MULT", "DIV", "MOD", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
                  "LESS_EQUAL", "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", "SHIFT_RIGHT", 
                  "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", "BITWISE_NOT", 
                  "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", "COLON", "SEMICOLON", 
                  "COMMA", "INT", "FLOAT", "CHAR", "WHITESPACE", "IDENTIFIER", 
                  "INCREMENT", "DECREMENT", "COMMENT", "BLOCKCOMMENT", "LINECOMMENT" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


