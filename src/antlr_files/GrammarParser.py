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
        4,1,62,737,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,1,0,1,0,1,0,4,0,114,8,0,11,0,12,0,115,1,0,4,
        0,119,8,0,11,0,12,0,120,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,130,8,1,
        1,2,1,2,5,2,134,8,2,10,2,12,2,137,9,2,1,2,1,2,1,3,1,3,4,3,143,8,
        3,11,3,12,3,144,1,3,1,3,4,3,149,8,3,11,3,12,3,150,1,3,1,3,1,3,4,
        3,156,8,3,11,3,12,3,157,1,3,1,3,4,3,162,8,3,11,3,12,3,163,1,3,1,
        3,1,3,1,3,1,3,1,3,4,3,172,8,3,11,3,12,3,173,1,3,1,3,4,3,178,8,3,
        11,3,12,3,179,1,3,1,3,1,3,1,3,4,3,186,8,3,11,3,12,3,187,1,3,1,3,
        4,3,192,8,3,11,3,12,3,193,3,3,196,8,3,1,4,1,4,3,4,200,8,4,1,4,1,
        4,1,4,3,4,205,8,4,1,4,1,4,1,4,1,4,1,4,3,4,212,8,4,1,4,1,4,1,4,3,
        4,217,8,4,1,4,1,4,1,4,3,4,222,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,
        5,231,8,5,1,5,1,5,5,5,235,8,5,10,5,12,5,238,9,5,1,5,1,5,1,6,1,6,
        3,6,244,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,257,
        8,8,10,8,12,8,260,9,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,269,8,
        10,1,10,1,10,3,10,273,8,10,1,10,1,10,1,10,5,10,278,8,10,10,10,12,
        10,281,9,10,1,11,1,11,1,11,3,11,286,8,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,5,12,296,8,12,10,12,12,12,299,9,12,1,13,1,13,1,13,
        1,13,1,13,1,13,5,13,307,8,13,10,13,12,13,310,9,13,1,13,1,13,1,14,
        1,14,1,14,1,14,5,14,318,8,14,10,14,12,14,321,9,14,1,14,1,14,1,14,
        5,14,326,8,14,10,14,12,14,329,9,14,3,14,331,8,14,1,15,1,15,5,15,
        335,8,15,10,15,12,15,338,9,15,1,15,3,15,341,8,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,
        3,21,372,8,21,1,21,1,21,3,21,376,8,21,1,21,1,21,3,21,380,8,21,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,390,8,22,5,22,392,8,22,
        10,22,12,22,395,9,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,5,23,404,
        8,23,10,23,12,23,407,9,23,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,
        1,27,1,27,1,27,1,27,1,27,1,27,3,27,423,8,27,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,437,8,28,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,449,8,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,464,
        8,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,5,29,520,8,29,10,29,12,29,523,9,29,1,30,1,30,1,30,
        1,30,3,30,529,8,30,3,30,531,8,30,1,31,3,31,534,8,31,1,31,1,31,1,
        31,3,31,539,8,31,1,31,1,31,4,31,543,8,31,11,31,12,31,544,1,31,3,
        31,548,8,31,1,31,1,31,1,31,3,31,553,8,31,1,31,1,31,4,31,557,8,31,
        11,31,12,31,558,1,31,3,31,562,8,31,1,31,1,31,1,31,3,31,567,8,31,
        3,31,569,8,31,1,32,1,32,1,33,4,33,574,8,33,11,33,12,33,575,1,33,
        4,33,579,8,33,11,33,12,33,580,1,33,1,33,1,33,1,34,1,34,4,34,588,
        8,34,11,34,12,34,589,1,35,4,35,593,8,35,11,35,12,35,594,1,35,1,35,
        1,36,4,36,600,8,36,11,36,12,36,601,1,36,1,36,1,37,1,37,1,37,1,37,
        1,37,1,37,5,37,612,8,37,10,37,12,37,615,9,37,1,37,1,37,1,38,1,38,
        3,38,621,8,38,1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,
        1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,44,1,45,
        1,45,1,45,3,45,648,8,45,1,46,1,46,1,46,1,46,1,46,1,46,4,46,656,8,
        46,11,46,12,46,657,1,47,1,47,1,47,1,47,1,47,4,47,665,8,47,11,47,
        12,47,666,1,47,1,47,1,47,3,47,672,8,47,1,47,1,47,1,47,1,47,3,47,
        678,8,47,1,48,1,48,1,48,1,48,1,48,1,48,4,48,686,8,48,11,48,12,48,
        687,1,48,1,48,1,48,3,48,693,8,48,1,49,1,49,1,49,3,49,698,8,49,1,
        49,1,49,1,49,3,49,703,8,49,5,49,705,8,49,10,49,12,49,708,9,49,1,
        49,1,49,1,50,1,50,1,50,1,50,1,50,4,50,717,8,50,11,50,12,50,718,1,
        51,1,51,1,51,1,51,1,52,5,52,726,8,52,10,52,12,52,729,9,52,1,52,1,
        52,1,53,1,53,1,54,1,54,1,54,0,3,20,24,58,55,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,
        104,106,108,0,3,1,0,29,30,1,0,52,54,2,0,21,24,57,57,816,0,118,1,
        0,0,0,2,129,1,0,0,0,4,131,1,0,0,0,6,195,1,0,0,0,8,221,1,0,0,0,10,
        223,1,0,0,0,12,243,1,0,0,0,14,245,1,0,0,0,16,249,1,0,0,0,18,261,
        1,0,0,0,20,265,1,0,0,0,22,282,1,0,0,0,24,289,1,0,0,0,26,300,1,0,
        0,0,28,330,1,0,0,0,30,332,1,0,0,0,32,342,1,0,0,0,34,348,1,0,0,0,
        36,355,1,0,0,0,38,358,1,0,0,0,40,364,1,0,0,0,42,371,1,0,0,0,44,381,
        1,0,0,0,46,398,1,0,0,0,48,410,1,0,0,0,50,412,1,0,0,0,52,414,1,0,
        0,0,54,422,1,0,0,0,56,436,1,0,0,0,58,463,1,0,0,0,60,530,1,0,0,0,
        62,568,1,0,0,0,64,570,1,0,0,0,66,573,1,0,0,0,68,585,1,0,0,0,70,592,
        1,0,0,0,72,599,1,0,0,0,74,605,1,0,0,0,76,620,1,0,0,0,78,622,1,0,
        0,0,80,628,1,0,0,0,82,632,1,0,0,0,84,635,1,0,0,0,86,638,1,0,0,0,
        88,641,1,0,0,0,90,647,1,0,0,0,92,649,1,0,0,0,94,677,1,0,0,0,96,679,
        1,0,0,0,98,694,1,0,0,0,100,711,1,0,0,0,102,720,1,0,0,0,104,727,1,
        0,0,0,106,732,1,0,0,0,108,734,1,0,0,0,110,119,3,108,54,0,111,113,
        3,2,1,0,112,114,5,50,0,0,113,112,1,0,0,0,114,115,1,0,0,0,115,113,
        1,0,0,0,115,116,1,0,0,0,116,119,1,0,0,0,117,119,3,8,4,0,118,110,
        1,0,0,0,118,111,1,0,0,0,118,117,1,0,0,0,119,120,1,0,0,0,120,118,
        1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,5,0,0,1,123,1,1,
        0,0,0,124,130,3,74,37,0,125,130,3,10,5,0,126,130,3,54,27,0,127,130,
        3,102,51,0,128,130,3,90,45,0,129,124,1,0,0,0,129,125,1,0,0,0,129,
        126,1,0,0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,3,1,0,0,0,131,135,
        5,27,0,0,132,134,3,6,3,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,
        1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,139,
        5,28,0,0,139,5,1,0,0,0,140,142,3,58,29,0,141,143,5,50,0,0,142,141,
        1,0,0,0,143,144,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,196,
        1,0,0,0,146,148,3,54,27,0,147,149,5,50,0,0,148,147,1,0,0,0,149,150,
        1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,196,1,0,0,0,152,196,
        3,108,54,0,153,155,3,44,22,0,154,156,5,50,0,0,155,154,1,0,0,0,156,
        157,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,196,1,0,0,0,159,
        161,3,46,23,0,160,162,5,50,0,0,161,160,1,0,0,0,162,163,1,0,0,0,163,
        161,1,0,0,0,163,164,1,0,0,0,164,196,1,0,0,0,165,196,3,4,2,0,166,
        196,3,30,15,0,167,196,3,38,19,0,168,196,3,40,20,0,169,171,3,76,38,
        0,170,172,5,50,0,0,171,170,1,0,0,0,172,173,1,0,0,0,173,171,1,0,0,
        0,173,174,1,0,0,0,174,196,1,0,0,0,175,177,3,60,30,0,176,178,5,50,
        0,0,177,176,1,0,0,0,178,179,1,0,0,0,179,177,1,0,0,0,179,180,1,0,
        0,0,180,196,1,0,0,0,181,196,3,8,4,0,182,196,3,26,13,0,183,185,3,
        90,45,0,184,186,5,50,0,0,185,184,1,0,0,0,186,187,1,0,0,0,187,185,
        1,0,0,0,187,188,1,0,0,0,188,196,1,0,0,0,189,191,3,12,6,0,190,192,
        5,50,0,0,191,190,1,0,0,0,192,193,1,0,0,0,193,191,1,0,0,0,193,194,
        1,0,0,0,194,196,1,0,0,0,195,140,1,0,0,0,195,146,1,0,0,0,195,152,
        1,0,0,0,195,153,1,0,0,0,195,159,1,0,0,0,195,165,1,0,0,0,195,166,
        1,0,0,0,195,167,1,0,0,0,195,168,1,0,0,0,195,169,1,0,0,0,195,175,
        1,0,0,0,195,181,1,0,0,0,195,182,1,0,0,0,195,183,1,0,0,0,195,189,
        1,0,0,0,196,7,1,0,0,0,197,200,3,104,52,0,198,200,3,68,34,0,199,197,
        1,0,0,0,199,198,1,0,0,0,200,201,1,0,0,0,201,202,5,57,0,0,202,204,
        5,25,0,0,203,205,3,20,10,0,204,203,1,0,0,0,204,205,1,0,0,0,205,206,
        1,0,0,0,206,207,5,26,0,0,207,208,3,4,2,0,208,222,1,0,0,0,209,212,
        3,104,52,0,210,212,3,68,34,0,211,209,1,0,0,0,211,210,1,0,0,0,212,
        213,1,0,0,0,213,214,5,57,0,0,214,216,5,25,0,0,215,217,3,20,10,0,
        216,215,1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,218,219,5,26,0,0,
        219,220,5,50,0,0,220,222,1,0,0,0,221,199,1,0,0,0,221,211,1,0,0,0,
        222,9,1,0,0,0,223,224,5,1,0,0,224,225,5,57,0,0,225,236,5,27,0,0,
        226,227,3,104,52,0,227,228,3,106,53,0,228,231,1,0,0,0,229,231,3,
        92,46,0,230,226,1,0,0,0,230,229,1,0,0,0,231,232,1,0,0,0,232,233,
        5,50,0,0,233,235,1,0,0,0,234,230,1,0,0,0,235,238,1,0,0,0,236,234,
        1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,236,1,0,0,0,239,240,
        5,28,0,0,240,11,1,0,0,0,241,244,3,14,7,0,242,244,3,18,9,0,243,241,
        1,0,0,0,243,242,1,0,0,0,244,13,1,0,0,0,245,246,5,1,0,0,246,247,5,
        57,0,0,247,248,5,57,0,0,248,15,1,0,0,0,249,250,5,57,0,0,250,251,
        5,2,0,0,251,258,5,57,0,0,252,253,5,3,0,0,253,254,3,58,29,0,254,255,
        5,4,0,0,255,257,1,0,0,0,256,252,1,0,0,0,257,260,1,0,0,0,258,256,
        1,0,0,0,258,259,1,0,0,0,259,17,1,0,0,0,260,258,1,0,0,0,261,262,3,
        16,8,0,262,263,5,5,0,0,263,264,3,58,29,0,264,19,1,0,0,0,265,268,
        6,10,-1,0,266,269,3,68,34,0,267,269,3,104,52,0,268,266,1,0,0,0,268,
        267,1,0,0,0,269,272,1,0,0,0,270,273,3,72,36,0,271,273,3,106,53,0,
        272,270,1,0,0,0,272,271,1,0,0,0,273,279,1,0,0,0,274,275,10,1,0,0,
        275,276,5,51,0,0,276,278,3,20,10,2,277,274,1,0,0,0,278,281,1,0,0,
        0,279,277,1,0,0,0,279,280,1,0,0,0,280,21,1,0,0,0,281,279,1,0,0,0,
        282,283,5,57,0,0,283,285,5,25,0,0,284,286,3,24,12,0,285,284,1,0,
        0,0,285,286,1,0,0,0,286,287,1,0,0,0,287,288,5,26,0,0,288,23,1,0,
        0,0,289,290,6,12,-1,0,290,291,3,58,29,0,291,297,1,0,0,0,292,293,
        10,1,0,0,293,294,5,51,0,0,294,296,3,24,12,2,295,292,1,0,0,0,296,
        299,1,0,0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,25,1,0,0,0,299,297,
        1,0,0,0,300,301,5,6,0,0,301,302,5,25,0,0,302,303,3,58,29,0,303,304,
        5,26,0,0,304,308,5,27,0,0,305,307,3,28,14,0,306,305,1,0,0,0,307,
        310,1,0,0,0,308,306,1,0,0,0,308,309,1,0,0,0,309,311,1,0,0,0,310,
        308,1,0,0,0,311,312,5,28,0,0,312,27,1,0,0,0,313,314,5,7,0,0,314,
        315,3,64,32,0,315,319,5,49,0,0,316,318,3,6,3,0,317,316,1,0,0,0,318,
        321,1,0,0,0,319,317,1,0,0,0,319,320,1,0,0,0,320,331,1,0,0,0,321,
        319,1,0,0,0,322,323,5,8,0,0,323,327,5,49,0,0,324,326,3,6,3,0,325,
        324,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,
        331,1,0,0,0,329,327,1,0,0,0,330,313,1,0,0,0,330,322,1,0,0,0,331,
        29,1,0,0,0,332,336,3,32,16,0,333,335,3,34,17,0,334,333,1,0,0,0,335,
        338,1,0,0,0,336,334,1,0,0,0,336,337,1,0,0,0,337,340,1,0,0,0,338,
        336,1,0,0,0,339,341,3,36,18,0,340,339,1,0,0,0,340,341,1,0,0,0,341,
        31,1,0,0,0,342,343,5,9,0,0,343,344,5,25,0,0,344,345,3,58,29,0,345,
        346,5,26,0,0,346,347,3,4,2,0,347,33,1,0,0,0,348,349,5,10,0,0,349,
        350,5,9,0,0,350,351,5,25,0,0,351,352,3,58,29,0,352,353,5,26,0,0,
        353,354,3,4,2,0,354,35,1,0,0,0,355,356,5,10,0,0,356,357,3,4,2,0,
        357,37,1,0,0,0,358,359,5,11,0,0,359,360,5,25,0,0,360,361,3,58,29,
        0,361,362,5,26,0,0,362,363,3,4,2,0,363,39,1,0,0,0,364,365,5,12,0,
        0,365,366,5,25,0,0,366,367,3,42,21,0,367,368,5,26,0,0,368,369,3,
        4,2,0,369,41,1,0,0,0,370,372,3,54,27,0,371,370,1,0,0,0,371,372,1,
        0,0,0,372,373,1,0,0,0,373,375,5,50,0,0,374,376,3,58,29,0,375,374,
        1,0,0,0,375,376,1,0,0,0,376,377,1,0,0,0,377,379,5,50,0,0,378,380,
        3,58,29,0,379,378,1,0,0,0,379,380,1,0,0,0,380,43,1,0,0,0,381,382,
        5,13,0,0,382,383,5,25,0,0,383,393,3,48,24,0,384,389,5,51,0,0,385,
        390,3,50,25,0,386,390,3,52,26,0,387,390,3,58,29,0,388,390,3,16,8,
        0,389,385,1,0,0,0,389,386,1,0,0,0,389,387,1,0,0,0,389,388,1,0,0,
        0,390,392,1,0,0,0,391,384,1,0,0,0,392,395,1,0,0,0,393,391,1,0,0,
        0,393,394,1,0,0,0,394,396,1,0,0,0,395,393,1,0,0,0,396,397,5,26,0,
        0,397,45,1,0,0,0,398,399,5,14,0,0,399,400,5,25,0,0,400,405,3,48,
        24,0,401,402,5,51,0,0,402,404,3,72,36,0,403,401,1,0,0,0,404,407,
        1,0,0,0,405,403,1,0,0,0,405,406,1,0,0,0,406,408,1,0,0,0,407,405,
        1,0,0,0,408,409,5,26,0,0,409,47,1,0,0,0,410,411,5,55,0,0,411,49,
        1,0,0,0,412,413,5,54,0,0,413,51,1,0,0,0,414,415,5,55,0,0,415,53,
        1,0,0,0,416,417,3,56,28,0,417,418,5,5,0,0,418,419,3,58,29,0,419,
        423,1,0,0,0,420,423,3,56,28,0,421,423,3,102,51,0,422,416,1,0,0,0,
        422,420,1,0,0,0,422,421,1,0,0,0,423,55,1,0,0,0,424,437,3,106,53,
        0,425,426,3,104,52,0,426,427,3,106,53,0,427,437,1,0,0,0,428,429,
        3,68,34,0,429,430,3,106,53,0,430,437,1,0,0,0,431,437,3,70,35,0,432,
        433,5,25,0,0,433,434,3,56,28,0,434,435,5,26,0,0,435,437,1,0,0,0,
        436,424,1,0,0,0,436,425,1,0,0,0,436,428,1,0,0,0,436,431,1,0,0,0,
        436,432,1,0,0,0,437,57,1,0,0,0,438,439,6,29,-1,0,439,464,3,62,31,
        0,440,464,3,106,53,0,441,464,3,70,35,0,442,464,3,72,36,0,443,444,
        5,48,0,0,444,464,3,58,29,30,445,446,5,45,0,0,446,464,3,58,29,29,
        447,449,7,0,0,0,448,447,1,0,0,0,448,449,1,0,0,0,449,450,1,0,0,0,
        450,451,5,25,0,0,451,452,3,58,29,0,452,453,5,26,0,0,453,464,1,0,
        0,0,454,464,3,66,33,0,455,464,3,82,41,0,456,464,3,84,42,0,457,464,
        3,86,43,0,458,464,3,88,44,0,459,464,3,22,11,0,460,464,3,60,30,0,
        461,464,3,100,50,0,462,464,3,52,26,0,463,438,1,0,0,0,463,440,1,0,
        0,0,463,441,1,0,0,0,463,442,1,0,0,0,463,443,1,0,0,0,463,445,1,0,
        0,0,463,448,1,0,0,0,463,454,1,0,0,0,463,455,1,0,0,0,463,456,1,0,
        0,0,463,457,1,0,0,0,463,458,1,0,0,0,463,459,1,0,0,0,463,460,1,0,
        0,0,463,461,1,0,0,0,463,462,1,0,0,0,464,521,1,0,0,0,465,466,10,28,
        0,0,466,467,5,32,0,0,467,520,3,58,29,29,468,469,10,27,0,0,469,470,
        5,33,0,0,470,520,3,58,29,28,471,472,10,26,0,0,472,473,5,31,0,0,473,
        520,3,58,29,27,474,475,10,25,0,0,475,476,5,30,0,0,476,520,3,58,29,
        26,477,478,10,24,0,0,478,479,5,29,0,0,479,520,3,58,29,25,480,481,
        10,23,0,0,481,482,5,40,0,0,482,520,3,58,29,24,483,484,10,22,0,0,
        484,485,5,41,0,0,485,520,3,58,29,23,486,487,10,21,0,0,487,488,5,
        42,0,0,488,520,3,58,29,22,489,490,10,20,0,0,490,491,5,43,0,0,491,
        520,3,58,29,21,492,493,10,19,0,0,493,494,5,44,0,0,494,520,3,58,29,
        20,495,496,10,18,0,0,496,497,5,38,0,0,497,520,3,58,29,19,498,499,
        10,17,0,0,499,500,5,39,0,0,500,520,3,58,29,18,501,502,10,16,0,0,
        502,503,5,46,0,0,503,520,3,58,29,17,504,505,10,15,0,0,505,506,5,
        47,0,0,506,520,3,58,29,16,507,508,10,14,0,0,508,509,5,34,0,0,509,
        520,3,58,29,15,510,511,10,13,0,0,511,512,5,35,0,0,512,520,3,58,29,
        14,513,514,10,12,0,0,514,515,5,36,0,0,515,520,3,58,29,13,516,517,
        10,11,0,0,517,518,5,37,0,0,518,520,3,58,29,12,519,465,1,0,0,0,519,
        468,1,0,0,0,519,471,1,0,0,0,519,474,1,0,0,0,519,477,1,0,0,0,519,
        480,1,0,0,0,519,483,1,0,0,0,519,486,1,0,0,0,519,489,1,0,0,0,519,
        492,1,0,0,0,519,495,1,0,0,0,519,498,1,0,0,0,519,501,1,0,0,0,519,
        504,1,0,0,0,519,507,1,0,0,0,519,510,1,0,0,0,519,513,1,0,0,0,519,
        516,1,0,0,0,520,523,1,0,0,0,521,519,1,0,0,0,521,522,1,0,0,0,522,
        59,1,0,0,0,523,521,1,0,0,0,524,531,5,15,0,0,525,531,5,16,0,0,526,
        528,5,17,0,0,527,529,3,58,29,0,528,527,1,0,0,0,528,529,1,0,0,0,529,
        531,1,0,0,0,530,524,1,0,0,0,530,525,1,0,0,0,530,526,1,0,0,0,531,
        61,1,0,0,0,532,534,7,0,0,0,533,532,1,0,0,0,533,534,1,0,0,0,534,538,
        1,0,0,0,535,539,3,64,32,0,536,539,3,106,53,0,537,539,3,70,35,0,538,
        535,1,0,0,0,538,536,1,0,0,0,538,537,1,0,0,0,539,569,1,0,0,0,540,
        541,5,29,0,0,541,543,5,30,0,0,542,540,1,0,0,0,543,544,1,0,0,0,544,
        542,1,0,0,0,544,545,1,0,0,0,545,547,1,0,0,0,546,548,5,29,0,0,547,
        546,1,0,0,0,547,548,1,0,0,0,548,552,1,0,0,0,549,553,3,64,32,0,550,
        553,3,106,53,0,551,553,3,70,35,0,552,549,1,0,0,0,552,550,1,0,0,0,
        552,551,1,0,0,0,553,569,1,0,0,0,554,555,5,30,0,0,555,557,5,29,0,
        0,556,554,1,0,0,0,557,558,1,0,0,0,558,556,1,0,0,0,558,559,1,0,0,
        0,559,561,1,0,0,0,560,562,5,30,0,0,561,560,1,0,0,0,561,562,1,0,0,
        0,562,566,1,0,0,0,563,567,3,64,32,0,564,567,3,106,53,0,565,567,3,
        70,35,0,566,563,1,0,0,0,566,564,1,0,0,0,566,565,1,0,0,0,567,569,
        1,0,0,0,568,533,1,0,0,0,568,542,1,0,0,0,568,556,1,0,0,0,569,63,1,
        0,0,0,570,571,7,1,0,0,571,65,1,0,0,0,572,574,5,25,0,0,573,572,1,
        0,0,0,574,575,1,0,0,0,575,573,1,0,0,0,575,576,1,0,0,0,576,578,1,
        0,0,0,577,579,3,104,52,0,578,577,1,0,0,0,579,580,1,0,0,0,580,578,
        1,0,0,0,580,581,1,0,0,0,581,582,1,0,0,0,582,583,5,26,0,0,583,584,
        3,58,29,0,584,67,1,0,0,0,585,587,3,104,52,0,586,588,5,31,0,0,587,
        586,1,0,0,0,588,589,1,0,0,0,589,587,1,0,0,0,589,590,1,0,0,0,590,
        69,1,0,0,0,591,593,5,31,0,0,592,591,1,0,0,0,593,594,1,0,0,0,594,
        592,1,0,0,0,594,595,1,0,0,0,595,596,1,0,0,0,596,597,3,106,53,0,597,
        71,1,0,0,0,598,600,5,42,0,0,599,598,1,0,0,0,600,601,1,0,0,0,601,
        599,1,0,0,0,601,602,1,0,0,0,602,603,1,0,0,0,603,604,3,106,53,0,604,
        73,1,0,0,0,605,606,5,18,0,0,606,607,5,57,0,0,607,608,5,27,0,0,608,
        613,5,57,0,0,609,610,5,51,0,0,610,612,5,57,0,0,611,609,1,0,0,0,612,
        615,1,0,0,0,613,611,1,0,0,0,613,614,1,0,0,0,614,616,1,0,0,0,615,
        613,1,0,0,0,616,617,5,28,0,0,617,75,1,0,0,0,618,621,3,78,39,0,619,
        621,3,80,40,0,620,618,1,0,0,0,620,619,1,0,0,0,621,77,1,0,0,0,622,
        623,5,18,0,0,623,624,5,57,0,0,624,625,5,57,0,0,625,626,5,5,0,0,626,
        627,5,57,0,0,627,79,1,0,0,0,628,629,5,18,0,0,629,630,5,57,0,0,630,
        631,5,57,0,0,631,81,1,0,0,0,632,633,3,56,28,0,633,634,5,58,0,0,634,
        83,1,0,0,0,635,636,3,56,28,0,636,637,5,59,0,0,637,85,1,0,0,0,638,
        639,5,58,0,0,639,640,3,56,28,0,640,87,1,0,0,0,641,642,5,59,0,0,642,
        643,3,56,28,0,643,89,1,0,0,0,644,648,3,92,46,0,645,648,3,94,47,0,
        646,648,3,96,48,0,647,644,1,0,0,0,647,645,1,0,0,0,647,646,1,0,0,
        0,648,91,1,0,0,0,649,650,3,104,52,0,650,655,3,106,53,0,651,652,5,
        3,0,0,652,653,3,58,29,0,653,654,5,4,0,0,654,656,1,0,0,0,655,651,
        1,0,0,0,656,657,1,0,0,0,657,655,1,0,0,0,657,658,1,0,0,0,658,93,1,
        0,0,0,659,664,3,106,53,0,660,661,5,3,0,0,661,662,3,58,29,0,662,663,
        5,4,0,0,663,665,1,0,0,0,664,660,1,0,0,0,665,666,1,0,0,0,666,664,
        1,0,0,0,666,667,1,0,0,0,667,668,1,0,0,0,668,671,5,5,0,0,669,672,
        3,58,29,0,670,672,3,98,49,0,671,669,1,0,0,0,671,670,1,0,0,0,672,
        678,1,0,0,0,673,674,3,106,53,0,674,675,5,5,0,0,675,676,3,98,49,0,
        676,678,1,0,0,0,677,659,1,0,0,0,677,673,1,0,0,0,678,95,1,0,0,0,679,
        680,3,104,52,0,680,685,3,106,53,0,681,682,5,3,0,0,682,683,3,58,29,
        0,683,684,5,4,0,0,684,686,1,0,0,0,685,681,1,0,0,0,686,687,1,0,0,
        0,687,685,1,0,0,0,687,688,1,0,0,0,688,689,1,0,0,0,689,692,5,5,0,
        0,690,693,3,98,49,0,691,693,3,52,26,0,692,690,1,0,0,0,692,691,1,
        0,0,0,693,97,1,0,0,0,694,697,5,27,0,0,695,698,3,58,29,0,696,698,
        3,98,49,0,697,695,1,0,0,0,697,696,1,0,0,0,698,706,1,0,0,0,699,702,
        5,51,0,0,700,703,3,58,29,0,701,703,3,98,49,0,702,700,1,0,0,0,702,
        701,1,0,0,0,703,705,1,0,0,0,704,699,1,0,0,0,705,708,1,0,0,0,706,
        704,1,0,0,0,706,707,1,0,0,0,707,709,1,0,0,0,708,706,1,0,0,0,709,
        710,5,28,0,0,710,99,1,0,0,0,711,716,3,106,53,0,712,713,5,3,0,0,713,
        714,3,58,29,0,714,715,5,4,0,0,715,717,1,0,0,0,716,712,1,0,0,0,717,
        718,1,0,0,0,718,716,1,0,0,0,718,719,1,0,0,0,719,101,1,0,0,0,720,
        721,5,19,0,0,721,722,3,104,52,0,722,723,5,57,0,0,723,103,1,0,0,0,
        724,726,5,20,0,0,725,724,1,0,0,0,726,729,1,0,0,0,727,725,1,0,0,0,
        727,728,1,0,0,0,728,730,1,0,0,0,729,727,1,0,0,0,730,731,7,2,0,0,
        731,105,1,0,0,0,732,733,5,57,0,0,733,107,1,0,0,0,734,735,5,60,0,
        0,735,109,1,0,0,0,76,115,118,120,129,135,144,150,157,163,173,179,
        187,193,195,199,204,211,216,221,230,236,243,258,268,272,279,285,
        297,308,319,327,330,336,340,371,375,379,389,393,405,422,436,448,
        463,519,521,528,530,533,538,544,547,552,558,561,566,568,575,580,
        589,594,601,613,620,647,657,666,671,677,687,692,697,702,706,718,
        727
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
    RULE_char = 25
    RULE_string = 26
    RULE_variable = 27
    RULE_lvalue = 28
    RULE_rvalue = 29
    RULE_jumpStatement = 30
    RULE_unaryExpression = 31
    RULE_literal = 32
    RULE_explicitConversion = 33
    RULE_pointer = 34
    RULE_deref = 35
    RULE_addr = 36
    RULE_enumDeclaration = 37
    RULE_enumStatement = 38
    RULE_enumVariableDefinition = 39
    RULE_enumVariableDeclaration = 40
    RULE_postFixIncrement = 41
    RULE_postFixDecrement = 42
    RULE_preFixIncrement = 43
    RULE_preFixDecrement = 44
    RULE_arrayStatement = 45
    RULE_arrayDeclaration = 46
    RULE_arrayAssignment = 47
    RULE_arrayDefinition = 48
    RULE_array = 49
    RULE_arrayElement = 50
    RULE_typedef = 51
    RULE_type = 52
    RULE_identifier = 53
    RULE_comment = 54

    ruleNames =  [ "program", "declaration", "scope", "statement", "function", 
                   "structDefinition", "structStatement", "structVariable", 
                   "structMember", "structAssignment", "functionParams", 
                   "functionCall", "callParams", "switchStatement", "switchCase", 
                   "conditional", "ifStatement", "elseIfStatement", "elseStatement", 
                   "whileLoop", "forLoop", "forCondition", "printfStatement", 
                   "scanfStatement", "formatSpecifier", "char", "string", 
                   "variable", "lvalue", "rvalue", "jumpStatement", "unaryExpression", 
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
            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 118
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 110
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 111
                    self.declaration()
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

                elif la_ == 3:
                    self.state = 117
                    self.function()
                    pass


                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1297036694897033218) != 0)):
                    break

            self.state = 122
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


        def arrayStatement(self):
            return self.getTypedRuleContext(GrammarParser.ArrayStatementContext,0)


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
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.enumDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.structDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.variable()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.typedef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.arrayStatement()
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
            self.state = 131
            self.match(GrammarParser.LBRACE)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                self.state = 132
                self.statement()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
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
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.rvalue(0)
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

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.variable()
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

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.printfStatement()
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 154
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 157 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.scanfStatement()
                self.state = 161 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 160
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 163 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                self.scope()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 166
                self.conditional()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 167
                self.whileLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 168
                self.forLoop()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 169
                self.enumStatement()
                self.state = 171 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 170
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 173 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 175
                self.jumpStatement()
                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 176
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 179 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 181
                self.function()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 182
                self.switchStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 183
                self.arrayStatement()
                self.state = 185 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 184
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 187 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 189
                self.structStatement()
                self.state = 191 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 190
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 193 
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
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 197
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 198
                    self.pointer()
                    pass


                self.state = 201
                self.match(GrammarParser.IDENTIFIER)
                self.state = 202
                self.match(GrammarParser.LPAREN)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                    self.state = 203
                    self.functionParams(0)


                self.state = 206
                self.match(GrammarParser.RPAREN)
                self.state = 207
                self.scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 209
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 210
                    self.pointer()
                    pass


                self.state = 213
                self.match(GrammarParser.IDENTIFIER)
                self.state = 214
                self.match(GrammarParser.LPAREN)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                    self.state = 215
                    self.functionParams(0)


                self.state = 218
                self.match(GrammarParser.RPAREN)
                self.state = 219
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
            self.state = 223
            self.match(GrammarParser.T__0)
            self.state = 224
            self.match(GrammarParser.IDENTIFIER)
            self.state = 225
            self.match(GrammarParser.LBRACE)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                self.state = 230
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 226
                    self.type_()
                    self.state = 227
                    self.identifier()
                    pass

                elif la_ == 2:
                    self.state = 229
                    self.arrayDeclaration()
                    pass


                self.state = 232
                self.match(GrammarParser.SEMICOLON)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
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
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.structVariable()
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
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
            self.state = 245
            self.match(GrammarParser.T__0)
            self.state = 246
            self.match(GrammarParser.IDENTIFIER)
            self.state = 247
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

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


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
            self.state = 249
            self.match(GrammarParser.IDENTIFIER)
            self.state = 250
            self.match(GrammarParser.T__1)
            self.state = 251
            self.match(GrammarParser.IDENTIFIER)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 252
                self.match(GrammarParser.T__2)
                self.state = 253
                self.rvalue(0)
                self.state = 254
                self.match(GrammarParser.T__3)
                self.state = 260
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
            self.state = 261
            self.structMember()
            self.state = 262
            self.match(GrammarParser.T__4)
            self.state = 263
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
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 266
                self.pointer()
                pass

            elif la_ == 2:
                self.state = 267
                self.type_()
                pass


            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 270
                self.addr()
                pass
            elif token in [57]:
                self.state = 271
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.FunctionParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParams)
                    self.state = 274
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 275
                    self.match(GrammarParser.COMMA)
                    self.state = 276
                    self.functionParams(2) 
                self.state = 281
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
            self.state = 282
            self.match(GrammarParser.IDENTIFIER)
            self.state = 283
            self.match(GrammarParser.LPAREN)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 284
                self.callParams(0)


            self.state = 287
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
            self.state = 290
            self.rvalue(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CallParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callParams)
                    self.state = 292
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 293
                    self.match(GrammarParser.COMMA)
                    self.state = 294
                    self.callParams(2) 
                self.state = 299
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
            self.state = 300
            self.match(GrammarParser.T__5)
            self.state = 301
            self.match(GrammarParser.LPAREN)
            self.state = 302
            self.rvalue(0)
            self.state = 303
            self.match(GrammarParser.RPAREN)
            self.state = 304
            self.match(GrammarParser.LBRACE)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 305
                self.switchCase()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 311
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
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(GrammarParser.T__6)
                self.state = 314
                self.literal()
                self.state = 315
                self.match(GrammarParser.COLON)
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                    self.state = 316
                    self.statement()
                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(GrammarParser.T__7)
                self.state = 323
                self.match(GrammarParser.COLON)
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                    self.state = 324
                    self.statement()
                    self.state = 329
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
            self.state = 332
            self.ifStatement()
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 333
                    self.elseIfStatement() 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 339
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
            self.state = 342
            self.match(GrammarParser.T__8)
            self.state = 343
            self.match(GrammarParser.LPAREN)
            self.state = 344
            self.rvalue(0)
            self.state = 345
            self.match(GrammarParser.RPAREN)
            self.state = 346
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
            self.state = 348
            self.match(GrammarParser.T__9)
            self.state = 349
            self.match(GrammarParser.T__8)
            self.state = 350
            self.match(GrammarParser.LPAREN)
            self.state = 351
            self.rvalue(0)
            self.state = 352
            self.match(GrammarParser.RPAREN)
            self.state = 353
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
            self.state = 355
            self.match(GrammarParser.T__9)
            self.state = 356
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
            self.state = 358
            self.match(GrammarParser.T__10)
            self.state = 359
            self.match(GrammarParser.LPAREN)
            self.state = 360
            self.rvalue(0)
            self.state = 361
            self.match(GrammarParser.RPAREN)
            self.state = 362
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
            self.state = 364
            self.match(GrammarParser.T__11)
            self.state = 365
            self.match(GrammarParser.LPAREN)
            self.state = 366
            self.forCondition()
            self.state = 367
            self.match(GrammarParser.RPAREN)
            self.state = 368
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
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115190289924096) != 0):
                self.state = 370
                self.variable()


            self.state = 373
            self.match(GrammarParser.SEMICOLON)
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 374
                self.rvalue(0)


            self.state = 377
            self.match(GrammarParser.SEMICOLON)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 378
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

        def char(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.CharContext)
            else:
                return self.getTypedRuleContext(GrammarParser.CharContext,i)


        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StringContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StringContext,i)


        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


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
            self.state = 381
            self.match(GrammarParser.T__12)
            self.state = 382
            self.match(GrammarParser.LPAREN)
            self.state = 383
            self.formatSpecifier()
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 384
                self.match(GrammarParser.COMMA)
                self.state = 389
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 385
                    self.char()
                    pass

                elif la_ == 2:
                    self.state = 386
                    self.string()
                    pass

                elif la_ == 3:
                    self.state = 387
                    self.rvalue(0)
                    pass

                elif la_ == 4:
                    self.state = 388
                    self.structMember()
                    pass


                self.state = 395
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 396
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
            self.state = 398
            self.match(GrammarParser.T__13)
            self.state = 399
            self.match(GrammarParser.LPAREN)
            self.state = 400
            self.formatSpecifier()
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 401
                self.match(GrammarParser.COMMA)
                self.state = 402
                self.addr()
                self.state = 407
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 408
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
            self.state = 410
            self.match(GrammarParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(GrammarParser.CHAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar" ):
                return visitor.visitChar(self)
            else:
                return visitor.visitChildren(self)




    def char(self):

        localctx = GrammarParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(GrammarParser.CHAR)
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
        self.enterRule(localctx, 52, self.RULE_string)
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
        self.enterRule(localctx, 54, self.RULE_variable)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
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
        self.enterRule(localctx, 56, self.RULE_lvalue)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
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

        def PLUS(self):
            return self.getToken(GrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GrammarParser.MINUS, 0)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_rvalue, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
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
                self.state = 448
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29 or _la==30:
                    self.state = 447
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 450
                self.match(GrammarParser.LPAREN)
                self.state = 451
                self.rvalue(0)
                self.state = 452
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 454
                self.explicitConversion()
                pass

            elif la_ == 9:
                self.state = 455
                self.postFixIncrement()
                pass

            elif la_ == 10:
                self.state = 456
                self.postFixDecrement()
                pass

            elif la_ == 11:
                self.state = 457
                self.preFixIncrement()
                pass

            elif la_ == 12:
                self.state = 458
                self.preFixDecrement()
                pass

            elif la_ == 13:
                self.state = 459
                self.functionCall()
                pass

            elif la_ == 14:
                self.state = 460
                self.jumpStatement()
                pass

            elif la_ == 15:
                self.state = 461
                self.arrayElement()
                pass

            elif la_ == 16:
                self.state = 462
                self.string()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 521
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 519
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 465
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 466
                        self.match(GrammarParser.DIV)
                        self.state = 467
                        self.rvalue(29)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 468
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 469
                        self.match(GrammarParser.MOD)
                        self.state = 470
                        self.rvalue(28)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 471
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 472
                        self.match(GrammarParser.MULT)
                        self.state = 473
                        self.rvalue(27)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 474
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 475
                        self.match(GrammarParser.MINUS)
                        self.state = 476
                        self.rvalue(26)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 477
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 478
                        self.match(GrammarParser.PLUS)
                        self.state = 479
                        self.rvalue(25)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 480
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 481
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 482
                        self.rvalue(24)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 483
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 484
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 485
                        self.rvalue(23)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 486
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 487
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 488
                        self.rvalue(22)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 489
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 490
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 491
                        self.rvalue(21)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 492
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 493
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 494
                        self.rvalue(20)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 495
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 496
                        self.match(GrammarParser.EQUALS)
                        self.state = 497
                        self.rvalue(19)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 498
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 499
                        self.match(GrammarParser.NOT_EQUAL)
                        self.state = 500
                        self.rvalue(18)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 501
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 502
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 503
                        self.rvalue(17)
                        pass

                    elif la_ == 14:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 504
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 505
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 506
                        self.rvalue(16)
                        pass

                    elif la_ == 15:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 507
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 508
                        self.match(GrammarParser.GREATER_THAN)
                        self.state = 509
                        self.rvalue(15)
                        pass

                    elif la_ == 16:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 510
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 511
                        self.match(GrammarParser.LESS_THAN)
                        self.state = 512
                        self.rvalue(14)
                        pass

                    elif la_ == 17:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 513
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 514
                        self.match(GrammarParser.GREATER_EQUAL)
                        self.state = 515
                        self.rvalue(13)
                        pass

                    elif la_ == 18:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 516
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 517
                        self.match(GrammarParser.LESS_EQUAL)
                        self.state = 518
                        self.rvalue(12)
                        pass

             
                self.state = 523
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_jumpStatement)
        try:
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.match(GrammarParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.match(GrammarParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 526
                self.match(GrammarParser.T__16)
                self.state = 528
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 527
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
        self.enterRule(localctx, 62, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 568
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29 or _la==30:
                    self.state = 532
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 538
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 535
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 536
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 537
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 542 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 540
                        self.match(GrammarParser.PLUS)
                        self.state = 541
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 544 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

                self.state = 547
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 546
                    self.match(GrammarParser.PLUS)


                self.state = 552
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 549
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 550
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 551
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 556 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 554
                        self.match(GrammarParser.MINUS)
                        self.state = 555
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 558 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

                self.state = 561
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 560
                    self.match(GrammarParser.MINUS)


                self.state = 566
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 563
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 564
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 565
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
        self.enterRule(localctx, 64, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
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
        self.enterRule(localctx, 66, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 572
                self.match(GrammarParser.LPAREN)
                self.state = 575 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 578 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 577
                self.type_()
                self.state = 580 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0)):
                    break

            self.state = 582
            self.match(GrammarParser.RPAREN)
            self.state = 583
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
        self.enterRule(localctx, 68, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.type_()
            self.state = 587 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 586
                self.match(GrammarParser.MULT)
                self.state = 589 
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
        self.enterRule(localctx, 70, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 591
                self.match(GrammarParser.MULT)
                self.state = 594 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 596
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
        self.enterRule(localctx, 72, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 598
                self.match(GrammarParser.BITWISE_AND)
                self.state = 601 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 603
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
        self.enterRule(localctx, 74, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(GrammarParser.T__17)
            self.state = 606
            self.match(GrammarParser.IDENTIFIER)
            self.state = 607
            self.match(GrammarParser.LBRACE)
            self.state = 608
            self.match(GrammarParser.IDENTIFIER)
            self.state = 613
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 609
                self.match(GrammarParser.COMMA)
                self.state = 610
                self.match(GrammarParser.IDENTIFIER)
                self.state = 615
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 616
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
        self.enterRule(localctx, 76, self.RULE_enumStatement)
        try:
            self.state = 620
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                self.enumVariableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 619
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
        self.enterRule(localctx, 78, self.RULE_enumVariableDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.match(GrammarParser.T__17)
            self.state = 623
            self.match(GrammarParser.IDENTIFIER)
            self.state = 624
            self.match(GrammarParser.IDENTIFIER)
            self.state = 625
            self.match(GrammarParser.T__4)
            self.state = 626
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
        self.enterRule(localctx, 80, self.RULE_enumVariableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self.match(GrammarParser.T__17)
            self.state = 629
            self.match(GrammarParser.IDENTIFIER)
            self.state = 630
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
        self.enterRule(localctx, 82, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.lvalue()
            self.state = 633
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
        self.enterRule(localctx, 84, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.lvalue()
            self.state = 636
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
        self.enterRule(localctx, 86, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(GrammarParser.INCREMENT)
            self.state = 639
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
        self.enterRule(localctx, 88, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(GrammarParser.DECREMENT)
            self.state = 642
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
        self.enterRule(localctx, 90, self.RULE_arrayStatement)
        try:
            self.state = 647
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 644
                self.arrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 645
                self.arrayAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 646
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


        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


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
        self.enterRule(localctx, 92, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.type_()
            self.state = 650
            self.identifier()
            self.state = 655 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 651
                self.match(GrammarParser.T__2)
                self.state = 652
                self.rvalue(0)
                self.state = 653
                self.match(GrammarParser.T__3)
                self.state = 657 
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


        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


        def array(self):
            return self.getTypedRuleContext(GrammarParser.ArrayContext,0)


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
        self.enterRule(localctx, 94, self.RULE_arrayAssignment)
        self._la = 0 # Token type
        try:
            self.state = 677
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 659
                self.identifier()
                self.state = 664 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 660
                    self.match(GrammarParser.T__2)
                    self.state = 661
                    self.rvalue(0)
                    self.state = 662
                    self.match(GrammarParser.T__3)
                    self.state = 666 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                self.state = 668
                self.match(GrammarParser.T__4)
                self.state = 671
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                    self.state = 669
                    self.rvalue(0)
                    pass
                elif token in [27]:
                    self.state = 670
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 673
                self.identifier()
                self.state = 674
                self.match(GrammarParser.T__4)
                self.state = 675
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


        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RvalueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RvalueContext,i)


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
        self.enterRule(localctx, 96, self.RULE_arrayDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            self.type_()
            self.state = 680
            self.identifier()
            self.state = 685 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 681
                self.match(GrammarParser.T__2)
                self.state = 682
                self.rvalue(0)
                self.state = 683
                self.match(GrammarParser.T__3)
                self.state = 687 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 689
            self.match(GrammarParser.T__4)
            self.state = 692
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 690
                self.array()
                pass
            elif token in [55]:
                self.state = 691
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
        self.enterRule(localctx, 98, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 694
            self.match(GrammarParser.LBRACE)
            self.state = 697
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                self.state = 695
                self.rvalue(0)
                pass
            elif token in [27]:
                self.state = 696
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 706
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 699
                self.match(GrammarParser.COMMA)
                self.state = 702
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                    self.state = 700
                    self.rvalue(0)
                    pass
                elif token in [27]:
                    self.state = 701
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 708
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 709
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
        self.enterRule(localctx, 100, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 711
            self.identifier()
            self.state = 716 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 712
                    self.match(GrammarParser.T__2)
                    self.state = 713
                    self.rvalue(0)
                    self.state = 714
                    self.match(GrammarParser.T__3)

                else:
                    raise NoViableAltException(self)
                self.state = 718 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

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
        self.enterRule(localctx, 102, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            self.match(GrammarParser.T__18)
            self.state = 721
            self.type_()
            self.state = 722
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
        self.enterRule(localctx, 104, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 724
                self.match(GrammarParser.T__19)
                self.state = 729
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 730
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
        self.enterRule(localctx, 106, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
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
        self.enterRule(localctx, 108, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
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
        self._predicates[29] = self.rvalue_sempred
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
         




