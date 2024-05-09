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
        4,1,62,731,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,1,0,3,0,110,8,0,1,0,4,0,113,8,0,11,0,12,0,114,1,0,1,0,4,
        0,119,8,0,11,0,12,0,120,1,0,1,0,4,0,125,8,0,11,0,12,0,126,1,0,4,
        0,130,8,0,11,0,12,0,131,1,0,1,0,1,1,1,1,5,1,138,8,1,10,1,12,1,141,
        9,1,1,1,1,1,1,2,1,2,4,2,147,8,2,11,2,12,2,148,1,2,1,2,4,2,153,8,
        2,11,2,12,2,154,1,2,1,2,1,2,4,2,160,8,2,11,2,12,2,161,1,2,1,2,4,
        2,166,8,2,11,2,12,2,167,1,2,1,2,1,2,1,2,1,2,1,2,4,2,176,8,2,11,2,
        12,2,177,1,2,1,2,4,2,182,8,2,11,2,12,2,183,1,2,1,2,1,2,1,2,4,2,190,
        8,2,11,2,12,2,191,1,2,1,2,4,2,196,8,2,11,2,12,2,197,3,2,200,8,2,
        1,3,1,3,3,3,204,8,3,1,3,1,3,1,3,3,3,209,8,3,1,3,1,3,1,3,1,3,1,3,
        3,3,216,8,3,1,3,1,3,1,3,3,3,221,8,3,1,3,1,3,1,3,3,3,226,8,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,3,4,235,8,4,1,4,1,4,5,4,239,8,4,10,4,12,
        4,242,9,4,1,4,1,4,1,5,1,5,3,5,248,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,7,5,7,260,8,7,10,7,12,7,263,9,7,1,8,1,8,1,8,1,8,1,9,
        1,9,1,9,3,9,272,8,9,1,9,1,9,3,9,276,8,9,1,9,1,9,1,9,5,9,281,8,9,
        10,9,12,9,284,9,9,1,10,1,10,1,10,3,10,289,8,10,1,10,1,10,1,11,1,
        11,1,11,1,11,1,11,1,11,5,11,299,8,11,10,11,12,11,302,9,11,1,12,1,
        12,1,12,1,12,1,12,1,12,5,12,310,8,12,10,12,12,12,313,9,12,1,12,1,
        12,1,13,1,13,1,13,1,13,5,13,321,8,13,10,13,12,13,324,9,13,1,13,1,
        13,1,13,5,13,329,8,13,10,13,12,13,332,9,13,3,13,334,8,13,1,14,1,
        14,5,14,338,8,14,10,14,12,14,341,9,14,1,14,3,14,344,8,14,1,15,1,
        15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,
        19,1,20,3,20,375,8,20,1,20,1,20,3,20,379,8,20,1,20,1,20,3,20,383,
        8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,392,8,21,5,21,394,8,
        21,10,21,12,21,397,9,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,5,22,
        406,8,22,10,22,12,22,409,9,22,1,22,1,22,1,23,1,23,1,24,1,24,1,25,
        1,25,1,25,1,25,1,25,1,25,3,25,423,8,25,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,437,8,26,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,3,27,461,8,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,5,27,517,
        8,27,10,27,12,27,520,9,27,1,28,1,28,1,28,1,28,3,28,526,8,28,3,28,
        528,8,28,1,29,3,29,531,8,29,1,29,1,29,1,29,3,29,536,8,29,1,29,1,
        29,4,29,540,8,29,11,29,12,29,541,1,29,3,29,545,8,29,1,29,1,29,1,
        29,3,29,550,8,29,1,29,1,29,4,29,554,8,29,11,29,12,29,555,1,29,3,
        29,559,8,29,1,29,1,29,1,29,3,29,564,8,29,3,29,566,8,29,1,30,1,30,
        1,31,4,31,571,8,31,11,31,12,31,572,1,31,4,31,576,8,31,11,31,12,31,
        577,1,31,1,31,1,31,1,32,1,32,4,32,585,8,32,11,32,12,32,586,1,33,
        4,33,590,8,33,11,33,12,33,591,1,33,1,33,1,34,4,34,597,8,34,11,34,
        12,34,598,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,5,35,609,8,35,
        10,35,12,35,612,9,35,1,35,1,35,1,36,1,36,3,36,618,8,36,1,37,1,37,
        1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,
        1,40,1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,3,43,645,8,43,
        1,44,1,44,1,44,1,44,1,44,4,44,652,8,44,11,44,12,44,653,1,45,1,45,
        1,45,1,45,4,45,660,8,45,11,45,12,45,661,1,45,1,45,1,45,3,45,667,
        8,45,1,45,1,45,1,45,1,45,3,45,673,8,45,1,46,1,46,1,46,1,46,1,46,
        4,46,680,8,46,11,46,12,46,681,1,46,1,46,1,46,3,46,687,8,46,1,47,
        1,47,1,47,3,47,692,8,47,1,47,1,47,1,47,3,47,697,8,47,5,47,699,8,
        47,10,47,12,47,702,9,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,4,48,
        711,8,48,11,48,12,48,712,1,49,1,49,1,49,1,49,1,50,5,50,720,8,50,
        10,50,12,50,723,9,50,1,50,1,50,1,51,1,51,1,52,1,52,1,52,0,3,18,22,
        54,53,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,
        86,88,90,92,94,96,98,100,102,104,0,3,1,0,29,30,1,0,52,54,2,0,21,
        24,57,57,811,0,129,1,0,0,0,2,135,1,0,0,0,4,199,1,0,0,0,6,225,1,0,
        0,0,8,227,1,0,0,0,10,247,1,0,0,0,12,249,1,0,0,0,14,253,1,0,0,0,16,
        264,1,0,0,0,18,268,1,0,0,0,20,285,1,0,0,0,22,292,1,0,0,0,24,303,
        1,0,0,0,26,333,1,0,0,0,28,335,1,0,0,0,30,345,1,0,0,0,32,351,1,0,
        0,0,34,358,1,0,0,0,36,361,1,0,0,0,38,367,1,0,0,0,40,374,1,0,0,0,
        42,384,1,0,0,0,44,400,1,0,0,0,46,412,1,0,0,0,48,414,1,0,0,0,50,422,
        1,0,0,0,52,436,1,0,0,0,54,460,1,0,0,0,56,527,1,0,0,0,58,565,1,0,
        0,0,60,567,1,0,0,0,62,570,1,0,0,0,64,582,1,0,0,0,66,589,1,0,0,0,
        68,596,1,0,0,0,70,602,1,0,0,0,72,617,1,0,0,0,74,619,1,0,0,0,76,625,
        1,0,0,0,78,629,1,0,0,0,80,632,1,0,0,0,82,635,1,0,0,0,84,638,1,0,
        0,0,86,644,1,0,0,0,88,646,1,0,0,0,90,672,1,0,0,0,92,674,1,0,0,0,
        94,688,1,0,0,0,96,705,1,0,0,0,98,714,1,0,0,0,100,721,1,0,0,0,102,
        726,1,0,0,0,104,728,1,0,0,0,106,130,3,104,52,0,107,110,3,70,35,0,
        108,110,3,8,4,0,109,107,1,0,0,0,109,108,1,0,0,0,110,112,1,0,0,0,
        111,113,5,50,0,0,112,111,1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,
        114,115,1,0,0,0,115,130,1,0,0,0,116,118,3,50,25,0,117,119,5,50,0,
        0,118,117,1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,
        0,121,130,1,0,0,0,122,124,3,98,49,0,123,125,5,50,0,0,124,123,1,0,
        0,0,125,126,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,130,1,0,
        0,0,128,130,3,6,3,0,129,106,1,0,0,0,129,109,1,0,0,0,129,116,1,0,
        0,0,129,122,1,0,0,0,129,128,1,0,0,0,130,131,1,0,0,0,131,129,1,0,
        0,0,131,132,1,0,0,0,132,133,1,0,0,0,133,134,5,0,0,1,134,1,1,0,0,
        0,135,139,5,27,0,0,136,138,3,4,2,0,137,136,1,0,0,0,138,141,1,0,0,
        0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,
        0,142,143,5,28,0,0,143,3,1,0,0,0,144,146,3,54,27,0,145,147,5,50,
        0,0,146,145,1,0,0,0,147,148,1,0,0,0,148,146,1,0,0,0,148,149,1,0,
        0,0,149,200,1,0,0,0,150,152,3,50,25,0,151,153,5,50,0,0,152,151,1,
        0,0,0,153,154,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,200,1,
        0,0,0,156,200,3,104,52,0,157,159,3,42,21,0,158,160,5,50,0,0,159,
        158,1,0,0,0,160,161,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,
        200,1,0,0,0,163,165,3,44,22,0,164,166,5,50,0,0,165,164,1,0,0,0,166,
        167,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,200,1,0,0,0,169,
        200,3,2,1,0,170,200,3,28,14,0,171,200,3,36,18,0,172,200,3,38,19,
        0,173,175,3,72,36,0,174,176,5,50,0,0,175,174,1,0,0,0,176,177,1,0,
        0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,200,1,0,0,0,179,181,3,56,
        28,0,180,182,5,50,0,0,181,180,1,0,0,0,182,183,1,0,0,0,183,181,1,
        0,0,0,183,184,1,0,0,0,184,200,1,0,0,0,185,200,3,6,3,0,186,200,3,
        24,12,0,187,189,3,86,43,0,188,190,5,50,0,0,189,188,1,0,0,0,190,191,
        1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,200,1,0,0,0,193,195,
        3,10,5,0,194,196,5,50,0,0,195,194,1,0,0,0,196,197,1,0,0,0,197,195,
        1,0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,144,1,0,0,0,199,150,
        1,0,0,0,199,156,1,0,0,0,199,157,1,0,0,0,199,163,1,0,0,0,199,169,
        1,0,0,0,199,170,1,0,0,0,199,171,1,0,0,0,199,172,1,0,0,0,199,173,
        1,0,0,0,199,179,1,0,0,0,199,185,1,0,0,0,199,186,1,0,0,0,199,187,
        1,0,0,0,199,193,1,0,0,0,200,5,1,0,0,0,201,204,3,100,50,0,202,204,
        3,64,32,0,203,201,1,0,0,0,203,202,1,0,0,0,204,205,1,0,0,0,205,206,
        5,57,0,0,206,208,5,25,0,0,207,209,3,18,9,0,208,207,1,0,0,0,208,209,
        1,0,0,0,209,210,1,0,0,0,210,211,5,26,0,0,211,212,3,2,1,0,212,226,
        1,0,0,0,213,216,3,100,50,0,214,216,3,64,32,0,215,213,1,0,0,0,215,
        214,1,0,0,0,216,217,1,0,0,0,217,218,5,57,0,0,218,220,5,25,0,0,219,
        221,3,18,9,0,220,219,1,0,0,0,220,221,1,0,0,0,221,222,1,0,0,0,222,
        223,5,26,0,0,223,224,5,50,0,0,224,226,1,0,0,0,225,203,1,0,0,0,225,
        215,1,0,0,0,226,7,1,0,0,0,227,228,5,1,0,0,228,229,5,57,0,0,229,240,
        5,27,0,0,230,231,3,100,50,0,231,232,3,102,51,0,232,235,1,0,0,0,233,
        235,3,88,44,0,234,230,1,0,0,0,234,233,1,0,0,0,235,236,1,0,0,0,236,
        237,5,50,0,0,237,239,1,0,0,0,238,234,1,0,0,0,239,242,1,0,0,0,240,
        238,1,0,0,0,240,241,1,0,0,0,241,243,1,0,0,0,242,240,1,0,0,0,243,
        244,5,28,0,0,244,9,1,0,0,0,245,248,3,12,6,0,246,248,3,16,8,0,247,
        245,1,0,0,0,247,246,1,0,0,0,248,11,1,0,0,0,249,250,5,1,0,0,250,251,
        5,57,0,0,251,252,5,57,0,0,252,13,1,0,0,0,253,254,5,57,0,0,254,255,
        5,2,0,0,255,261,5,57,0,0,256,257,5,3,0,0,257,258,5,52,0,0,258,260,
        5,4,0,0,259,256,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,
        1,0,0,0,262,15,1,0,0,0,263,261,1,0,0,0,264,265,3,14,7,0,265,266,
        5,5,0,0,266,267,3,54,27,0,267,17,1,0,0,0,268,271,6,9,-1,0,269,272,
        3,64,32,0,270,272,3,100,50,0,271,269,1,0,0,0,271,270,1,0,0,0,272,
        275,1,0,0,0,273,276,3,68,34,0,274,276,3,102,51,0,275,273,1,0,0,0,
        275,274,1,0,0,0,276,282,1,0,0,0,277,278,10,1,0,0,278,279,5,51,0,
        0,279,281,3,18,9,2,280,277,1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,
        0,282,283,1,0,0,0,283,19,1,0,0,0,284,282,1,0,0,0,285,286,5,57,0,
        0,286,288,5,25,0,0,287,289,3,22,11,0,288,287,1,0,0,0,288,289,1,0,
        0,0,289,290,1,0,0,0,290,291,5,26,0,0,291,21,1,0,0,0,292,293,6,11,
        -1,0,293,294,3,54,27,0,294,300,1,0,0,0,295,296,10,1,0,0,296,297,
        5,51,0,0,297,299,3,22,11,2,298,295,1,0,0,0,299,302,1,0,0,0,300,298,
        1,0,0,0,300,301,1,0,0,0,301,23,1,0,0,0,302,300,1,0,0,0,303,304,5,
        6,0,0,304,305,5,25,0,0,305,306,3,54,27,0,306,307,5,26,0,0,307,311,
        5,27,0,0,308,310,3,26,13,0,309,308,1,0,0,0,310,313,1,0,0,0,311,309,
        1,0,0,0,311,312,1,0,0,0,312,314,1,0,0,0,313,311,1,0,0,0,314,315,
        5,28,0,0,315,25,1,0,0,0,316,317,5,7,0,0,317,318,3,60,30,0,318,322,
        5,49,0,0,319,321,3,4,2,0,320,319,1,0,0,0,321,324,1,0,0,0,322,320,
        1,0,0,0,322,323,1,0,0,0,323,334,1,0,0,0,324,322,1,0,0,0,325,326,
        5,8,0,0,326,330,5,49,0,0,327,329,3,4,2,0,328,327,1,0,0,0,329,332,
        1,0,0,0,330,328,1,0,0,0,330,331,1,0,0,0,331,334,1,0,0,0,332,330,
        1,0,0,0,333,316,1,0,0,0,333,325,1,0,0,0,334,27,1,0,0,0,335,339,3,
        30,15,0,336,338,3,32,16,0,337,336,1,0,0,0,338,341,1,0,0,0,339,337,
        1,0,0,0,339,340,1,0,0,0,340,343,1,0,0,0,341,339,1,0,0,0,342,344,
        3,34,17,0,343,342,1,0,0,0,343,344,1,0,0,0,344,29,1,0,0,0,345,346,
        5,9,0,0,346,347,5,25,0,0,347,348,3,54,27,0,348,349,5,26,0,0,349,
        350,3,2,1,0,350,31,1,0,0,0,351,352,5,10,0,0,352,353,5,9,0,0,353,
        354,5,25,0,0,354,355,3,54,27,0,355,356,5,26,0,0,356,357,3,2,1,0,
        357,33,1,0,0,0,358,359,5,10,0,0,359,360,3,2,1,0,360,35,1,0,0,0,361,
        362,5,11,0,0,362,363,5,25,0,0,363,364,3,54,27,0,364,365,5,26,0,0,
        365,366,3,2,1,0,366,37,1,0,0,0,367,368,5,12,0,0,368,369,5,25,0,0,
        369,370,3,40,20,0,370,371,5,26,0,0,371,372,3,2,1,0,372,39,1,0,0,
        0,373,375,3,50,25,0,374,373,1,0,0,0,374,375,1,0,0,0,375,376,1,0,
        0,0,376,378,5,50,0,0,377,379,3,54,27,0,378,377,1,0,0,0,378,379,1,
        0,0,0,379,380,1,0,0,0,380,382,5,50,0,0,381,383,3,54,27,0,382,381,
        1,0,0,0,382,383,1,0,0,0,383,41,1,0,0,0,384,385,5,13,0,0,385,386,
        5,25,0,0,386,395,3,46,23,0,387,391,5,51,0,0,388,392,3,54,27,0,389,
        392,3,48,24,0,390,392,3,14,7,0,391,388,1,0,0,0,391,389,1,0,0,0,391,
        390,1,0,0,0,392,394,1,0,0,0,393,387,1,0,0,0,394,397,1,0,0,0,395,
        393,1,0,0,0,395,396,1,0,0,0,396,398,1,0,0,0,397,395,1,0,0,0,398,
        399,5,26,0,0,399,43,1,0,0,0,400,401,5,14,0,0,401,402,5,25,0,0,402,
        407,3,46,23,0,403,404,5,51,0,0,404,406,3,68,34,0,405,403,1,0,0,0,
        406,409,1,0,0,0,407,405,1,0,0,0,407,408,1,0,0,0,408,410,1,0,0,0,
        409,407,1,0,0,0,410,411,5,26,0,0,411,45,1,0,0,0,412,413,5,55,0,0,
        413,47,1,0,0,0,414,415,5,55,0,0,415,49,1,0,0,0,416,417,3,52,26,0,
        417,418,5,5,0,0,418,419,3,54,27,0,419,423,1,0,0,0,420,423,3,52,26,
        0,421,423,3,98,49,0,422,416,1,0,0,0,422,420,1,0,0,0,422,421,1,0,
        0,0,423,51,1,0,0,0,424,437,3,102,51,0,425,426,3,100,50,0,426,427,
        3,102,51,0,427,437,1,0,0,0,428,429,3,64,32,0,429,430,3,102,51,0,
        430,437,1,0,0,0,431,437,3,66,33,0,432,433,5,25,0,0,433,434,3,52,
        26,0,434,435,5,26,0,0,435,437,1,0,0,0,436,424,1,0,0,0,436,425,1,
        0,0,0,436,428,1,0,0,0,436,431,1,0,0,0,436,432,1,0,0,0,437,53,1,0,
        0,0,438,439,6,27,-1,0,439,461,3,58,29,0,440,461,3,102,51,0,441,461,
        3,66,33,0,442,461,3,68,34,0,443,444,5,48,0,0,444,461,3,54,27,30,
        445,446,5,45,0,0,446,461,3,54,27,29,447,448,5,25,0,0,448,449,3,54,
        27,0,449,450,5,26,0,0,450,461,1,0,0,0,451,461,3,62,31,0,452,461,
        3,78,39,0,453,461,3,80,40,0,454,461,3,82,41,0,455,461,3,84,42,0,
        456,461,3,20,10,0,457,461,3,56,28,0,458,461,3,96,48,0,459,461,3,
        48,24,0,460,438,1,0,0,0,460,440,1,0,0,0,460,441,1,0,0,0,460,442,
        1,0,0,0,460,443,1,0,0,0,460,445,1,0,0,0,460,447,1,0,0,0,460,451,
        1,0,0,0,460,452,1,0,0,0,460,453,1,0,0,0,460,454,1,0,0,0,460,455,
        1,0,0,0,460,456,1,0,0,0,460,457,1,0,0,0,460,458,1,0,0,0,460,459,
        1,0,0,0,461,518,1,0,0,0,462,463,10,28,0,0,463,464,5,32,0,0,464,517,
        3,54,27,29,465,466,10,27,0,0,466,467,5,33,0,0,467,517,3,54,27,28,
        468,469,10,26,0,0,469,470,5,31,0,0,470,517,3,54,27,27,471,472,10,
        25,0,0,472,473,5,30,0,0,473,517,3,54,27,26,474,475,10,24,0,0,475,
        476,5,29,0,0,476,517,3,54,27,25,477,478,10,23,0,0,478,479,5,40,0,
        0,479,517,3,54,27,24,480,481,10,22,0,0,481,482,5,41,0,0,482,517,
        3,54,27,23,483,484,10,21,0,0,484,485,5,42,0,0,485,517,3,54,27,22,
        486,487,10,20,0,0,487,488,5,43,0,0,488,517,3,54,27,21,489,490,10,
        19,0,0,490,491,5,44,0,0,491,517,3,54,27,20,492,493,10,18,0,0,493,
        494,5,38,0,0,494,517,3,54,27,19,495,496,10,17,0,0,496,497,5,39,0,
        0,497,517,3,54,27,18,498,499,10,16,0,0,499,500,5,46,0,0,500,517,
        3,54,27,17,501,502,10,15,0,0,502,503,5,47,0,0,503,517,3,54,27,16,
        504,505,10,14,0,0,505,506,5,34,0,0,506,517,3,54,27,15,507,508,10,
        13,0,0,508,509,5,35,0,0,509,517,3,54,27,14,510,511,10,12,0,0,511,
        512,5,36,0,0,512,517,3,54,27,13,513,514,10,11,0,0,514,515,5,37,0,
        0,515,517,3,54,27,12,516,462,1,0,0,0,516,465,1,0,0,0,516,468,1,0,
        0,0,516,471,1,0,0,0,516,474,1,0,0,0,516,477,1,0,0,0,516,480,1,0,
        0,0,516,483,1,0,0,0,516,486,1,0,0,0,516,489,1,0,0,0,516,492,1,0,
        0,0,516,495,1,0,0,0,516,498,1,0,0,0,516,501,1,0,0,0,516,504,1,0,
        0,0,516,507,1,0,0,0,516,510,1,0,0,0,516,513,1,0,0,0,517,520,1,0,
        0,0,518,516,1,0,0,0,518,519,1,0,0,0,519,55,1,0,0,0,520,518,1,0,0,
        0,521,528,5,15,0,0,522,528,5,16,0,0,523,525,5,17,0,0,524,526,3,54,
        27,0,525,524,1,0,0,0,525,526,1,0,0,0,526,528,1,0,0,0,527,521,1,0,
        0,0,527,522,1,0,0,0,527,523,1,0,0,0,528,57,1,0,0,0,529,531,7,0,0,
        0,530,529,1,0,0,0,530,531,1,0,0,0,531,535,1,0,0,0,532,536,3,60,30,
        0,533,536,3,102,51,0,534,536,3,66,33,0,535,532,1,0,0,0,535,533,1,
        0,0,0,535,534,1,0,0,0,536,566,1,0,0,0,537,538,5,29,0,0,538,540,5,
        30,0,0,539,537,1,0,0,0,540,541,1,0,0,0,541,539,1,0,0,0,541,542,1,
        0,0,0,542,544,1,0,0,0,543,545,5,29,0,0,544,543,1,0,0,0,544,545,1,
        0,0,0,545,549,1,0,0,0,546,550,3,60,30,0,547,550,3,102,51,0,548,550,
        3,66,33,0,549,546,1,0,0,0,549,547,1,0,0,0,549,548,1,0,0,0,550,566,
        1,0,0,0,551,552,5,30,0,0,552,554,5,29,0,0,553,551,1,0,0,0,554,555,
        1,0,0,0,555,553,1,0,0,0,555,556,1,0,0,0,556,558,1,0,0,0,557,559,
        5,30,0,0,558,557,1,0,0,0,558,559,1,0,0,0,559,563,1,0,0,0,560,564,
        3,60,30,0,561,564,3,102,51,0,562,564,3,66,33,0,563,560,1,0,0,0,563,
        561,1,0,0,0,563,562,1,0,0,0,564,566,1,0,0,0,565,530,1,0,0,0,565,
        539,1,0,0,0,565,553,1,0,0,0,566,59,1,0,0,0,567,568,7,1,0,0,568,61,
        1,0,0,0,569,571,5,25,0,0,570,569,1,0,0,0,571,572,1,0,0,0,572,570,
        1,0,0,0,572,573,1,0,0,0,573,575,1,0,0,0,574,576,3,100,50,0,575,574,
        1,0,0,0,576,577,1,0,0,0,577,575,1,0,0,0,577,578,1,0,0,0,578,579,
        1,0,0,0,579,580,5,26,0,0,580,581,3,54,27,0,581,63,1,0,0,0,582,584,
        3,100,50,0,583,585,5,31,0,0,584,583,1,0,0,0,585,586,1,0,0,0,586,
        584,1,0,0,0,586,587,1,0,0,0,587,65,1,0,0,0,588,590,5,31,0,0,589,
        588,1,0,0,0,590,591,1,0,0,0,591,589,1,0,0,0,591,592,1,0,0,0,592,
        593,1,0,0,0,593,594,3,102,51,0,594,67,1,0,0,0,595,597,5,42,0,0,596,
        595,1,0,0,0,597,598,1,0,0,0,598,596,1,0,0,0,598,599,1,0,0,0,599,
        600,1,0,0,0,600,601,3,102,51,0,601,69,1,0,0,0,602,603,5,18,0,0,603,
        604,5,57,0,0,604,605,5,27,0,0,605,610,5,57,0,0,606,607,5,51,0,0,
        607,609,5,57,0,0,608,606,1,0,0,0,609,612,1,0,0,0,610,608,1,0,0,0,
        610,611,1,0,0,0,611,613,1,0,0,0,612,610,1,0,0,0,613,614,5,28,0,0,
        614,71,1,0,0,0,615,618,3,74,37,0,616,618,3,76,38,0,617,615,1,0,0,
        0,617,616,1,0,0,0,618,73,1,0,0,0,619,620,5,18,0,0,620,621,5,57,0,
        0,621,622,5,57,0,0,622,623,5,5,0,0,623,624,5,57,0,0,624,75,1,0,0,
        0,625,626,5,18,0,0,626,627,5,57,0,0,627,628,5,57,0,0,628,77,1,0,
        0,0,629,630,3,52,26,0,630,631,5,58,0,0,631,79,1,0,0,0,632,633,3,
        52,26,0,633,634,5,59,0,0,634,81,1,0,0,0,635,636,5,58,0,0,636,637,
        3,52,26,0,637,83,1,0,0,0,638,639,5,59,0,0,639,640,3,52,26,0,640,
        85,1,0,0,0,641,645,3,88,44,0,642,645,3,90,45,0,643,645,3,92,46,0,
        644,641,1,0,0,0,644,642,1,0,0,0,644,643,1,0,0,0,645,87,1,0,0,0,646,
        647,3,100,50,0,647,651,3,102,51,0,648,649,5,3,0,0,649,650,5,52,0,
        0,650,652,5,4,0,0,651,648,1,0,0,0,652,653,1,0,0,0,653,651,1,0,0,
        0,653,654,1,0,0,0,654,89,1,0,0,0,655,659,3,102,51,0,656,657,5,3,
        0,0,657,658,5,52,0,0,658,660,5,4,0,0,659,656,1,0,0,0,660,661,1,0,
        0,0,661,659,1,0,0,0,661,662,1,0,0,0,662,663,1,0,0,0,663,666,5,5,
        0,0,664,667,3,54,27,0,665,667,3,94,47,0,666,664,1,0,0,0,666,665,
        1,0,0,0,667,673,1,0,0,0,668,669,3,102,51,0,669,670,5,5,0,0,670,671,
        3,94,47,0,671,673,1,0,0,0,672,655,1,0,0,0,672,668,1,0,0,0,673,91,
        1,0,0,0,674,675,3,100,50,0,675,679,3,102,51,0,676,677,5,3,0,0,677,
        678,5,52,0,0,678,680,5,4,0,0,679,676,1,0,0,0,680,681,1,0,0,0,681,
        679,1,0,0,0,681,682,1,0,0,0,682,683,1,0,0,0,683,686,5,5,0,0,684,
        687,3,94,47,0,685,687,3,48,24,0,686,684,1,0,0,0,686,685,1,0,0,0,
        687,93,1,0,0,0,688,691,5,27,0,0,689,692,3,54,27,0,690,692,3,94,47,
        0,691,689,1,0,0,0,691,690,1,0,0,0,692,700,1,0,0,0,693,696,5,51,0,
        0,694,697,3,54,27,0,695,697,3,94,47,0,696,694,1,0,0,0,696,695,1,
        0,0,0,697,699,1,0,0,0,698,693,1,0,0,0,699,702,1,0,0,0,700,698,1,
        0,0,0,700,701,1,0,0,0,701,703,1,0,0,0,702,700,1,0,0,0,703,704,5,
        28,0,0,704,95,1,0,0,0,705,710,3,102,51,0,706,707,5,3,0,0,707,708,
        3,54,27,0,708,709,5,4,0,0,709,711,1,0,0,0,710,706,1,0,0,0,711,712,
        1,0,0,0,712,710,1,0,0,0,712,713,1,0,0,0,713,97,1,0,0,0,714,715,5,
        19,0,0,715,716,3,100,50,0,716,717,5,57,0,0,717,99,1,0,0,0,718,720,
        5,20,0,0,719,718,1,0,0,0,720,723,1,0,0,0,721,719,1,0,0,0,721,722,
        1,0,0,0,722,724,1,0,0,0,723,721,1,0,0,0,724,725,7,2,0,0,725,101,
        1,0,0,0,726,727,5,57,0,0,727,103,1,0,0,0,728,729,5,60,0,0,729,105,
        1,0,0,0,77,109,114,120,126,129,131,139,148,154,161,167,177,183,191,
        197,199,203,208,215,220,225,234,240,247,261,271,275,282,288,300,
        311,322,330,333,339,343,374,378,382,391,395,407,422,436,460,516,
        518,525,527,530,535,541,544,549,555,558,563,565,572,577,586,591,
        598,610,617,644,653,661,666,672,681,686,691,696,700,712,721
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'.'", "'['", "']'", "'='", 
                     "'switch'", "'case'", "'default'", "'if'", "'else'", 
                     "'while'", "'for'", "'printf'", "'scanf'", "'break'", 
                     "'continue'", "'return'", "'enum'", "'typedef'", "'const'", 
                     "'int'", "'float'", "'char'", "'void'", "'('", "')'", 
                     "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "'<<'", "'>>'", 
                     "'&'", "'|'", "'^'", "'~'", "'&&'", "'||'", "'!'", 
                     "':'", "';'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
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
                      "COMMA", "INT", "FLOAT", "CHAR", "STRING", "WHITESPACE", 
                      "IDENTIFIER", "INCREMENT", "DECREMENT", "COMMENT", 
                      "BLOCKCOMMENT", "LINECOMMENT" ]

    RULE_program = 0
    RULE_scope = 1
    RULE_statement = 2
    RULE_function = 3
    RULE_structDefinition = 4
    RULE_structStatement = 5
    RULE_structVariable = 6
    RULE_structMember = 7
    RULE_structAssignment = 8
    RULE_functionParams = 9
    RULE_functionCall = 10
    RULE_callParams = 11
    RULE_switchStatement = 12
    RULE_switchCase = 13
    RULE_conditional = 14
    RULE_ifStatement = 15
    RULE_elseIfStatement = 16
    RULE_elseStatement = 17
    RULE_whileLoop = 18
    RULE_forLoop = 19
    RULE_forCondition = 20
    RULE_printfStatement = 21
    RULE_scanfStatement = 22
    RULE_formatSpecifier = 23
    RULE_string = 24
    RULE_variable = 25
    RULE_lvalue = 26
    RULE_rvalue = 27
    RULE_jumpStatement = 28
    RULE_unaryExpression = 29
    RULE_literal = 30
    RULE_explicitConversion = 31
    RULE_pointer = 32
    RULE_deref = 33
    RULE_addr = 34
    RULE_enumDeclaration = 35
    RULE_enumStatement = 36
    RULE_enumVariableDefinition = 37
    RULE_enumVariableDeclaration = 38
    RULE_postFixIncrement = 39
    RULE_postFixDecrement = 40
    RULE_preFixIncrement = 41
    RULE_preFixDecrement = 42
    RULE_arrayStatement = 43
    RULE_arrayDeclaration = 44
    RULE_arrayAssignment = 45
    RULE_arrayDefinition = 46
    RULE_array = 47
    RULE_arrayElement = 48
    RULE_typedef = 49
    RULE_type = 50
    RULE_identifier = 51
    RULE_comment = 52

    ruleNames =  [ "program", "scope", "statement", "function", "structDefinition", 
                   "structStatement", "structVariable", "structMember", 
                   "structAssignment", "functionParams", "functionCall", 
                   "callParams", "switchStatement", "switchCase", "conditional", 
                   "ifStatement", "elseIfStatement", "elseStatement", "whileLoop", 
                   "forLoop", "forCondition", "printfStatement", "scanfStatement", 
                   "formatSpecifier", "string", "variable", "lvalue", "rvalue", 
                   "jumpStatement", "unaryExpression", "literal", "explicitConversion", 
                   "pointer", "deref", "addr", "enumDeclaration", "enumStatement", 
                   "enumVariableDefinition", "enumVariableDeclaration", 
                   "postFixIncrement", "postFixDecrement", "preFixIncrement", 
                   "preFixDecrement", "arrayStatement", "arrayDeclaration", 
                   "arrayAssignment", "arrayDefinition", "array", "arrayElement", 
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
    STRING=55
    WHITESPACE=56
    IDENTIFIER=57
    INCREMENT=58
    DECREMENT=59
    COMMENT=60
    BLOCKCOMMENT=61
    LINECOMMENT=62

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


        def enumDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.EnumDeclarationContext)
            else:
                return self.getTypedRuleContext(GrammarParser.EnumDeclarationContext,i)


        def structDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StructDefinitionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StructDefinitionContext,i)


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
            self.state = 129 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 129
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 109
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [18]:
                        self.state = 107
                        self.enumDeclaration()
                        pass
                    elif token in [1]:
                        self.state = 108
                        self.structDefinition()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 112 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 111
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 114 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==50):
                            break

                    pass

                elif la_ == 3:
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
                        if not (_la==50):
                            break

                    pass

                elif la_ == 4:
                    self.state = 122
                    self.typedef()
                    self.state = 124 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 123
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 126 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==50):
                            break

                    pass

                elif la_ == 5:
                    self.state = 128
                    self.function()
                    pass


                self.state = 131 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1297036694897033218) != 0)):
                    break

            self.state = 133
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
            self.state = 135
            self.match(GrammarParser.LBRACE)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                self.state = 136
                self.statement()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
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


        def scanfStatement(self):
            return self.getTypedRuleContext(GrammarParser.ScanfStatementContext,0)


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


        def arrayStatement(self):
            return self.getTypedRuleContext(GrammarParser.ArrayStatementContext,0)


        def structStatement(self):
            return self.getTypedRuleContext(GrammarParser.StructStatementContext,0)


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
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.rvalue(0)
                self.state = 146 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 145
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 148 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.variable()
                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 151
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 154 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.printfStatement()
                self.state = 159 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 158
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 161 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.scanfStatement()
                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 164
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 167 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 169
                self.scope()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 170
                self.conditional()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 171
                self.whileLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 172
                self.forLoop()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 173
                self.enumStatement()
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 174
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 177 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 179
                self.jumpStatement()
                self.state = 181 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 180
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 183 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 185
                self.function()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 186
                self.switchStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 187
                self.arrayStatement()
                self.state = 189 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 188
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 191 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 193
                self.structStatement()
                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 194
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 197 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

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
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 201
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 202
                    self.pointer()
                    pass


                self.state = 205
                self.match(GrammarParser.IDENTIFIER)
                self.state = 206
                self.match(GrammarParser.LPAREN)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                    self.state = 207
                    self.functionParams(0)


                self.state = 210
                self.match(GrammarParser.RPAREN)
                self.state = 211
                self.scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 213
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 214
                    self.pointer()
                    pass


                self.state = 217
                self.match(GrammarParser.IDENTIFIER)
                self.state = 218
                self.match(GrammarParser.LPAREN)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                    self.state = 219
                    self.functionParams(0)


                self.state = 222
                self.match(GrammarParser.RPAREN)
                self.state = 223
                self.match(GrammarParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(GrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GrammarParser.RBRACE, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def arrayDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ArrayDeclarationContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ArrayDeclarationContext,i)


        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.TypeContext)
            else:
                return self.getTypedRuleContext(GrammarParser.TypeContext,i)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(GrammarParser.IdentifierContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_structDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDefinition" ):
                listener.enterStructDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDefinition" ):
                listener.exitStructDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefinition" ):
                return visitor.visitStructDefinition(self)
            else:
                return visitor.visitChildren(self)




    def structDefinition(self):

        localctx = GrammarParser.StructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(GrammarParser.T__0)
            self.state = 228
            self.match(GrammarParser.IDENTIFIER)
            self.state = 229
            self.match(GrammarParser.LBRACE)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                self.state = 234
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 230
                    self.type_()
                    self.state = 231
                    self.identifier()
                    pass

                elif la_ == 2:
                    self.state = 233
                    self.arrayDeclaration()
                    pass


                self.state = 236
                self.match(GrammarParser.SEMICOLON)
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 243
            self.match(GrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structVariable(self):
            return self.getTypedRuleContext(GrammarParser.StructVariableContext,0)


        def structAssignment(self):
            return self.getTypedRuleContext(GrammarParser.StructAssignmentContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_structStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructStatement" ):
                listener.enterStructStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructStatement" ):
                listener.exitStructStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructStatement" ):
                return visitor.visitStructStatement(self)
            else:
                return visitor.visitChildren(self)




    def structStatement(self):

        localctx = GrammarParser.StructStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_structStatement)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.structVariable()
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.structAssignment()
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


    class StructVariableContext(ParserRuleContext):
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
            return GrammarParser.RULE_structVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructVariable" ):
                listener.enterStructVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructVariable" ):
                listener.exitStructVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructVariable" ):
                return visitor.visitStructVariable(self)
            else:
                return visitor.visitChildren(self)




    def structVariable(self):

        localctx = GrammarParser.StructVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_structVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(GrammarParser.T__0)
            self.state = 250
            self.match(GrammarParser.IDENTIFIER)
            self.state = 251
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENTIFIER)
            else:
                return self.getToken(GrammarParser.IDENTIFIER, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.INT)
            else:
                return self.getToken(GrammarParser.INT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_structMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructMember" ):
                listener.enterStructMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructMember" ):
                listener.exitStructMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructMember" ):
                return visitor.visitStructMember(self)
            else:
                return visitor.visitChildren(self)




    def structMember(self):

        localctx = GrammarParser.StructMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_structMember)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(GrammarParser.IDENTIFIER)
            self.state = 254
            self.match(GrammarParser.T__1)
            self.state = 255
            self.match(GrammarParser.IDENTIFIER)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 256
                self.match(GrammarParser.T__2)
                self.state = 257
                self.match(GrammarParser.INT)
                self.state = 258
                self.match(GrammarParser.T__3)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structMember(self):
            return self.getTypedRuleContext(GrammarParser.StructMemberContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_structAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructAssignment" ):
                listener.enterStructAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructAssignment" ):
                listener.exitStructAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructAssignment" ):
                return visitor.visitStructAssignment(self)
            else:
                return visitor.visitChildren(self)




    def structAssignment(self):

        localctx = GrammarParser.StructAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.structMember()
            self.state = 265
            self.match(GrammarParser.T__4)
            self.state = 266
            self.rvalue(0)
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_functionParams, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 269
                self.pointer()
                pass

            elif la_ == 2:
                self.state = 270
                self.type_()
                pass


            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 273
                self.addr()
                pass
            elif token in [57]:
                self.state = 274
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.FunctionParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParams)
                    self.state = 277
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 278
                    self.match(GrammarParser.COMMA)
                    self.state = 279
                    self.functionParams(2) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(GrammarParser.IDENTIFIER)
            self.state = 286
            self.match(GrammarParser.LPAREN)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 287
                self.callParams(0)


            self.state = 290
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_callParams, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.rvalue(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CallParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callParams)
                    self.state = 295
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 296
                    self.match(GrammarParser.COMMA)
                    self.state = 297
                    self.callParams(2) 
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(GrammarParser.T__5)
            self.state = 304
            self.match(GrammarParser.LPAREN)
            self.state = 305
            self.rvalue(0)
            self.state = 306
            self.match(GrammarParser.RPAREN)
            self.state = 307
            self.match(GrammarParser.LBRACE)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 308
                self.switchCase()
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 314
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
        self.enterRule(localctx, 26, self.RULE_switchCase)
        self._la = 0 # Token type
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(GrammarParser.T__6)
                self.state = 317
                self.literal()
                self.state = 318
                self.match(GrammarParser.COLON)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                    self.state = 319
                    self.statement()
                    self.state = 324
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(GrammarParser.T__7)
                self.state = 326
                self.match(GrammarParser.COLON)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                    self.state = 327
                    self.statement()
                    self.state = 332
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
        self.enterRule(localctx, 28, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.ifStatement()
            self.state = 339
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 336
                    self.elseIfStatement() 
                self.state = 341
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 342
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
        self.enterRule(localctx, 30, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(GrammarParser.T__8)
            self.state = 346
            self.match(GrammarParser.LPAREN)
            self.state = 347
            self.rvalue(0)
            self.state = 348
            self.match(GrammarParser.RPAREN)
            self.state = 349
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
        self.enterRule(localctx, 32, self.RULE_elseIfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(GrammarParser.T__9)
            self.state = 352
            self.match(GrammarParser.T__8)
            self.state = 353
            self.match(GrammarParser.LPAREN)
            self.state = 354
            self.rvalue(0)
            self.state = 355
            self.match(GrammarParser.RPAREN)
            self.state = 356
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
        self.enterRule(localctx, 34, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(GrammarParser.T__9)
            self.state = 359
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
        self.enterRule(localctx, 36, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(GrammarParser.T__10)
            self.state = 362
            self.match(GrammarParser.LPAREN)
            self.state = 363
            self.rvalue(0)
            self.state = 364
            self.match(GrammarParser.RPAREN)
            self.state = 365
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
        self.enterRule(localctx, 38, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(GrammarParser.T__11)
            self.state = 368
            self.match(GrammarParser.LPAREN)
            self.state = 369
            self.forCondition()
            self.state = 370
            self.match(GrammarParser.RPAREN)
            self.state = 371
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
        self.enterRule(localctx, 40, self.RULE_forCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115190289924096) != 0):
                self.state = 373
                self.variable()


            self.state = 376
            self.match(GrammarParser.SEMICOLON)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 377
                self.rvalue(0)


            self.state = 380
            self.match(GrammarParser.SEMICOLON)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 381
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


        def structMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StructMemberContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StructMemberContext,i)


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
        self.enterRule(localctx, 42, self.RULE_printfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(GrammarParser.T__12)
            self.state = 385
            self.match(GrammarParser.LPAREN)
            self.state = 386
            self.formatSpecifier()
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 387
                self.match(GrammarParser.COMMA)
                self.state = 391
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 388
                    self.rvalue(0)
                    pass

                elif la_ == 2:
                    self.state = 389
                    self.string()
                    pass

                elif la_ == 3:
                    self.state = 390
                    self.structMember()
                    pass


                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 398
            self.match(GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScanfStatementContext(ParserRuleContext):
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

        def addr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.AddrContext)
            else:
                return self.getTypedRuleContext(GrammarParser.AddrContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_scanfStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanfStatement" ):
                listener.enterScanfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanfStatement" ):
                listener.exitScanfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScanfStatement" ):
                return visitor.visitScanfStatement(self)
            else:
                return visitor.visitChildren(self)




    def scanfStatement(self):

        localctx = GrammarParser.ScanfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_scanfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(GrammarParser.T__13)
            self.state = 401
            self.match(GrammarParser.LPAREN)
            self.state = 402
            self.formatSpecifier()
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 403
                self.match(GrammarParser.COMMA)
                self.state = 404
                self.addr()
                self.state = 409
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 410
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
        self.enterRule(localctx, 46, self.RULE_formatSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
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
        self.enterRule(localctx, 48, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
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
        self.enterRule(localctx, 50, self.RULE_variable)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.lvalue()
                self.state = 417
                self.match(GrammarParser.T__4)
                self.state = 418
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.lvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 421
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


        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def lvalue(self):
            return self.getTypedRuleContext(GrammarParser.LvalueContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

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
        self.enterRule(localctx, 52, self.RULE_lvalue)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.type_()
                self.state = 426
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 428
                self.pointer()
                self.state = 429
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 431
                self.deref()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 432
                self.match(GrammarParser.LPAREN)
                self.state = 433
                self.lvalue()
                self.state = 434
                self.match(GrammarParser.RPAREN)
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


        def string(self):
            return self.getTypedRuleContext(GrammarParser.StringContext,0)


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

        def EQUALS(self):
            return self.getToken(GrammarParser.EQUALS, 0)

        def NOT_EQUAL(self):
            return self.getToken(GrammarParser.NOT_EQUAL, 0)

        def LOGICAL_AND(self):
            return self.getToken(GrammarParser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(GrammarParser.LOGICAL_OR, 0)

        def GREATER_THAN(self):
            return self.getToken(GrammarParser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(GrammarParser.LESS_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(GrammarParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(GrammarParser.LESS_EQUAL, 0)

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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 439
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 440
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 441
                self.deref()
                pass

            elif la_ == 4:
                self.state = 442
                self.addr()
                pass

            elif la_ == 5:
                self.state = 443
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 444
                self.rvalue(30)
                pass

            elif la_ == 6:
                self.state = 445
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 446
                self.rvalue(29)
                pass

            elif la_ == 7:
                self.state = 447
                self.match(GrammarParser.LPAREN)
                self.state = 448
                self.rvalue(0)
                self.state = 449
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 451
                self.explicitConversion()
                pass

            elif la_ == 9:
                self.state = 452
                self.postFixIncrement()
                pass

            elif la_ == 10:
                self.state = 453
                self.postFixDecrement()
                pass

            elif la_ == 11:
                self.state = 454
                self.preFixIncrement()
                pass

            elif la_ == 12:
                self.state = 455
                self.preFixDecrement()
                pass

            elif la_ == 13:
                self.state = 456
                self.functionCall()
                pass

            elif la_ == 14:
                self.state = 457
                self.jumpStatement()
                pass

            elif la_ == 15:
                self.state = 458
                self.arrayElement()
                pass

            elif la_ == 16:
                self.state = 459
                self.string()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 516
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 462
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 463
                        self.match(GrammarParser.DIV)
                        self.state = 464
                        self.rvalue(29)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 465
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 466
                        self.match(GrammarParser.MOD)
                        self.state = 467
                        self.rvalue(28)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 468
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 469
                        self.match(GrammarParser.MULT)
                        self.state = 470
                        self.rvalue(27)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 471
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 472
                        self.match(GrammarParser.MINUS)
                        self.state = 473
                        self.rvalue(26)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 474
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 475
                        self.match(GrammarParser.PLUS)
                        self.state = 476
                        self.rvalue(25)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 477
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 478
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 479
                        self.rvalue(24)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 480
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 481
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 482
                        self.rvalue(23)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 483
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 484
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 485
                        self.rvalue(22)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 486
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 487
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 488
                        self.rvalue(21)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 489
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 490
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 491
                        self.rvalue(20)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 492
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 493
                        self.match(GrammarParser.EQUALS)
                        self.state = 494
                        self.rvalue(19)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 495
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 496
                        self.match(GrammarParser.NOT_EQUAL)
                        self.state = 497
                        self.rvalue(18)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 498
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 499
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 500
                        self.rvalue(17)
                        pass

                    elif la_ == 14:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 501
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 502
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 503
                        self.rvalue(16)
                        pass

                    elif la_ == 15:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 504
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 505
                        self.match(GrammarParser.GREATER_THAN)
                        self.state = 506
                        self.rvalue(15)
                        pass

                    elif la_ == 16:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 507
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 508
                        self.match(GrammarParser.LESS_THAN)
                        self.state = 509
                        self.rvalue(14)
                        pass

                    elif la_ == 17:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 510
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 511
                        self.match(GrammarParser.GREATER_EQUAL)
                        self.state = 512
                        self.rvalue(13)
                        pass

                    elif la_ == 18:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 513
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 514
                        self.match(GrammarParser.LESS_EQUAL)
                        self.state = 515
                        self.rvalue(12)
                        pass

             
                self.state = 520
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 56, self.RULE_jumpStatement)
        try:
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(GrammarParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(GrammarParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.match(GrammarParser.T__16)
                self.state = 525
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 524
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
        self.enterRule(localctx, 58, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 565
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29 or _la==30:
                    self.state = 529
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 535
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 532
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 533
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 534
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 537
                        self.match(GrammarParser.PLUS)
                        self.state = 538
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 541 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

                self.state = 544
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 543
                    self.match(GrammarParser.PLUS)


                self.state = 549
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 546
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 547
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 548
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 553 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 551
                        self.match(GrammarParser.MINUS)
                        self.state = 552
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 555 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

                self.state = 558
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 557
                    self.match(GrammarParser.MINUS)


                self.state = 563
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 560
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 561
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 562
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
        self.enterRule(localctx, 60, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
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
        self.enterRule(localctx, 62, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 569
                self.match(GrammarParser.LPAREN)
                self.state = 572 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 575 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 574
                self.type_()
                self.state = 577 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0)):
                    break

            self.state = 579
            self.match(GrammarParser.RPAREN)
            self.state = 580
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
        self.enterRule(localctx, 64, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self.type_()
            self.state = 584 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 583
                self.match(GrammarParser.MULT)
                self.state = 586 
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
        self.enterRule(localctx, 66, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 588
                self.match(GrammarParser.MULT)
                self.state = 591 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 593
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
        self.enterRule(localctx, 68, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 595
                self.match(GrammarParser.BITWISE_AND)
                self.state = 598 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 600
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
        self.enterRule(localctx, 70, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(GrammarParser.T__17)
            self.state = 603
            self.match(GrammarParser.IDENTIFIER)
            self.state = 604
            self.match(GrammarParser.LBRACE)
            self.state = 605
            self.match(GrammarParser.IDENTIFIER)
            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 606
                self.match(GrammarParser.COMMA)
                self.state = 607
                self.match(GrammarParser.IDENTIFIER)
                self.state = 612
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
        self.enterRule(localctx, 72, self.RULE_enumStatement)
        try:
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 615
                self.enumVariableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 616
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
        self.enterRule(localctx, 74, self.RULE_enumVariableDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.match(GrammarParser.T__17)
            self.state = 620
            self.match(GrammarParser.IDENTIFIER)
            self.state = 621
            self.match(GrammarParser.IDENTIFIER)
            self.state = 622
            self.match(GrammarParser.T__4)
            self.state = 623
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
        self.enterRule(localctx, 76, self.RULE_enumVariableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.match(GrammarParser.T__17)
            self.state = 626
            self.match(GrammarParser.IDENTIFIER)
            self.state = 627
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
        self.enterRule(localctx, 78, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.lvalue()
            self.state = 630
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
        self.enterRule(localctx, 80, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.lvalue()
            self.state = 633
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
        self.enterRule(localctx, 82, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.match(GrammarParser.INCREMENT)
            self.state = 636
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
        self.enterRule(localctx, 84, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(GrammarParser.DECREMENT)
            self.state = 639
            self.lvalue()
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


        def arrayAssignment(self):
            return self.getTypedRuleContext(GrammarParser.ArrayAssignmentContext,0)


        def arrayDefinition(self):
            return self.getTypedRuleContext(GrammarParser.ArrayDefinitionContext,0)


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
        self.enterRule(localctx, 86, self.RULE_arrayStatement)
        try:
            self.state = 644
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 641
                self.arrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 642
                self.arrayAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 643
                self.arrayDefinition()
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


        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


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
        self.enterRule(localctx, 88, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.type_()
            self.state = 647
            self.identifier()
            self.state = 651 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 648
                self.match(GrammarParser.T__2)
                self.state = 649
                self.match(GrammarParser.INT)
                self.state = 650
                self.match(GrammarParser.T__3)
                self.state = 653 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(GrammarParser.RvalueContext,0)


        def array(self):
            return self.getTypedRuleContext(GrammarParser.ArrayContext,0)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.INT)
            else:
                return self.getToken(GrammarParser.INT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_arrayAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAssignment" ):
                listener.enterArrayAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAssignment" ):
                listener.exitArrayAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssignment" ):
                return visitor.visitArrayAssignment(self)
            else:
                return visitor.visitChildren(self)




    def arrayAssignment(self):

        localctx = GrammarParser.ArrayAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arrayAssignment)
        self._la = 0 # Token type
        try:
            self.state = 672
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 655
                self.identifier()
                self.state = 659 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 656
                    self.match(GrammarParser.T__2)
                    self.state = 657
                    self.match(GrammarParser.INT)
                    self.state = 658
                    self.match(GrammarParser.T__3)
                    self.state = 661 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                self.state = 663
                self.match(GrammarParser.T__4)
                self.state = 666
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                    self.state = 664
                    self.rvalue(0)
                    pass
                elif token in [27]:
                    self.state = 665
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 668
                self.identifier()
                self.state = 669
                self.match(GrammarParser.T__4)
                self.state = 670
                self.array()
                pass


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


        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def array(self):
            return self.getTypedRuleContext(GrammarParser.ArrayContext,0)


        def string(self):
            return self.getTypedRuleContext(GrammarParser.StringContext,0)


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
        self.enterRule(localctx, 92, self.RULE_arrayDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
            self.type_()
            self.state = 675
            self.identifier()
            self.state = 679 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 676
                self.match(GrammarParser.T__2)
                self.state = 677
                self.match(GrammarParser.INT)
                self.state = 678
                self.match(GrammarParser.T__3)
                self.state = 681 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 683
            self.match(GrammarParser.T__4)
            self.state = 686
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 684
                self.array()
                pass
            elif token in [55]:
                self.state = 685
                self.string()
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


    class ArrayContext(ParserRuleContext):
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


        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ArrayContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ArrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = GrammarParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.match(GrammarParser.LBRACE)
            self.state = 691
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                self.state = 689
                self.rvalue(0)
                pass
            elif token in [27]:
                self.state = 690
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 700
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 693
                self.match(GrammarParser.COMMA)
                self.state = 696
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                    self.state = 694
                    self.rvalue(0)
                    pass
                elif token in [27]:
                    self.state = 695
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 702
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 703
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

        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


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
        self.enterRule(localctx, 96, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 705
            self.identifier()
            self.state = 710 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 706
                    self.match(GrammarParser.T__2)
                    self.state = 707
                    self.rvalue(0)
                    self.state = 708
                    self.match(GrammarParser.T__3)

                else:
                    raise NoViableAltException(self)
                self.state = 712 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

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
        self.enterRule(localctx, 98, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self.match(GrammarParser.T__18)
            self.state = 715
            self.type_()
            self.state = 716
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
        self.enterRule(localctx, 100, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 718
                self.match(GrammarParser.T__19)
                self.state = 723
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 724
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188107313152) != 0)):
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
        self.enterRule(localctx, 102, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 726
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
        self.enterRule(localctx, 104, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 728
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
        self._predicates[9] = self.functionParams_sempred
        self._predicates[11] = self.callParams_sempred
        self._predicates[27] = self.rvalue_sempred
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
                return self.precpred(self._ctx, 28)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 11)
         




