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
        4,1,62,724,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,1,0,1,0,1,0,4,0,112,8,0,11,0,12,0,113,1,0,4,0,117,8,0,
        11,0,12,0,118,1,0,1,0,1,1,1,1,1,1,1,1,3,1,127,8,1,1,2,1,2,5,2,131,
        8,2,10,2,12,2,134,9,2,1,2,1,2,1,3,1,3,4,3,140,8,3,11,3,12,3,141,
        1,3,1,3,4,3,146,8,3,11,3,12,3,147,1,3,1,3,1,3,4,3,153,8,3,11,3,12,
        3,154,1,3,1,3,4,3,159,8,3,11,3,12,3,160,1,3,1,3,1,3,1,3,1,3,1,3,
        4,3,169,8,3,11,3,12,3,170,1,3,1,3,4,3,175,8,3,11,3,12,3,176,1,3,
        1,3,1,3,1,3,4,3,183,8,3,11,3,12,3,184,1,3,1,3,4,3,189,8,3,11,3,12,
        3,190,3,3,193,8,3,1,4,1,4,3,4,197,8,4,1,4,1,4,1,4,3,4,202,8,4,1,
        4,1,4,1,4,1,4,1,4,3,4,209,8,4,1,4,1,4,1,4,3,4,214,8,4,1,4,1,4,1,
        4,3,4,219,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,228,8,5,1,5,1,5,5,
        5,232,8,5,10,5,12,5,235,9,5,1,5,1,5,1,6,1,6,3,6,241,8,6,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,253,8,8,10,8,12,8,256,9,8,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,265,8,10,1,10,1,10,3,10,269,8,
        10,1,10,1,10,1,10,5,10,274,8,10,10,10,12,10,277,9,10,1,11,1,11,1,
        11,3,11,282,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,292,
        8,12,10,12,12,12,295,9,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,303,
        8,13,10,13,12,13,306,9,13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,314,
        8,14,10,14,12,14,317,9,14,1,14,1,14,1,14,5,14,322,8,14,10,14,12,
        14,325,9,14,3,14,327,8,14,1,15,1,15,5,15,331,8,15,10,15,12,15,334,
        9,15,1,15,3,15,337,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,3,21,368,8,21,1,21,1,21,
        3,21,372,8,21,1,21,1,21,3,21,376,8,21,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,3,22,385,8,22,5,22,387,8,22,10,22,12,22,390,9,22,1,22,1,
        22,1,23,1,23,1,23,1,23,1,23,5,23,399,8,23,10,23,12,23,402,9,23,1,
        23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,3,26,416,
        8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        3,27,430,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,
        454,8,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,5,28,510,8,28,10,28,12,28,513,9,28,1,29,1,29,
        1,29,1,29,3,29,519,8,29,3,29,521,8,29,1,30,3,30,524,8,30,1,30,1,
        30,1,30,3,30,529,8,30,1,30,1,30,4,30,533,8,30,11,30,12,30,534,1,
        30,3,30,538,8,30,1,30,1,30,1,30,3,30,543,8,30,1,30,1,30,4,30,547,
        8,30,11,30,12,30,548,1,30,3,30,552,8,30,1,30,1,30,1,30,3,30,557,
        8,30,3,30,559,8,30,1,31,1,31,1,32,4,32,564,8,32,11,32,12,32,565,
        1,32,4,32,569,8,32,11,32,12,32,570,1,32,1,32,1,32,1,33,1,33,4,33,
        578,8,33,11,33,12,33,579,1,34,4,34,583,8,34,11,34,12,34,584,1,34,
        1,34,1,35,4,35,590,8,35,11,35,12,35,591,1,35,1,35,1,36,1,36,1,36,
        1,36,1,36,1,36,5,36,602,8,36,10,36,12,36,605,9,36,1,36,1,36,1,37,
        1,37,3,37,611,8,37,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,
        1,39,1,40,1,40,1,40,1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,
        1,44,1,44,1,44,3,44,638,8,44,1,45,1,45,1,45,1,45,1,45,4,45,645,8,
        45,11,45,12,45,646,1,46,1,46,1,46,1,46,4,46,653,8,46,11,46,12,46,
        654,1,46,1,46,1,46,3,46,660,8,46,1,46,1,46,1,46,1,46,3,46,666,8,
        46,1,47,1,47,1,47,1,47,1,47,4,47,673,8,47,11,47,12,47,674,1,47,1,
        47,1,47,3,47,680,8,47,1,48,1,48,1,48,3,48,685,8,48,1,48,1,48,1,48,
        3,48,690,8,48,5,48,692,8,48,10,48,12,48,695,9,48,1,48,1,48,1,49,
        1,49,1,49,1,49,1,49,4,49,704,8,49,11,49,12,49,705,1,50,1,50,1,50,
        1,50,1,51,5,51,713,8,51,10,51,12,51,716,9,51,1,51,1,51,1,52,1,52,
        1,53,1,53,1,53,0,3,20,24,56,54,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,0,3,
        1,0,29,30,1,0,52,54,2,0,21,24,57,57,801,0,116,1,0,0,0,2,126,1,0,
        0,0,4,128,1,0,0,0,6,192,1,0,0,0,8,218,1,0,0,0,10,220,1,0,0,0,12,
        240,1,0,0,0,14,242,1,0,0,0,16,246,1,0,0,0,18,257,1,0,0,0,20,261,
        1,0,0,0,22,278,1,0,0,0,24,285,1,0,0,0,26,296,1,0,0,0,28,326,1,0,
        0,0,30,328,1,0,0,0,32,338,1,0,0,0,34,344,1,0,0,0,36,351,1,0,0,0,
        38,354,1,0,0,0,40,360,1,0,0,0,42,367,1,0,0,0,44,377,1,0,0,0,46,393,
        1,0,0,0,48,405,1,0,0,0,50,407,1,0,0,0,52,415,1,0,0,0,54,429,1,0,
        0,0,56,453,1,0,0,0,58,520,1,0,0,0,60,558,1,0,0,0,62,560,1,0,0,0,
        64,563,1,0,0,0,66,575,1,0,0,0,68,582,1,0,0,0,70,589,1,0,0,0,72,595,
        1,0,0,0,74,610,1,0,0,0,76,612,1,0,0,0,78,618,1,0,0,0,80,622,1,0,
        0,0,82,625,1,0,0,0,84,628,1,0,0,0,86,631,1,0,0,0,88,637,1,0,0,0,
        90,639,1,0,0,0,92,665,1,0,0,0,94,667,1,0,0,0,96,681,1,0,0,0,98,698,
        1,0,0,0,100,707,1,0,0,0,102,714,1,0,0,0,104,719,1,0,0,0,106,721,
        1,0,0,0,108,117,3,106,53,0,109,111,3,2,1,0,110,112,5,50,0,0,111,
        110,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,
        117,1,0,0,0,115,117,3,8,4,0,116,108,1,0,0,0,116,109,1,0,0,0,116,
        115,1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,
        120,1,0,0,0,120,121,5,0,0,1,121,1,1,0,0,0,122,127,3,72,36,0,123,
        127,3,10,5,0,124,127,3,52,26,0,125,127,3,100,50,0,126,122,1,0,0,
        0,126,123,1,0,0,0,126,124,1,0,0,0,126,125,1,0,0,0,127,3,1,0,0,0,
        128,132,5,27,0,0,129,131,3,6,3,0,130,129,1,0,0,0,131,134,1,0,0,0,
        132,130,1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,132,1,0,0,0,
        135,136,5,28,0,0,136,5,1,0,0,0,137,139,3,56,28,0,138,140,5,50,0,
        0,139,138,1,0,0,0,140,141,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,
        0,142,193,1,0,0,0,143,145,3,52,26,0,144,146,5,50,0,0,145,144,1,0,
        0,0,146,147,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,193,1,0,
        0,0,149,193,3,106,53,0,150,152,3,44,22,0,151,153,5,50,0,0,152,151,
        1,0,0,0,153,154,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,193,
        1,0,0,0,156,158,3,46,23,0,157,159,5,50,0,0,158,157,1,0,0,0,159,160,
        1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,193,1,0,0,0,162,193,
        3,4,2,0,163,193,3,30,15,0,164,193,3,38,19,0,165,193,3,40,20,0,166,
        168,3,74,37,0,167,169,5,50,0,0,168,167,1,0,0,0,169,170,1,0,0,0,170,
        168,1,0,0,0,170,171,1,0,0,0,171,193,1,0,0,0,172,174,3,58,29,0,173,
        175,5,50,0,0,174,173,1,0,0,0,175,176,1,0,0,0,176,174,1,0,0,0,176,
        177,1,0,0,0,177,193,1,0,0,0,178,193,3,8,4,0,179,193,3,26,13,0,180,
        182,3,88,44,0,181,183,5,50,0,0,182,181,1,0,0,0,183,184,1,0,0,0,184,
        182,1,0,0,0,184,185,1,0,0,0,185,193,1,0,0,0,186,188,3,12,6,0,187,
        189,5,50,0,0,188,187,1,0,0,0,189,190,1,0,0,0,190,188,1,0,0,0,190,
        191,1,0,0,0,191,193,1,0,0,0,192,137,1,0,0,0,192,143,1,0,0,0,192,
        149,1,0,0,0,192,150,1,0,0,0,192,156,1,0,0,0,192,162,1,0,0,0,192,
        163,1,0,0,0,192,164,1,0,0,0,192,165,1,0,0,0,192,166,1,0,0,0,192,
        172,1,0,0,0,192,178,1,0,0,0,192,179,1,0,0,0,192,180,1,0,0,0,192,
        186,1,0,0,0,193,7,1,0,0,0,194,197,3,102,51,0,195,197,3,66,33,0,196,
        194,1,0,0,0,196,195,1,0,0,0,197,198,1,0,0,0,198,199,5,57,0,0,199,
        201,5,25,0,0,200,202,3,20,10,0,201,200,1,0,0,0,201,202,1,0,0,0,202,
        203,1,0,0,0,203,204,5,26,0,0,204,205,3,4,2,0,205,219,1,0,0,0,206,
        209,3,102,51,0,207,209,3,66,33,0,208,206,1,0,0,0,208,207,1,0,0,0,
        209,210,1,0,0,0,210,211,5,57,0,0,211,213,5,25,0,0,212,214,3,20,10,
        0,213,212,1,0,0,0,213,214,1,0,0,0,214,215,1,0,0,0,215,216,5,26,0,
        0,216,217,5,50,0,0,217,219,1,0,0,0,218,196,1,0,0,0,218,208,1,0,0,
        0,219,9,1,0,0,0,220,221,5,1,0,0,221,222,5,57,0,0,222,233,5,27,0,
        0,223,224,3,102,51,0,224,225,3,104,52,0,225,228,1,0,0,0,226,228,
        3,90,45,0,227,223,1,0,0,0,227,226,1,0,0,0,228,229,1,0,0,0,229,230,
        5,50,0,0,230,232,1,0,0,0,231,227,1,0,0,0,232,235,1,0,0,0,233,231,
        1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,233,1,0,0,0,236,237,
        5,28,0,0,237,11,1,0,0,0,238,241,3,14,7,0,239,241,3,18,9,0,240,238,
        1,0,0,0,240,239,1,0,0,0,241,13,1,0,0,0,242,243,5,1,0,0,243,244,5,
        57,0,0,244,245,5,57,0,0,245,15,1,0,0,0,246,247,5,57,0,0,247,248,
        5,2,0,0,248,254,5,57,0,0,249,250,5,3,0,0,250,251,5,52,0,0,251,253,
        5,4,0,0,252,249,1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,
        1,0,0,0,255,17,1,0,0,0,256,254,1,0,0,0,257,258,3,16,8,0,258,259,
        5,5,0,0,259,260,3,56,28,0,260,19,1,0,0,0,261,264,6,10,-1,0,262,265,
        3,66,33,0,263,265,3,102,51,0,264,262,1,0,0,0,264,263,1,0,0,0,265,
        268,1,0,0,0,266,269,3,70,35,0,267,269,3,104,52,0,268,266,1,0,0,0,
        268,267,1,0,0,0,269,275,1,0,0,0,270,271,10,1,0,0,271,272,5,51,0,
        0,272,274,3,20,10,2,273,270,1,0,0,0,274,277,1,0,0,0,275,273,1,0,
        0,0,275,276,1,0,0,0,276,21,1,0,0,0,277,275,1,0,0,0,278,279,5,57,
        0,0,279,281,5,25,0,0,280,282,3,24,12,0,281,280,1,0,0,0,281,282,1,
        0,0,0,282,283,1,0,0,0,283,284,5,26,0,0,284,23,1,0,0,0,285,286,6,
        12,-1,0,286,287,3,56,28,0,287,293,1,0,0,0,288,289,10,1,0,0,289,290,
        5,51,0,0,290,292,3,24,12,2,291,288,1,0,0,0,292,295,1,0,0,0,293,291,
        1,0,0,0,293,294,1,0,0,0,294,25,1,0,0,0,295,293,1,0,0,0,296,297,5,
        6,0,0,297,298,5,25,0,0,298,299,3,56,28,0,299,300,5,26,0,0,300,304,
        5,27,0,0,301,303,3,28,14,0,302,301,1,0,0,0,303,306,1,0,0,0,304,302,
        1,0,0,0,304,305,1,0,0,0,305,307,1,0,0,0,306,304,1,0,0,0,307,308,
        5,28,0,0,308,27,1,0,0,0,309,310,5,7,0,0,310,311,3,62,31,0,311,315,
        5,49,0,0,312,314,3,6,3,0,313,312,1,0,0,0,314,317,1,0,0,0,315,313,
        1,0,0,0,315,316,1,0,0,0,316,327,1,0,0,0,317,315,1,0,0,0,318,319,
        5,8,0,0,319,323,5,49,0,0,320,322,3,6,3,0,321,320,1,0,0,0,322,325,
        1,0,0,0,323,321,1,0,0,0,323,324,1,0,0,0,324,327,1,0,0,0,325,323,
        1,0,0,0,326,309,1,0,0,0,326,318,1,0,0,0,327,29,1,0,0,0,328,332,3,
        32,16,0,329,331,3,34,17,0,330,329,1,0,0,0,331,334,1,0,0,0,332,330,
        1,0,0,0,332,333,1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,0,335,337,
        3,36,18,0,336,335,1,0,0,0,336,337,1,0,0,0,337,31,1,0,0,0,338,339,
        5,9,0,0,339,340,5,25,0,0,340,341,3,56,28,0,341,342,5,26,0,0,342,
        343,3,4,2,0,343,33,1,0,0,0,344,345,5,10,0,0,345,346,5,9,0,0,346,
        347,5,25,0,0,347,348,3,56,28,0,348,349,5,26,0,0,349,350,3,4,2,0,
        350,35,1,0,0,0,351,352,5,10,0,0,352,353,3,4,2,0,353,37,1,0,0,0,354,
        355,5,11,0,0,355,356,5,25,0,0,356,357,3,56,28,0,357,358,5,26,0,0,
        358,359,3,4,2,0,359,39,1,0,0,0,360,361,5,12,0,0,361,362,5,25,0,0,
        362,363,3,42,21,0,363,364,5,26,0,0,364,365,3,4,2,0,365,41,1,0,0,
        0,366,368,3,52,26,0,367,366,1,0,0,0,367,368,1,0,0,0,368,369,1,0,
        0,0,369,371,5,50,0,0,370,372,3,56,28,0,371,370,1,0,0,0,371,372,1,
        0,0,0,372,373,1,0,0,0,373,375,5,50,0,0,374,376,3,56,28,0,375,374,
        1,0,0,0,375,376,1,0,0,0,376,43,1,0,0,0,377,378,5,13,0,0,378,379,
        5,25,0,0,379,388,3,48,24,0,380,384,5,51,0,0,381,385,3,56,28,0,382,
        385,3,50,25,0,383,385,3,16,8,0,384,381,1,0,0,0,384,382,1,0,0,0,384,
        383,1,0,0,0,385,387,1,0,0,0,386,380,1,0,0,0,387,390,1,0,0,0,388,
        386,1,0,0,0,388,389,1,0,0,0,389,391,1,0,0,0,390,388,1,0,0,0,391,
        392,5,26,0,0,392,45,1,0,0,0,393,394,5,14,0,0,394,395,5,25,0,0,395,
        400,3,48,24,0,396,397,5,51,0,0,397,399,3,70,35,0,398,396,1,0,0,0,
        399,402,1,0,0,0,400,398,1,0,0,0,400,401,1,0,0,0,401,403,1,0,0,0,
        402,400,1,0,0,0,403,404,5,26,0,0,404,47,1,0,0,0,405,406,5,55,0,0,
        406,49,1,0,0,0,407,408,5,55,0,0,408,51,1,0,0,0,409,410,3,54,27,0,
        410,411,5,5,0,0,411,412,3,56,28,0,412,416,1,0,0,0,413,416,3,54,27,
        0,414,416,3,100,50,0,415,409,1,0,0,0,415,413,1,0,0,0,415,414,1,0,
        0,0,416,53,1,0,0,0,417,430,3,104,52,0,418,419,3,102,51,0,419,420,
        3,104,52,0,420,430,1,0,0,0,421,422,3,66,33,0,422,423,3,104,52,0,
        423,430,1,0,0,0,424,430,3,68,34,0,425,426,5,25,0,0,426,427,3,54,
        27,0,427,428,5,26,0,0,428,430,1,0,0,0,429,417,1,0,0,0,429,418,1,
        0,0,0,429,421,1,0,0,0,429,424,1,0,0,0,429,425,1,0,0,0,430,55,1,0,
        0,0,431,432,6,28,-1,0,432,454,3,60,30,0,433,454,3,104,52,0,434,454,
        3,68,34,0,435,454,3,70,35,0,436,437,5,48,0,0,437,454,3,56,28,30,
        438,439,5,45,0,0,439,454,3,56,28,29,440,441,5,25,0,0,441,442,3,56,
        28,0,442,443,5,26,0,0,443,454,1,0,0,0,444,454,3,64,32,0,445,454,
        3,80,40,0,446,454,3,82,41,0,447,454,3,84,42,0,448,454,3,86,43,0,
        449,454,3,22,11,0,450,454,3,58,29,0,451,454,3,98,49,0,452,454,3,
        50,25,0,453,431,1,0,0,0,453,433,1,0,0,0,453,434,1,0,0,0,453,435,
        1,0,0,0,453,436,1,0,0,0,453,438,1,0,0,0,453,440,1,0,0,0,453,444,
        1,0,0,0,453,445,1,0,0,0,453,446,1,0,0,0,453,447,1,0,0,0,453,448,
        1,0,0,0,453,449,1,0,0,0,453,450,1,0,0,0,453,451,1,0,0,0,453,452,
        1,0,0,0,454,511,1,0,0,0,455,456,10,28,0,0,456,457,5,32,0,0,457,510,
        3,56,28,29,458,459,10,27,0,0,459,460,5,33,0,0,460,510,3,56,28,28,
        461,462,10,26,0,0,462,463,5,31,0,0,463,510,3,56,28,27,464,465,10,
        25,0,0,465,466,5,30,0,0,466,510,3,56,28,26,467,468,10,24,0,0,468,
        469,5,29,0,0,469,510,3,56,28,25,470,471,10,23,0,0,471,472,5,40,0,
        0,472,510,3,56,28,24,473,474,10,22,0,0,474,475,5,41,0,0,475,510,
        3,56,28,23,476,477,10,21,0,0,477,478,5,42,0,0,478,510,3,56,28,22,
        479,480,10,20,0,0,480,481,5,43,0,0,481,510,3,56,28,21,482,483,10,
        19,0,0,483,484,5,44,0,0,484,510,3,56,28,20,485,486,10,18,0,0,486,
        487,5,38,0,0,487,510,3,56,28,19,488,489,10,17,0,0,489,490,5,39,0,
        0,490,510,3,56,28,18,491,492,10,16,0,0,492,493,5,46,0,0,493,510,
        3,56,28,17,494,495,10,15,0,0,495,496,5,47,0,0,496,510,3,56,28,16,
        497,498,10,14,0,0,498,499,5,34,0,0,499,510,3,56,28,15,500,501,10,
        13,0,0,501,502,5,35,0,0,502,510,3,56,28,14,503,504,10,12,0,0,504,
        505,5,36,0,0,505,510,3,56,28,13,506,507,10,11,0,0,507,508,5,37,0,
        0,508,510,3,56,28,12,509,455,1,0,0,0,509,458,1,0,0,0,509,461,1,0,
        0,0,509,464,1,0,0,0,509,467,1,0,0,0,509,470,1,0,0,0,509,473,1,0,
        0,0,509,476,1,0,0,0,509,479,1,0,0,0,509,482,1,0,0,0,509,485,1,0,
        0,0,509,488,1,0,0,0,509,491,1,0,0,0,509,494,1,0,0,0,509,497,1,0,
        0,0,509,500,1,0,0,0,509,503,1,0,0,0,509,506,1,0,0,0,510,513,1,0,
        0,0,511,509,1,0,0,0,511,512,1,0,0,0,512,57,1,0,0,0,513,511,1,0,0,
        0,514,521,5,15,0,0,515,521,5,16,0,0,516,518,5,17,0,0,517,519,3,56,
        28,0,518,517,1,0,0,0,518,519,1,0,0,0,519,521,1,0,0,0,520,514,1,0,
        0,0,520,515,1,0,0,0,520,516,1,0,0,0,521,59,1,0,0,0,522,524,7,0,0,
        0,523,522,1,0,0,0,523,524,1,0,0,0,524,528,1,0,0,0,525,529,3,62,31,
        0,526,529,3,104,52,0,527,529,3,68,34,0,528,525,1,0,0,0,528,526,1,
        0,0,0,528,527,1,0,0,0,529,559,1,0,0,0,530,531,5,29,0,0,531,533,5,
        30,0,0,532,530,1,0,0,0,533,534,1,0,0,0,534,532,1,0,0,0,534,535,1,
        0,0,0,535,537,1,0,0,0,536,538,5,29,0,0,537,536,1,0,0,0,537,538,1,
        0,0,0,538,542,1,0,0,0,539,543,3,62,31,0,540,543,3,104,52,0,541,543,
        3,68,34,0,542,539,1,0,0,0,542,540,1,0,0,0,542,541,1,0,0,0,543,559,
        1,0,0,0,544,545,5,30,0,0,545,547,5,29,0,0,546,544,1,0,0,0,547,548,
        1,0,0,0,548,546,1,0,0,0,548,549,1,0,0,0,549,551,1,0,0,0,550,552,
        5,30,0,0,551,550,1,0,0,0,551,552,1,0,0,0,552,556,1,0,0,0,553,557,
        3,62,31,0,554,557,3,104,52,0,555,557,3,68,34,0,556,553,1,0,0,0,556,
        554,1,0,0,0,556,555,1,0,0,0,557,559,1,0,0,0,558,523,1,0,0,0,558,
        532,1,0,0,0,558,546,1,0,0,0,559,61,1,0,0,0,560,561,7,1,0,0,561,63,
        1,0,0,0,562,564,5,25,0,0,563,562,1,0,0,0,564,565,1,0,0,0,565,563,
        1,0,0,0,565,566,1,0,0,0,566,568,1,0,0,0,567,569,3,102,51,0,568,567,
        1,0,0,0,569,570,1,0,0,0,570,568,1,0,0,0,570,571,1,0,0,0,571,572,
        1,0,0,0,572,573,5,26,0,0,573,574,3,56,28,0,574,65,1,0,0,0,575,577,
        3,102,51,0,576,578,5,31,0,0,577,576,1,0,0,0,578,579,1,0,0,0,579,
        577,1,0,0,0,579,580,1,0,0,0,580,67,1,0,0,0,581,583,5,31,0,0,582,
        581,1,0,0,0,583,584,1,0,0,0,584,582,1,0,0,0,584,585,1,0,0,0,585,
        586,1,0,0,0,586,587,3,104,52,0,587,69,1,0,0,0,588,590,5,42,0,0,589,
        588,1,0,0,0,590,591,1,0,0,0,591,589,1,0,0,0,591,592,1,0,0,0,592,
        593,1,0,0,0,593,594,3,104,52,0,594,71,1,0,0,0,595,596,5,18,0,0,596,
        597,5,57,0,0,597,598,5,27,0,0,598,603,5,57,0,0,599,600,5,51,0,0,
        600,602,5,57,0,0,601,599,1,0,0,0,602,605,1,0,0,0,603,601,1,0,0,0,
        603,604,1,0,0,0,604,606,1,0,0,0,605,603,1,0,0,0,606,607,5,28,0,0,
        607,73,1,0,0,0,608,611,3,76,38,0,609,611,3,78,39,0,610,608,1,0,0,
        0,610,609,1,0,0,0,611,75,1,0,0,0,612,613,5,18,0,0,613,614,5,57,0,
        0,614,615,5,57,0,0,615,616,5,5,0,0,616,617,5,57,0,0,617,77,1,0,0,
        0,618,619,5,18,0,0,619,620,5,57,0,0,620,621,5,57,0,0,621,79,1,0,
        0,0,622,623,3,54,27,0,623,624,5,58,0,0,624,81,1,0,0,0,625,626,3,
        54,27,0,626,627,5,59,0,0,627,83,1,0,0,0,628,629,5,58,0,0,629,630,
        3,54,27,0,630,85,1,0,0,0,631,632,5,59,0,0,632,633,3,54,27,0,633,
        87,1,0,0,0,634,638,3,90,45,0,635,638,3,92,46,0,636,638,3,94,47,0,
        637,634,1,0,0,0,637,635,1,0,0,0,637,636,1,0,0,0,638,89,1,0,0,0,639,
        640,3,102,51,0,640,644,3,104,52,0,641,642,5,3,0,0,642,643,5,52,0,
        0,643,645,5,4,0,0,644,641,1,0,0,0,645,646,1,0,0,0,646,644,1,0,0,
        0,646,647,1,0,0,0,647,91,1,0,0,0,648,652,3,104,52,0,649,650,5,3,
        0,0,650,651,5,52,0,0,651,653,5,4,0,0,652,649,1,0,0,0,653,654,1,0,
        0,0,654,652,1,0,0,0,654,655,1,0,0,0,655,656,1,0,0,0,656,659,5,5,
        0,0,657,660,3,56,28,0,658,660,3,96,48,0,659,657,1,0,0,0,659,658,
        1,0,0,0,660,666,1,0,0,0,661,662,3,104,52,0,662,663,5,5,0,0,663,664,
        3,96,48,0,664,666,1,0,0,0,665,648,1,0,0,0,665,661,1,0,0,0,666,93,
        1,0,0,0,667,668,3,102,51,0,668,672,3,104,52,0,669,670,5,3,0,0,670,
        671,5,52,0,0,671,673,5,4,0,0,672,669,1,0,0,0,673,674,1,0,0,0,674,
        672,1,0,0,0,674,675,1,0,0,0,675,676,1,0,0,0,676,679,5,5,0,0,677,
        680,3,96,48,0,678,680,3,50,25,0,679,677,1,0,0,0,679,678,1,0,0,0,
        680,95,1,0,0,0,681,684,5,27,0,0,682,685,3,56,28,0,683,685,3,96,48,
        0,684,682,1,0,0,0,684,683,1,0,0,0,685,693,1,0,0,0,686,689,5,51,0,
        0,687,690,3,56,28,0,688,690,3,96,48,0,689,687,1,0,0,0,689,688,1,
        0,0,0,690,692,1,0,0,0,691,686,1,0,0,0,692,695,1,0,0,0,693,691,1,
        0,0,0,693,694,1,0,0,0,694,696,1,0,0,0,695,693,1,0,0,0,696,697,5,
        28,0,0,697,97,1,0,0,0,698,703,3,104,52,0,699,700,5,3,0,0,700,701,
        3,56,28,0,701,702,5,4,0,0,702,704,1,0,0,0,703,699,1,0,0,0,704,705,
        1,0,0,0,705,703,1,0,0,0,705,706,1,0,0,0,706,99,1,0,0,0,707,708,5,
        19,0,0,708,709,3,102,51,0,709,710,5,57,0,0,710,101,1,0,0,0,711,713,
        5,20,0,0,712,711,1,0,0,0,713,716,1,0,0,0,714,712,1,0,0,0,714,715,
        1,0,0,0,715,717,1,0,0,0,716,714,1,0,0,0,717,718,7,2,0,0,718,103,
        1,0,0,0,719,720,5,57,0,0,720,105,1,0,0,0,721,722,5,60,0,0,722,107,
        1,0,0,0,75,113,116,118,126,132,141,147,154,160,170,176,184,190,192,
        196,201,208,213,218,227,233,240,254,264,268,275,281,293,304,315,
        323,326,332,336,367,371,375,384,388,400,415,429,453,509,511,518,
        520,523,528,534,537,542,548,551,556,558,565,570,579,584,591,603,
        610,637,646,654,659,665,674,679,684,689,693,705,714
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
    RULE_declaration = 1
    RULE_scope = 2
    RULE_statement = 3
    RULE_function = 4
    RULE_structDefinition = 5
    RULE_structStatement = 6
    RULE_structVariable = 7
    RULE_structMember = 8
    RULE_structAssignment = 9
    RULE_functionParams = 10
    RULE_functionCall = 11
    RULE_callParams = 12
    RULE_switchStatement = 13
    RULE_switchCase = 14
    RULE_conditional = 15
    RULE_ifStatement = 16
    RULE_elseIfStatement = 17
    RULE_elseStatement = 18
    RULE_whileLoop = 19
    RULE_forLoop = 20
    RULE_forCondition = 21
    RULE_printfStatement = 22
    RULE_scanfStatement = 23
    RULE_formatSpecifier = 24
    RULE_string = 25
    RULE_variable = 26
    RULE_lvalue = 27
    RULE_rvalue = 28
    RULE_jumpStatement = 29
    RULE_unaryExpression = 30
    RULE_literal = 31
    RULE_explicitConversion = 32
    RULE_pointer = 33
    RULE_deref = 34
    RULE_addr = 35
    RULE_enumDeclaration = 36
    RULE_enumStatement = 37
    RULE_enumVariableDefinition = 38
    RULE_enumVariableDeclaration = 39
    RULE_postFixIncrement = 40
    RULE_postFixDecrement = 41
    RULE_preFixIncrement = 42
    RULE_preFixDecrement = 43
    RULE_arrayStatement = 44
    RULE_arrayDeclaration = 45
    RULE_arrayAssignment = 46
    RULE_arrayDefinition = 47
    RULE_array = 48
    RULE_arrayElement = 49
    RULE_typedef = 50
    RULE_type = 51
    RULE_identifier = 52
    RULE_comment = 53

    ruleNames =  [ "program", "declaration", "scope", "statement", "function", 
                   "structDefinition", "structStatement", "structVariable", 
                   "structMember", "structAssignment", "functionParams", 
                   "functionCall", "callParams", "switchStatement", "switchCase", 
                   "conditional", "ifStatement", "elseIfStatement", "elseStatement", 
                   "whileLoop", "forLoop", "forCondition", "printfStatement", 
                   "scanfStatement", "formatSpecifier", "string", "variable", 
                   "lvalue", "rvalue", "jumpStatement", "unaryExpression", 
                   "literal", "explicitConversion", "pointer", "deref", 
                   "addr", "enumDeclaration", "enumStatement", "enumVariableDefinition", 
                   "enumVariableDeclaration", "postFixIncrement", "postFixDecrement", 
                   "preFixIncrement", "preFixDecrement", "arrayStatement", 
                   "arrayDeclaration", "arrayAssignment", "arrayDefinition", 
                   "array", "arrayElement", "typedef", "type", "identifier", 
                   "comment" ]

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


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(GrammarParser.DeclarationContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.FunctionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.FunctionContext,i)


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
            self.state = 116 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 108
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 109
                    self.declaration()
                    self.state = 111 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 110
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 113 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==50):
                            break

                    pass

                elif la_ == 3:
                    self.state = 115
                    self.function()
                    pass


                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1297036694897033218) != 0)):
                    break

            self.state = 120
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumDeclaration(self):
            return self.getTypedRuleContext(GrammarParser.EnumDeclarationContext,0)


        def structDefinition(self):
            return self.getTypedRuleContext(GrammarParser.StructDefinitionContext,0)


        def variable(self):
            return self.getTypedRuleContext(GrammarParser.VariableContext,0)


        def typedef(self):
            return self.getTypedRuleContext(GrammarParser.TypedefContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = GrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.enumDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.structDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.variable()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.typedef()
                pass


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
            self.state = 128
            self.match(GrammarParser.LBRACE)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                self.state = 129
                self.statement()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
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
        self.enterRule(localctx, 6, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.rvalue(0)
                self.state = 139 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 138
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 141 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.variable()
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 144
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 147 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.printfStatement()
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

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 156
                self.scanfStatement()
                self.state = 158 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 157
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 160 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.scope()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 163
                self.conditional()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 164
                self.whileLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 165
                self.forLoop()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 166
                self.enumStatement()
                self.state = 168 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 167
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 170 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 172
                self.jumpStatement()
                self.state = 174 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 173
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 176 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 178
                self.function()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 179
                self.switchStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 180
                self.arrayStatement()
                self.state = 182 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 181
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 184 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 186
                self.structStatement()
                self.state = 188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 187
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 190 
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
        self.enterRule(localctx, 8, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 194
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 195
                    self.pointer()
                    pass


                self.state = 198
                self.match(GrammarParser.IDENTIFIER)
                self.state = 199
                self.match(GrammarParser.LPAREN)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                    self.state = 200
                    self.functionParams(0)


                self.state = 203
                self.match(GrammarParser.RPAREN)
                self.state = 204
                self.scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 206
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 207
                    self.pointer()
                    pass


                self.state = 210
                self.match(GrammarParser.IDENTIFIER)
                self.state = 211
                self.match(GrammarParser.LPAREN)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                    self.state = 212
                    self.functionParams(0)


                self.state = 215
                self.match(GrammarParser.RPAREN)
                self.state = 216
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
        self.enterRule(localctx, 10, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(GrammarParser.T__0)
            self.state = 221
            self.match(GrammarParser.IDENTIFIER)
            self.state = 222
            self.match(GrammarParser.LBRACE)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                self.state = 227
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 223
                    self.type_()
                    self.state = 224
                    self.identifier()
                    pass

                elif la_ == 2:
                    self.state = 226
                    self.arrayDeclaration()
                    pass


                self.state = 229
                self.match(GrammarParser.SEMICOLON)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 236
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
        self.enterRule(localctx, 12, self.RULE_structStatement)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.structVariable()
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
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
        self.enterRule(localctx, 14, self.RULE_structVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(GrammarParser.T__0)
            self.state = 243
            self.match(GrammarParser.IDENTIFIER)
            self.state = 244
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
        self.enterRule(localctx, 16, self.RULE_structMember)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(GrammarParser.IDENTIFIER)
            self.state = 247
            self.match(GrammarParser.T__1)
            self.state = 248
            self.match(GrammarParser.IDENTIFIER)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 249
                self.match(GrammarParser.T__2)
                self.state = 250
                self.match(GrammarParser.INT)
                self.state = 251
                self.match(GrammarParser.T__3)
                self.state = 256
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
        self.enterRule(localctx, 18, self.RULE_structAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.structMember()
            self.state = 258
            self.match(GrammarParser.T__4)
            self.state = 259
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_functionParams, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 262
                self.pointer()
                pass

            elif la_ == 2:
                self.state = 263
                self.type_()
                pass


            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 266
                self.addr()
                pass
            elif token in [57]:
                self.state = 267
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.FunctionParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParams)
                    self.state = 270
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 271
                    self.match(GrammarParser.COMMA)
                    self.state = 272
                    self.functionParams(2) 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(GrammarParser.IDENTIFIER)
            self.state = 279
            self.match(GrammarParser.LPAREN)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 280
                self.callParams(0)


            self.state = 283
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_callParams, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.rvalue(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CallParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callParams)
                    self.state = 288
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 289
                    self.match(GrammarParser.COMMA)
                    self.state = 290
                    self.callParams(2) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(GrammarParser.T__5)
            self.state = 297
            self.match(GrammarParser.LPAREN)
            self.state = 298
            self.rvalue(0)
            self.state = 299
            self.match(GrammarParser.RPAREN)
            self.state = 300
            self.match(GrammarParser.LBRACE)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 301
                self.switchCase()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
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
        self.enterRule(localctx, 28, self.RULE_switchCase)
        self._la = 0 # Token type
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(GrammarParser.T__6)
                self.state = 310
                self.literal()
                self.state = 311
                self.match(GrammarParser.COLON)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                    self.state = 312
                    self.statement()
                    self.state = 317
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(GrammarParser.T__7)
                self.state = 319
                self.match(GrammarParser.COLON)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                    self.state = 320
                    self.statement()
                    self.state = 325
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
        self.enterRule(localctx, 30, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.ifStatement()
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 329
                    self.elseIfStatement() 
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 335
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
        self.enterRule(localctx, 32, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(GrammarParser.T__8)
            self.state = 339
            self.match(GrammarParser.LPAREN)
            self.state = 340
            self.rvalue(0)
            self.state = 341
            self.match(GrammarParser.RPAREN)
            self.state = 342
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
        self.enterRule(localctx, 34, self.RULE_elseIfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(GrammarParser.T__9)
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
        self.enterRule(localctx, 36, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(GrammarParser.T__9)
            self.state = 352
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
        self.enterRule(localctx, 38, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(GrammarParser.T__10)
            self.state = 355
            self.match(GrammarParser.LPAREN)
            self.state = 356
            self.rvalue(0)
            self.state = 357
            self.match(GrammarParser.RPAREN)
            self.state = 358
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
        self.enterRule(localctx, 40, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(GrammarParser.T__11)
            self.state = 361
            self.match(GrammarParser.LPAREN)
            self.state = 362
            self.forCondition()
            self.state = 363
            self.match(GrammarParser.RPAREN)
            self.state = 364
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
        self.enterRule(localctx, 42, self.RULE_forCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115190289924096) != 0):
                self.state = 366
                self.variable()


            self.state = 369
            self.match(GrammarParser.SEMICOLON)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 370
                self.rvalue(0)


            self.state = 373
            self.match(GrammarParser.SEMICOLON)
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 374
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
        self.enterRule(localctx, 44, self.RULE_printfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(GrammarParser.T__12)
            self.state = 378
            self.match(GrammarParser.LPAREN)
            self.state = 379
            self.formatSpecifier()
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 380
                self.match(GrammarParser.COMMA)
                self.state = 384
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 381
                    self.rvalue(0)
                    pass

                elif la_ == 2:
                    self.state = 382
                    self.string()
                    pass

                elif la_ == 3:
                    self.state = 383
                    self.structMember()
                    pass


                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 391
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
        self.enterRule(localctx, 46, self.RULE_scanfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(GrammarParser.T__13)
            self.state = 394
            self.match(GrammarParser.LPAREN)
            self.state = 395
            self.formatSpecifier()
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 396
                self.match(GrammarParser.COMMA)
                self.state = 397
                self.addr()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 403
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
        self.enterRule(localctx, 48, self.RULE_formatSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
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
        self.enterRule(localctx, 50, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
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
        self.enterRule(localctx, 52, self.RULE_variable)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.lvalue()
                self.state = 410
                self.match(GrammarParser.T__4)
                self.state = 411
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.lvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
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
        self.enterRule(localctx, 54, self.RULE_lvalue)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.type_()
                self.state = 419
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 421
                self.pointer()
                self.state = 422
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 424
                self.deref()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 425
                self.match(GrammarParser.LPAREN)
                self.state = 426
                self.lvalue()
                self.state = 427
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_rvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 432
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 433
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 434
                self.deref()
                pass

            elif la_ == 4:
                self.state = 435
                self.addr()
                pass

            elif la_ == 5:
                self.state = 436
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 437
                self.rvalue(30)
                pass

            elif la_ == 6:
                self.state = 438
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 439
                self.rvalue(29)
                pass

            elif la_ == 7:
                self.state = 440
                self.match(GrammarParser.LPAREN)
                self.state = 441
                self.rvalue(0)
                self.state = 442
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 444
                self.explicitConversion()
                pass

            elif la_ == 9:
                self.state = 445
                self.postFixIncrement()
                pass

            elif la_ == 10:
                self.state = 446
                self.postFixDecrement()
                pass

            elif la_ == 11:
                self.state = 447
                self.preFixIncrement()
                pass

            elif la_ == 12:
                self.state = 448
                self.preFixDecrement()
                pass

            elif la_ == 13:
                self.state = 449
                self.functionCall()
                pass

            elif la_ == 14:
                self.state = 450
                self.jumpStatement()
                pass

            elif la_ == 15:
                self.state = 451
                self.arrayElement()
                pass

            elif la_ == 16:
                self.state = 452
                self.string()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 509
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 455
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 456
                        self.match(GrammarParser.DIV)
                        self.state = 457
                        self.rvalue(29)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 458
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 459
                        self.match(GrammarParser.MOD)
                        self.state = 460
                        self.rvalue(28)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 461
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 462
                        self.match(GrammarParser.MULT)
                        self.state = 463
                        self.rvalue(27)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 464
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 465
                        self.match(GrammarParser.MINUS)
                        self.state = 466
                        self.rvalue(26)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 467
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 468
                        self.match(GrammarParser.PLUS)
                        self.state = 469
                        self.rvalue(25)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 470
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 471
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 472
                        self.rvalue(24)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 473
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 474
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 475
                        self.rvalue(23)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 476
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 477
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 478
                        self.rvalue(22)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 479
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 480
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 481
                        self.rvalue(21)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 482
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 483
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 484
                        self.rvalue(20)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 485
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 486
                        self.match(GrammarParser.EQUALS)
                        self.state = 487
                        self.rvalue(19)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 488
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 489
                        self.match(GrammarParser.NOT_EQUAL)
                        self.state = 490
                        self.rvalue(18)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 491
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 492
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 493
                        self.rvalue(17)
                        pass

                    elif la_ == 14:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 494
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 495
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 496
                        self.rvalue(16)
                        pass

                    elif la_ == 15:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 497
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 498
                        self.match(GrammarParser.GREATER_THAN)
                        self.state = 499
                        self.rvalue(15)
                        pass

                    elif la_ == 16:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 500
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 501
                        self.match(GrammarParser.LESS_THAN)
                        self.state = 502
                        self.rvalue(14)
                        pass

                    elif la_ == 17:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 503
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 504
                        self.match(GrammarParser.GREATER_EQUAL)
                        self.state = 505
                        self.rvalue(13)
                        pass

                    elif la_ == 18:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 506
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 507
                        self.match(GrammarParser.LESS_EQUAL)
                        self.state = 508
                        self.rvalue(12)
                        pass

             
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_jumpStatement)
        try:
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(GrammarParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(GrammarParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 516
                self.match(GrammarParser.T__16)
                self.state = 518
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 517
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
        self.enterRule(localctx, 60, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29 or _la==30:
                    self.state = 522
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 528
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 525
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 526
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 527
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 532 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 530
                        self.match(GrammarParser.PLUS)
                        self.state = 531
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 534 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

                self.state = 537
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 536
                    self.match(GrammarParser.PLUS)


                self.state = 542
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 539
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 540
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 541
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 546 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 544
                        self.match(GrammarParser.MINUS)
                        self.state = 545
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 548 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

                self.state = 551
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 550
                    self.match(GrammarParser.MINUS)


                self.state = 556
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 553
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 554
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 555
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
        self.enterRule(localctx, 62, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
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
        self.enterRule(localctx, 64, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 562
                self.match(GrammarParser.LPAREN)
                self.state = 565 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 568 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 567
                self.type_()
                self.state = 570 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0)):
                    break

            self.state = 572
            self.match(GrammarParser.RPAREN)
            self.state = 573
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
        self.enterRule(localctx, 66, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.type_()
            self.state = 577 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 576
                self.match(GrammarParser.MULT)
                self.state = 579 
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
        self.enterRule(localctx, 68, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 581
                self.match(GrammarParser.MULT)
                self.state = 584 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 586
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
        self.enterRule(localctx, 70, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 588
                self.match(GrammarParser.BITWISE_AND)
                self.state = 591 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
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
        self.enterRule(localctx, 72, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.match(GrammarParser.T__17)
            self.state = 596
            self.match(GrammarParser.IDENTIFIER)
            self.state = 597
            self.match(GrammarParser.LBRACE)
            self.state = 598
            self.match(GrammarParser.IDENTIFIER)
            self.state = 603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 599
                self.match(GrammarParser.COMMA)
                self.state = 600
                self.match(GrammarParser.IDENTIFIER)
                self.state = 605
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 606
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
        self.enterRule(localctx, 74, self.RULE_enumStatement)
        try:
            self.state = 610
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 608
                self.enumVariableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 609
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
        self.enterRule(localctx, 76, self.RULE_enumVariableDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.match(GrammarParser.T__17)
            self.state = 613
            self.match(GrammarParser.IDENTIFIER)
            self.state = 614
            self.match(GrammarParser.IDENTIFIER)
            self.state = 615
            self.match(GrammarParser.T__4)
            self.state = 616
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
        self.enterRule(localctx, 78, self.RULE_enumVariableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.match(GrammarParser.T__17)
            self.state = 619
            self.match(GrammarParser.IDENTIFIER)
            self.state = 620
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
        self.enterRule(localctx, 80, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.lvalue()
            self.state = 623
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
        self.enterRule(localctx, 82, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.lvalue()
            self.state = 626
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
        self.enterRule(localctx, 84, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self.match(GrammarParser.INCREMENT)
            self.state = 629
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
        self.enterRule(localctx, 86, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            self.match(GrammarParser.DECREMENT)
            self.state = 632
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
        self.enterRule(localctx, 88, self.RULE_arrayStatement)
        try:
            self.state = 637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 634
                self.arrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 635
                self.arrayAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 636
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
        self.enterRule(localctx, 90, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.type_()
            self.state = 640
            self.identifier()
            self.state = 644 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 641
                self.match(GrammarParser.T__2)
                self.state = 642
                self.match(GrammarParser.INT)
                self.state = 643
                self.match(GrammarParser.T__3)
                self.state = 646 
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
        self.enterRule(localctx, 92, self.RULE_arrayAssignment)
        self._la = 0 # Token type
        try:
            self.state = 665
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 648
                self.identifier()
                self.state = 652 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 649
                    self.match(GrammarParser.T__2)
                    self.state = 650
                    self.match(GrammarParser.INT)
                    self.state = 651
                    self.match(GrammarParser.T__3)
                    self.state = 654 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                self.state = 656
                self.match(GrammarParser.T__4)
                self.state = 659
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                    self.state = 657
                    self.rvalue(0)
                    pass
                elif token in [27]:
                    self.state = 658
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 661
                self.identifier()
                self.state = 662
                self.match(GrammarParser.T__4)
                self.state = 663
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
        self.enterRule(localctx, 94, self.RULE_arrayDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.type_()
            self.state = 668
            self.identifier()
            self.state = 672 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 669
                self.match(GrammarParser.T__2)
                self.state = 670
                self.match(GrammarParser.INT)
                self.state = 671
                self.match(GrammarParser.T__3)
                self.state = 674 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 676
            self.match(GrammarParser.T__4)
            self.state = 679
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 677
                self.array()
                pass
            elif token in [55]:
                self.state = 678
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
        self.enterRule(localctx, 96, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.match(GrammarParser.LBRACE)
            self.state = 684
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                self.state = 682
                self.rvalue(0)
                pass
            elif token in [27]:
                self.state = 683
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 693
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 686
                self.match(GrammarParser.COMMA)
                self.state = 689
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                    self.state = 687
                    self.rvalue(0)
                    pass
                elif token in [27]:
                    self.state = 688
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 695
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 696
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
        self.enterRule(localctx, 98, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self.identifier()
            self.state = 703 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 699
                    self.match(GrammarParser.T__2)
                    self.state = 700
                    self.rvalue(0)
                    self.state = 701
                    self.match(GrammarParser.T__3)

                else:
                    raise NoViableAltException(self)
                self.state = 705 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

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
        self.enterRule(localctx, 100, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
            self.match(GrammarParser.T__18)
            self.state = 708
            self.type_()
            self.state = 709
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
        self.enterRule(localctx, 102, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 711
                self.match(GrammarParser.T__19)
                self.state = 716
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 717
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
        self.enterRule(localctx, 104, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
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
        self.enterRule(localctx, 106, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
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
        self._predicates[10] = self.functionParams_sempred
        self._predicates[12] = self.callParams_sempred
        self._predicates[28] = self.rvalue_sempred
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
         




