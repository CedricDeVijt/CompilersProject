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
        4,1,59,628,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,1,0,1,0,1,0,4,0,98,8,0,11,0,12,0,99,1,0,1,0,4,0,104,8,0,11,
        0,12,0,105,1,0,1,0,4,0,110,8,0,11,0,12,0,111,1,0,4,0,115,8,0,11,
        0,12,0,116,1,0,1,0,1,1,1,1,5,1,123,8,1,10,1,12,1,126,9,1,1,1,1,1,
        1,2,1,2,4,2,132,8,2,11,2,12,2,133,1,2,1,2,4,2,138,8,2,11,2,12,2,
        139,1,2,1,2,1,2,4,2,145,8,2,11,2,12,2,146,1,2,1,2,1,2,1,2,1,2,1,
        2,4,2,155,8,2,11,2,12,2,156,1,2,1,2,4,2,161,8,2,11,2,12,2,162,1,
        2,1,2,4,2,167,8,2,11,2,12,2,168,1,2,1,2,3,2,173,8,2,1,3,1,3,3,3,
        177,8,3,1,3,1,3,1,3,3,3,182,8,3,1,3,1,3,1,3,1,3,1,3,3,3,189,8,3,
        1,3,1,3,1,3,3,3,194,8,3,1,3,1,3,1,3,3,3,199,8,3,1,4,1,4,1,4,3,4,
        204,8,4,1,4,1,4,3,4,208,8,4,1,4,1,4,1,4,5,4,213,8,4,10,4,12,4,216,
        9,4,1,5,1,5,1,5,3,5,221,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        231,8,6,10,6,12,6,234,9,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,242,8,7,10,
        7,12,7,245,9,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,253,8,8,10,8,12,8,256,
        9,8,1,8,1,8,1,8,5,8,261,8,8,10,8,12,8,264,9,8,3,8,266,8,8,1,9,1,
        9,5,9,270,8,9,10,9,12,9,273,9,9,1,9,3,9,276,8,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,3,
        15,307,8,15,1,15,1,15,3,15,311,8,15,1,15,1,15,3,15,315,8,15,1,16,
        1,16,1,16,1,16,1,16,1,16,3,16,323,8,16,5,16,325,8,16,10,16,12,16,
        328,9,16,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,3,19,343,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,3,20,354,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,378,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,5,21,418,8,21,10,21,12,21,421,9,21,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,435,8,22,1,23,1,23,
        1,23,1,23,3,23,441,8,23,3,23,443,8,23,1,24,3,24,446,8,24,1,24,1,
        24,1,24,3,24,451,8,24,1,24,1,24,4,24,455,8,24,11,24,12,24,456,1,
        24,3,24,460,8,24,1,24,1,24,1,24,3,24,465,8,24,1,24,1,24,4,24,469,
        8,24,11,24,12,24,470,1,24,3,24,474,8,24,1,24,1,24,1,24,3,24,479,
        8,24,3,24,481,8,24,1,25,1,25,1,26,4,26,486,8,26,11,26,12,26,487,
        1,26,4,26,491,8,26,11,26,12,26,492,1,26,1,26,1,26,1,27,1,27,4,27,
        500,8,27,11,27,12,27,501,1,28,4,28,505,8,28,11,28,12,28,506,1,28,
        1,28,1,29,4,29,512,8,29,11,29,12,29,513,1,29,1,29,1,30,1,30,1,30,
        1,30,1,30,1,30,5,30,524,8,30,10,30,12,30,527,9,30,1,30,1,30,1,31,
        1,31,3,31,533,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,
        1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,
        1,38,1,38,1,38,1,38,1,39,5,39,562,8,39,10,39,12,39,565,9,39,1,39,
        1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,42,1,42,1,42,3,42,578,8,42,
        1,43,1,43,1,43,1,43,1,43,4,43,585,8,43,11,43,12,43,586,1,44,1,44,
        1,44,1,44,1,44,4,44,594,8,44,11,44,12,44,595,1,44,1,44,1,44,3,44,
        601,8,44,1,45,1,45,1,45,1,45,5,45,607,8,45,10,45,12,45,610,9,45,
        3,45,612,8,45,1,45,1,45,1,46,1,46,1,46,1,46,3,46,620,8,46,1,46,1,
        46,4,46,624,8,46,11,46,12,46,625,1,46,0,3,8,12,42,47,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,0,3,1,0,
        26,27,1,0,49,51,2,0,16,19,54,54,700,0,114,1,0,0,0,2,120,1,0,0,0,
        4,172,1,0,0,0,6,198,1,0,0,0,8,200,1,0,0,0,10,217,1,0,0,0,12,224,
        1,0,0,0,14,235,1,0,0,0,16,265,1,0,0,0,18,267,1,0,0,0,20,277,1,0,
        0,0,22,283,1,0,0,0,24,290,1,0,0,0,26,293,1,0,0,0,28,299,1,0,0,0,
        30,306,1,0,0,0,32,316,1,0,0,0,34,331,1,0,0,0,36,333,1,0,0,0,38,342,
        1,0,0,0,40,353,1,0,0,0,42,377,1,0,0,0,44,434,1,0,0,0,46,442,1,0,
        0,0,48,480,1,0,0,0,50,482,1,0,0,0,52,485,1,0,0,0,54,497,1,0,0,0,
        56,504,1,0,0,0,58,511,1,0,0,0,60,517,1,0,0,0,62,532,1,0,0,0,64,534,
        1,0,0,0,66,540,1,0,0,0,68,544,1,0,0,0,70,547,1,0,0,0,72,550,1,0,
        0,0,74,553,1,0,0,0,76,556,1,0,0,0,78,563,1,0,0,0,80,568,1,0,0,0,
        82,570,1,0,0,0,84,577,1,0,0,0,86,579,1,0,0,0,88,588,1,0,0,0,90,602,
        1,0,0,0,92,615,1,0,0,0,94,115,3,82,41,0,95,97,3,60,30,0,96,98,5,
        47,0,0,97,96,1,0,0,0,98,99,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,
        100,115,1,0,0,0,101,103,3,38,19,0,102,104,5,47,0,0,103,102,1,0,0,
        0,104,105,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,115,1,0,0,
        0,107,109,3,76,38,0,108,110,5,47,0,0,109,108,1,0,0,0,110,111,1,0,
        0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,115,1,0,0,0,113,115,3,6,
        3,0,114,94,1,0,0,0,114,95,1,0,0,0,114,101,1,0,0,0,114,107,1,0,0,
        0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,
        0,117,118,1,0,0,0,118,119,5,0,0,1,119,1,1,0,0,0,120,124,5,24,0,0,
        121,123,3,4,2,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,
        124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,25,0,0,
        128,3,1,0,0,0,129,131,3,42,21,0,130,132,5,47,0,0,131,130,1,0,0,0,
        132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,173,1,0,0,0,
        135,137,3,38,19,0,136,138,5,47,0,0,137,136,1,0,0,0,138,139,1,0,0,
        0,139,137,1,0,0,0,139,140,1,0,0,0,140,173,1,0,0,0,141,173,3,82,41,
        0,142,144,3,32,16,0,143,145,5,47,0,0,144,143,1,0,0,0,145,146,1,0,
        0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,173,1,0,0,0,148,173,3,2,
        1,0,149,173,3,18,9,0,150,173,3,26,13,0,151,173,3,28,14,0,152,154,
        3,62,31,0,153,155,5,47,0,0,154,153,1,0,0,0,155,156,1,0,0,0,156,154,
        1,0,0,0,156,157,1,0,0,0,157,173,1,0,0,0,158,160,3,84,42,0,159,161,
        5,47,0,0,160,159,1,0,0,0,161,162,1,0,0,0,162,160,1,0,0,0,162,163,
        1,0,0,0,163,173,1,0,0,0,164,166,3,46,23,0,165,167,5,47,0,0,166,165,
        1,0,0,0,167,168,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,173,
        1,0,0,0,170,173,3,6,3,0,171,173,3,14,7,0,172,129,1,0,0,0,172,135,
        1,0,0,0,172,141,1,0,0,0,172,142,1,0,0,0,172,148,1,0,0,0,172,149,
        1,0,0,0,172,150,1,0,0,0,172,151,1,0,0,0,172,152,1,0,0,0,172,158,
        1,0,0,0,172,164,1,0,0,0,172,170,1,0,0,0,172,171,1,0,0,0,173,5,1,
        0,0,0,174,177,3,78,39,0,175,177,3,54,27,0,176,174,1,0,0,0,176,175,
        1,0,0,0,177,178,1,0,0,0,178,179,5,54,0,0,179,181,5,22,0,0,180,182,
        3,8,4,0,181,180,1,0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,184,
        5,23,0,0,184,185,3,2,1,0,185,199,1,0,0,0,186,189,3,78,39,0,187,189,
        3,54,27,0,188,186,1,0,0,0,188,187,1,0,0,0,189,190,1,0,0,0,190,191,
        5,54,0,0,191,193,5,22,0,0,192,194,3,8,4,0,193,192,1,0,0,0,193,194,
        1,0,0,0,194,195,1,0,0,0,195,196,5,23,0,0,196,197,5,47,0,0,197,199,
        1,0,0,0,198,176,1,0,0,0,198,188,1,0,0,0,199,7,1,0,0,0,200,203,6,
        4,-1,0,201,204,3,54,27,0,202,204,3,78,39,0,203,201,1,0,0,0,203,202,
        1,0,0,0,204,207,1,0,0,0,205,208,3,58,29,0,206,208,3,80,40,0,207,
        205,1,0,0,0,207,206,1,0,0,0,208,214,1,0,0,0,209,210,10,1,0,0,210,
        211,5,48,0,0,211,213,3,8,4,2,212,209,1,0,0,0,213,216,1,0,0,0,214,
        212,1,0,0,0,214,215,1,0,0,0,215,9,1,0,0,0,216,214,1,0,0,0,217,218,
        5,54,0,0,218,220,5,22,0,0,219,221,3,12,6,0,220,219,1,0,0,0,220,221,
        1,0,0,0,221,222,1,0,0,0,222,223,5,23,0,0,223,11,1,0,0,0,224,225,
        6,6,-1,0,225,226,3,42,21,0,226,232,1,0,0,0,227,228,10,1,0,0,228,
        229,5,48,0,0,229,231,3,12,6,2,230,227,1,0,0,0,231,234,1,0,0,0,232,
        230,1,0,0,0,232,233,1,0,0,0,233,13,1,0,0,0,234,232,1,0,0,0,235,236,
        5,1,0,0,236,237,5,22,0,0,237,238,3,42,21,0,238,239,5,23,0,0,239,
        243,5,24,0,0,240,242,3,16,8,0,241,240,1,0,0,0,242,245,1,0,0,0,243,
        241,1,0,0,0,243,244,1,0,0,0,244,246,1,0,0,0,245,243,1,0,0,0,246,
        247,5,25,0,0,247,15,1,0,0,0,248,249,5,2,0,0,249,250,3,50,25,0,250,
        254,5,46,0,0,251,253,3,4,2,0,252,251,1,0,0,0,253,256,1,0,0,0,254,
        252,1,0,0,0,254,255,1,0,0,0,255,266,1,0,0,0,256,254,1,0,0,0,257,
        258,5,3,0,0,258,262,5,46,0,0,259,261,3,4,2,0,260,259,1,0,0,0,261,
        264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,266,1,0,0,0,264,
        262,1,0,0,0,265,248,1,0,0,0,265,257,1,0,0,0,266,17,1,0,0,0,267,271,
        3,20,10,0,268,270,3,22,11,0,269,268,1,0,0,0,270,273,1,0,0,0,271,
        269,1,0,0,0,271,272,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,274,
        276,3,24,12,0,275,274,1,0,0,0,275,276,1,0,0,0,276,19,1,0,0,0,277,
        278,5,4,0,0,278,279,5,22,0,0,279,280,3,42,21,0,280,281,5,23,0,0,
        281,282,3,2,1,0,282,21,1,0,0,0,283,284,5,5,0,0,284,285,5,4,0,0,285,
        286,5,22,0,0,286,287,3,42,21,0,287,288,5,23,0,0,288,289,3,2,1,0,
        289,23,1,0,0,0,290,291,5,5,0,0,291,292,3,2,1,0,292,25,1,0,0,0,293,
        294,5,6,0,0,294,295,5,22,0,0,295,296,3,42,21,0,296,297,5,23,0,0,
        297,298,3,2,1,0,298,27,1,0,0,0,299,300,5,7,0,0,300,301,5,22,0,0,
        301,302,3,30,15,0,302,303,5,23,0,0,303,304,3,2,1,0,304,29,1,0,0,
        0,305,307,3,38,19,0,306,305,1,0,0,0,306,307,1,0,0,0,307,308,1,0,
        0,0,308,310,5,47,0,0,309,311,3,42,21,0,310,309,1,0,0,0,310,311,1,
        0,0,0,311,312,1,0,0,0,312,314,5,47,0,0,313,315,3,42,21,0,314,313,
        1,0,0,0,314,315,1,0,0,0,315,31,1,0,0,0,316,317,5,8,0,0,317,318,5,
        22,0,0,318,326,3,34,17,0,319,322,5,48,0,0,320,323,3,42,21,0,321,
        323,3,36,18,0,322,320,1,0,0,0,322,321,1,0,0,0,323,325,1,0,0,0,324,
        319,1,0,0,0,325,328,1,0,0,0,326,324,1,0,0,0,326,327,1,0,0,0,327,
        329,1,0,0,0,328,326,1,0,0,0,329,330,5,23,0,0,330,33,1,0,0,0,331,
        332,5,52,0,0,332,35,1,0,0,0,333,334,5,52,0,0,334,37,1,0,0,0,335,
        336,3,40,20,0,336,337,5,9,0,0,337,338,3,42,21,0,338,343,1,0,0,0,
        339,343,3,40,20,0,340,343,3,76,38,0,341,343,3,86,43,0,342,335,1,
        0,0,0,342,339,1,0,0,0,342,340,1,0,0,0,342,341,1,0,0,0,343,39,1,0,
        0,0,344,354,3,80,40,0,345,346,3,78,39,0,346,347,3,80,40,0,347,354,
        1,0,0,0,348,349,3,54,27,0,349,350,3,80,40,0,350,354,1,0,0,0,351,
        354,3,56,28,0,352,354,3,92,46,0,353,344,1,0,0,0,353,345,1,0,0,0,
        353,348,1,0,0,0,353,351,1,0,0,0,353,352,1,0,0,0,354,41,1,0,0,0,355,
        356,6,21,-1,0,356,378,3,48,24,0,357,378,3,80,40,0,358,378,3,56,28,
        0,359,378,3,58,29,0,360,361,5,45,0,0,361,378,3,42,21,25,362,363,
        5,42,0,0,363,378,3,42,21,24,364,365,5,22,0,0,365,366,3,42,21,0,366,
        367,5,23,0,0,367,378,1,0,0,0,368,378,3,52,26,0,369,378,3,68,34,0,
        370,378,3,70,35,0,371,378,3,72,36,0,372,378,3,74,37,0,373,378,3,
        10,5,0,374,378,3,46,23,0,375,378,3,92,46,0,376,378,3,90,45,0,377,
        355,1,0,0,0,377,357,1,0,0,0,377,358,1,0,0,0,377,359,1,0,0,0,377,
        360,1,0,0,0,377,362,1,0,0,0,377,364,1,0,0,0,377,368,1,0,0,0,377,
        369,1,0,0,0,377,370,1,0,0,0,377,371,1,0,0,0,377,372,1,0,0,0,377,
        373,1,0,0,0,377,374,1,0,0,0,377,375,1,0,0,0,377,376,1,0,0,0,378,
        419,1,0,0,0,379,380,10,23,0,0,380,381,5,29,0,0,381,418,3,42,21,24,
        382,383,10,22,0,0,383,384,5,30,0,0,384,418,3,42,21,23,385,386,10,
        21,0,0,386,387,5,28,0,0,387,418,3,42,21,22,388,389,10,20,0,0,389,
        390,5,27,0,0,390,418,3,42,21,21,391,392,10,19,0,0,392,393,5,26,0,
        0,393,418,3,42,21,20,394,395,10,18,0,0,395,396,5,37,0,0,396,418,
        3,42,21,19,397,398,10,17,0,0,398,399,5,38,0,0,399,418,3,42,21,18,
        400,401,10,16,0,0,401,402,5,39,0,0,402,418,3,42,21,17,403,404,10,
        15,0,0,404,405,5,40,0,0,405,418,3,42,21,16,406,407,10,14,0,0,407,
        408,5,41,0,0,408,418,3,42,21,15,409,410,10,13,0,0,410,411,5,43,0,
        0,411,418,3,42,21,14,412,413,10,12,0,0,413,414,5,44,0,0,414,418,
        3,42,21,13,415,416,10,5,0,0,416,418,3,44,22,0,417,379,1,0,0,0,417,
        382,1,0,0,0,417,385,1,0,0,0,417,388,1,0,0,0,417,391,1,0,0,0,417,
        394,1,0,0,0,417,397,1,0,0,0,417,400,1,0,0,0,417,403,1,0,0,0,417,
        406,1,0,0,0,417,409,1,0,0,0,417,412,1,0,0,0,417,415,1,0,0,0,418,
        421,1,0,0,0,419,417,1,0,0,0,419,420,1,0,0,0,420,43,1,0,0,0,421,419,
        1,0,0,0,422,423,5,31,0,0,423,435,3,42,21,0,424,425,5,32,0,0,425,
        435,3,42,21,0,426,427,5,33,0,0,427,435,3,42,21,0,428,429,5,34,0,
        0,429,435,3,42,21,0,430,431,5,35,0,0,431,435,3,42,21,0,432,433,5,
        36,0,0,433,435,3,42,21,0,434,422,1,0,0,0,434,424,1,0,0,0,434,426,
        1,0,0,0,434,428,1,0,0,0,434,430,1,0,0,0,434,432,1,0,0,0,435,45,1,
        0,0,0,436,443,5,10,0,0,437,443,5,11,0,0,438,440,5,12,0,0,439,441,
        3,42,21,0,440,439,1,0,0,0,440,441,1,0,0,0,441,443,1,0,0,0,442,436,
        1,0,0,0,442,437,1,0,0,0,442,438,1,0,0,0,443,47,1,0,0,0,444,446,7,
        0,0,0,445,444,1,0,0,0,445,446,1,0,0,0,446,450,1,0,0,0,447,451,3,
        50,25,0,448,451,3,80,40,0,449,451,3,56,28,0,450,447,1,0,0,0,450,
        448,1,0,0,0,450,449,1,0,0,0,451,481,1,0,0,0,452,453,5,26,0,0,453,
        455,5,27,0,0,454,452,1,0,0,0,455,456,1,0,0,0,456,454,1,0,0,0,456,
        457,1,0,0,0,457,459,1,0,0,0,458,460,5,26,0,0,459,458,1,0,0,0,459,
        460,1,0,0,0,460,464,1,0,0,0,461,465,3,50,25,0,462,465,3,80,40,0,
        463,465,3,56,28,0,464,461,1,0,0,0,464,462,1,0,0,0,464,463,1,0,0,
        0,465,481,1,0,0,0,466,467,5,27,0,0,467,469,5,26,0,0,468,466,1,0,
        0,0,469,470,1,0,0,0,470,468,1,0,0,0,470,471,1,0,0,0,471,473,1,0,
        0,0,472,474,5,27,0,0,473,472,1,0,0,0,473,474,1,0,0,0,474,478,1,0,
        0,0,475,479,3,50,25,0,476,479,3,80,40,0,477,479,3,56,28,0,478,475,
        1,0,0,0,478,476,1,0,0,0,478,477,1,0,0,0,479,481,1,0,0,0,480,445,
        1,0,0,0,480,454,1,0,0,0,480,468,1,0,0,0,481,49,1,0,0,0,482,483,7,
        1,0,0,483,51,1,0,0,0,484,486,5,22,0,0,485,484,1,0,0,0,486,487,1,
        0,0,0,487,485,1,0,0,0,487,488,1,0,0,0,488,490,1,0,0,0,489,491,3,
        78,39,0,490,489,1,0,0,0,491,492,1,0,0,0,492,490,1,0,0,0,492,493,
        1,0,0,0,493,494,1,0,0,0,494,495,5,23,0,0,495,496,3,42,21,0,496,53,
        1,0,0,0,497,499,3,78,39,0,498,500,5,28,0,0,499,498,1,0,0,0,500,501,
        1,0,0,0,501,499,1,0,0,0,501,502,1,0,0,0,502,55,1,0,0,0,503,505,5,
        28,0,0,504,503,1,0,0,0,505,506,1,0,0,0,506,504,1,0,0,0,506,507,1,
        0,0,0,507,508,1,0,0,0,508,509,3,80,40,0,509,57,1,0,0,0,510,512,5,
        39,0,0,511,510,1,0,0,0,512,513,1,0,0,0,513,511,1,0,0,0,513,514,1,
        0,0,0,514,515,1,0,0,0,515,516,3,80,40,0,516,59,1,0,0,0,517,518,5,
        13,0,0,518,519,5,54,0,0,519,520,5,24,0,0,520,525,5,54,0,0,521,522,
        5,48,0,0,522,524,5,54,0,0,523,521,1,0,0,0,524,527,1,0,0,0,525,523,
        1,0,0,0,525,526,1,0,0,0,526,528,1,0,0,0,527,525,1,0,0,0,528,529,
        5,25,0,0,529,61,1,0,0,0,530,533,3,64,32,0,531,533,3,66,33,0,532,
        530,1,0,0,0,532,531,1,0,0,0,533,63,1,0,0,0,534,535,5,13,0,0,535,
        536,5,54,0,0,536,537,5,54,0,0,537,538,5,9,0,0,538,539,5,54,0,0,539,
        65,1,0,0,0,540,541,5,13,0,0,541,542,5,54,0,0,542,543,5,54,0,0,543,
        67,1,0,0,0,544,545,3,40,20,0,545,546,5,55,0,0,546,69,1,0,0,0,547,
        548,3,40,20,0,548,549,5,56,0,0,549,71,1,0,0,0,550,551,5,55,0,0,551,
        552,3,40,20,0,552,73,1,0,0,0,553,554,5,56,0,0,554,555,3,40,20,0,
        555,75,1,0,0,0,556,557,5,14,0,0,557,558,3,78,39,0,558,559,5,54,0,
        0,559,77,1,0,0,0,560,562,5,15,0,0,561,560,1,0,0,0,562,565,1,0,0,
        0,563,561,1,0,0,0,563,564,1,0,0,0,564,566,1,0,0,0,565,563,1,0,0,
        0,566,567,7,2,0,0,567,79,1,0,0,0,568,569,5,54,0,0,569,81,1,0,0,0,
        570,571,5,57,0,0,571,83,1,0,0,0,572,578,3,86,43,0,573,574,3,88,44,
        0,574,575,5,9,0,0,575,576,3,42,21,0,576,578,1,0,0,0,577,572,1,0,
        0,0,577,573,1,0,0,0,578,85,1,0,0,0,579,580,3,78,39,0,580,584,5,54,
        0,0,581,582,5,20,0,0,582,583,5,49,0,0,583,585,5,21,0,0,584,581,1,
        0,0,0,585,586,1,0,0,0,586,584,1,0,0,0,586,587,1,0,0,0,587,87,1,0,
        0,0,588,589,3,78,39,0,589,593,5,54,0,0,590,591,5,20,0,0,591,592,
        5,49,0,0,592,594,5,21,0,0,593,590,1,0,0,0,594,595,1,0,0,0,595,593,
        1,0,0,0,595,596,1,0,0,0,596,597,1,0,0,0,597,600,5,9,0,0,598,601,
        3,90,45,0,599,601,3,80,40,0,600,598,1,0,0,0,600,599,1,0,0,0,601,
        89,1,0,0,0,602,611,5,24,0,0,603,608,3,42,21,0,604,605,5,48,0,0,605,
        607,3,42,21,0,606,604,1,0,0,0,607,610,1,0,0,0,608,606,1,0,0,0,608,
        609,1,0,0,0,609,612,1,0,0,0,610,608,1,0,0,0,611,603,1,0,0,0,611,
        612,1,0,0,0,612,613,1,0,0,0,613,614,5,25,0,0,614,91,1,0,0,0,615,
        623,3,80,40,0,616,619,5,20,0,0,617,620,3,42,21,0,618,620,3,80,40,
        0,619,617,1,0,0,0,619,618,1,0,0,0,620,621,1,0,0,0,621,622,5,21,0,
        0,622,624,1,0,0,0,623,616,1,0,0,0,624,625,1,0,0,0,625,623,1,0,0,
        0,625,626,1,0,0,0,626,93,1,0,0,0,67,99,105,111,114,116,124,133,139,
        146,156,162,168,172,176,181,188,193,198,203,207,214,220,232,243,
        254,262,265,271,275,306,310,314,322,326,342,353,377,417,419,434,
        440,442,445,450,456,459,464,470,473,478,480,487,492,501,506,513,
        525,532,563,577,586,595,600,608,611,619,625
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'switch'", "'case'", "'default'", "'if'", 
                     "'else'", "'while'", "'for'", "'printf'", "'='", "'break'", 
                     "'continue'", "'return'", "'enum'", "'typedef'", "'const'", 
                     "'int'", "'float'", "'char'", "'void'", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'<<'", "'>>'", "'&'", "'|'", "'^'", "'~'", "'&&'", 
                     "'||'", "'!'", "':'", "';'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "PLUS", "MINUS", "MULT", "DIV", "MOD", "GREATER_THAN", 
                      "LESS_THAN", "GREATER_EQUAL", "LESS_EQUAL", "EQUALS", 
                      "NOT_EQUAL", "SHIFT_LEFT", "SHIFT_RIGHT", "BITWISE_AND", 
                      "BITWISE_OR", "BITWISE_XOR", "BITWISE_NOT", "LOGICAL_AND", 
                      "LOGICAL_OR", "LOGICAL_NOT", "COLON", "SEMICOLON", 
                      "COMMA", "INT", "FLOAT", "CHAR", "STRING", "WHITESPACE", 
                      "IDENTIFIER", "INCREMENT", "DECREMENT", "COMMENT", 
                      "BLOCKCOMMENT", "LINECOMMENT" ]

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
    RULE_string = 18
    RULE_variable = 19
    RULE_lvalue = 20
    RULE_rvalue = 21
    RULE_conditionalExpression = 22
    RULE_jumpStatement = 23
    RULE_unaryExpression = 24
    RULE_literal = 25
    RULE_explicitConversion = 26
    RULE_pointer = 27
    RULE_deref = 28
    RULE_addr = 29
    RULE_enumDeclaration = 30
    RULE_enumStatement = 31
    RULE_enumVariableDefinition = 32
    RULE_enumVariableDeclaration = 33
    RULE_postFixIncrement = 34
    RULE_postFixDecrement = 35
    RULE_preFixIncrement = 36
    RULE_preFixDecrement = 37
    RULE_typedef = 38
    RULE_type = 39
    RULE_identifier = 40
    RULE_comment = 41
    RULE_arrayStatement = 42
    RULE_arrayDeclaration = 43
    RULE_arrayDefinition = 44
    RULE_arrayInitializer = 45
    RULE_arrayElement = 46

    ruleNames =  [ "program", "scope", "statement", "function", "functionParams", 
                   "functionCall", "callParams", "switchStatement", "switchCase", 
                   "conditional", "ifStatement", "elseIfStatement", "elseStatement", 
                   "whileLoop", "forLoop", "forCondition", "printfStatement", 
                   "formatSpecifier", "string", "variable", "lvalue", "rvalue", 
                   "conditionalExpression", "jumpStatement", "unaryExpression", 
                   "literal", "explicitConversion", "pointer", "deref", 
                   "addr", "enumDeclaration", "enumStatement", "enumVariableDefinition", 
                   "enumVariableDeclaration", "postFixIncrement", "postFixDecrement", 
                   "preFixIncrement", "preFixDecrement", "typedef", "type", 
                   "identifier", "comment", "arrayStatement", "arrayDeclaration", 
                   "arrayDefinition", "arrayInitializer", "arrayElement" ]

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
    LPAREN=22
    RPAREN=23
    LBRACE=24
    RBRACE=25
    PLUS=26
    MINUS=27
    MULT=28
    DIV=29
    MOD=30
    GREATER_THAN=31
    LESS_THAN=32
    GREATER_EQUAL=33
    LESS_EQUAL=34
    EQUALS=35
    NOT_EQUAL=36
    SHIFT_LEFT=37
    SHIFT_RIGHT=38
    BITWISE_AND=39
    BITWISE_OR=40
    BITWISE_XOR=41
    BITWISE_NOT=42
    LOGICAL_AND=43
    LOGICAL_OR=44
    LOGICAL_NOT=45
    COLON=46
    SEMICOLON=47
    COMMA=48
    INT=49
    FLOAT=50
    CHAR=51
    STRING=52
    WHITESPACE=53
    IDENTIFIER=54
    INCREMENT=55
    DECREMENT=56
    COMMENT=57
    BLOCKCOMMENT=58
    LINECOMMENT=59

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
            self.state = 114 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 94
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 95
                    self.enumDeclaration()
                    self.state = 97 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 96
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 99 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==47):
                            break

                    pass

                elif la_ == 3:
                    self.state = 101
                    self.variable()
                    self.state = 103 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 102
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 105 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==47):
                            break

                    pass

                elif la_ == 4:
                    self.state = 107
                    self.typedef()
                    self.state = 109 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 108
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 111 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==47):
                            break

                    pass

                elif la_ == 5:
                    self.state = 113
                    self.function()
                    pass


                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 162129586854813696) != 0)):
                    break

            self.state = 118
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
            self.state = 120
            self.match(GrammarParser.LBRACE)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274196759982374354) != 0):
                self.state = 121
                self.statement()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
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


        def arrayStatement(self):
            return self.getTypedRuleContext(GrammarParser.ArrayStatementContext,0)


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
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.rvalue(0)
                self.state = 131 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 130
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 133 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.variable()
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 136
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 139 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.printfStatement()
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 143
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 146 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
                self.scope()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 149
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 150
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 151
                self.forLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 152
                self.enumStatement()
                self.state = 154 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 153
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 156 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 158
                self.arrayStatement()
                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 159
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 162 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 164
                self.jumpStatement()
                self.state = 166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 165
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 168 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 170
                self.function()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 171
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
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 174
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 175
                    self.pointer()
                    pass


                self.state = 178
                self.match(GrammarParser.IDENTIFIER)
                self.state = 179
                self.match(GrammarParser.LPAREN)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398510497792) != 0):
                    self.state = 180
                    self.functionParams(0)


                self.state = 183
                self.match(GrammarParser.RPAREN)
                self.state = 184
                self.scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 186
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 187
                    self.pointer()
                    pass


                self.state = 190
                self.match(GrammarParser.IDENTIFIER)
                self.state = 191
                self.match(GrammarParser.LPAREN)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398510497792) != 0):
                    self.state = 192
                    self.functionParams(0)


                self.state = 195
                self.match(GrammarParser.RPAREN)
                self.state = 196
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
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 201
                self.pointer()
                pass

            elif la_ == 2:
                self.state = 202
                self.type_()
                pass


            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 205
                self.addr()
                pass
            elif token in [54]:
                self.state = 206
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.FunctionParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParams)
                    self.state = 209
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 210
                    self.match(GrammarParser.COMMA)
                    self.state = 211
                    self.functionParams(2) 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 217
            self.match(GrammarParser.IDENTIFIER)
            self.state = 218
            self.match(GrammarParser.LPAREN)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130081571906493440) != 0):
                self.state = 219
                self.callParams(0)


            self.state = 222
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
            self.state = 225
            self.rvalue(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CallParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callParams)
                    self.state = 227
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 228
                    self.match(GrammarParser.COMMA)
                    self.state = 229
                    self.callParams(2) 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 235
            self.match(GrammarParser.T__0)
            self.state = 236
            self.match(GrammarParser.LPAREN)
            self.state = 237
            self.rvalue(0)
            self.state = 238
            self.match(GrammarParser.RPAREN)
            self.state = 239
            self.match(GrammarParser.LBRACE)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 240
                self.switchCase()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
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
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(GrammarParser.T__1)
                self.state = 249
                self.literal()
                self.state = 250
                self.match(GrammarParser.COLON)
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274196759982374354) != 0):
                    self.state = 251
                    self.statement()
                    self.state = 256
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(GrammarParser.T__2)
                self.state = 258
                self.match(GrammarParser.COLON)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274196759982374354) != 0):
                    self.state = 259
                    self.statement()
                    self.state = 264
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
            self.state = 267
            self.ifStatement()
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 268
                    self.elseIfStatement() 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 274
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
            self.state = 277
            self.match(GrammarParser.T__3)
            self.state = 278
            self.match(GrammarParser.LPAREN)
            self.state = 279
            self.rvalue(0)
            self.state = 280
            self.match(GrammarParser.RPAREN)
            self.state = 281
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
            self.state = 283
            self.match(GrammarParser.T__4)
            self.state = 284
            self.match(GrammarParser.T__3)
            self.state = 285
            self.match(GrammarParser.LPAREN)
            self.state = 286
            self.rvalue(0)
            self.state = 287
            self.match(GrammarParser.RPAREN)
            self.state = 288
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
            self.state = 290
            self.match(GrammarParser.T__4)
            self.state = 291
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
            self.state = 293
            self.match(GrammarParser.T__5)
            self.state = 294
            self.match(GrammarParser.LPAREN)
            self.state = 295
            self.rvalue(0)
            self.state = 296
            self.match(GrammarParser.RPAREN)
            self.state = 297
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
            self.state = 299
            self.match(GrammarParser.T__6)
            self.state = 300
            self.match(GrammarParser.LPAREN)
            self.state = 301
            self.forCondition()
            self.state = 302
            self.match(GrammarParser.RPAREN)
            self.state = 303
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
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398778949632) != 0):
                self.state = 305
                self.variable()


            self.state = 308
            self.match(GrammarParser.SEMICOLON)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130081571906493440) != 0):
                self.state = 309
                self.rvalue(0)


            self.state = 312
            self.match(GrammarParser.SEMICOLON)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130081571906493440) != 0):
                self.state = 313
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StringContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StringContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(GrammarParser.T__7)
            self.state = 317
            self.match(GrammarParser.LPAREN)
            self.state = 318
            self.formatSpecifier()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 319
                self.match(GrammarParser.COMMA)
                self.state = 322
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 11, 12, 15, 16, 17, 18, 19, 22, 24, 26, 27, 28, 39, 42, 45, 49, 50, 51, 54, 55, 56]:
                    self.state = 320
                    self.rvalue(0)
                    pass
                elif token in [52]:
                    self.state = 321
                    self.string()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 329
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

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(GrammarParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = GrammarParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(GrammarParser.STRING)
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


        def arrayDeclaration(self):
            return self.getTypedRuleContext(GrammarParser.ArrayDeclarationContext,0)


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
        self.enterRule(localctx, 38, self.RULE_variable)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.lvalue()
                self.state = 336
                self.match(GrammarParser.T__8)
                self.state = 337
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.lvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 340
                self.typedef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 341
                self.arrayDeclaration()
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


        def arrayElement(self):
            return self.getTypedRuleContext(GrammarParser.ArrayElementContext,0)


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
        self.enterRule(localctx, 40, self.RULE_lvalue)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.type_()
                self.state = 346
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 348
                self.pointer()
                self.state = 349
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.deref()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 352
                self.arrayElement()
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


        def arrayElement(self):
            return self.getTypedRuleContext(GrammarParser.ArrayElementContext,0)


        def arrayInitializer(self):
            return self.getTypedRuleContext(GrammarParser.ArrayInitializerContext,0)


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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 356
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 357
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 358
                self.deref()
                pass

            elif la_ == 4:
                self.state = 359
                self.addr()
                pass

            elif la_ == 5:
                self.state = 360
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 361
                self.rvalue(25)
                pass

            elif la_ == 6:
                self.state = 362
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 363
                self.rvalue(24)
                pass

            elif la_ == 7:
                self.state = 364
                self.match(GrammarParser.LPAREN)
                self.state = 365
                self.rvalue(0)
                self.state = 366
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 368
                self.explicitConversion()
                pass

            elif la_ == 9:
                self.state = 369
                self.postFixIncrement()
                pass

            elif la_ == 10:
                self.state = 370
                self.postFixDecrement()
                pass

            elif la_ == 11:
                self.state = 371
                self.preFixIncrement()
                pass

            elif la_ == 12:
                self.state = 372
                self.preFixDecrement()
                pass

            elif la_ == 13:
                self.state = 373
                self.functionCall()
                pass

            elif la_ == 14:
                self.state = 374
                self.jumpStatement()
                pass

            elif la_ == 15:
                self.state = 375
                self.arrayElement()
                pass

            elif la_ == 16:
                self.state = 376
                self.arrayInitializer()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 417
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 379
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 380
                        self.match(GrammarParser.DIV)
                        self.state = 381
                        self.rvalue(24)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 382
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 383
                        self.match(GrammarParser.MOD)
                        self.state = 384
                        self.rvalue(23)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 385
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 386
                        self.match(GrammarParser.MULT)
                        self.state = 387
                        self.rvalue(22)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 388
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 389
                        self.match(GrammarParser.MINUS)
                        self.state = 390
                        self.rvalue(21)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 391
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 392
                        self.match(GrammarParser.PLUS)
                        self.state = 393
                        self.rvalue(20)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 394
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 395
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 396
                        self.rvalue(19)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 397
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 398
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 399
                        self.rvalue(18)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 400
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 401
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 402
                        self.rvalue(17)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 403
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 404
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 405
                        self.rvalue(16)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 406
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 407
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 408
                        self.rvalue(15)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 409
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 410
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 411
                        self.rvalue(14)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 412
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 413
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 414
                        self.rvalue(13)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 415
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 416
                        self.conditionalExpression()
                        pass

             
                self.state = 421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_conditionalExpression)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.match(GrammarParser.GREATER_THAN)
                self.state = 423
                self.rvalue(0)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(GrammarParser.LESS_THAN)
                self.state = 425
                self.rvalue(0)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                self.match(GrammarParser.GREATER_EQUAL)
                self.state = 427
                self.rvalue(0)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 428
                self.match(GrammarParser.LESS_EQUAL)
                self.state = 429
                self.rvalue(0)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 5)
                self.state = 430
                self.match(GrammarParser.EQUALS)
                self.state = 431
                self.rvalue(0)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 6)
                self.state = 432
                self.match(GrammarParser.NOT_EQUAL)
                self.state = 433
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
        self.enterRule(localctx, 46, self.RULE_jumpStatement)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(GrammarParser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(GrammarParser.T__10)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(GrammarParser.T__11)
                self.state = 440
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 439
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
        self.enterRule(localctx, 48, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26 or _la==27:
                    self.state = 444
                    _la = self._input.LA(1)
                    if not(_la==26 or _la==27):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 450
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [49, 50, 51]:
                    self.state = 447
                    self.literal()
                    pass
                elif token in [54]:
                    self.state = 448
                    self.identifier()
                    pass
                elif token in [28]:
                    self.state = 449
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 452
                        self.match(GrammarParser.PLUS)
                        self.state = 453
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 456 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 458
                    self.match(GrammarParser.PLUS)


                self.state = 464
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [49, 50, 51]:
                    self.state = 461
                    self.literal()
                    pass
                elif token in [54]:
                    self.state = 462
                    self.identifier()
                    pass
                elif token in [28]:
                    self.state = 463
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 468 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 466
                        self.match(GrammarParser.MINUS)
                        self.state = 467
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 470 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

                self.state = 473
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 472
                    self.match(GrammarParser.MINUS)


                self.state = 478
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [49, 50, 51]:
                    self.state = 475
                    self.literal()
                    pass
                elif token in [54]:
                    self.state = 476
                    self.identifier()
                    pass
                elif token in [28]:
                    self.state = 477
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
        self.enterRule(localctx, 50, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3940649673949184) != 0)):
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
        self.enterRule(localctx, 52, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 484
                self.match(GrammarParser.LPAREN)
                self.state = 487 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 490 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 489
                self.type_()
                self.state = 492 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398510497792) != 0)):
                    break

            self.state = 494
            self.match(GrammarParser.RPAREN)
            self.state = 495
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
        self.enterRule(localctx, 54, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.type_()
            self.state = 499 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 498
                self.match(GrammarParser.MULT)
                self.state = 501 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==28):
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
        self.enterRule(localctx, 56, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 503
                self.match(GrammarParser.MULT)
                self.state = 506 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==28):
                    break

            self.state = 508
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
        self.enterRule(localctx, 58, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 510
                self.match(GrammarParser.BITWISE_AND)
                self.state = 513 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 515
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
        self.enterRule(localctx, 60, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(GrammarParser.T__12)
            self.state = 518
            self.match(GrammarParser.IDENTIFIER)
            self.state = 519
            self.match(GrammarParser.LBRACE)
            self.state = 520
            self.match(GrammarParser.IDENTIFIER)
            self.state = 525
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 521
                self.match(GrammarParser.COMMA)
                self.state = 522
                self.match(GrammarParser.IDENTIFIER)
                self.state = 527
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 528
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
        self.enterRule(localctx, 62, self.RULE_enumStatement)
        try:
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.enumVariableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
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
        self.enterRule(localctx, 64, self.RULE_enumVariableDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(GrammarParser.T__12)
            self.state = 535
            self.match(GrammarParser.IDENTIFIER)
            self.state = 536
            self.match(GrammarParser.IDENTIFIER)
            self.state = 537
            self.match(GrammarParser.T__8)
            self.state = 538
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
        self.enterRule(localctx, 66, self.RULE_enumVariableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(GrammarParser.T__12)
            self.state = 541
            self.match(GrammarParser.IDENTIFIER)
            self.state = 542
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
        self.enterRule(localctx, 68, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.lvalue()
            self.state = 545
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
        self.enterRule(localctx, 70, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.lvalue()
            self.state = 548
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
        self.enterRule(localctx, 72, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(GrammarParser.INCREMENT)
            self.state = 551
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
        self.enterRule(localctx, 74, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(GrammarParser.DECREMENT)
            self.state = 554
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
        self.enterRule(localctx, 76, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(GrammarParser.T__13)
            self.state = 557
            self.type_()
            self.state = 558
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
        self.enterRule(localctx, 78, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 560
                self.match(GrammarParser.T__14)
                self.state = 565
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 566
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398510465024) != 0)):
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
        self.enterRule(localctx, 80, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
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
        self.enterRule(localctx, 82, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(GrammarParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayDeclaration(self):
            return self.getTypedRuleContext(GrammarParser.ArrayDeclarationContext,0)


        def arrayDefinition(self):
            return self.getTypedRuleContext(GrammarParser.ArrayDefinitionContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_arrayStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayStatement" ):
                listener.enterArrayStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayStatement" ):
                listener.exitArrayStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayStatement" ):
                return visitor.visitArrayStatement(self)
            else:
                return visitor.visitChildren(self)




    def arrayStatement(self):

        localctx = GrammarParser.ArrayStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arrayStatement)
        try:
            self.state = 577
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                self.arrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                self.arrayDefinition()
                self.state = 574
                self.match(GrammarParser.T__8)
                self.state = 575
                self.rvalue(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.INT)
            else:
                return self.getToken(GrammarParser.INT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_arrayDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDeclaration" ):
                listener.enterArrayDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDeclaration" ):
                listener.exitArrayDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclaration" ):
                return visitor.visitArrayDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def arrayDeclaration(self):

        localctx = GrammarParser.ArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.type_()
            self.state = 580
            self.match(GrammarParser.IDENTIFIER)
            self.state = 584 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 581
                self.match(GrammarParser.T__19)
                self.state = 582
                self.match(GrammarParser.INT)
                self.state = 583
                self.match(GrammarParser.T__20)
                self.state = 586 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def arrayInitializer(self):
            return self.getTypedRuleContext(GrammarParser.ArrayInitializerContext,0)


        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.INT)
            else:
                return self.getToken(GrammarParser.INT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_arrayDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDefinition" ):
                listener.enterArrayDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDefinition" ):
                listener.exitArrayDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDefinition" ):
                return visitor.visitArrayDefinition(self)
            else:
                return visitor.visitChildren(self)




    def arrayDefinition(self):

        localctx = GrammarParser.ArrayDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arrayDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.type_()
            self.state = 589
            self.match(GrammarParser.IDENTIFIER)
            self.state = 593 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 590
                self.match(GrammarParser.T__19)
                self.state = 591
                self.match(GrammarParser.INT)
                self.state = 592
                self.match(GrammarParser.T__20)
                self.state = 595 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

            self.state = 597
            self.match(GrammarParser.T__8)
            self.state = 600
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 598
                self.arrayInitializer()
                pass
            elif token in [54]:
                self.state = 599
                self.identifier()
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


    class ArrayInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(GrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GrammarParser.RBRACE, 0)

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_arrayInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayInitializer" ):
                listener.enterArrayInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayInitializer" ):
                listener.exitArrayInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayInitializer" ):
                return visitor.visitArrayInitializer(self)
            else:
                return visitor.visitChildren(self)




    def arrayInitializer(self):

        localctx = GrammarParser.ArrayInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arrayInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(GrammarParser.LBRACE)
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130081571906493440) != 0):
                self.state = 603
                self.rvalue(0)
                self.state = 608
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==48:
                    self.state = 604
                    self.match(GrammarParser.COMMA)
                    self.state = 605
                    self.rvalue(0)
                    self.state = 610
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 613
            self.match(GrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(GrammarParser.IdentifierContext,i)


        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_arrayElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayElement" ):
                listener.enterArrayElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayElement" ):
                listener.exitArrayElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElement" ):
                return visitor.visitArrayElement(self)
            else:
                return visitor.visitChildren(self)




    def arrayElement(self):

        localctx = GrammarParser.ArrayElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.identifier()
            self.state = 623 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 616
                    self.match(GrammarParser.T__19)
                    self.state = 619
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                    if la_ == 1:
                        self.state = 617
                        self.rvalue(0)
                        pass

                    elif la_ == 2:
                        self.state = 618
                        self.identifier()
                        pass


                    self.state = 621
                    self.match(GrammarParser.T__20)

                else:
                    raise NoViableAltException(self)
                self.state = 625 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

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
        self._predicates[21] = self.rvalue_sempred
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
                return self.precpred(self._ctx, 23)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 5)
         




