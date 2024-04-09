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
        4,1,55,395,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,4,0,70,8,0,11,0,12,0,71,1,0,1,0,4,0,76,8,0,11,0,12,0,77,
        5,0,80,8,0,10,0,12,0,83,9,0,1,0,1,0,1,0,1,0,5,0,89,8,0,10,0,12,0,
        92,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,104,8,2,10,2,
        12,2,107,9,2,1,2,1,2,1,3,1,3,4,3,113,8,3,11,3,12,3,114,1,3,1,3,4,
        3,119,8,3,11,3,12,3,120,1,3,1,3,1,3,4,3,126,8,3,11,3,12,3,127,1,
        3,1,3,1,3,1,3,1,3,1,3,4,3,136,8,3,11,3,12,3,137,3,3,140,8,3,1,4,
        1,4,5,4,144,8,4,10,4,12,4,147,9,4,1,4,3,4,150,8,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,3,10,182,8,10,1,11,3,
        11,185,8,11,1,11,1,11,1,11,3,11,190,8,11,3,11,192,8,11,1,11,1,11,
        3,11,196,8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,204,8,12,1,12,1,
        12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,216,8,14,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,226,8,15,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,3,16,247,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,281,
        8,16,10,16,12,16,284,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,302,8,17,1,18,1,18,
        1,19,3,19,307,8,19,1,19,1,19,1,19,4,19,312,8,19,11,19,12,19,313,
        1,19,3,19,317,8,19,1,19,1,19,1,19,4,19,322,8,19,11,19,12,19,323,
        1,19,3,19,327,8,19,1,19,3,19,330,8,19,1,20,1,20,1,21,4,21,335,8,
        21,11,21,12,21,336,1,21,4,21,340,8,21,11,21,12,21,341,1,21,1,21,
        1,21,1,22,1,22,4,22,349,8,22,11,22,12,22,350,1,23,4,23,354,8,23,
        11,23,12,23,355,1,23,1,23,1,24,4,24,361,8,24,11,24,12,24,362,1,24,
        1,24,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,
        1,29,1,29,1,29,1,29,1,30,5,30,384,8,30,10,30,12,30,387,9,30,1,30,
        1,30,1,31,1,31,1,32,1,32,1,32,0,1,32,33,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,0,5,1,0,9,13,1,0,15,16,1,0,25,26,1,0,46,48,3,0,1,1,19,20,50,50,
        438,0,81,1,0,0,0,2,95,1,0,0,0,4,101,1,0,0,0,6,139,1,0,0,0,8,141,
        1,0,0,0,10,151,1,0,0,0,12,157,1,0,0,0,14,164,1,0,0,0,16,167,1,0,
        0,0,18,173,1,0,0,0,20,181,1,0,0,0,22,184,1,0,0,0,24,197,1,0,0,0,
        26,207,1,0,0,0,28,215,1,0,0,0,30,225,1,0,0,0,32,246,1,0,0,0,34,301,
        1,0,0,0,36,303,1,0,0,0,38,329,1,0,0,0,40,331,1,0,0,0,42,334,1,0,
        0,0,44,346,1,0,0,0,46,353,1,0,0,0,48,360,1,0,0,0,50,366,1,0,0,0,
        52,369,1,0,0,0,54,372,1,0,0,0,56,375,1,0,0,0,58,378,1,0,0,0,60,385,
        1,0,0,0,62,390,1,0,0,0,64,392,1,0,0,0,66,80,3,64,32,0,67,69,3,28,
        14,0,68,70,5,45,0,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,
        72,1,0,0,0,72,80,1,0,0,0,73,75,3,58,29,0,74,76,5,45,0,0,75,74,1,
        0,0,0,76,77,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,
        66,1,0,0,0,79,67,1,0,0,0,79,73,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,
        0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,90,3,2,1,0,85,89,
        3,64,32,0,86,89,3,28,14,0,87,89,3,58,29,0,88,85,1,0,0,0,88,86,1,
        0,0,0,88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,
        93,1,0,0,0,92,90,1,0,0,0,93,94,5,0,0,1,94,1,1,0,0,0,95,96,5,1,0,
        0,96,97,5,2,0,0,97,98,5,21,0,0,98,99,5,22,0,0,99,100,3,4,2,0,100,
        3,1,0,0,0,101,105,5,23,0,0,102,104,3,6,3,0,103,102,1,0,0,0,104,107,
        1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,
        1,0,0,0,108,109,5,24,0,0,109,5,1,0,0,0,110,112,3,32,16,0,111,113,
        5,45,0,0,112,111,1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,
        1,0,0,0,115,140,1,0,0,0,116,118,3,28,14,0,117,119,5,45,0,0,118,117,
        1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,140,
        1,0,0,0,122,140,3,64,32,0,123,125,3,24,12,0,124,126,5,45,0,0,125,
        124,1,0,0,0,126,127,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,
        140,1,0,0,0,129,140,3,4,2,0,130,140,3,8,4,0,131,140,3,16,8,0,132,
        140,3,18,9,0,133,135,3,36,18,0,134,136,5,45,0,0,135,134,1,0,0,0,
        136,137,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,
        139,110,1,0,0,0,139,116,1,0,0,0,139,122,1,0,0,0,139,123,1,0,0,0,
        139,129,1,0,0,0,139,130,1,0,0,0,139,131,1,0,0,0,139,132,1,0,0,0,
        139,133,1,0,0,0,140,7,1,0,0,0,141,145,3,10,5,0,142,144,3,12,6,0,
        143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,
        146,149,1,0,0,0,147,145,1,0,0,0,148,150,3,14,7,0,149,148,1,0,0,0,
        149,150,1,0,0,0,150,9,1,0,0,0,151,152,5,3,0,0,152,153,5,21,0,0,153,
        154,3,32,16,0,154,155,5,22,0,0,155,156,3,4,2,0,156,11,1,0,0,0,157,
        158,5,4,0,0,158,159,5,3,0,0,159,160,5,21,0,0,160,161,3,32,16,0,161,
        162,5,22,0,0,162,163,3,4,2,0,163,13,1,0,0,0,164,165,5,4,0,0,165,
        166,3,4,2,0,166,15,1,0,0,0,167,168,5,5,0,0,168,169,5,21,0,0,169,
        170,3,32,16,0,170,171,5,22,0,0,171,172,3,4,2,0,172,17,1,0,0,0,173,
        174,5,6,0,0,174,175,5,21,0,0,175,176,3,22,11,0,176,177,5,22,0,0,
        177,178,3,4,2,0,178,19,1,0,0,0,179,182,3,28,14,0,180,182,3,32,16,
        0,181,179,1,0,0,0,181,180,1,0,0,0,182,21,1,0,0,0,183,185,3,28,14,
        0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,191,5,45,0,
        0,187,189,3,32,16,0,188,190,3,34,17,0,189,188,1,0,0,0,189,190,1,
        0,0,0,190,192,1,0,0,0,191,187,1,0,0,0,191,192,1,0,0,0,192,193,1,
        0,0,0,193,195,5,45,0,0,194,196,3,32,16,0,195,194,1,0,0,0,195,196,
        1,0,0,0,196,23,1,0,0,0,197,198,5,7,0,0,198,199,5,21,0,0,199,200,
        3,26,13,0,200,203,5,8,0,0,201,204,3,62,31,0,202,204,3,40,20,0,203,
        201,1,0,0,0,203,202,1,0,0,0,204,205,1,0,0,0,205,206,5,22,0,0,206,
        25,1,0,0,0,207,208,7,0,0,0,208,27,1,0,0,0,209,210,3,30,15,0,210,
        211,5,14,0,0,211,212,3,32,16,0,212,216,1,0,0,0,213,216,3,30,15,0,
        214,216,3,58,29,0,215,209,1,0,0,0,215,213,1,0,0,0,215,214,1,0,0,
        0,216,29,1,0,0,0,217,226,3,62,31,0,218,219,3,60,30,0,219,220,3,62,
        31,0,220,226,1,0,0,0,221,222,3,44,22,0,222,223,3,62,31,0,223,226,
        1,0,0,0,224,226,3,46,23,0,225,217,1,0,0,0,225,218,1,0,0,0,225,221,
        1,0,0,0,225,224,1,0,0,0,226,31,1,0,0,0,227,228,6,16,-1,0,228,247,
        3,38,19,0,229,247,3,62,31,0,230,247,3,46,23,0,231,247,3,48,24,0,
        232,233,5,44,0,0,233,247,3,32,16,20,234,235,5,41,0,0,235,247,3,32,
        16,19,236,237,5,21,0,0,237,238,3,32,16,0,238,239,5,22,0,0,239,247,
        1,0,0,0,240,247,3,42,21,0,241,247,3,50,25,0,242,247,3,52,26,0,243,
        247,3,54,27,0,244,247,3,56,28,0,245,247,3,36,18,0,246,227,1,0,0,
        0,246,229,1,0,0,0,246,230,1,0,0,0,246,231,1,0,0,0,246,232,1,0,0,
        0,246,234,1,0,0,0,246,236,1,0,0,0,246,240,1,0,0,0,246,241,1,0,0,
        0,246,242,1,0,0,0,246,243,1,0,0,0,246,244,1,0,0,0,246,245,1,0,0,
        0,247,282,1,0,0,0,248,249,10,18,0,0,249,250,5,28,0,0,250,281,3,32,
        16,19,251,252,10,17,0,0,252,253,5,29,0,0,253,281,3,32,16,18,254,
        255,10,16,0,0,255,256,5,27,0,0,256,281,3,32,16,17,257,258,10,15,
        0,0,258,259,5,26,0,0,259,281,3,32,16,16,260,261,10,14,0,0,261,262,
        5,25,0,0,262,281,3,32,16,15,263,264,10,13,0,0,264,265,5,36,0,0,265,
        281,3,32,16,14,266,267,10,12,0,0,267,268,5,37,0,0,268,281,3,32,16,
        13,269,270,10,11,0,0,270,271,5,38,0,0,271,281,3,32,16,12,272,273,
        10,10,0,0,273,274,5,39,0,0,274,281,3,32,16,11,275,276,10,9,0,0,276,
        277,5,40,0,0,277,281,3,32,16,10,278,279,10,2,0,0,279,281,3,34,17,
        0,280,248,1,0,0,0,280,251,1,0,0,0,280,254,1,0,0,0,280,257,1,0,0,
        0,280,260,1,0,0,0,280,263,1,0,0,0,280,266,1,0,0,0,280,269,1,0,0,
        0,280,272,1,0,0,0,280,275,1,0,0,0,280,278,1,0,0,0,281,284,1,0,0,
        0,282,280,1,0,0,0,282,283,1,0,0,0,283,33,1,0,0,0,284,282,1,0,0,0,
        285,286,5,30,0,0,286,302,3,32,16,0,287,288,5,31,0,0,288,302,3,32,
        16,0,289,290,5,32,0,0,290,302,3,32,16,0,291,292,5,33,0,0,292,302,
        3,32,16,0,293,294,5,34,0,0,294,302,3,32,16,0,295,296,5,35,0,0,296,
        302,3,32,16,0,297,298,5,42,0,0,298,302,3,32,16,0,299,300,5,43,0,
        0,300,302,3,32,16,0,301,285,1,0,0,0,301,287,1,0,0,0,301,289,1,0,
        0,0,301,291,1,0,0,0,301,293,1,0,0,0,301,295,1,0,0,0,301,297,1,0,
        0,0,301,299,1,0,0,0,302,35,1,0,0,0,303,304,7,1,0,0,304,37,1,0,0,
        0,305,307,7,2,0,0,306,305,1,0,0,0,306,307,1,0,0,0,307,308,1,0,0,
        0,308,330,3,40,20,0,309,310,5,25,0,0,310,312,5,26,0,0,311,309,1,
        0,0,0,312,313,1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,316,1,
        0,0,0,315,317,5,25,0,0,316,315,1,0,0,0,316,317,1,0,0,0,317,318,1,
        0,0,0,318,330,3,40,20,0,319,320,5,26,0,0,320,322,5,25,0,0,321,319,
        1,0,0,0,322,323,1,0,0,0,323,321,1,0,0,0,323,324,1,0,0,0,324,326,
        1,0,0,0,325,327,5,26,0,0,326,325,1,0,0,0,326,327,1,0,0,0,327,328,
        1,0,0,0,328,330,3,40,20,0,329,306,1,0,0,0,329,311,1,0,0,0,329,321,
        1,0,0,0,330,39,1,0,0,0,331,332,7,3,0,0,332,41,1,0,0,0,333,335,5,
        21,0,0,334,333,1,0,0,0,335,336,1,0,0,0,336,334,1,0,0,0,336,337,1,
        0,0,0,337,339,1,0,0,0,338,340,3,60,30,0,339,338,1,0,0,0,340,341,
        1,0,0,0,341,339,1,0,0,0,341,342,1,0,0,0,342,343,1,0,0,0,343,344,
        5,22,0,0,344,345,3,32,16,0,345,43,1,0,0,0,346,348,3,60,30,0,347,
        349,5,27,0,0,348,347,1,0,0,0,349,350,1,0,0,0,350,348,1,0,0,0,350,
        351,1,0,0,0,351,45,1,0,0,0,352,354,5,27,0,0,353,352,1,0,0,0,354,
        355,1,0,0,0,355,353,1,0,0,0,355,356,1,0,0,0,356,357,1,0,0,0,357,
        358,3,62,31,0,358,47,1,0,0,0,359,361,5,38,0,0,360,359,1,0,0,0,361,
        362,1,0,0,0,362,360,1,0,0,0,362,363,1,0,0,0,363,364,1,0,0,0,364,
        365,3,62,31,0,365,49,1,0,0,0,366,367,3,30,15,0,367,368,5,51,0,0,
        368,51,1,0,0,0,369,370,3,30,15,0,370,371,5,52,0,0,371,53,1,0,0,0,
        372,373,5,51,0,0,373,374,3,30,15,0,374,55,1,0,0,0,375,376,5,52,0,
        0,376,377,3,30,15,0,377,57,1,0,0,0,378,379,5,17,0,0,379,380,3,60,
        30,0,380,381,5,50,0,0,381,59,1,0,0,0,382,384,5,18,0,0,383,382,1,
        0,0,0,384,387,1,0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,388,1,
        0,0,0,387,385,1,0,0,0,388,389,7,4,0,0,389,61,1,0,0,0,390,391,5,50,
        0,0,391,63,1,0,0,0,392,393,5,53,0,0,393,65,1,0,0,0,38,71,77,79,81,
        88,90,105,114,120,127,137,139,145,149,181,184,189,191,195,203,215,
        225,246,280,282,301,306,313,316,323,326,329,336,341,350,355,362,
        385
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'if'", "'else'", "'while'", 
                     "'for'", "'printf'", "','", "'\"%s\"'", "'\"%d\"'", 
                     "'\"%x\"'", "'\"%f\"'", "'\"%c\"'", "'='", "'break'", 
                     "'continue'", "'typedef'", "'const'", "'float'", "'char'", 
                     "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'<<'", "'>>'", "'&'", "'|'", "'^'", "'~'", "'&&'", 
                     "'||'", "'!'", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "PLUS", "MINUS", "MULT", "DIV", "MOD", "GREATER_THAN", 
                      "LESS_THAN", "GREATER_EQUAL", "LESS_EQUAL", "EQUALS", 
                      "NOT_EQUAL", "SHIFT_LEFT", "SHIFT_RIGHT", "BITWISE_AND", 
                      "BITWISE_OR", "BITWISE_XOR", "BITWISE_NOT", "LOGICAL_AND", 
                      "LOGICAL_OR", "LOGICAL_NOT", "SEMICOLON", "INT", "FLOAT", 
                      "CHAR", "WHITESPACE", "IDENTIFIER", "INCREMENT", "DECREMENT", 
                      "COMMENT", "BLOCKCOMMENT", "LINECOMMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_scope = 2
    RULE_statement = 3
    RULE_conditional = 4
    RULE_ifStatement = 5
    RULE_elseIfStatement = 6
    RULE_elseStatement = 7
    RULE_whileLoop = 8
    RULE_forLoop = 9
    RULE_forInit = 10
    RULE_forCondition = 11
    RULE_printfStatement = 12
    RULE_formatSpecifier = 13
    RULE_variable = 14
    RULE_lvalue = 15
    RULE_rvalue = 16
    RULE_conditionalExpression = 17
    RULE_jumpStatement = 18
    RULE_unaryExpression = 19
    RULE_literal = 20
    RULE_explicitConversion = 21
    RULE_pointer = 22
    RULE_deref = 23
    RULE_addr = 24
    RULE_postFixIncrement = 25
    RULE_postFixDecrement = 26
    RULE_preFixIncrement = 27
    RULE_preFixDecrement = 28
    RULE_typedef = 29
    RULE_type = 30
    RULE_identifier = 31
    RULE_comment = 32

    ruleNames =  [ "program", "main", "scope", "statement", "conditional", 
                   "ifStatement", "elseIfStatement", "elseStatement", "whileLoop", 
                   "forLoop", "forInit", "forCondition", "printfStatement", 
                   "formatSpecifier", "variable", "lvalue", "rvalue", "conditionalExpression", 
                   "jumpStatement", "unaryExpression", "literal", "explicitConversion", 
                   "pointer", "deref", "addr", "postFixIncrement", "postFixDecrement", 
                   "preFixIncrement", "preFixDecrement", "typedef", "type", 
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
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    LPAREN=21
    RPAREN=22
    LBRACE=23
    RBRACE=24
    PLUS=25
    MINUS=26
    MULT=27
    DIV=28
    MOD=29
    GREATER_THAN=30
    LESS_THAN=31
    GREATER_EQUAL=32
    LESS_EQUAL=33
    EQUALS=34
    NOT_EQUAL=35
    SHIFT_LEFT=36
    SHIFT_RIGHT=37
    BITWISE_AND=38
    BITWISE_OR=39
    BITWISE_XOR=40
    BITWISE_NOT=41
    LOGICAL_AND=42
    LOGICAL_OR=43
    LOGICAL_NOT=44
    SEMICOLON=45
    INT=46
    FLOAT=47
    CHAR=48
    WHITESPACE=49
    IDENTIFIER=50
    INCREMENT=51
    DECREMENT=52
    COMMENT=53
    BLOCKCOMMENT=54
    LINECOMMENT=55

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


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.VariableContext)
            else:
                return self.getTypedRuleContext(GrammarParser.VariableContext,i)


        def typedef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.TypedefContext)
            else:
                return self.getTypedRuleContext(GrammarParser.TypedefContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

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
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 79
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        self.state = 66
                        self.comment()
                        pass

                    elif la_ == 2:
                        self.state = 67
                        self.variable()
                        self.state = 69 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 68
                            self.match(GrammarParser.SEMICOLON)
                            self.state = 71 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==45):
                                break

                        pass

                    elif la_ == 3:
                        self.state = 73
                        self.typedef()
                        self.state = 75 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 74
                            self.match(GrammarParser.SEMICOLON)
                            self.state = 77 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==45):
                                break

                        pass

             
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 84
            self.main()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10133099297767426) != 0):
                self.state = 88
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 85
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 86
                    self.variable()
                    pass

                elif la_ == 3:
                    self.state = 87
                    self.typedef()
                    pass


                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
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
            self.state = 95
            self.match(GrammarParser.T__0)
            self.state = 96
            self.match(GrammarParser.T__1)
            self.state = 97
            self.match(GrammarParser.LPAREN)
            self.state = 98
            self.match(GrammarParser.RPAREN)
            self.state = 99
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
            self.state = 101
            self.match(GrammarParser.LBRACE)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17401146146521322) != 0):
                self.state = 102
                self.statement()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
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

        def variable(self):
            return self.getTypedRuleContext(GrammarParser.VariableContext,0)


        def comment(self):
            return self.getTypedRuleContext(GrammarParser.CommentContext,0)


        def printfStatement(self):
            return self.getTypedRuleContext(GrammarParser.PrintfStatementContext,0)


        def scope(self):
            return self.getTypedRuleContext(GrammarParser.ScopeContext,0)


        def conditional(self):
            return self.getTypedRuleContext(GrammarParser.ConditionalContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(GrammarParser.WhileLoopContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(GrammarParser.ForLoopContext,0)


        def jumpStatement(self):
            return self.getTypedRuleContext(GrammarParser.JumpStatementContext,0)


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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.rvalue(0)
                self.state = 112 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 111
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 114 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==45):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.variable()
                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 117
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 120 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==45):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.printfStatement()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 124
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 127 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==45):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.scope()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 132
                self.forLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 133
                self.jumpStatement()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 134
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 137 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==45):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(GrammarParser.IfStatementContext,0)


        def elseIfStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ElseIfStatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ElseIfStatementContext,i)


        def elseStatement(self):
            return self.getTypedRuleContext(GrammarParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = GrammarParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.ifStatement()
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 142
                    self.elseIfStatement() 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 148
                self.elseStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def scope(self):
            return self.getTypedRuleContext(GrammarParser.ScopeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = GrammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(GrammarParser.T__2)
            self.state = 152
            self.match(GrammarParser.LPAREN)
            self.state = 153
            self.rvalue(0)
            self.state = 154
            self.match(GrammarParser.RPAREN)
            self.state = 155
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def scope(self):
            return self.getTypedRuleContext(GrammarParser.ScopeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_elseIfStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfStatement" ):
                listener.enterElseIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfStatement" ):
                listener.exitElseIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfStatement" ):
                return visitor.visitElseIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseIfStatement(self):

        localctx = GrammarParser.ElseIfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elseIfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(GrammarParser.T__3)
            self.state = 158
            self.match(GrammarParser.T__2)
            self.state = 159
            self.match(GrammarParser.LPAREN)
            self.state = 160
            self.rvalue(0)
            self.state = 161
            self.match(GrammarParser.RPAREN)
            self.state = 162
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scope(self):
            return self.getTypedRuleContext(GrammarParser.ScopeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStatement" ):
                return visitor.visitElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseStatement(self):

        localctx = GrammarParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(GrammarParser.T__3)
            self.state = 165
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def scope(self):
            return self.getTypedRuleContext(GrammarParser.ScopeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = GrammarParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(GrammarParser.T__4)
            self.state = 168
            self.match(GrammarParser.LPAREN)
            self.state = 169
            self.rvalue(0)
            self.state = 170
            self.match(GrammarParser.RPAREN)
            self.state = 171
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def forCondition(self):
            return self.getTypedRuleContext(GrammarParser.ForConditionContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def scope(self):
            return self.getTypedRuleContext(GrammarParser.ScopeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = GrammarParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(GrammarParser.T__5)
            self.state = 174
            self.match(GrammarParser.LPAREN)
            self.state = 175
            self.forCondition()
            self.state = 176
            self.match(GrammarParser.RPAREN)
            self.state = 177
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(GrammarParser.VariableContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = GrammarParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forInit)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.rvalue(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def variable(self):
            return self.getTypedRuleContext(GrammarParser.VariableContext,0)


        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


        def conditionalExpression(self):
            return self.getTypedRuleContext(GrammarParser.ConditionalExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_forCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondition" ):
                listener.enterForCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondition" ):
                listener.exitForCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = GrammarParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125900043026434) != 0):
                self.state = 183
                self.variable()


            self.state = 186
            self.match(GrammarParser.SEMICOLON)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8393946883260418) != 0):
                self.state = 187
                self.rvalue(0)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 13261785268224) != 0):
                    self.state = 188
                    self.conditionalExpression()




            self.state = 193
            self.match(GrammarParser.SEMICOLON)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8393946883260418) != 0):
                self.state = 194
                self.rvalue(0)


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
        self.enterRule(localctx, 24, self.RULE_printfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(GrammarParser.T__6)
            self.state = 198
            self.match(GrammarParser.LPAREN)
            self.state = 199
            self.formatSpecifier()
            self.state = 200
            self.match(GrammarParser.T__7)
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.state = 201
                self.identifier()
                pass
            elif token in [46, 47, 48]:
                self.state = 202
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 205
            self.match(GrammarParser.RPAREN)
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
        self.enterRule(localctx, 26, self.RULE_formatSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0)):
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


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(GrammarParser.LvalueContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def typedef(self):
            return self.getTypedRuleContext(GrammarParser.TypedefContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = GrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variable)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.lvalue()
                self.state = 210
                self.match(GrammarParser.T__13)
                self.state = 211
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.lvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.typedef()
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
        self.enterRule(localctx, 30, self.RULE_lvalue)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.type_()
                self.state = 219
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.pointer()
                self.state = 222
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
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


        def postFixIncrement(self):
            return self.getTypedRuleContext(GrammarParser.PostFixIncrementContext,0)


        def postFixDecrement(self):
            return self.getTypedRuleContext(GrammarParser.PostFixDecrementContext,0)


        def preFixIncrement(self):
            return self.getTypedRuleContext(GrammarParser.PreFixIncrementContext,0)


        def preFixDecrement(self):
            return self.getTypedRuleContext(GrammarParser.PreFixDecrementContext,0)


        def jumpStatement(self):
            return self.getTypedRuleContext(GrammarParser.JumpStatementContext,0)


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

        def conditionalExpression(self):
            return self.getTypedRuleContext(GrammarParser.ConditionalExpressionContext,0)


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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 228
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 229
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 230
                self.deref()
                pass

            elif la_ == 4:
                self.state = 231
                self.addr()
                pass

            elif la_ == 5:
                self.state = 232
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 233
                self.rvalue(20)
                pass

            elif la_ == 6:
                self.state = 234
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 235
                self.rvalue(19)
                pass

            elif la_ == 7:
                self.state = 236
                self.match(GrammarParser.LPAREN)
                self.state = 237
                self.rvalue(0)
                self.state = 238
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 240
                self.explicitConversion()
                pass

            elif la_ == 9:
                self.state = 241
                self.postFixIncrement()
                pass

            elif la_ == 10:
                self.state = 242
                self.postFixDecrement()
                pass

            elif la_ == 11:
                self.state = 243
                self.preFixIncrement()
                pass

            elif la_ == 12:
                self.state = 244
                self.preFixDecrement()
                pass

            elif la_ == 13:
                self.state = 245
                self.jumpStatement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 280
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 248
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 249
                        self.match(GrammarParser.DIV)
                        self.state = 250
                        self.rvalue(19)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 251
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 252
                        self.match(GrammarParser.MOD)
                        self.state = 253
                        self.rvalue(18)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 254
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 255
                        self.match(GrammarParser.MULT)
                        self.state = 256
                        self.rvalue(17)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 257
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 258
                        self.match(GrammarParser.MINUS)
                        self.state = 259
                        self.rvalue(16)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 260
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 261
                        self.match(GrammarParser.PLUS)
                        self.state = 262
                        self.rvalue(15)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 263
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 264
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 265
                        self.rvalue(14)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 266
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 267
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 268
                        self.rvalue(13)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 269
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 270
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 271
                        self.rvalue(12)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 272
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 273
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 274
                        self.rvalue(11)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 275
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 276
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 277
                        self.rvalue(10)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 278
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 279
                        self.conditionalExpression()
                        pass

             
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREATER_THAN(self):
            return self.getToken(GrammarParser.GREATER_THAN, 0)

        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


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

        def LOGICAL_AND(self):
            return self.getToken(GrammarParser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(GrammarParser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_conditionalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalExpression" ):
                listener.enterConditionalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalExpression" ):
                listener.exitConditionalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalExpression" ):
                return visitor.visitConditionalExpression(self)
            else:
                return visitor.visitChildren(self)




    def conditionalExpression(self):

        localctx = GrammarParser.ConditionalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_conditionalExpression)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(GrammarParser.GREATER_THAN)
                self.state = 286
                self.rvalue(0)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(GrammarParser.LESS_THAN)
                self.state = 288
                self.rvalue(0)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
                self.match(GrammarParser.GREATER_EQUAL)
                self.state = 290
                self.rvalue(0)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                self.match(GrammarParser.LESS_EQUAL)
                self.state = 292
                self.rvalue(0)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 5)
                self.state = 293
                self.match(GrammarParser.EQUALS)
                self.state = 294
                self.rvalue(0)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 6)
                self.state = 295
                self.match(GrammarParser.NOT_EQUAL)
                self.state = 296
                self.rvalue(0)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 7)
                self.state = 297
                self.match(GrammarParser.LOGICAL_AND)
                self.state = 298
                self.rvalue(0)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 8)
                self.state = 299
                self.match(GrammarParser.LOGICAL_OR)
                self.state = 300
                self.rvalue(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_jumpStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpStatement" ):
                listener.enterJumpStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpStatement" ):
                listener.exitJumpStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpStatement" ):
                return visitor.visitJumpStatement(self)
            else:
                return visitor.visitChildren(self)




    def jumpStatement(self):

        localctx = GrammarParser.JumpStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_jumpStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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
        self.enterRule(localctx, 38, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25 or _la==26:
                    self.state = 305
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 308
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 309
                        self.match(GrammarParser.PLUS)
                        self.state = 310
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 313 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 315
                    self.match(GrammarParser.PLUS)


                self.state = 318
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 319
                        self.match(GrammarParser.MINUS)
                        self.state = 320
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 323 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 325
                    self.match(GrammarParser.MINUS)


                self.state = 328
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
        self.enterRule(localctx, 40, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 492581209243648) != 0)):
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

        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


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
        self.enterRule(localctx, 42, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 333
                self.match(GrammarParser.LPAREN)
                self.state = 336 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 339 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 338
                self.type_()
                self.state = 341 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899908677634) != 0)):
                    break

            self.state = 343
            self.match(GrammarParser.RPAREN)
            self.state = 344
            self.rvalue(0)
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
        self.enterRule(localctx, 44, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.type_()
            self.state = 348 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 347
                self.match(GrammarParser.MULT)
                self.state = 350 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==27):
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
        self.enterRule(localctx, 46, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 352
                self.match(GrammarParser.MULT)
                self.state = 355 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==27):
                    break

            self.state = 357
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
        self.enterRule(localctx, 48, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 359
                self.match(GrammarParser.BITWISE_AND)
                self.state = 362 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
                    break

            self.state = 364
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
        self.enterRule(localctx, 50, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.lvalue()
            self.state = 367
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
        self.enterRule(localctx, 52, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.lvalue()
            self.state = 370
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
        self.enterRule(localctx, 54, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(GrammarParser.INCREMENT)
            self.state = 373
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
        self.enterRule(localctx, 56, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(GrammarParser.DECREMENT)
            self.state = 376
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
        self.enterRule(localctx, 58, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(GrammarParser.T__16)
            self.state = 379
            self.type_()
            self.state = 380
            self.match(GrammarParser.IDENTIFIER)
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
        self.enterRule(localctx, 60, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 382
                self.match(GrammarParser.T__17)
                self.state = 387
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 388
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899908415490) != 0)):
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
        self.enterRule(localctx, 62, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
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
        self.enterRule(localctx, 64, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
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
        self._predicates[16] = self.rvalue_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def rvalue_sempred(self, localctx:RvalueContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




