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
        4,1,61,544,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,1,0,1,0,4,0,86,8,0,11,0,12,0,87,1,0,1,0,4,0,92,8,0,
        11,0,12,0,93,1,0,1,0,4,0,98,8,0,11,0,12,0,99,1,0,4,0,103,8,0,11,
        0,12,0,104,1,0,1,0,1,1,1,1,5,1,111,8,1,10,1,12,1,114,9,1,1,1,1,1,
        1,2,1,2,4,2,120,8,2,11,2,12,2,121,1,2,1,2,4,2,126,8,2,11,2,12,2,
        127,1,2,1,2,1,2,4,2,133,8,2,11,2,12,2,134,1,2,1,2,1,2,1,2,1,2,1,
        2,4,2,143,8,2,11,2,12,2,144,1,2,1,2,4,2,149,8,2,11,2,12,2,150,1,
        2,1,2,3,2,155,8,2,1,3,1,3,3,3,159,8,3,1,3,1,3,1,3,3,3,164,8,3,1,
        3,1,3,1,3,1,3,1,3,3,3,171,8,3,1,3,1,3,1,3,3,3,176,8,3,1,3,1,3,1,
        3,3,3,181,8,3,1,4,1,4,1,4,3,4,186,8,4,1,4,1,4,3,4,190,8,4,1,4,1,
        4,1,4,5,4,195,8,4,10,4,12,4,198,9,4,1,5,1,5,1,5,3,5,203,8,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,213,8,6,10,6,12,6,216,9,6,1,7,1,
        7,1,7,1,7,1,7,1,7,5,7,224,8,7,10,7,12,7,227,9,7,1,7,1,7,1,8,1,8,
        1,8,1,8,5,8,235,8,8,10,8,12,8,238,9,8,1,8,1,8,1,8,5,8,243,8,8,10,
        8,12,8,246,9,8,3,8,248,8,8,1,9,1,9,5,9,252,8,9,10,9,12,9,255,9,9,
        1,9,3,9,258,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,15,3,15,289,8,15,1,15,1,15,3,15,293,8,
        15,1,15,1,15,3,15,297,8,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,305,
        8,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,317,
        8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,327,8,19,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,3,20,349,8,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,5,20,389,8,20,10,20,12,20,
        392,9,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,3,21,406,8,21,1,22,1,22,1,22,1,22,3,22,412,8,22,3,22,414,8,
        22,1,23,3,23,417,8,23,1,23,1,23,1,23,3,23,422,8,23,1,23,1,23,4,23,
        426,8,23,11,23,12,23,427,1,23,3,23,431,8,23,1,23,1,23,1,23,3,23,
        436,8,23,1,23,1,23,4,23,440,8,23,11,23,12,23,441,1,23,3,23,445,8,
        23,1,23,1,23,1,23,3,23,450,8,23,3,23,452,8,23,1,24,1,24,1,25,4,25,
        457,8,25,11,25,12,25,458,1,25,4,25,462,8,25,11,25,12,25,463,1,25,
        1,25,1,25,1,26,1,26,4,26,471,8,26,11,26,12,26,472,1,27,4,27,476,
        8,27,11,27,12,27,477,1,27,1,27,1,28,4,28,483,8,28,11,28,12,28,484,
        1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,495,8,29,10,29,12,29,
        498,9,29,1,29,1,29,1,30,1,30,3,30,504,8,30,1,31,1,31,1,31,1,31,1,
        31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,
        35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,38,5,38,533,8,38,10,
        38,12,38,536,9,38,1,38,1,38,1,39,1,39,1,40,1,40,1,40,0,3,8,12,40,
        41,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,0,4,1,0,
        9,13,1,0,29,30,1,0,52,54,2,0,21,24,56,56,607,0,102,1,0,0,0,2,108,
        1,0,0,0,4,154,1,0,0,0,6,180,1,0,0,0,8,182,1,0,0,0,10,199,1,0,0,0,
        12,206,1,0,0,0,14,217,1,0,0,0,16,247,1,0,0,0,18,249,1,0,0,0,20,259,
        1,0,0,0,22,265,1,0,0,0,24,272,1,0,0,0,26,275,1,0,0,0,28,281,1,0,
        0,0,30,288,1,0,0,0,32,298,1,0,0,0,34,308,1,0,0,0,36,316,1,0,0,0,
        38,326,1,0,0,0,40,348,1,0,0,0,42,405,1,0,0,0,44,413,1,0,0,0,46,451,
        1,0,0,0,48,453,1,0,0,0,50,456,1,0,0,0,52,468,1,0,0,0,54,475,1,0,
        0,0,56,482,1,0,0,0,58,488,1,0,0,0,60,503,1,0,0,0,62,505,1,0,0,0,
        64,511,1,0,0,0,66,515,1,0,0,0,68,518,1,0,0,0,70,521,1,0,0,0,72,524,
        1,0,0,0,74,527,1,0,0,0,76,534,1,0,0,0,78,539,1,0,0,0,80,541,1,0,
        0,0,82,103,3,80,40,0,83,85,3,58,29,0,84,86,5,50,0,0,85,84,1,0,0,
        0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,103,1,0,0,0,89,91,
        3,36,18,0,90,92,5,50,0,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,
        0,93,94,1,0,0,0,94,103,1,0,0,0,95,97,3,74,37,0,96,98,5,50,0,0,97,
        96,1,0,0,0,98,99,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,103,1,
        0,0,0,101,103,3,6,3,0,102,82,1,0,0,0,102,83,1,0,0,0,102,89,1,0,0,
        0,102,95,1,0,0,0,102,101,1,0,0,0,103,104,1,0,0,0,104,102,1,0,0,0,
        104,105,1,0,0,0,105,106,1,0,0,0,106,107,5,0,0,1,107,1,1,0,0,0,108,
        112,5,27,0,0,109,111,3,4,2,0,110,109,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,
        116,5,28,0,0,116,3,1,0,0,0,117,119,3,40,20,0,118,120,5,50,0,0,119,
        118,1,0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,
        155,1,0,0,0,123,125,3,36,18,0,124,126,5,50,0,0,125,124,1,0,0,0,126,
        127,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,155,1,0,0,0,129,
        155,3,80,40,0,130,132,3,32,16,0,131,133,5,50,0,0,132,131,1,0,0,0,
        133,134,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,155,1,0,0,0,
        136,155,3,2,1,0,137,155,3,18,9,0,138,155,3,26,13,0,139,155,3,28,
        14,0,140,142,3,60,30,0,141,143,5,50,0,0,142,141,1,0,0,0,143,144,
        1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,155,1,0,0,0,146,148,
        3,44,22,0,147,149,5,50,0,0,148,147,1,0,0,0,149,150,1,0,0,0,150,148,
        1,0,0,0,150,151,1,0,0,0,151,155,1,0,0,0,152,155,3,6,3,0,153,155,
        3,14,7,0,154,117,1,0,0,0,154,123,1,0,0,0,154,129,1,0,0,0,154,130,
        1,0,0,0,154,136,1,0,0,0,154,137,1,0,0,0,154,138,1,0,0,0,154,139,
        1,0,0,0,154,140,1,0,0,0,154,146,1,0,0,0,154,152,1,0,0,0,154,153,
        1,0,0,0,155,5,1,0,0,0,156,159,3,76,38,0,157,159,3,52,26,0,158,156,
        1,0,0,0,158,157,1,0,0,0,159,160,1,0,0,0,160,161,5,56,0,0,161,163,
        5,25,0,0,162,164,3,8,4,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,
        1,0,0,0,165,166,5,26,0,0,166,167,3,2,1,0,167,181,1,0,0,0,168,171,
        3,76,38,0,169,171,3,52,26,0,170,168,1,0,0,0,170,169,1,0,0,0,171,
        172,1,0,0,0,172,173,5,56,0,0,173,175,5,25,0,0,174,176,3,8,4,0,175,
        174,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,5,26,0,0,178,
        179,5,50,0,0,179,181,1,0,0,0,180,158,1,0,0,0,180,170,1,0,0,0,181,
        7,1,0,0,0,182,185,6,4,-1,0,183,186,3,52,26,0,184,186,3,76,38,0,185,
        183,1,0,0,0,185,184,1,0,0,0,186,189,1,0,0,0,187,190,3,56,28,0,188,
        190,3,78,39,0,189,187,1,0,0,0,189,188,1,0,0,0,190,196,1,0,0,0,191,
        192,10,1,0,0,192,193,5,51,0,0,193,195,3,8,4,2,194,191,1,0,0,0,195,
        198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,9,1,0,0,0,198,196,
        1,0,0,0,199,200,5,56,0,0,200,202,5,25,0,0,201,203,3,12,6,0,202,201,
        1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,205,5,26,0,0,205,11,
        1,0,0,0,206,207,6,6,-1,0,207,208,3,40,20,0,208,214,1,0,0,0,209,210,
        10,1,0,0,210,211,5,51,0,0,211,213,3,12,6,2,212,209,1,0,0,0,213,216,
        1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,13,1,0,0,0,216,214,1,
        0,0,0,217,218,5,1,0,0,218,219,5,25,0,0,219,220,3,40,20,0,220,221,
        5,26,0,0,221,225,5,27,0,0,222,224,3,16,8,0,223,222,1,0,0,0,224,227,
        1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,228,1,0,0,0,227,225,
        1,0,0,0,228,229,5,28,0,0,229,15,1,0,0,0,230,231,5,2,0,0,231,232,
        3,48,24,0,232,236,5,49,0,0,233,235,3,4,2,0,234,233,1,0,0,0,235,238,
        1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,248,1,0,0,0,238,236,
        1,0,0,0,239,240,5,3,0,0,240,244,5,49,0,0,241,243,3,4,2,0,242,241,
        1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,248,
        1,0,0,0,246,244,1,0,0,0,247,230,1,0,0,0,247,239,1,0,0,0,248,17,1,
        0,0,0,249,253,3,20,10,0,250,252,3,22,11,0,251,250,1,0,0,0,252,255,
        1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,257,1,0,0,0,255,253,
        1,0,0,0,256,258,3,24,12,0,257,256,1,0,0,0,257,258,1,0,0,0,258,19,
        1,0,0,0,259,260,5,4,0,0,260,261,5,25,0,0,261,262,3,40,20,0,262,263,
        5,26,0,0,263,264,3,2,1,0,264,21,1,0,0,0,265,266,5,5,0,0,266,267,
        5,4,0,0,267,268,5,25,0,0,268,269,3,40,20,0,269,270,5,26,0,0,270,
        271,3,2,1,0,271,23,1,0,0,0,272,273,5,5,0,0,273,274,3,2,1,0,274,25,
        1,0,0,0,275,276,5,6,0,0,276,277,5,25,0,0,277,278,3,40,20,0,278,279,
        5,26,0,0,279,280,3,2,1,0,280,27,1,0,0,0,281,282,5,7,0,0,282,283,
        5,25,0,0,283,284,3,30,15,0,284,285,5,26,0,0,285,286,3,2,1,0,286,
        29,1,0,0,0,287,289,3,36,18,0,288,287,1,0,0,0,288,289,1,0,0,0,289,
        290,1,0,0,0,290,292,5,50,0,0,291,293,3,40,20,0,292,291,1,0,0,0,292,
        293,1,0,0,0,293,294,1,0,0,0,294,296,5,50,0,0,295,297,3,40,20,0,296,
        295,1,0,0,0,296,297,1,0,0,0,297,31,1,0,0,0,298,299,5,8,0,0,299,300,
        5,25,0,0,300,301,3,34,17,0,301,304,5,51,0,0,302,305,3,78,39,0,303,
        305,3,48,24,0,304,302,1,0,0,0,304,303,1,0,0,0,305,306,1,0,0,0,306,
        307,5,26,0,0,307,33,1,0,0,0,308,309,7,0,0,0,309,35,1,0,0,0,310,311,
        3,38,19,0,311,312,5,14,0,0,312,313,3,40,20,0,313,317,1,0,0,0,314,
        317,3,38,19,0,315,317,3,74,37,0,316,310,1,0,0,0,316,314,1,0,0,0,
        316,315,1,0,0,0,317,37,1,0,0,0,318,327,3,78,39,0,319,320,3,76,38,
        0,320,321,3,78,39,0,321,327,1,0,0,0,322,323,3,52,26,0,323,324,3,
        78,39,0,324,327,1,0,0,0,325,327,3,54,27,0,326,318,1,0,0,0,326,319,
        1,0,0,0,326,322,1,0,0,0,326,325,1,0,0,0,327,39,1,0,0,0,328,329,6,
        20,-1,0,329,349,3,46,23,0,330,349,3,78,39,0,331,349,3,54,27,0,332,
        349,3,56,28,0,333,334,5,48,0,0,334,349,3,40,20,23,335,336,5,45,0,
        0,336,349,3,40,20,22,337,338,5,25,0,0,338,339,3,40,20,0,339,340,
        5,26,0,0,340,349,1,0,0,0,341,349,3,50,25,0,342,349,3,66,33,0,343,
        349,3,68,34,0,344,349,3,70,35,0,345,349,3,72,36,0,346,349,3,10,5,
        0,347,349,3,44,22,0,348,328,1,0,0,0,348,330,1,0,0,0,348,331,1,0,
        0,0,348,332,1,0,0,0,348,333,1,0,0,0,348,335,1,0,0,0,348,337,1,0,
        0,0,348,341,1,0,0,0,348,342,1,0,0,0,348,343,1,0,0,0,348,344,1,0,
        0,0,348,345,1,0,0,0,348,346,1,0,0,0,348,347,1,0,0,0,349,390,1,0,
        0,0,350,351,10,21,0,0,351,352,5,32,0,0,352,389,3,40,20,22,353,354,
        10,20,0,0,354,355,5,33,0,0,355,389,3,40,20,21,356,357,10,19,0,0,
        357,358,5,31,0,0,358,389,3,40,20,20,359,360,10,18,0,0,360,361,5,
        30,0,0,361,389,3,40,20,19,362,363,10,17,0,0,363,364,5,29,0,0,364,
        389,3,40,20,18,365,366,10,16,0,0,366,367,5,40,0,0,367,389,3,40,20,
        17,368,369,10,15,0,0,369,370,5,41,0,0,370,389,3,40,20,16,371,372,
        10,14,0,0,372,373,5,42,0,0,373,389,3,40,20,15,374,375,10,13,0,0,
        375,376,5,43,0,0,376,389,3,40,20,14,377,378,10,12,0,0,378,379,5,
        44,0,0,379,389,3,40,20,13,380,381,10,11,0,0,381,382,5,46,0,0,382,
        389,3,40,20,12,383,384,10,10,0,0,384,385,5,47,0,0,385,389,3,40,20,
        11,386,387,10,3,0,0,387,389,3,42,21,0,388,350,1,0,0,0,388,353,1,
        0,0,0,388,356,1,0,0,0,388,359,1,0,0,0,388,362,1,0,0,0,388,365,1,
        0,0,0,388,368,1,0,0,0,388,371,1,0,0,0,388,374,1,0,0,0,388,377,1,
        0,0,0,388,380,1,0,0,0,388,383,1,0,0,0,388,386,1,0,0,0,389,392,1,
        0,0,0,390,388,1,0,0,0,390,391,1,0,0,0,391,41,1,0,0,0,392,390,1,0,
        0,0,393,394,5,34,0,0,394,406,3,40,20,0,395,396,5,35,0,0,396,406,
        3,40,20,0,397,398,5,36,0,0,398,406,3,40,20,0,399,400,5,37,0,0,400,
        406,3,40,20,0,401,402,5,38,0,0,402,406,3,40,20,0,403,404,5,39,0,
        0,404,406,3,40,20,0,405,393,1,0,0,0,405,395,1,0,0,0,405,397,1,0,
        0,0,405,399,1,0,0,0,405,401,1,0,0,0,405,403,1,0,0,0,406,43,1,0,0,
        0,407,414,5,15,0,0,408,414,5,16,0,0,409,411,5,17,0,0,410,412,3,40,
        20,0,411,410,1,0,0,0,411,412,1,0,0,0,412,414,1,0,0,0,413,407,1,0,
        0,0,413,408,1,0,0,0,413,409,1,0,0,0,414,45,1,0,0,0,415,417,7,1,0,
        0,416,415,1,0,0,0,416,417,1,0,0,0,417,421,1,0,0,0,418,422,3,48,24,
        0,419,422,3,78,39,0,420,422,3,54,27,0,421,418,1,0,0,0,421,419,1,
        0,0,0,421,420,1,0,0,0,422,452,1,0,0,0,423,424,5,29,0,0,424,426,5,
        30,0,0,425,423,1,0,0,0,426,427,1,0,0,0,427,425,1,0,0,0,427,428,1,
        0,0,0,428,430,1,0,0,0,429,431,5,29,0,0,430,429,1,0,0,0,430,431,1,
        0,0,0,431,435,1,0,0,0,432,436,3,48,24,0,433,436,3,78,39,0,434,436,
        3,54,27,0,435,432,1,0,0,0,435,433,1,0,0,0,435,434,1,0,0,0,436,452,
        1,0,0,0,437,438,5,30,0,0,438,440,5,29,0,0,439,437,1,0,0,0,440,441,
        1,0,0,0,441,439,1,0,0,0,441,442,1,0,0,0,442,444,1,0,0,0,443,445,
        5,30,0,0,444,443,1,0,0,0,444,445,1,0,0,0,445,449,1,0,0,0,446,450,
        3,48,24,0,447,450,3,78,39,0,448,450,3,54,27,0,449,446,1,0,0,0,449,
        447,1,0,0,0,449,448,1,0,0,0,450,452,1,0,0,0,451,416,1,0,0,0,451,
        425,1,0,0,0,451,439,1,0,0,0,452,47,1,0,0,0,453,454,7,2,0,0,454,49,
        1,0,0,0,455,457,5,25,0,0,456,455,1,0,0,0,457,458,1,0,0,0,458,456,
        1,0,0,0,458,459,1,0,0,0,459,461,1,0,0,0,460,462,3,76,38,0,461,460,
        1,0,0,0,462,463,1,0,0,0,463,461,1,0,0,0,463,464,1,0,0,0,464,465,
        1,0,0,0,465,466,5,26,0,0,466,467,3,40,20,0,467,51,1,0,0,0,468,470,
        3,76,38,0,469,471,5,31,0,0,470,469,1,0,0,0,471,472,1,0,0,0,472,470,
        1,0,0,0,472,473,1,0,0,0,473,53,1,0,0,0,474,476,5,31,0,0,475,474,
        1,0,0,0,476,477,1,0,0,0,477,475,1,0,0,0,477,478,1,0,0,0,478,479,
        1,0,0,0,479,480,3,78,39,0,480,55,1,0,0,0,481,483,5,42,0,0,482,481,
        1,0,0,0,483,484,1,0,0,0,484,482,1,0,0,0,484,485,1,0,0,0,485,486,
        1,0,0,0,486,487,3,78,39,0,487,57,1,0,0,0,488,489,5,18,0,0,489,490,
        5,56,0,0,490,491,5,27,0,0,491,496,5,56,0,0,492,493,5,51,0,0,493,
        495,5,56,0,0,494,492,1,0,0,0,495,498,1,0,0,0,496,494,1,0,0,0,496,
        497,1,0,0,0,497,499,1,0,0,0,498,496,1,0,0,0,499,500,5,28,0,0,500,
        59,1,0,0,0,501,504,3,62,31,0,502,504,3,64,32,0,503,501,1,0,0,0,503,
        502,1,0,0,0,504,61,1,0,0,0,505,506,5,18,0,0,506,507,5,56,0,0,507,
        508,5,56,0,0,508,509,5,14,0,0,509,510,5,56,0,0,510,63,1,0,0,0,511,
        512,5,18,0,0,512,513,5,56,0,0,513,514,5,56,0,0,514,65,1,0,0,0,515,
        516,3,38,19,0,516,517,5,57,0,0,517,67,1,0,0,0,518,519,3,38,19,0,
        519,520,5,58,0,0,520,69,1,0,0,0,521,522,5,57,0,0,522,523,3,38,19,
        0,523,71,1,0,0,0,524,525,5,58,0,0,525,526,3,38,19,0,526,73,1,0,0,
        0,527,528,5,19,0,0,528,529,3,76,38,0,529,530,5,56,0,0,530,75,1,0,
        0,0,531,533,5,20,0,0,532,531,1,0,0,0,533,536,1,0,0,0,534,532,1,0,
        0,0,534,535,1,0,0,0,535,537,1,0,0,0,536,534,1,0,0,0,537,538,7,3,
        0,0,538,77,1,0,0,0,539,540,5,56,0,0,540,79,1,0,0,0,541,542,5,59,
        0,0,542,81,1,0,0,0,57,87,93,99,102,104,112,121,127,134,144,150,154,
        158,163,170,175,180,185,189,196,202,214,225,236,244,247,253,257,
        288,292,296,304,316,326,348,388,390,405,411,413,416,421,427,430,
        435,441,444,449,451,458,463,472,477,484,496,503,534
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'switch'", "'case'", "'default'", "'if'", 
                     "'else'", "'while'", "'for'", "'printf'", "'\"%s\"'", 
                     "'\"%d\"'", "'\"%x\"'", "'\"%f\"'", "'\"%c\"'", "'='", 
                     "'break'", "'continue'", "'return'", "'enum'", "'typedef'", 
                     "'const'", "'int'", "'float'", "'char'", "'void'", 
                     "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'<<'", "'>>'", "'&'", "'|'", "'^'", "'~'", "'&&'", 
                     "'||'", "'!'", "':'", "';'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "PLUS", "MINUS", "MULT", "DIV", "MOD", "GREATER_THAN", 
                      "LESS_THAN", "GREATER_EQUAL", "LESS_EQUAL", "EQUALS", 
                      "NOT_EQUAL", "SHIFT_LEFT", "SHIFT_RIGHT", "BITWISE_AND", 
                      "BITWISE_OR", "BITWISE_XOR", "BITWISE_NOT", "LOGICAL_AND", 
                      "LOGICAL_OR", "LOGICAL_NOT", "COLON", "SEMICOLON", 
                      "COMMA", "INT", "FLOAT", "CHAR", "WHITESPACE", "IDENTIFIER", 
                      "INCREMENT", "DECREMENT", "COMMENT", "BLOCKCOMMENT", 
                      "LINECOMMENT" ]

    RULE_program = 0
    RULE_scope = 1
    RULE_statement = 2
    RULE_function = 3
    RULE_functionParams = 4
    RULE_functionCall = 5
    RULE_callParams = 6
    RULE_switchStatement = 7
    RULE_switchCase = 8
    RULE_conditional = 9
    RULE_ifStatement = 10
    RULE_elseIfStatement = 11
    RULE_elseStatement = 12
    RULE_whileLoop = 13
    RULE_forLoop = 14
    RULE_forCondition = 15
    RULE_printfStatement = 16
    RULE_formatSpecifier = 17
    RULE_variable = 18
    RULE_lvalue = 19
    RULE_rvalue = 20
    RULE_conditionalExpression = 21
    RULE_jumpStatement = 22
    RULE_unaryExpression = 23
    RULE_literal = 24
    RULE_explicitConversion = 25
    RULE_pointer = 26
    RULE_deref = 27
    RULE_addr = 28
    RULE_enumDeclaration = 29
    RULE_enumStatement = 30
    RULE_enumVariableDefinition = 31
    RULE_enumVariableDeclaration = 32
    RULE_postFixIncrement = 33
    RULE_postFixDecrement = 34
    RULE_preFixIncrement = 35
    RULE_preFixDecrement = 36
    RULE_typedef = 37
    RULE_type = 38
    RULE_identifier = 39
    RULE_comment = 40

    ruleNames =  [ "program", "scope", "statement", "function", "functionParams", 
                   "functionCall", "callParams", "switchStatement", "switchCase", 
                   "conditional", "ifStatement", "elseIfStatement", "elseStatement", 
                   "whileLoop", "forLoop", "forCondition", "printfStatement", 
                   "formatSpecifier", "variable", "lvalue", "rvalue", "conditionalExpression", 
                   "jumpStatement", "unaryExpression", "literal", "explicitConversion", 
                   "pointer", "deref", "addr", "enumDeclaration", "enumStatement", 
                   "enumVariableDefinition", "enumVariableDeclaration", 
                   "postFixIncrement", "postFixDecrement", "preFixIncrement", 
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
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    LPAREN=25
    RPAREN=26
    LBRACE=27
    RBRACE=28
    PLUS=29
    MINUS=30
    MULT=31
    DIV=32
    MOD=33
    GREATER_THAN=34
    LESS_THAN=35
    GREATER_EQUAL=36
    LESS_EQUAL=37
    EQUALS=38
    NOT_EQUAL=39
    SHIFT_LEFT=40
    SHIFT_RIGHT=41
    BITWISE_AND=42
    BITWISE_OR=43
    BITWISE_XOR=44
    BITWISE_NOT=45
    LOGICAL_AND=46
    LOGICAL_OR=47
    LOGICAL_NOT=48
    COLON=49
    SEMICOLON=50
    COMMA=51
    INT=52
    FLOAT=53
    CHAR=54
    WHITESPACE=55
    IDENTIFIER=56
    INCREMENT=57
    DECREMENT=58
    COMMENT=59
    BLOCKCOMMENT=60
    LINECOMMENT=61

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

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.CommentContext)
            else:
                return self.getTypedRuleContext(GrammarParser.CommentContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.FunctionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.FunctionContext,i)


        def enumDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.EnumDeclarationContext)
            else:
                return self.getTypedRuleContext(GrammarParser.EnumDeclarationContext,i)


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
            self.state = 102 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 82
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 83
                    self.enumDeclaration()
                    self.state = 85 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 84
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 87 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==50):
                            break

                    pass

                elif la_ == 3:
                    self.state = 89
                    self.variable()
                    self.state = 91 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 90
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 93 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==50):
                            break

                    pass

                elif la_ == 4:
                    self.state = 95
                    self.typedef()
                    self.state = 97 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 96
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 99 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==50):
                            break

                    pass

                elif la_ == 5:
                    self.state = 101
                    self.function()
                    pass


                self.state = 104 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 648518348522127360) != 0)):
                    break

            self.state = 106
            self.match(GrammarParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(GrammarParser.LBRACE)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1112710169315213778) != 0):
                self.state = 109
                self.statement()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
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


        def enumStatement(self):
            return self.getTypedRuleContext(GrammarParser.EnumStatementContext,0)


        def jumpStatement(self):
            return self.getTypedRuleContext(GrammarParser.JumpStatementContext,0)


        def function(self):
            return self.getTypedRuleContext(GrammarParser.FunctionContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(GrammarParser.SwitchStatementContext,0)


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
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.rvalue(0)
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 118
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 121 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.variable()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 124
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 127 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.printfStatement()
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 131
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 134 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 136
                self.scope()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 137
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 138
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 139
                self.forLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 140
                self.enumStatement()
                self.state = 142 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 141
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 144 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 146
                self.jumpStatement()
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 147
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 150 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 152
                self.function()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 153
                self.switchStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def scope(self):
            return self.getTypedRuleContext(GrammarParser.ScopeContext,0)


        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def pointer(self):
            return self.getTypedRuleContext(GrammarParser.PointerContext,0)


        def functionParams(self):
            return self.getTypedRuleContext(GrammarParser.FunctionParamsContext,0)


        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = GrammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 156
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 157
                    self.pointer()
                    pass


                self.state = 160
                self.match(GrammarParser.IDENTIFIER)
                self.state = 161
                self.match(GrammarParser.LPAREN)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594070433792) != 0):
                    self.state = 162
                    self.functionParams(0)


                self.state = 165
                self.match(GrammarParser.RPAREN)
                self.state = 166
                self.scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 168
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 169
                    self.pointer()
                    pass


                self.state = 172
                self.match(GrammarParser.IDENTIFIER)
                self.state = 173
                self.match(GrammarParser.LPAREN)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594070433792) != 0):
                    self.state = 174
                    self.functionParams(0)


                self.state = 177
                self.match(GrammarParser.RPAREN)
                self.state = 178
                self.match(GrammarParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pointer(self):
            return self.getTypedRuleContext(GrammarParser.PointerContext,0)


        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def addr(self):
            return self.getTypedRuleContext(GrammarParser.AddrContext,0)


        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def functionParams(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.FunctionParamsContext)
            else:
                return self.getTypedRuleContext(GrammarParser.FunctionParamsContext,i)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_functionParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParams" ):
                listener.enterFunctionParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParams" ):
                listener.exitFunctionParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionParams" ):
                return visitor.visitFunctionParams(self)
            else:
                return visitor.visitChildren(self)



    def functionParams(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.FunctionParamsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_functionParams, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 183
                self.pointer()
                pass

            elif la_ == 2:
                self.state = 184
                self.type_()
                pass


            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 187
                self.addr()
                pass
            elif token in [56]:
                self.state = 188
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.FunctionParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParams)
                    self.state = 191
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 192
                    self.match(GrammarParser.COMMA)
                    self.state = 193
                    self.functionParams(2) 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def callParams(self):
            return self.getTypedRuleContext(GrammarParser.CallParamsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = GrammarParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(GrammarParser.IDENTIFIER)
            self.state = 200
            self.match(GrammarParser.LPAREN)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536249416876785664) != 0):
                self.state = 201
                self.callParams(0)


            self.state = 204
            self.match(GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def callParams(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.CallParamsContext)
            else:
                return self.getTypedRuleContext(GrammarParser.CallParamsContext,i)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_callParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallParams" ):
                listener.enterCallParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallParams" ):
                listener.exitCallParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallParams" ):
                return visitor.visitCallParams(self)
            else:
                return visitor.visitChildren(self)



    def callParams(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.CallParamsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_callParams, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.rvalue(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CallParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callParams)
                    self.state = 209
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 210
                    self.match(GrammarParser.COMMA)
                    self.state = 211
                    self.callParams(2) 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SwitchStatementContext(ParserRuleContext):
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

        def LBRACE(self):
            return self.getToken(GrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GrammarParser.RBRACE, 0)

        def switchCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.SwitchCaseContext)
            else:
                return self.getTypedRuleContext(GrammarParser.SwitchCaseContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = GrammarParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(GrammarParser.T__0)
            self.state = 218
            self.match(GrammarParser.LPAREN)
            self.state = 219
            self.rvalue(0)
            self.state = 220
            self.match(GrammarParser.RPAREN)
            self.state = 221
            self.match(GrammarParser.LBRACE)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 222
                self.switchCase()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self.match(GrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(GrammarParser.LiteralContext,0)


        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_switchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchCase" ):
                listener.enterSwitchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchCase" ):
                listener.exitSwitchCase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchCase" ):
                return visitor.visitSwitchCase(self)
            else:
                return visitor.visitChildren(self)




    def switchCase(self):

        localctx = GrammarParser.SwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_switchCase)
        self._la = 0 # Token type
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(GrammarParser.T__1)
                self.state = 231
                self.literal()
                self.state = 232
                self.match(GrammarParser.COLON)
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1112710169315213778) != 0):
                    self.state = 233
                    self.statement()
                    self.state = 238
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(GrammarParser.T__2)
                self.state = 240
                self.match(GrammarParser.COLON)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1112710169315213778) != 0):
                    self.state = 241
                    self.statement()
                    self.state = 246
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
        self.enterRule(localctx, 18, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.ifStatement()
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 250
                    self.elseIfStatement() 
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 256
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
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(GrammarParser.T__3)
            self.state = 260
            self.match(GrammarParser.LPAREN)
            self.state = 261
            self.rvalue(0)
            self.state = 262
            self.match(GrammarParser.RPAREN)
            self.state = 263
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
        self.enterRule(localctx, 22, self.RULE_elseIfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(GrammarParser.T__4)
            self.state = 266
            self.match(GrammarParser.T__3)
            self.state = 267
            self.match(GrammarParser.LPAREN)
            self.state = 268
            self.rvalue(0)
            self.state = 269
            self.match(GrammarParser.RPAREN)
            self.state = 270
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
        self.enterRule(localctx, 24, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(GrammarParser.T__4)
            self.state = 273
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
        self.enterRule(localctx, 26, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(GrammarParser.T__5)
            self.state = 276
            self.match(GrammarParser.LPAREN)
            self.state = 277
            self.rvalue(0)
            self.state = 278
            self.match(GrammarParser.RPAREN)
            self.state = 279
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
        self.enterRule(localctx, 28, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(GrammarParser.T__6)
            self.state = 282
            self.match(GrammarParser.LPAREN)
            self.state = 283
            self.forCondition()
            self.state = 284
            self.match(GrammarParser.RPAREN)
            self.state = 285
            self.scope()
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
        self.enterRule(localctx, 30, self.RULE_forCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057596218441728) != 0):
                self.state = 287
                self.variable()


            self.state = 290
            self.match(GrammarParser.SEMICOLON)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536249416876785664) != 0):
                self.state = 291
                self.rvalue(0)


            self.state = 294
            self.match(GrammarParser.SEMICOLON)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536249416876785664) != 0):
                self.state = 295
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


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

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
        self.enterRule(localctx, 32, self.RULE_printfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(GrammarParser.T__7)
            self.state = 299
            self.match(GrammarParser.LPAREN)
            self.state = 300
            self.formatSpecifier()
            self.state = 301
            self.match(GrammarParser.COMMA)
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.state = 302
                self.identifier()
                pass
            elif token in [52, 53, 54]:
                self.state = 303
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 306
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
        self.enterRule(localctx, 34, self.RULE_formatSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
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
        self.enterRule(localctx, 36, self.RULE_variable)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.lvalue()
                self.state = 311
                self.match(GrammarParser.T__13)
                self.state = 312
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.lvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
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
        self.enterRule(localctx, 38, self.RULE_lvalue)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.type_()
                self.state = 320
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.pointer()
                self.state = 323
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 325
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


        def functionCall(self):
            return self.getTypedRuleContext(GrammarParser.FunctionCallContext,0)


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

        def LOGICAL_AND(self):
            return self.getToken(GrammarParser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(GrammarParser.LOGICAL_OR, 0)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 329
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 330
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 331
                self.deref()
                pass

            elif la_ == 4:
                self.state = 332
                self.addr()
                pass

            elif la_ == 5:
                self.state = 333
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 334
                self.rvalue(23)
                pass

            elif la_ == 6:
                self.state = 335
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 336
                self.rvalue(22)
                pass

            elif la_ == 7:
                self.state = 337
                self.match(GrammarParser.LPAREN)
                self.state = 338
                self.rvalue(0)
                self.state = 339
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 341
                self.explicitConversion()
                pass

            elif la_ == 9:
                self.state = 342
                self.postFixIncrement()
                pass

            elif la_ == 10:
                self.state = 343
                self.postFixDecrement()
                pass

            elif la_ == 11:
                self.state = 344
                self.preFixIncrement()
                pass

            elif la_ == 12:
                self.state = 345
                self.preFixDecrement()
                pass

            elif la_ == 13:
                self.state = 346
                self.functionCall()
                pass

            elif la_ == 14:
                self.state = 347
                self.jumpStatement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 388
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 350
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 351
                        self.match(GrammarParser.DIV)
                        self.state = 352
                        self.rvalue(22)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 353
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 354
                        self.match(GrammarParser.MOD)
                        self.state = 355
                        self.rvalue(21)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 356
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 357
                        self.match(GrammarParser.MULT)
                        self.state = 358
                        self.rvalue(20)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 359
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 360
                        self.match(GrammarParser.MINUS)
                        self.state = 361
                        self.rvalue(19)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 362
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 363
                        self.match(GrammarParser.PLUS)
                        self.state = 364
                        self.rvalue(18)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 365
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 366
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 367
                        self.rvalue(17)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 368
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 369
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 370
                        self.rvalue(16)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 371
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 372
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 373
                        self.rvalue(15)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 374
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 375
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 376
                        self.rvalue(14)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 377
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 378
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 379
                        self.rvalue(13)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 380
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 381
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 382
                        self.rvalue(12)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 383
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 384
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 385
                        self.rvalue(11)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 386
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 387
                        self.conditionalExpression()
                        pass

             
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_conditionalExpression)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(GrammarParser.GREATER_THAN)
                self.state = 394
                self.rvalue(0)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(GrammarParser.LESS_THAN)
                self.state = 396
                self.rvalue(0)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 397
                self.match(GrammarParser.GREATER_EQUAL)
                self.state = 398
                self.rvalue(0)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 399
                self.match(GrammarParser.LESS_EQUAL)
                self.state = 400
                self.rvalue(0)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 5)
                self.state = 401
                self.match(GrammarParser.EQUALS)
                self.state = 402
                self.rvalue(0)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 403
                self.match(GrammarParser.NOT_EQUAL)
                self.state = 404
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

        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


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
        self.enterRule(localctx, 44, self.RULE_jumpStatement)
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(GrammarParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(GrammarParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.match(GrammarParser.T__16)
                self.state = 411
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 410
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


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(GrammarParser.LiteralContext,0)


        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def deref(self):
            return self.getTypedRuleContext(GrammarParser.DerefContext,0)


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
        self.enterRule(localctx, 46, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29 or _la==30:
                    self.state = 415
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 421
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 418
                    self.literal()
                    pass
                elif token in [56]:
                    self.state = 419
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 420
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 423
                        self.match(GrammarParser.PLUS)
                        self.state = 424
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 427 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                self.state = 430
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 429
                    self.match(GrammarParser.PLUS)


                self.state = 435
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 432
                    self.literal()
                    pass
                elif token in [56]:
                    self.state = 433
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 434
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 439 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 437
                        self.match(GrammarParser.MINUS)
                        self.state = 438
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 441 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 443
                    self.match(GrammarParser.MINUS)


                self.state = 449
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 446
                    self.literal()
                    pass
                elif token in [56]:
                    self.state = 447
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 448
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

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
        self.enterRule(localctx, 48, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31525197391593472) != 0)):
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
        self.enterRule(localctx, 50, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 455
                self.match(GrammarParser.LPAREN)
                self.state = 458 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 461 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 460
                self.type_()
                self.state = 463 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594070433792) != 0)):
                    break

            self.state = 465
            self.match(GrammarParser.RPAREN)
            self.state = 466
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
        self.enterRule(localctx, 52, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.type_()
            self.state = 470 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 469
                self.match(GrammarParser.MULT)
                self.state = 472 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
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
        self.enterRule(localctx, 54, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 474
                self.match(GrammarParser.MULT)
                self.state = 477 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 479
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
        self.enterRule(localctx, 56, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 481
                self.match(GrammarParser.BITWISE_AND)
                self.state = 484 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 486
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENTIFIER)
            else:
                return self.getToken(GrammarParser.IDENTIFIER, i)

        def LBRACE(self):
            return self.getToken(GrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GrammarParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_enumDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDeclaration" ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDeclaration" ):
                listener.exitEnumDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDeclaration" ):
                return visitor.visitEnumDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def enumDeclaration(self):

        localctx = GrammarParser.EnumDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(GrammarParser.T__17)
            self.state = 489
            self.match(GrammarParser.IDENTIFIER)
            self.state = 490
            self.match(GrammarParser.LBRACE)
            self.state = 491
            self.match(GrammarParser.IDENTIFIER)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 492
                self.match(GrammarParser.COMMA)
                self.state = 493
                self.match(GrammarParser.IDENTIFIER)
                self.state = 498
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 499
            self.match(GrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumVariableDefinition(self):
            return self.getTypedRuleContext(GrammarParser.EnumVariableDefinitionContext,0)


        def enumVariableDeclaration(self):
            return self.getTypedRuleContext(GrammarParser.EnumVariableDeclarationContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_enumStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumStatement" ):
                listener.enterEnumStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumStatement" ):
                listener.exitEnumStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumStatement" ):
                return visitor.visitEnumStatement(self)
            else:
                return visitor.visitChildren(self)




    def enumStatement(self):

        localctx = GrammarParser.EnumStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_enumStatement)
        try:
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.enumVariableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.enumVariableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumVariableDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENTIFIER)
            else:
                return self.getToken(GrammarParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_enumVariableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumVariableDefinition" ):
                listener.enterEnumVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumVariableDefinition" ):
                listener.exitEnumVariableDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumVariableDefinition" ):
                return visitor.visitEnumVariableDefinition(self)
            else:
                return visitor.visitChildren(self)




    def enumVariableDefinition(self):

        localctx = GrammarParser.EnumVariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_enumVariableDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(GrammarParser.T__17)
            self.state = 506
            self.match(GrammarParser.IDENTIFIER)
            self.state = 507
            self.match(GrammarParser.IDENTIFIER)
            self.state = 508
            self.match(GrammarParser.T__13)
            self.state = 509
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumVariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENTIFIER)
            else:
                return self.getToken(GrammarParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_enumVariableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumVariableDeclaration" ):
                listener.enterEnumVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumVariableDeclaration" ):
                listener.exitEnumVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumVariableDeclaration" ):
                return visitor.visitEnumVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def enumVariableDeclaration(self):

        localctx = GrammarParser.EnumVariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_enumVariableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(GrammarParser.T__17)
            self.state = 512
            self.match(GrammarParser.IDENTIFIER)
            self.state = 513
            self.match(GrammarParser.IDENTIFIER)
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
        self.enterRule(localctx, 66, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.lvalue()
            self.state = 516
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
        self.enterRule(localctx, 68, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.lvalue()
            self.state = 519
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
        self.enterRule(localctx, 70, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(GrammarParser.INCREMENT)
            self.state = 522
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
        self.enterRule(localctx, 72, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(GrammarParser.DECREMENT)
            self.state = 525
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
        self.enterRule(localctx, 74, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(GrammarParser.T__18)
            self.state = 528
            self.type_()
            self.state = 529
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
        self.enterRule(localctx, 76, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 531
                self.match(GrammarParser.T__19)
                self.state = 536
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 537
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594069385216) != 0)):
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
        self.enterRule(localctx, 78, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
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
        self.enterRule(localctx, 80, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
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
        self._predicates[4] = self.functionParams_sempred
        self._predicates[6] = self.callParams_sempred
        self._predicates[20] = self.rvalue_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def functionParams_sempred(self, localctx:FunctionParamsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def callParams_sempred(self, localctx:CallParamsContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def rvalue_sempred(self, localctx:RvalueContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 3)
         




