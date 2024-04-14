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
        4,1,61,517,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,4,0,80,
        8,0,11,0,12,0,81,1,0,1,0,4,0,86,8,0,11,0,12,0,87,1,0,1,0,4,0,92,
        8,0,11,0,12,0,93,1,0,4,0,97,8,0,11,0,12,0,98,1,0,1,0,1,1,1,1,5,1,
        105,8,1,10,1,12,1,108,9,1,1,1,1,1,1,2,1,2,4,2,114,8,2,11,2,12,2,
        115,1,2,1,2,4,2,120,8,2,11,2,12,2,121,1,2,1,2,1,2,4,2,127,8,2,11,
        2,12,2,128,1,2,1,2,1,2,1,2,1,2,1,2,4,2,137,8,2,11,2,12,2,138,1,2,
        3,2,142,8,2,1,3,1,3,3,3,146,8,3,1,3,1,3,1,3,3,3,151,8,3,1,3,1,3,
        1,3,1,3,1,3,3,3,158,8,3,1,3,1,3,1,3,3,3,163,8,3,1,3,1,3,1,3,3,3,
        168,8,3,1,4,1,4,1,4,3,4,173,8,4,1,4,1,4,3,4,177,8,4,1,4,1,4,1,4,
        5,4,182,8,4,10,4,12,4,185,9,4,1,5,1,5,1,5,3,5,190,8,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,5,6,200,8,6,10,6,12,6,203,9,6,1,7,1,7,1,7,
        1,7,1,7,1,7,5,7,211,8,7,10,7,12,7,214,9,7,1,7,1,7,1,8,1,8,1,8,1,
        8,5,8,222,8,8,10,8,12,8,225,9,8,1,8,1,8,1,8,5,8,230,8,8,10,8,12,
        8,233,9,8,3,8,235,8,8,1,9,1,9,5,9,239,8,9,10,9,12,9,242,9,9,1,9,
        3,9,245,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,14,1,14,1,15,3,15,276,8,15,1,15,1,15,3,15,280,8,15,
        1,15,1,15,3,15,284,8,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,292,8,
        16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,304,8,
        18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,314,8,19,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,3,20,336,8,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,5,20,376,8,20,10,20,12,20,
        379,9,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,3,21,393,8,21,1,22,1,22,1,22,1,22,3,22,399,8,22,3,22,401,8,
        22,1,23,3,23,404,8,23,1,23,1,23,1,23,3,23,409,8,23,1,23,1,23,4,23,
        413,8,23,11,23,12,23,414,1,23,3,23,418,8,23,1,23,1,23,1,23,3,23,
        423,8,23,1,23,1,23,4,23,427,8,23,11,23,12,23,428,1,23,3,23,432,8,
        23,1,23,1,23,1,23,3,23,437,8,23,3,23,439,8,23,1,24,1,24,1,25,4,25,
        444,8,25,11,25,12,25,445,1,25,4,25,449,8,25,11,25,12,25,450,1,25,
        1,25,1,25,1,26,1,26,4,26,458,8,26,11,26,12,26,459,1,27,4,27,463,
        8,27,11,27,12,27,464,1,27,1,27,1,28,4,28,470,8,28,11,28,12,28,471,
        1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,482,8,29,10,29,12,29,
        485,9,29,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,
        1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,5,35,506,8,35,10,35,12,35,
        509,9,35,1,35,1,35,1,36,1,36,1,37,1,37,1,37,0,3,8,12,40,38,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,0,4,1,0,9,13,1,0,29,30,1,
        0,52,54,2,0,21,24,56,56,579,0,96,1,0,0,0,2,102,1,0,0,0,4,141,1,0,
        0,0,6,167,1,0,0,0,8,169,1,0,0,0,10,186,1,0,0,0,12,193,1,0,0,0,14,
        204,1,0,0,0,16,234,1,0,0,0,18,236,1,0,0,0,20,246,1,0,0,0,22,252,
        1,0,0,0,24,259,1,0,0,0,26,262,1,0,0,0,28,268,1,0,0,0,30,275,1,0,
        0,0,32,285,1,0,0,0,34,295,1,0,0,0,36,303,1,0,0,0,38,313,1,0,0,0,
        40,335,1,0,0,0,42,392,1,0,0,0,44,400,1,0,0,0,46,438,1,0,0,0,48,440,
        1,0,0,0,50,443,1,0,0,0,52,455,1,0,0,0,54,462,1,0,0,0,56,469,1,0,
        0,0,58,475,1,0,0,0,60,488,1,0,0,0,62,491,1,0,0,0,64,494,1,0,0,0,
        66,497,1,0,0,0,68,500,1,0,0,0,70,507,1,0,0,0,72,512,1,0,0,0,74,514,
        1,0,0,0,76,97,3,74,37,0,77,79,3,58,29,0,78,80,5,50,0,0,79,78,1,0,
        0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,97,1,0,0,0,83,85,
        3,36,18,0,84,86,5,50,0,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,
        0,87,88,1,0,0,0,88,97,1,0,0,0,89,91,3,68,34,0,90,92,5,50,0,0,91,
        90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,97,1,0,0,
        0,95,97,3,6,3,0,96,76,1,0,0,0,96,77,1,0,0,0,96,83,1,0,0,0,96,89,
        1,0,0,0,96,95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,
        99,100,1,0,0,0,100,101,5,0,0,1,101,1,1,0,0,0,102,106,5,27,0,0,103,
        105,3,4,2,0,104,103,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,
        107,1,0,0,0,107,109,1,0,0,0,108,106,1,0,0,0,109,110,5,28,0,0,110,
        3,1,0,0,0,111,113,3,40,20,0,112,114,5,50,0,0,113,112,1,0,0,0,114,
        115,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,142,1,0,0,0,117,
        119,3,36,18,0,118,120,5,50,0,0,119,118,1,0,0,0,120,121,1,0,0,0,121,
        119,1,0,0,0,121,122,1,0,0,0,122,142,1,0,0,0,123,142,3,74,37,0,124,
        126,3,32,16,0,125,127,5,50,0,0,126,125,1,0,0,0,127,128,1,0,0,0,128,
        126,1,0,0,0,128,129,1,0,0,0,129,142,1,0,0,0,130,142,3,2,1,0,131,
        142,3,18,9,0,132,142,3,26,13,0,133,142,3,28,14,0,134,136,3,44,22,
        0,135,137,5,50,0,0,136,135,1,0,0,0,137,138,1,0,0,0,138,136,1,0,0,
        0,138,139,1,0,0,0,139,142,1,0,0,0,140,142,3,14,7,0,141,111,1,0,0,
        0,141,117,1,0,0,0,141,123,1,0,0,0,141,124,1,0,0,0,141,130,1,0,0,
        0,141,131,1,0,0,0,141,132,1,0,0,0,141,133,1,0,0,0,141,134,1,0,0,
        0,141,140,1,0,0,0,142,5,1,0,0,0,143,146,3,70,35,0,144,146,3,52,26,
        0,145,143,1,0,0,0,145,144,1,0,0,0,146,147,1,0,0,0,147,148,5,56,0,
        0,148,150,5,25,0,0,149,151,3,8,4,0,150,149,1,0,0,0,150,151,1,0,0,
        0,151,152,1,0,0,0,152,153,5,26,0,0,153,154,3,2,1,0,154,168,1,0,0,
        0,155,158,3,70,35,0,156,158,3,52,26,0,157,155,1,0,0,0,157,156,1,
        0,0,0,158,159,1,0,0,0,159,160,5,56,0,0,160,162,5,25,0,0,161,163,
        3,8,4,0,162,161,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,
        5,26,0,0,165,166,5,50,0,0,166,168,1,0,0,0,167,145,1,0,0,0,167,157,
        1,0,0,0,168,7,1,0,0,0,169,172,6,4,-1,0,170,173,3,52,26,0,171,173,
        3,70,35,0,172,170,1,0,0,0,172,171,1,0,0,0,173,176,1,0,0,0,174,177,
        3,56,28,0,175,177,3,72,36,0,176,174,1,0,0,0,176,175,1,0,0,0,177,
        183,1,0,0,0,178,179,10,1,0,0,179,180,5,51,0,0,180,182,3,8,4,2,181,
        178,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,
        9,1,0,0,0,185,183,1,0,0,0,186,187,5,56,0,0,187,189,5,25,0,0,188,
        190,3,12,6,0,189,188,1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,191,
        192,5,26,0,0,192,11,1,0,0,0,193,194,6,6,-1,0,194,195,3,40,20,0,195,
        201,1,0,0,0,196,197,10,1,0,0,197,198,5,51,0,0,198,200,3,12,6,2,199,
        196,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,
        13,1,0,0,0,203,201,1,0,0,0,204,205,5,1,0,0,205,206,5,25,0,0,206,
        207,3,40,20,0,207,208,5,26,0,0,208,212,5,27,0,0,209,211,3,16,8,0,
        210,209,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,
        213,215,1,0,0,0,214,212,1,0,0,0,215,216,5,28,0,0,216,15,1,0,0,0,
        217,218,5,2,0,0,218,219,3,48,24,0,219,223,5,49,0,0,220,222,3,4,2,
        0,221,220,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,
        0,224,235,1,0,0,0,225,223,1,0,0,0,226,227,5,3,0,0,227,231,5,49,0,
        0,228,230,3,4,2,0,229,228,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,
        0,231,232,1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,234,217,1,0,0,
        0,234,226,1,0,0,0,235,17,1,0,0,0,236,240,3,20,10,0,237,239,3,22,
        11,0,238,237,1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,240,241,1,0,
        0,0,241,244,1,0,0,0,242,240,1,0,0,0,243,245,3,24,12,0,244,243,1,
        0,0,0,244,245,1,0,0,0,245,19,1,0,0,0,246,247,5,4,0,0,247,248,5,25,
        0,0,248,249,3,40,20,0,249,250,5,26,0,0,250,251,3,2,1,0,251,21,1,
        0,0,0,252,253,5,5,0,0,253,254,5,4,0,0,254,255,5,25,0,0,255,256,3,
        40,20,0,256,257,5,26,0,0,257,258,3,2,1,0,258,23,1,0,0,0,259,260,
        5,5,0,0,260,261,3,2,1,0,261,25,1,0,0,0,262,263,5,6,0,0,263,264,5,
        25,0,0,264,265,3,40,20,0,265,266,5,26,0,0,266,267,3,2,1,0,267,27,
        1,0,0,0,268,269,5,7,0,0,269,270,5,25,0,0,270,271,3,30,15,0,271,272,
        5,26,0,0,272,273,3,2,1,0,273,29,1,0,0,0,274,276,3,36,18,0,275,274,
        1,0,0,0,275,276,1,0,0,0,276,277,1,0,0,0,277,279,5,50,0,0,278,280,
        3,40,20,0,279,278,1,0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,283,
        5,50,0,0,282,284,3,40,20,0,283,282,1,0,0,0,283,284,1,0,0,0,284,31,
        1,0,0,0,285,286,5,8,0,0,286,287,5,25,0,0,287,288,3,34,17,0,288,291,
        5,51,0,0,289,292,3,72,36,0,290,292,3,48,24,0,291,289,1,0,0,0,291,
        290,1,0,0,0,292,293,1,0,0,0,293,294,5,26,0,0,294,33,1,0,0,0,295,
        296,7,0,0,0,296,35,1,0,0,0,297,298,3,38,19,0,298,299,5,14,0,0,299,
        300,3,40,20,0,300,304,1,0,0,0,301,304,3,38,19,0,302,304,3,68,34,
        0,303,297,1,0,0,0,303,301,1,0,0,0,303,302,1,0,0,0,304,37,1,0,0,0,
        305,314,3,72,36,0,306,307,3,70,35,0,307,308,3,72,36,0,308,314,1,
        0,0,0,309,310,3,52,26,0,310,311,3,72,36,0,311,314,1,0,0,0,312,314,
        3,54,27,0,313,305,1,0,0,0,313,306,1,0,0,0,313,309,1,0,0,0,313,312,
        1,0,0,0,314,39,1,0,0,0,315,316,6,20,-1,0,316,336,3,46,23,0,317,336,
        3,72,36,0,318,336,3,54,27,0,319,336,3,56,28,0,320,321,5,48,0,0,321,
        336,3,40,20,23,322,323,5,45,0,0,323,336,3,40,20,22,324,325,5,25,
        0,0,325,326,3,40,20,0,326,327,5,26,0,0,327,336,1,0,0,0,328,336,3,
        50,25,0,329,336,3,60,30,0,330,336,3,62,31,0,331,336,3,64,32,0,332,
        336,3,66,33,0,333,336,3,10,5,0,334,336,3,44,22,0,335,315,1,0,0,0,
        335,317,1,0,0,0,335,318,1,0,0,0,335,319,1,0,0,0,335,320,1,0,0,0,
        335,322,1,0,0,0,335,324,1,0,0,0,335,328,1,0,0,0,335,329,1,0,0,0,
        335,330,1,0,0,0,335,331,1,0,0,0,335,332,1,0,0,0,335,333,1,0,0,0,
        335,334,1,0,0,0,336,377,1,0,0,0,337,338,10,21,0,0,338,339,5,32,0,
        0,339,376,3,40,20,22,340,341,10,20,0,0,341,342,5,33,0,0,342,376,
        3,40,20,21,343,344,10,19,0,0,344,345,5,31,0,0,345,376,3,40,20,20,
        346,347,10,18,0,0,347,348,5,30,0,0,348,376,3,40,20,19,349,350,10,
        17,0,0,350,351,5,29,0,0,351,376,3,40,20,18,352,353,10,16,0,0,353,
        354,5,40,0,0,354,376,3,40,20,17,355,356,10,15,0,0,356,357,5,41,0,
        0,357,376,3,40,20,16,358,359,10,14,0,0,359,360,5,42,0,0,360,376,
        3,40,20,15,361,362,10,13,0,0,362,363,5,43,0,0,363,376,3,40,20,14,
        364,365,10,12,0,0,365,366,5,44,0,0,366,376,3,40,20,13,367,368,10,
        11,0,0,368,369,5,46,0,0,369,376,3,40,20,12,370,371,10,10,0,0,371,
        372,5,47,0,0,372,376,3,40,20,11,373,374,10,3,0,0,374,376,3,42,21,
        0,375,337,1,0,0,0,375,340,1,0,0,0,375,343,1,0,0,0,375,346,1,0,0,
        0,375,349,1,0,0,0,375,352,1,0,0,0,375,355,1,0,0,0,375,358,1,0,0,
        0,375,361,1,0,0,0,375,364,1,0,0,0,375,367,1,0,0,0,375,370,1,0,0,
        0,375,373,1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,0,377,378,1,0,0,
        0,378,41,1,0,0,0,379,377,1,0,0,0,380,381,5,34,0,0,381,393,3,40,20,
        0,382,383,5,35,0,0,383,393,3,40,20,0,384,385,5,36,0,0,385,393,3,
        40,20,0,386,387,5,37,0,0,387,393,3,40,20,0,388,389,5,38,0,0,389,
        393,3,40,20,0,390,391,5,39,0,0,391,393,3,40,20,0,392,380,1,0,0,0,
        392,382,1,0,0,0,392,384,1,0,0,0,392,386,1,0,0,0,392,388,1,0,0,0,
        392,390,1,0,0,0,393,43,1,0,0,0,394,401,5,15,0,0,395,401,5,16,0,0,
        396,398,5,17,0,0,397,399,3,40,20,0,398,397,1,0,0,0,398,399,1,0,0,
        0,399,401,1,0,0,0,400,394,1,0,0,0,400,395,1,0,0,0,400,396,1,0,0,
        0,401,45,1,0,0,0,402,404,7,1,0,0,403,402,1,0,0,0,403,404,1,0,0,0,
        404,408,1,0,0,0,405,409,3,48,24,0,406,409,3,72,36,0,407,409,3,54,
        27,0,408,405,1,0,0,0,408,406,1,0,0,0,408,407,1,0,0,0,409,439,1,0,
        0,0,410,411,5,29,0,0,411,413,5,30,0,0,412,410,1,0,0,0,413,414,1,
        0,0,0,414,412,1,0,0,0,414,415,1,0,0,0,415,417,1,0,0,0,416,418,5,
        29,0,0,417,416,1,0,0,0,417,418,1,0,0,0,418,422,1,0,0,0,419,423,3,
        48,24,0,420,423,3,72,36,0,421,423,3,54,27,0,422,419,1,0,0,0,422,
        420,1,0,0,0,422,421,1,0,0,0,423,439,1,0,0,0,424,425,5,30,0,0,425,
        427,5,29,0,0,426,424,1,0,0,0,427,428,1,0,0,0,428,426,1,0,0,0,428,
        429,1,0,0,0,429,431,1,0,0,0,430,432,5,30,0,0,431,430,1,0,0,0,431,
        432,1,0,0,0,432,436,1,0,0,0,433,437,3,48,24,0,434,437,3,72,36,0,
        435,437,3,54,27,0,436,433,1,0,0,0,436,434,1,0,0,0,436,435,1,0,0,
        0,437,439,1,0,0,0,438,403,1,0,0,0,438,412,1,0,0,0,438,426,1,0,0,
        0,439,47,1,0,0,0,440,441,7,2,0,0,441,49,1,0,0,0,442,444,5,25,0,0,
        443,442,1,0,0,0,444,445,1,0,0,0,445,443,1,0,0,0,445,446,1,0,0,0,
        446,448,1,0,0,0,447,449,3,70,35,0,448,447,1,0,0,0,449,450,1,0,0,
        0,450,448,1,0,0,0,450,451,1,0,0,0,451,452,1,0,0,0,452,453,5,26,0,
        0,453,454,3,40,20,0,454,51,1,0,0,0,455,457,3,70,35,0,456,458,5,31,
        0,0,457,456,1,0,0,0,458,459,1,0,0,0,459,457,1,0,0,0,459,460,1,0,
        0,0,460,53,1,0,0,0,461,463,5,31,0,0,462,461,1,0,0,0,463,464,1,0,
        0,0,464,462,1,0,0,0,464,465,1,0,0,0,465,466,1,0,0,0,466,467,3,72,
        36,0,467,55,1,0,0,0,468,470,5,42,0,0,469,468,1,0,0,0,470,471,1,0,
        0,0,471,469,1,0,0,0,471,472,1,0,0,0,472,473,1,0,0,0,473,474,3,72,
        36,0,474,57,1,0,0,0,475,476,5,18,0,0,476,477,5,56,0,0,477,478,5,
        27,0,0,478,483,5,56,0,0,479,480,5,51,0,0,480,482,5,56,0,0,481,479,
        1,0,0,0,482,485,1,0,0,0,483,481,1,0,0,0,483,484,1,0,0,0,484,486,
        1,0,0,0,485,483,1,0,0,0,486,487,5,28,0,0,487,59,1,0,0,0,488,489,
        3,38,19,0,489,490,5,57,0,0,490,61,1,0,0,0,491,492,3,38,19,0,492,
        493,5,58,0,0,493,63,1,0,0,0,494,495,5,57,0,0,495,496,3,38,19,0,496,
        65,1,0,0,0,497,498,5,58,0,0,498,499,3,38,19,0,499,67,1,0,0,0,500,
        501,5,19,0,0,501,502,3,70,35,0,502,503,5,56,0,0,503,69,1,0,0,0,504,
        506,5,20,0,0,505,504,1,0,0,0,506,509,1,0,0,0,507,505,1,0,0,0,507,
        508,1,0,0,0,508,510,1,0,0,0,509,507,1,0,0,0,510,511,7,3,0,0,511,
        71,1,0,0,0,512,513,5,56,0,0,513,73,1,0,0,0,514,515,5,59,0,0,515,
        75,1,0,0,0,55,81,87,93,96,98,106,115,121,128,138,141,145,150,157,
        162,167,172,176,183,189,201,212,223,231,234,240,244,275,279,283,
        291,303,313,335,375,377,392,398,400,403,408,414,417,422,428,431,
        436,438,445,450,459,464,471,483,507
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
    RULE_enum = 29
    RULE_postFixIncrement = 30
    RULE_postFixDecrement = 31
    RULE_preFixIncrement = 32
    RULE_preFixDecrement = 33
    RULE_typedef = 34
    RULE_type = 35
    RULE_identifier = 36
    RULE_comment = 37

    ruleNames =  [ "program", "scope", "statement", "function", "functionParams", 
                   "functionCall", "callParams", "switchStatement", "switchCase", 
                   "conditional", "ifStatement", "elseIfStatement", "elseStatement", 
                   "whileLoop", "forLoop", "forCondition", "printfStatement", 
                   "formatSpecifier", "variable", "lvalue", "rvalue", "conditionalExpression", 
                   "jumpStatement", "unaryExpression", "literal", "explicitConversion", 
                   "pointer", "deref", "addr", "enum", "postFixIncrement", 
                   "postFixDecrement", "preFixIncrement", "preFixDecrement", 
                   "typedef", "type", "identifier", "comment" ]

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


        def enum(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.EnumContext)
            else:
                return self.getTypedRuleContext(GrammarParser.EnumContext,i)


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
            self.state = 96 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 76
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 77
                    self.enum()
                    self.state = 79 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 78
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 81 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==50):
                            break

                    pass

                elif la_ == 3:
                    self.state = 83
                    self.variable()
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

                elif la_ == 4:
                    self.state = 89
                    self.typedef()
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

                elif la_ == 5:
                    self.state = 95
                    self.function()
                    pass


                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 648518348522127360) != 0)):
                    break

            self.state = 100
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
            self.state = 102
            self.match(GrammarParser.LBRACE)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1112710169314951634) != 0):
                self.state = 103
                self.statement()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.rvalue(0)
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 112
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 115 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.variable()
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

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 124
                self.printfStatement()
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 125
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 128 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.scope()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 131
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 132
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 133
                self.forLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 134
                self.jumpStatement()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 135
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 138 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 140
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
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 143
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 144
                    self.pointer()
                    pass


                self.state = 147
                self.match(GrammarParser.IDENTIFIER)
                self.state = 148
                self.match(GrammarParser.LPAREN)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594070433792) != 0):
                    self.state = 149
                    self.functionParams(0)


                self.state = 152
                self.match(GrammarParser.RPAREN)
                self.state = 153
                self.scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 155
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 156
                    self.pointer()
                    pass


                self.state = 159
                self.match(GrammarParser.IDENTIFIER)
                self.state = 160
                self.match(GrammarParser.LPAREN)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594070433792) != 0):
                    self.state = 161
                    self.functionParams(0)


                self.state = 164
                self.match(GrammarParser.RPAREN)
                self.state = 165
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
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 170
                self.pointer()
                pass

            elif la_ == 2:
                self.state = 171
                self.type_()
                pass


            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 174
                self.addr()
                pass
            elif token in [56]:
                self.state = 175
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.FunctionParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParams)
                    self.state = 178
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 179
                    self.match(GrammarParser.COMMA)
                    self.state = 180
                    self.functionParams(2) 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
            self.state = 186
            self.match(GrammarParser.IDENTIFIER)
            self.state = 187
            self.match(GrammarParser.LPAREN)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536249416876785664) != 0):
                self.state = 188
                self.callParams(0)


            self.state = 191
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
            self.state = 194
            self.rvalue(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CallParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callParams)
                    self.state = 196
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 197
                    self.match(GrammarParser.COMMA)
                    self.state = 198
                    self.callParams(2) 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 204
            self.match(GrammarParser.T__0)
            self.state = 205
            self.match(GrammarParser.LPAREN)
            self.state = 206
            self.rvalue(0)
            self.state = 207
            self.match(GrammarParser.RPAREN)
            self.state = 208
            self.match(GrammarParser.LBRACE)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 209
                self.switchCase()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 215
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
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(GrammarParser.T__1)
                self.state = 218
                self.literal()
                self.state = 219
                self.match(GrammarParser.COLON)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1112710169314951634) != 0):
                    self.state = 220
                    self.statement()
                    self.state = 225
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(GrammarParser.T__2)
                self.state = 227
                self.match(GrammarParser.COLON)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1112710169314951634) != 0):
                    self.state = 228
                    self.statement()
                    self.state = 233
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
            self.state = 236
            self.ifStatement()
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 237
                    self.elseIfStatement() 
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 243
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
            self.state = 246
            self.match(GrammarParser.T__3)
            self.state = 247
            self.match(GrammarParser.LPAREN)
            self.state = 248
            self.rvalue(0)
            self.state = 249
            self.match(GrammarParser.RPAREN)
            self.state = 250
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
            self.state = 252
            self.match(GrammarParser.T__4)
            self.state = 253
            self.match(GrammarParser.T__3)
            self.state = 254
            self.match(GrammarParser.LPAREN)
            self.state = 255
            self.rvalue(0)
            self.state = 256
            self.match(GrammarParser.RPAREN)
            self.state = 257
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
            self.state = 259
            self.match(GrammarParser.T__4)
            self.state = 260
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
            self.state = 262
            self.match(GrammarParser.T__5)
            self.state = 263
            self.match(GrammarParser.LPAREN)
            self.state = 264
            self.rvalue(0)
            self.state = 265
            self.match(GrammarParser.RPAREN)
            self.state = 266
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
            self.state = 268
            self.match(GrammarParser.T__6)
            self.state = 269
            self.match(GrammarParser.LPAREN)
            self.state = 270
            self.forCondition()
            self.state = 271
            self.match(GrammarParser.RPAREN)
            self.state = 272
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
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057596218441728) != 0):
                self.state = 274
                self.variable()


            self.state = 277
            self.match(GrammarParser.SEMICOLON)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536249416876785664) != 0):
                self.state = 278
                self.rvalue(0)


            self.state = 281
            self.match(GrammarParser.SEMICOLON)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536249416876785664) != 0):
                self.state = 282
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
            self.state = 285
            self.match(GrammarParser.T__7)
            self.state = 286
            self.match(GrammarParser.LPAREN)
            self.state = 287
            self.formatSpecifier()
            self.state = 288
            self.match(GrammarParser.COMMA)
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.state = 289
                self.identifier()
                pass
            elif token in [52, 53, 54]:
                self.state = 290
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 293
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
            self.state = 295
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
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.lvalue()
                self.state = 298
                self.match(GrammarParser.T__13)
                self.state = 299
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.lvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
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
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.type_()
                self.state = 307
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.pointer()
                self.state = 310
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
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
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 316
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 317
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 318
                self.deref()
                pass

            elif la_ == 4:
                self.state = 319
                self.addr()
                pass

            elif la_ == 5:
                self.state = 320
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 321
                self.rvalue(23)
                pass

            elif la_ == 6:
                self.state = 322
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 323
                self.rvalue(22)
                pass

            elif la_ == 7:
                self.state = 324
                self.match(GrammarParser.LPAREN)
                self.state = 325
                self.rvalue(0)
                self.state = 326
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 328
                self.explicitConversion()
                pass

            elif la_ == 9:
                self.state = 329
                self.postFixIncrement()
                pass

            elif la_ == 10:
                self.state = 330
                self.postFixDecrement()
                pass

            elif la_ == 11:
                self.state = 331
                self.preFixIncrement()
                pass

            elif la_ == 12:
                self.state = 332
                self.preFixDecrement()
                pass

            elif la_ == 13:
                self.state = 333
                self.functionCall()
                pass

            elif la_ == 14:
                self.state = 334
                self.jumpStatement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 375
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 337
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 338
                        self.match(GrammarParser.DIV)
                        self.state = 339
                        self.rvalue(22)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 340
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 341
                        self.match(GrammarParser.MOD)
                        self.state = 342
                        self.rvalue(21)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 343
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 344
                        self.match(GrammarParser.MULT)
                        self.state = 345
                        self.rvalue(20)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 346
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 347
                        self.match(GrammarParser.MINUS)
                        self.state = 348
                        self.rvalue(19)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 349
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 350
                        self.match(GrammarParser.PLUS)
                        self.state = 351
                        self.rvalue(18)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 352
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 353
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 354
                        self.rvalue(17)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 355
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 356
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 357
                        self.rvalue(16)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 358
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 359
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 360
                        self.rvalue(15)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 361
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 362
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 363
                        self.rvalue(14)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 364
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 365
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 366
                        self.rvalue(13)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 367
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 368
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 369
                        self.rvalue(12)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 370
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 371
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 372
                        self.rvalue(11)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 373
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 374
                        self.conditionalExpression()
                        pass

             
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(GrammarParser.GREATER_THAN)
                self.state = 381
                self.rvalue(0)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(GrammarParser.LESS_THAN)
                self.state = 383
                self.rvalue(0)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.match(GrammarParser.GREATER_EQUAL)
                self.state = 385
                self.rvalue(0)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 386
                self.match(GrammarParser.LESS_EQUAL)
                self.state = 387
                self.rvalue(0)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 5)
                self.state = 388
                self.match(GrammarParser.EQUALS)
                self.state = 389
                self.rvalue(0)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 390
                self.match(GrammarParser.NOT_EQUAL)
                self.state = 391
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
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(GrammarParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(GrammarParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.match(GrammarParser.T__16)
                self.state = 398
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 397
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
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29 or _la==30:
                    self.state = 402
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 408
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 405
                    self.literal()
                    pass
                elif token in [56]:
                    self.state = 406
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 407
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 410
                        self.match(GrammarParser.PLUS)
                        self.state = 411
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 414 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 416
                    self.match(GrammarParser.PLUS)


                self.state = 422
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 419
                    self.literal()
                    pass
                elif token in [56]:
                    self.state = 420
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 421
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 426 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 424
                        self.match(GrammarParser.MINUS)
                        self.state = 425
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 428 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 430
                    self.match(GrammarParser.MINUS)


                self.state = 436
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 433
                    self.literal()
                    pass
                elif token in [56]:
                    self.state = 434
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 435
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
            self.state = 440
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
            self.state = 443 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 442
                self.match(GrammarParser.LPAREN)
                self.state = 445 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 448 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 447
                self.type_()
                self.state = 450 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594070433792) != 0)):
                    break

            self.state = 452
            self.match(GrammarParser.RPAREN)
            self.state = 453
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
            self.state = 455
            self.type_()
            self.state = 457 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 456
                self.match(GrammarParser.MULT)
                self.state = 459 
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
            self.state = 462 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 461
                self.match(GrammarParser.MULT)
                self.state = 464 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 466
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
            self.state = 469 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 468
                self.match(GrammarParser.BITWISE_AND)
                self.state = 471 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 473
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumContext(ParserRuleContext):
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
            return GrammarParser.RULE_enum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum" ):
                listener.enterEnum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum" ):
                listener.exitEnum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum" ):
                return visitor.visitEnum(self)
            else:
                return visitor.visitChildren(self)




    def enum(self):

        localctx = GrammarParser.EnumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(GrammarParser.T__17)
            self.state = 476
            self.match(GrammarParser.IDENTIFIER)
            self.state = 477
            self.match(GrammarParser.LBRACE)
            self.state = 478
            self.match(GrammarParser.IDENTIFIER)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 479
                self.match(GrammarParser.COMMA)
                self.state = 480
                self.match(GrammarParser.IDENTIFIER)
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 486
            self.match(GrammarParser.RBRACE)
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
        self.enterRule(localctx, 60, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.lvalue()
            self.state = 489
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
        self.enterRule(localctx, 62, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.lvalue()
            self.state = 492
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
        self.enterRule(localctx, 64, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(GrammarParser.INCREMENT)
            self.state = 495
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
        self.enterRule(localctx, 66, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(GrammarParser.DECREMENT)
            self.state = 498
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
        self.enterRule(localctx, 68, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(GrammarParser.T__18)
            self.state = 501
            self.type_()
            self.state = 502
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
        self.enterRule(localctx, 70, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 504
                self.match(GrammarParser.T__19)
                self.state = 509
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 510
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
        self.enterRule(localctx, 72, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
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
        self.enterRule(localctx, 74, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
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
         




