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
        4,1,63,619,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,4,0,96,8,0,11,0,12,0,97,1,0,1,0,4,0,102,8,0,11,0,12,0,103,
        1,0,1,0,4,0,108,8,0,11,0,12,0,109,1,0,4,0,113,8,0,11,0,12,0,114,
        1,0,1,0,1,1,1,1,5,1,121,8,1,10,1,12,1,124,9,1,1,1,1,1,1,2,1,2,4,
        2,130,8,2,11,2,12,2,131,1,2,1,2,4,2,136,8,2,11,2,12,2,137,1,2,1,
        2,1,2,4,2,143,8,2,11,2,12,2,144,1,2,1,2,1,2,1,2,1,2,1,2,4,2,153,
        8,2,11,2,12,2,154,1,2,1,2,4,2,159,8,2,11,2,12,2,160,1,2,1,2,4,2,
        165,8,2,11,2,12,2,166,1,2,1,2,3,2,171,8,2,1,3,1,3,3,3,175,8,3,1,
        3,1,3,1,3,3,3,180,8,3,1,3,1,3,1,3,1,3,1,3,3,3,187,8,3,1,3,1,3,1,
        3,3,3,192,8,3,1,3,1,3,1,3,3,3,197,8,3,1,4,1,4,1,4,3,4,202,8,4,1,
        4,1,4,3,4,206,8,4,1,4,1,4,1,4,5,4,211,8,4,10,4,12,4,214,9,4,1,5,
        1,5,1,5,3,5,219,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,229,8,6,
        10,6,12,6,232,9,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,240,8,7,10,7,12,7,
        243,9,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,251,8,8,10,8,12,8,254,9,8,1,
        8,1,8,1,8,5,8,259,8,8,10,8,12,8,262,9,8,3,8,264,8,8,1,9,1,9,5,9,
        268,8,9,10,9,12,9,271,9,9,1,9,3,9,274,8,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,3,15,305,
        8,15,1,15,1,15,3,15,309,8,15,1,15,1,15,3,15,313,8,15,1,16,1,16,1,
        16,1,16,1,16,1,16,3,16,321,8,16,1,16,1,16,1,17,1,17,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,3,18,334,8,18,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,3,19,345,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,3,20,369,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,5,20,409,8,20,10,20,12,20,412,9,20,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,426,8,
        21,1,22,1,22,1,22,1,22,3,22,432,8,22,3,22,434,8,22,1,23,3,23,437,
        8,23,1,23,1,23,1,23,3,23,442,8,23,1,23,1,23,4,23,446,8,23,11,23,
        12,23,447,1,23,3,23,451,8,23,1,23,1,23,1,23,3,23,456,8,23,1,23,1,
        23,4,23,460,8,23,11,23,12,23,461,1,23,3,23,465,8,23,1,23,1,23,1,
        23,3,23,470,8,23,3,23,472,8,23,1,24,1,24,1,25,4,25,477,8,25,11,25,
        12,25,478,1,25,4,25,482,8,25,11,25,12,25,483,1,25,1,25,1,25,1,26,
        1,26,4,26,491,8,26,11,26,12,26,492,1,27,4,27,496,8,27,11,27,12,27,
        497,1,27,1,27,1,28,4,28,503,8,28,11,28,12,28,504,1,28,1,28,1,29,
        1,29,1,29,1,29,1,29,1,29,5,29,515,8,29,10,29,12,29,518,9,29,1,29,
        1,29,1,30,1,30,3,30,524,8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,36,
        1,36,1,36,1,37,1,37,1,37,1,37,1,38,5,38,553,8,38,10,38,12,38,556,
        9,38,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,41,1,41,1,41,3,41,
        569,8,41,1,42,1,42,1,42,1,42,1,42,4,42,576,8,42,11,42,12,42,577,
        1,43,1,43,1,43,1,43,1,43,4,43,585,8,43,11,43,12,43,586,1,43,1,43,
        1,43,3,43,592,8,43,1,44,1,44,1,44,1,44,5,44,598,8,44,10,44,12,44,
        601,9,44,3,44,603,8,44,1,44,1,44,1,45,1,45,1,45,1,45,3,45,611,8,
        45,1,45,1,45,4,45,615,8,45,11,45,12,45,616,1,45,0,3,8,12,40,46,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,
        0,4,1,0,9,13,1,0,31,32,1,0,54,56,2,0,21,24,58,58,691,0,112,1,0,0,
        0,2,118,1,0,0,0,4,170,1,0,0,0,6,196,1,0,0,0,8,198,1,0,0,0,10,215,
        1,0,0,0,12,222,1,0,0,0,14,233,1,0,0,0,16,263,1,0,0,0,18,265,1,0,
        0,0,20,275,1,0,0,0,22,281,1,0,0,0,24,288,1,0,0,0,26,291,1,0,0,0,
        28,297,1,0,0,0,30,304,1,0,0,0,32,314,1,0,0,0,34,324,1,0,0,0,36,333,
        1,0,0,0,38,344,1,0,0,0,40,368,1,0,0,0,42,425,1,0,0,0,44,433,1,0,
        0,0,46,471,1,0,0,0,48,473,1,0,0,0,50,476,1,0,0,0,52,488,1,0,0,0,
        54,495,1,0,0,0,56,502,1,0,0,0,58,508,1,0,0,0,60,523,1,0,0,0,62,525,
        1,0,0,0,64,531,1,0,0,0,66,535,1,0,0,0,68,538,1,0,0,0,70,541,1,0,
        0,0,72,544,1,0,0,0,74,547,1,0,0,0,76,554,1,0,0,0,78,559,1,0,0,0,
        80,561,1,0,0,0,82,568,1,0,0,0,84,570,1,0,0,0,86,579,1,0,0,0,88,593,
        1,0,0,0,90,606,1,0,0,0,92,113,3,80,40,0,93,95,3,58,29,0,94,96,5,
        52,0,0,95,94,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,
        113,1,0,0,0,99,101,3,36,18,0,100,102,5,52,0,0,101,100,1,0,0,0,102,
        103,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,113,1,0,0,0,105,
        107,3,74,37,0,106,108,5,52,0,0,107,106,1,0,0,0,108,109,1,0,0,0,109,
        107,1,0,0,0,109,110,1,0,0,0,110,113,1,0,0,0,111,113,3,6,3,0,112,
        92,1,0,0,0,112,93,1,0,0,0,112,99,1,0,0,0,112,105,1,0,0,0,112,111,
        1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,116,
        1,0,0,0,116,117,5,0,0,1,117,1,1,0,0,0,118,122,5,29,0,0,119,121,3,
        4,2,0,120,119,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,
        0,0,0,123,125,1,0,0,0,124,122,1,0,0,0,125,126,5,30,0,0,126,3,1,0,
        0,0,127,129,3,40,20,0,128,130,5,52,0,0,129,128,1,0,0,0,130,131,1,
        0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,171,1,0,0,0,133,135,3,
        36,18,0,134,136,5,52,0,0,135,134,1,0,0,0,136,137,1,0,0,0,137,135,
        1,0,0,0,137,138,1,0,0,0,138,171,1,0,0,0,139,171,3,80,40,0,140,142,
        3,32,16,0,141,143,5,52,0,0,142,141,1,0,0,0,143,144,1,0,0,0,144,142,
        1,0,0,0,144,145,1,0,0,0,145,171,1,0,0,0,146,171,3,2,1,0,147,171,
        3,18,9,0,148,171,3,26,13,0,149,171,3,28,14,0,150,152,3,60,30,0,151,
        153,5,52,0,0,152,151,1,0,0,0,153,154,1,0,0,0,154,152,1,0,0,0,154,
        155,1,0,0,0,155,171,1,0,0,0,156,158,3,82,41,0,157,159,5,52,0,0,158,
        157,1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,
        171,1,0,0,0,162,164,3,44,22,0,163,165,5,52,0,0,164,163,1,0,0,0,165,
        166,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,171,1,0,0,0,168,
        171,3,6,3,0,169,171,3,14,7,0,170,127,1,0,0,0,170,133,1,0,0,0,170,
        139,1,0,0,0,170,140,1,0,0,0,170,146,1,0,0,0,170,147,1,0,0,0,170,
        148,1,0,0,0,170,149,1,0,0,0,170,150,1,0,0,0,170,156,1,0,0,0,170,
        162,1,0,0,0,170,168,1,0,0,0,170,169,1,0,0,0,171,5,1,0,0,0,172,175,
        3,76,38,0,173,175,3,52,26,0,174,172,1,0,0,0,174,173,1,0,0,0,175,
        176,1,0,0,0,176,177,5,58,0,0,177,179,5,27,0,0,178,180,3,8,4,0,179,
        178,1,0,0,0,179,180,1,0,0,0,180,181,1,0,0,0,181,182,5,28,0,0,182,
        183,3,2,1,0,183,197,1,0,0,0,184,187,3,76,38,0,185,187,3,52,26,0,
        186,184,1,0,0,0,186,185,1,0,0,0,187,188,1,0,0,0,188,189,5,58,0,0,
        189,191,5,27,0,0,190,192,3,8,4,0,191,190,1,0,0,0,191,192,1,0,0,0,
        192,193,1,0,0,0,193,194,5,28,0,0,194,195,5,52,0,0,195,197,1,0,0,
        0,196,174,1,0,0,0,196,186,1,0,0,0,197,7,1,0,0,0,198,201,6,4,-1,0,
        199,202,3,52,26,0,200,202,3,76,38,0,201,199,1,0,0,0,201,200,1,0,
        0,0,202,205,1,0,0,0,203,206,3,56,28,0,204,206,3,78,39,0,205,203,
        1,0,0,0,205,204,1,0,0,0,206,212,1,0,0,0,207,208,10,1,0,0,208,209,
        5,53,0,0,209,211,3,8,4,2,210,207,1,0,0,0,211,214,1,0,0,0,212,210,
        1,0,0,0,212,213,1,0,0,0,213,9,1,0,0,0,214,212,1,0,0,0,215,216,5,
        58,0,0,216,218,5,27,0,0,217,219,3,12,6,0,218,217,1,0,0,0,218,219,
        1,0,0,0,219,220,1,0,0,0,220,221,5,28,0,0,221,11,1,0,0,0,222,223,
        6,6,-1,0,223,224,3,40,20,0,224,230,1,0,0,0,225,226,10,1,0,0,226,
        227,5,53,0,0,227,229,3,12,6,2,228,225,1,0,0,0,229,232,1,0,0,0,230,
        228,1,0,0,0,230,231,1,0,0,0,231,13,1,0,0,0,232,230,1,0,0,0,233,234,
        5,1,0,0,234,235,5,27,0,0,235,236,3,40,20,0,236,237,5,28,0,0,237,
        241,5,29,0,0,238,240,3,16,8,0,239,238,1,0,0,0,240,243,1,0,0,0,241,
        239,1,0,0,0,241,242,1,0,0,0,242,244,1,0,0,0,243,241,1,0,0,0,244,
        245,5,30,0,0,245,15,1,0,0,0,246,247,5,2,0,0,247,248,3,48,24,0,248,
        252,5,51,0,0,249,251,3,4,2,0,250,249,1,0,0,0,251,254,1,0,0,0,252,
        250,1,0,0,0,252,253,1,0,0,0,253,264,1,0,0,0,254,252,1,0,0,0,255,
        256,5,3,0,0,256,260,5,51,0,0,257,259,3,4,2,0,258,257,1,0,0,0,259,
        262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,264,1,0,0,0,262,
        260,1,0,0,0,263,246,1,0,0,0,263,255,1,0,0,0,264,17,1,0,0,0,265,269,
        3,20,10,0,266,268,3,22,11,0,267,266,1,0,0,0,268,271,1,0,0,0,269,
        267,1,0,0,0,269,270,1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,272,
        274,3,24,12,0,273,272,1,0,0,0,273,274,1,0,0,0,274,19,1,0,0,0,275,
        276,5,4,0,0,276,277,5,27,0,0,277,278,3,40,20,0,278,279,5,28,0,0,
        279,280,3,2,1,0,280,21,1,0,0,0,281,282,5,5,0,0,282,283,5,4,0,0,283,
        284,5,27,0,0,284,285,3,40,20,0,285,286,5,28,0,0,286,287,3,2,1,0,
        287,23,1,0,0,0,288,289,5,5,0,0,289,290,3,2,1,0,290,25,1,0,0,0,291,
        292,5,6,0,0,292,293,5,27,0,0,293,294,3,40,20,0,294,295,5,28,0,0,
        295,296,3,2,1,0,296,27,1,0,0,0,297,298,5,7,0,0,298,299,5,27,0,0,
        299,300,3,30,15,0,300,301,5,28,0,0,301,302,3,2,1,0,302,29,1,0,0,
        0,303,305,3,36,18,0,304,303,1,0,0,0,304,305,1,0,0,0,305,306,1,0,
        0,0,306,308,5,52,0,0,307,309,3,40,20,0,308,307,1,0,0,0,308,309,1,
        0,0,0,309,310,1,0,0,0,310,312,5,52,0,0,311,313,3,40,20,0,312,311,
        1,0,0,0,312,313,1,0,0,0,313,31,1,0,0,0,314,315,5,8,0,0,315,316,5,
        27,0,0,316,317,3,34,17,0,317,320,5,53,0,0,318,321,3,78,39,0,319,
        321,3,48,24,0,320,318,1,0,0,0,320,319,1,0,0,0,321,322,1,0,0,0,322,
        323,5,28,0,0,323,33,1,0,0,0,324,325,7,0,0,0,325,35,1,0,0,0,326,327,
        3,38,19,0,327,328,5,14,0,0,328,329,3,40,20,0,329,334,1,0,0,0,330,
        334,3,38,19,0,331,334,3,74,37,0,332,334,3,84,42,0,333,326,1,0,0,
        0,333,330,1,0,0,0,333,331,1,0,0,0,333,332,1,0,0,0,334,37,1,0,0,0,
        335,345,3,78,39,0,336,337,3,76,38,0,337,338,3,78,39,0,338,345,1,
        0,0,0,339,340,3,52,26,0,340,341,3,78,39,0,341,345,1,0,0,0,342,345,
        3,54,27,0,343,345,3,90,45,0,344,335,1,0,0,0,344,336,1,0,0,0,344,
        339,1,0,0,0,344,342,1,0,0,0,344,343,1,0,0,0,345,39,1,0,0,0,346,347,
        6,20,-1,0,347,369,3,46,23,0,348,369,3,78,39,0,349,369,3,54,27,0,
        350,369,3,56,28,0,351,352,5,50,0,0,352,369,3,40,20,25,353,354,5,
        47,0,0,354,369,3,40,20,24,355,356,5,27,0,0,356,357,3,40,20,0,357,
        358,5,28,0,0,358,369,1,0,0,0,359,369,3,50,25,0,360,369,3,66,33,0,
        361,369,3,68,34,0,362,369,3,70,35,0,363,369,3,72,36,0,364,369,3,
        10,5,0,365,369,3,44,22,0,366,369,3,90,45,0,367,369,3,88,44,0,368,
        346,1,0,0,0,368,348,1,0,0,0,368,349,1,0,0,0,368,350,1,0,0,0,368,
        351,1,0,0,0,368,353,1,0,0,0,368,355,1,0,0,0,368,359,1,0,0,0,368,
        360,1,0,0,0,368,361,1,0,0,0,368,362,1,0,0,0,368,363,1,0,0,0,368,
        364,1,0,0,0,368,365,1,0,0,0,368,366,1,0,0,0,368,367,1,0,0,0,369,
        410,1,0,0,0,370,371,10,23,0,0,371,372,5,34,0,0,372,409,3,40,20,24,
        373,374,10,22,0,0,374,375,5,35,0,0,375,409,3,40,20,23,376,377,10,
        21,0,0,377,378,5,33,0,0,378,409,3,40,20,22,379,380,10,20,0,0,380,
        381,5,32,0,0,381,409,3,40,20,21,382,383,10,19,0,0,383,384,5,31,0,
        0,384,409,3,40,20,20,385,386,10,18,0,0,386,387,5,42,0,0,387,409,
        3,40,20,19,388,389,10,17,0,0,389,390,5,43,0,0,390,409,3,40,20,18,
        391,392,10,16,0,0,392,393,5,44,0,0,393,409,3,40,20,17,394,395,10,
        15,0,0,395,396,5,45,0,0,396,409,3,40,20,16,397,398,10,14,0,0,398,
        399,5,46,0,0,399,409,3,40,20,15,400,401,10,13,0,0,401,402,5,48,0,
        0,402,409,3,40,20,14,403,404,10,12,0,0,404,405,5,49,0,0,405,409,
        3,40,20,13,406,407,10,5,0,0,407,409,3,42,21,0,408,370,1,0,0,0,408,
        373,1,0,0,0,408,376,1,0,0,0,408,379,1,0,0,0,408,382,1,0,0,0,408,
        385,1,0,0,0,408,388,1,0,0,0,408,391,1,0,0,0,408,394,1,0,0,0,408,
        397,1,0,0,0,408,400,1,0,0,0,408,403,1,0,0,0,408,406,1,0,0,0,409,
        412,1,0,0,0,410,408,1,0,0,0,410,411,1,0,0,0,411,41,1,0,0,0,412,410,
        1,0,0,0,413,414,5,36,0,0,414,426,3,40,20,0,415,416,5,37,0,0,416,
        426,3,40,20,0,417,418,5,38,0,0,418,426,3,40,20,0,419,420,5,39,0,
        0,420,426,3,40,20,0,421,422,5,40,0,0,422,426,3,40,20,0,423,424,5,
        41,0,0,424,426,3,40,20,0,425,413,1,0,0,0,425,415,1,0,0,0,425,417,
        1,0,0,0,425,419,1,0,0,0,425,421,1,0,0,0,425,423,1,0,0,0,426,43,1,
        0,0,0,427,434,5,15,0,0,428,434,5,16,0,0,429,431,5,17,0,0,430,432,
        3,40,20,0,431,430,1,0,0,0,431,432,1,0,0,0,432,434,1,0,0,0,433,427,
        1,0,0,0,433,428,1,0,0,0,433,429,1,0,0,0,434,45,1,0,0,0,435,437,7,
        1,0,0,436,435,1,0,0,0,436,437,1,0,0,0,437,441,1,0,0,0,438,442,3,
        48,24,0,439,442,3,78,39,0,440,442,3,54,27,0,441,438,1,0,0,0,441,
        439,1,0,0,0,441,440,1,0,0,0,442,472,1,0,0,0,443,444,5,31,0,0,444,
        446,5,32,0,0,445,443,1,0,0,0,446,447,1,0,0,0,447,445,1,0,0,0,447,
        448,1,0,0,0,448,450,1,0,0,0,449,451,5,31,0,0,450,449,1,0,0,0,450,
        451,1,0,0,0,451,455,1,0,0,0,452,456,3,48,24,0,453,456,3,78,39,0,
        454,456,3,54,27,0,455,452,1,0,0,0,455,453,1,0,0,0,455,454,1,0,0,
        0,456,472,1,0,0,0,457,458,5,32,0,0,458,460,5,31,0,0,459,457,1,0,
        0,0,460,461,1,0,0,0,461,459,1,0,0,0,461,462,1,0,0,0,462,464,1,0,
        0,0,463,465,5,32,0,0,464,463,1,0,0,0,464,465,1,0,0,0,465,469,1,0,
        0,0,466,470,3,48,24,0,467,470,3,78,39,0,468,470,3,54,27,0,469,466,
        1,0,0,0,469,467,1,0,0,0,469,468,1,0,0,0,470,472,1,0,0,0,471,436,
        1,0,0,0,471,445,1,0,0,0,471,459,1,0,0,0,472,47,1,0,0,0,473,474,7,
        2,0,0,474,49,1,0,0,0,475,477,5,27,0,0,476,475,1,0,0,0,477,478,1,
        0,0,0,478,476,1,0,0,0,478,479,1,0,0,0,479,481,1,0,0,0,480,482,3,
        76,38,0,481,480,1,0,0,0,482,483,1,0,0,0,483,481,1,0,0,0,483,484,
        1,0,0,0,484,485,1,0,0,0,485,486,5,28,0,0,486,487,3,40,20,0,487,51,
        1,0,0,0,488,490,3,76,38,0,489,491,5,33,0,0,490,489,1,0,0,0,491,492,
        1,0,0,0,492,490,1,0,0,0,492,493,1,0,0,0,493,53,1,0,0,0,494,496,5,
        33,0,0,495,494,1,0,0,0,496,497,1,0,0,0,497,495,1,0,0,0,497,498,1,
        0,0,0,498,499,1,0,0,0,499,500,3,78,39,0,500,55,1,0,0,0,501,503,5,
        44,0,0,502,501,1,0,0,0,503,504,1,0,0,0,504,502,1,0,0,0,504,505,1,
        0,0,0,505,506,1,0,0,0,506,507,3,78,39,0,507,57,1,0,0,0,508,509,5,
        18,0,0,509,510,5,58,0,0,510,511,5,29,0,0,511,516,5,58,0,0,512,513,
        5,53,0,0,513,515,5,58,0,0,514,512,1,0,0,0,515,518,1,0,0,0,516,514,
        1,0,0,0,516,517,1,0,0,0,517,519,1,0,0,0,518,516,1,0,0,0,519,520,
        5,30,0,0,520,59,1,0,0,0,521,524,3,62,31,0,522,524,3,64,32,0,523,
        521,1,0,0,0,523,522,1,0,0,0,524,61,1,0,0,0,525,526,5,18,0,0,526,
        527,5,58,0,0,527,528,5,58,0,0,528,529,5,14,0,0,529,530,5,58,0,0,
        530,63,1,0,0,0,531,532,5,18,0,0,532,533,5,58,0,0,533,534,5,58,0,
        0,534,65,1,0,0,0,535,536,3,38,19,0,536,537,5,59,0,0,537,67,1,0,0,
        0,538,539,3,38,19,0,539,540,5,60,0,0,540,69,1,0,0,0,541,542,5,59,
        0,0,542,543,3,38,19,0,543,71,1,0,0,0,544,545,5,60,0,0,545,546,3,
        38,19,0,546,73,1,0,0,0,547,548,5,19,0,0,548,549,3,76,38,0,549,550,
        5,58,0,0,550,75,1,0,0,0,551,553,5,20,0,0,552,551,1,0,0,0,553,556,
        1,0,0,0,554,552,1,0,0,0,554,555,1,0,0,0,555,557,1,0,0,0,556,554,
        1,0,0,0,557,558,7,3,0,0,558,77,1,0,0,0,559,560,5,58,0,0,560,79,1,
        0,0,0,561,562,5,61,0,0,562,81,1,0,0,0,563,569,3,84,42,0,564,565,
        3,86,43,0,565,566,5,14,0,0,566,567,3,40,20,0,567,569,1,0,0,0,568,
        563,1,0,0,0,568,564,1,0,0,0,569,83,1,0,0,0,570,571,3,76,38,0,571,
        575,5,58,0,0,572,573,5,25,0,0,573,574,5,54,0,0,574,576,5,26,0,0,
        575,572,1,0,0,0,576,577,1,0,0,0,577,575,1,0,0,0,577,578,1,0,0,0,
        578,85,1,0,0,0,579,580,3,76,38,0,580,584,5,58,0,0,581,582,5,25,0,
        0,582,583,5,54,0,0,583,585,5,26,0,0,584,581,1,0,0,0,585,586,1,0,
        0,0,586,584,1,0,0,0,586,587,1,0,0,0,587,588,1,0,0,0,588,591,5,14,
        0,0,589,592,3,88,44,0,590,592,3,78,39,0,591,589,1,0,0,0,591,590,
        1,0,0,0,592,87,1,0,0,0,593,602,5,29,0,0,594,599,3,40,20,0,595,596,
        5,53,0,0,596,598,3,40,20,0,597,595,1,0,0,0,598,601,1,0,0,0,599,597,
        1,0,0,0,599,600,1,0,0,0,600,603,1,0,0,0,601,599,1,0,0,0,602,594,
        1,0,0,0,602,603,1,0,0,0,603,604,1,0,0,0,604,605,5,30,0,0,605,89,
        1,0,0,0,606,614,3,78,39,0,607,610,5,25,0,0,608,611,3,40,20,0,609,
        611,3,78,39,0,610,608,1,0,0,0,610,609,1,0,0,0,611,612,1,0,0,0,612,
        613,5,26,0,0,613,615,1,0,0,0,614,607,1,0,0,0,615,616,1,0,0,0,616,
        614,1,0,0,0,616,617,1,0,0,0,617,91,1,0,0,0,66,97,103,109,112,114,
        122,131,137,144,154,160,166,170,174,179,186,191,196,201,205,212,
        218,230,241,252,260,263,269,273,304,308,312,320,333,344,368,408,
        410,425,431,433,436,441,447,450,455,461,464,469,471,478,483,492,
        497,504,516,523,554,568,577,586,591,599,602,610,616
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
                     "'['", "']'", "'('", "')'", "'{'", "'}'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'<<'", "'>>'", "'&'", "'|'", "'^'", 
                     "'~'", "'&&'", "'||'", "'!'", "':'", "';'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
                      "LESS_EQUAL", "EQUALS", "NOT_EQUAL", "SHIFT_LEFT", 
                      "SHIFT_RIGHT", "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", 
                      "BITWISE_NOT", "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", 
                      "COLON", "SEMICOLON", "COMMA", "INT", "FLOAT", "CHAR", 
                      "WHITESPACE", "IDENTIFIER", "INCREMENT", "DECREMENT", 
                      "COMMENT", "BLOCKCOMMENT", "LINECOMMENT" ]

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
    RULE_arrayStatement = 41
    RULE_arrayDeclaration = 42
    RULE_arrayDefinition = 43
    RULE_arrayInitializer = 44
    RULE_arrayElement = 45

    ruleNames =  [ "program", "scope", "statement", "function", "functionParams", 
                   "functionCall", "callParams", "switchStatement", "switchCase", 
                   "conditional", "ifStatement", "elseIfStatement", "elseStatement", 
                   "whileLoop", "forLoop", "forCondition", "printfStatement", 
                   "formatSpecifier", "variable", "lvalue", "rvalue", "conditionalExpression", 
                   "jumpStatement", "unaryExpression", "literal", "explicitConversion", 
                   "pointer", "deref", "addr", "enumDeclaration", "enumStatement", 
                   "enumVariableDefinition", "enumVariableDeclaration", 
                   "postFixIncrement", "postFixDecrement", "preFixIncrement", 
                   "preFixDecrement", "typedef", "type", "identifier", "comment", 
                   "arrayStatement", "arrayDeclaration", "arrayDefinition", 
                   "arrayInitializer", "arrayElement" ]

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
    T__24=25
    T__25=26
    LPAREN=27
    RPAREN=28
    LBRACE=29
    RBRACE=30
    PLUS=31
    MINUS=32
    MULT=33
    DIV=34
    MOD=35
    GREATER_THAN=36
    LESS_THAN=37
    GREATER_EQUAL=38
    LESS_EQUAL=39
    EQUALS=40
    NOT_EQUAL=41
    SHIFT_LEFT=42
    SHIFT_RIGHT=43
    BITWISE_AND=44
    BITWISE_OR=45
    BITWISE_XOR=46
    BITWISE_NOT=47
    LOGICAL_AND=48
    LOGICAL_OR=49
    LOGICAL_NOT=50
    COLON=51
    SEMICOLON=52
    COMMA=53
    INT=54
    FLOAT=55
    CHAR=56
    WHITESPACE=57
    IDENTIFIER=58
    INCREMENT=59
    DECREMENT=60
    COMMENT=61
    BLOCKCOMMENT=62
    LINECOMMENT=63

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
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 92
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 93
                    self.enumDeclaration()
                    self.state = 95 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 94
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 97 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==52):
                            break

                    pass

                elif la_ == 3:
                    self.state = 99
                    self.variable()
                    self.state = 101 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 100
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 103 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==52):
                            break

                    pass

                elif la_ == 4:
                    self.state = 105
                    self.typedef()
                    self.state = 107 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 106
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 109 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==52):
                            break

                    pass

                elif la_ == 5:
                    self.state = 111
                    self.function()
                    pass


                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2594073393988632576) != 0)):
                    break

            self.state = 116
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
            self.state = 118
            self.match(GrammarParser.LBRACE)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4450840677160288722) != 0):
                self.state = 119
                self.statement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
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
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.rvalue(0)
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 128
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 131 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==52):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.variable()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 134
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 137 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==52):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.printfStatement()
                self.state = 142 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 141
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 144 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==52):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 146
                self.scope()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 147
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 148
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 149
                self.forLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 150
                self.enumStatement()
                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 151
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 154 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==52):
                        break

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 156
                self.arrayStatement()
                self.state = 158 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 157
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 160 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==52):
                        break

                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 162
                self.jumpStatement()
                self.state = 164 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 163
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 166 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==52):
                        break

                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 168
                self.function()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 169
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
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 172
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 173
                    self.pointer()
                    pass


                self.state = 176
                self.match(GrammarParser.IDENTIFIER)
                self.state = 177
                self.match(GrammarParser.LPAREN)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 288230376184217600) != 0):
                    self.state = 178
                    self.functionParams(0)


                self.state = 181
                self.match(GrammarParser.RPAREN)
                self.state = 182
                self.scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 184
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 185
                    self.pointer()
                    pass


                self.state = 188
                self.match(GrammarParser.IDENTIFIER)
                self.state = 189
                self.match(GrammarParser.LPAREN)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 288230376184217600) != 0):
                    self.state = 190
                    self.functionParams(0)


                self.state = 193
                self.match(GrammarParser.RPAREN)
                self.state = 194
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
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 199
                self.pointer()
                pass

            elif la_ == 2:
                self.state = 200
                self.type_()
                pass


            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.state = 203
                self.addr()
                pass
            elif token in [58]:
                self.state = 204
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.FunctionParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParams)
                    self.state = 207
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 208
                    self.match(GrammarParser.COMMA)
                    self.state = 209
                    self.functionParams(2) 
                self.state = 214
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
            self.state = 215
            self.match(GrammarParser.IDENTIFIER)
            self.state = 216
            self.match(GrammarParser.LPAREN)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2144997667945807872) != 0):
                self.state = 217
                self.callParams(0)


            self.state = 220
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
            self.state = 223
            self.rvalue(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CallParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callParams)
                    self.state = 225
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 226
                    self.match(GrammarParser.COMMA)
                    self.state = 227
                    self.callParams(2) 
                self.state = 232
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
            self.state = 233
            self.match(GrammarParser.T__0)
            self.state = 234
            self.match(GrammarParser.LPAREN)
            self.state = 235
            self.rvalue(0)
            self.state = 236
            self.match(GrammarParser.RPAREN)
            self.state = 237
            self.match(GrammarParser.LBRACE)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 238
                self.switchCase()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
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
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(GrammarParser.T__1)
                self.state = 247
                self.literal()
                self.state = 248
                self.match(GrammarParser.COLON)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4450840677160288722) != 0):
                    self.state = 249
                    self.statement()
                    self.state = 254
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(GrammarParser.T__2)
                self.state = 256
                self.match(GrammarParser.COLON)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4450840677160288722) != 0):
                    self.state = 257
                    self.statement()
                    self.state = 262
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
            self.state = 265
            self.ifStatement()
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 266
                    self.elseIfStatement() 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 272
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
            self.state = 275
            self.match(GrammarParser.T__3)
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
            self.state = 281
            self.match(GrammarParser.T__4)
            self.state = 282
            self.match(GrammarParser.T__3)
            self.state = 283
            self.match(GrammarParser.LPAREN)
            self.state = 284
            self.rvalue(0)
            self.state = 285
            self.match(GrammarParser.RPAREN)
            self.state = 286
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
            self.state = 288
            self.match(GrammarParser.T__4)
            self.state = 289
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
            self.state = 291
            self.match(GrammarParser.T__5)
            self.state = 292
            self.match(GrammarParser.LPAREN)
            self.state = 293
            self.rvalue(0)
            self.state = 294
            self.match(GrammarParser.RPAREN)
            self.state = 295
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
            self.state = 297
            self.match(GrammarParser.T__6)
            self.state = 298
            self.match(GrammarParser.LPAREN)
            self.state = 299
            self.forCondition()
            self.state = 300
            self.match(GrammarParser.RPAREN)
            self.state = 301
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
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 288230384774676480) != 0):
                self.state = 303
                self.variable()


            self.state = 306
            self.match(GrammarParser.SEMICOLON)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2144997667945807872) != 0):
                self.state = 307
                self.rvalue(0)


            self.state = 310
            self.match(GrammarParser.SEMICOLON)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2144997667945807872) != 0):
                self.state = 311
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
            self.state = 314
            self.match(GrammarParser.T__7)
            self.state = 315
            self.match(GrammarParser.LPAREN)
            self.state = 316
            self.formatSpecifier()
            self.state = 317
            self.match(GrammarParser.COMMA)
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.state = 318
                self.identifier()
                pass
            elif token in [54, 55, 56]:
                self.state = 319
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 322
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
            self.state = 324
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
        self.enterRule(localctx, 36, self.RULE_variable)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.lvalue()
                self.state = 327
                self.match(GrammarParser.T__13)
                self.state = 328
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.lvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 331
                self.typedef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 332
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
        self.enterRule(localctx, 38, self.RULE_lvalue)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.type_()
                self.state = 337
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
                self.pointer()
                self.state = 340
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 342
                self.deref()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 343
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 347
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 348
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 349
                self.deref()
                pass

            elif la_ == 4:
                self.state = 350
                self.addr()
                pass

            elif la_ == 5:
                self.state = 351
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 352
                self.rvalue(25)
                pass

            elif la_ == 6:
                self.state = 353
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 354
                self.rvalue(24)
                pass

            elif la_ == 7:
                self.state = 355
                self.match(GrammarParser.LPAREN)
                self.state = 356
                self.rvalue(0)
                self.state = 357
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 359
                self.explicitConversion()
                pass

            elif la_ == 9:
                self.state = 360
                self.postFixIncrement()
                pass

            elif la_ == 10:
                self.state = 361
                self.postFixDecrement()
                pass

            elif la_ == 11:
                self.state = 362
                self.preFixIncrement()
                pass

            elif la_ == 12:
                self.state = 363
                self.preFixDecrement()
                pass

            elif la_ == 13:
                self.state = 364
                self.functionCall()
                pass

            elif la_ == 14:
                self.state = 365
                self.jumpStatement()
                pass

            elif la_ == 15:
                self.state = 366
                self.arrayElement()
                pass

            elif la_ == 16:
                self.state = 367
                self.arrayInitializer()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 408
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 370
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 371
                        self.match(GrammarParser.DIV)
                        self.state = 372
                        self.rvalue(24)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 373
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 374
                        self.match(GrammarParser.MOD)
                        self.state = 375
                        self.rvalue(23)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 376
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 377
                        self.match(GrammarParser.MULT)
                        self.state = 378
                        self.rvalue(22)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 379
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 380
                        self.match(GrammarParser.MINUS)
                        self.state = 381
                        self.rvalue(21)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 382
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 383
                        self.match(GrammarParser.PLUS)
                        self.state = 384
                        self.rvalue(20)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 385
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 386
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 387
                        self.rvalue(19)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 388
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 389
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 390
                        self.rvalue(18)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 391
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 392
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 393
                        self.rvalue(17)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 394
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 395
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 396
                        self.rvalue(16)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 397
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 398
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 399
                        self.rvalue(15)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 400
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 401
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 402
                        self.rvalue(14)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 403
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 404
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 405
                        self.rvalue(13)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 406
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 407
                        self.conditionalExpression()
                        pass

             
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(GrammarParser.GREATER_THAN)
                self.state = 414
                self.rvalue(0)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.match(GrammarParser.LESS_THAN)
                self.state = 416
                self.rvalue(0)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                self.match(GrammarParser.GREATER_EQUAL)
                self.state = 418
                self.rvalue(0)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 419
                self.match(GrammarParser.LESS_EQUAL)
                self.state = 420
                self.rvalue(0)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 5)
                self.state = 421
                self.match(GrammarParser.EQUALS)
                self.state = 422
                self.rvalue(0)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 6)
                self.state = 423
                self.match(GrammarParser.NOT_EQUAL)
                self.state = 424
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
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(GrammarParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.match(GrammarParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.match(GrammarParser.T__16)
                self.state = 431
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 430
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
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31 or _la==32:
                    self.state = 435
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 441
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [54, 55, 56]:
                    self.state = 438
                    self.literal()
                    pass
                elif token in [58]:
                    self.state = 439
                    self.identifier()
                    pass
                elif token in [33]:
                    self.state = 440
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 443
                        self.match(GrammarParser.PLUS)
                        self.state = 444
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 447 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 449
                    self.match(GrammarParser.PLUS)


                self.state = 455
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [54, 55, 56]:
                    self.state = 452
                    self.literal()
                    pass
                elif token in [58]:
                    self.state = 453
                    self.identifier()
                    pass
                elif token in [33]:
                    self.state = 454
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 459 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 457
                        self.match(GrammarParser.MINUS)
                        self.state = 458
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 461 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 463
                    self.match(GrammarParser.MINUS)


                self.state = 469
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [54, 55, 56]:
                    self.state = 466
                    self.literal()
                    pass
                elif token in [58]:
                    self.state = 467
                    self.identifier()
                    pass
                elif token in [33]:
                    self.state = 468
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
            self.state = 473
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126100789566373888) != 0)):
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
            self.state = 476 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 475
                self.match(GrammarParser.LPAREN)
                self.state = 478 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==27):
                    break

            self.state = 481 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 480
                self.type_()
                self.state = 483 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 288230376184217600) != 0)):
                    break

            self.state = 485
            self.match(GrammarParser.RPAREN)
            self.state = 486
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
            self.state = 488
            self.type_()
            self.state = 490 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 489
                self.match(GrammarParser.MULT)
                self.state = 492 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==33):
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
            self.state = 495 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 494
                self.match(GrammarParser.MULT)
                self.state = 497 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==33):
                    break

            self.state = 499
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
            self.state = 502 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 501
                self.match(GrammarParser.BITWISE_AND)
                self.state = 504 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==44):
                    break

            self.state = 506
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
            self.state = 508
            self.match(GrammarParser.T__17)
            self.state = 509
            self.match(GrammarParser.IDENTIFIER)
            self.state = 510
            self.match(GrammarParser.LBRACE)
            self.state = 511
            self.match(GrammarParser.IDENTIFIER)
            self.state = 516
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 512
                self.match(GrammarParser.COMMA)
                self.state = 513
                self.match(GrammarParser.IDENTIFIER)
                self.state = 518
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 519
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
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.enumVariableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
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
            self.state = 525
            self.match(GrammarParser.T__17)
            self.state = 526
            self.match(GrammarParser.IDENTIFIER)
            self.state = 527
            self.match(GrammarParser.IDENTIFIER)
            self.state = 528
            self.match(GrammarParser.T__13)
            self.state = 529
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
            self.state = 531
            self.match(GrammarParser.T__17)
            self.state = 532
            self.match(GrammarParser.IDENTIFIER)
            self.state = 533
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
            self.state = 535
            self.lvalue()
            self.state = 536
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
            self.state = 538
            self.lvalue()
            self.state = 539
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
            self.state = 541
            self.match(GrammarParser.INCREMENT)
            self.state = 542
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
            self.state = 544
            self.match(GrammarParser.DECREMENT)
            self.state = 545
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
            self.state = 547
            self.match(GrammarParser.T__18)
            self.state = 548
            self.type_()
            self.state = 549
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
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 551
                self.match(GrammarParser.T__19)
                self.state = 556
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 557
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 288230376183169024) != 0)):
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
            self.state = 559
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
            self.state = 561
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
        self.enterRule(localctx, 82, self.RULE_arrayStatement)
        try:
            self.state = 568
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                self.arrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 564
                self.arrayDefinition()
                self.state = 565
                self.match(GrammarParser.T__13)
                self.state = 566
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
        self.enterRule(localctx, 84, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.type_()
            self.state = 571
            self.match(GrammarParser.IDENTIFIER)
            self.state = 575 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 572
                self.match(GrammarParser.T__24)
                self.state = 573
                self.match(GrammarParser.INT)
                self.state = 574
                self.match(GrammarParser.T__25)
                self.state = 577 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
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
        self.enterRule(localctx, 86, self.RULE_arrayDefinition)
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
                self.match(GrammarParser.T__24)
                self.state = 582
                self.match(GrammarParser.INT)
                self.state = 583
                self.match(GrammarParser.T__25)
                self.state = 586 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 588
            self.match(GrammarParser.T__13)
            self.state = 591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.state = 589
                self.arrayInitializer()
                pass
            elif token in [58]:
                self.state = 590
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
        self.enterRule(localctx, 88, self.RULE_arrayInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(GrammarParser.LBRACE)
            self.state = 602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2144997667945807872) != 0):
                self.state = 594
                self.rvalue(0)
                self.state = 599
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==53:
                    self.state = 595
                    self.match(GrammarParser.COMMA)
                    self.state = 596
                    self.rvalue(0)
                    self.state = 601
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 604
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
        self.enterRule(localctx, 90, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.identifier()
            self.state = 614 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 607
                    self.match(GrammarParser.T__24)
                    self.state = 610
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        self.state = 608
                        self.rvalue(0)
                        pass

                    elif la_ == 2:
                        self.state = 609
                        self.identifier()
                        pass


                    self.state = 612
                    self.match(GrammarParser.T__25)

                else:
                    raise NoViableAltException(self)
                self.state = 616 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

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
         




