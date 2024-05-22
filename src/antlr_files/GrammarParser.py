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
        4,1,62,765,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,1,0,1,0,1,0,4,0,116,8,0,11,0,12,0,
        117,1,0,4,0,121,8,0,11,0,12,0,122,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,133,8,1,1,2,1,2,5,2,137,8,2,10,2,12,2,140,9,2,1,2,1,2,1,3,
        1,3,4,3,146,8,3,11,3,12,3,147,1,3,1,3,4,3,152,8,3,11,3,12,3,153,
        1,3,1,3,1,3,4,3,159,8,3,11,3,12,3,160,1,3,1,3,4,3,165,8,3,11,3,12,
        3,166,1,3,1,3,1,3,1,3,1,3,1,3,4,3,175,8,3,11,3,12,3,176,1,3,1,3,
        4,3,181,8,3,11,3,12,3,182,1,3,1,3,1,3,1,3,4,3,189,8,3,11,3,12,3,
        190,1,3,1,3,4,3,195,8,3,11,3,12,3,196,3,3,199,8,3,1,4,1,4,3,4,203,
        8,4,1,4,1,4,1,4,3,4,208,8,4,1,4,1,4,1,4,1,4,1,4,3,4,215,8,4,1,4,
        1,4,1,4,3,4,220,8,4,1,4,1,4,1,4,3,4,225,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,234,8,5,1,5,1,5,5,5,238,8,5,10,5,12,5,241,9,5,1,5,1,
        5,1,6,1,6,1,6,3,6,248,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,3,8,261,8,8,1,8,1,8,1,8,3,8,266,8,8,5,8,268,8,8,10,8,12,8,
        271,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,282,8,9,10,9,12,
        9,285,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,3,11,294,8,11,1,11,
        1,11,3,11,298,8,11,1,11,1,11,1,11,5,11,303,8,11,10,11,12,11,306,
        9,11,1,12,1,12,1,12,3,12,311,8,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,321,8,13,10,13,12,13,324,9,13,1,14,1,14,1,14,1,14,
        1,14,1,14,5,14,332,8,14,10,14,12,14,335,9,14,1,14,1,14,1,15,1,15,
        1,15,1,15,5,15,343,8,15,10,15,12,15,346,9,15,1,15,1,15,1,15,5,15,
        351,8,15,10,15,12,15,354,9,15,3,15,356,8,15,1,16,1,16,5,16,360,8,
        16,10,16,12,16,363,9,16,1,16,3,16,366,8,16,1,17,1,17,1,17,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,
        20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,3,22,397,
        8,22,1,22,1,22,3,22,401,8,22,1,22,1,22,3,22,405,8,22,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,3,23,415,8,23,5,23,417,8,23,10,23,12,
        23,420,9,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,5,24,429,8,24,10,
        24,12,24,432,9,24,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,
        28,1,28,1,28,1,28,1,28,3,28,448,8,28,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,463,8,29,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,475,8,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,491,
        8,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,5,30,547,8,30,10,30,12,30,550,9,30,1,31,1,31,1,31,
        1,31,3,31,556,8,31,3,31,558,8,31,1,32,3,32,561,8,32,1,32,1,32,1,
        32,3,32,566,8,32,1,32,1,32,4,32,570,8,32,11,32,12,32,571,1,32,3,
        32,575,8,32,1,32,1,32,1,32,3,32,580,8,32,1,32,1,32,4,32,584,8,32,
        11,32,12,32,585,1,32,3,32,589,8,32,1,32,1,32,1,32,3,32,594,8,32,
        3,32,596,8,32,1,33,1,33,1,34,4,34,601,8,34,11,34,12,34,602,1,34,
        4,34,606,8,34,11,34,12,34,607,1,34,1,34,1,34,1,35,1,35,4,35,615,
        8,35,11,35,12,35,616,1,36,4,36,620,8,36,11,36,12,36,621,1,36,1,36,
        1,37,4,37,627,8,37,11,37,12,37,628,1,37,1,37,3,37,633,8,37,1,38,
        1,38,1,38,1,38,1,38,1,38,5,38,641,8,38,10,38,12,38,644,9,38,1,38,
        1,38,1,39,1,39,3,39,650,8,39,1,40,1,40,1,40,1,40,1,40,1,40,1,41,
        1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,44,1,45,
        1,45,1,45,1,46,1,46,3,46,676,8,46,1,47,1,47,1,47,1,47,1,47,1,47,
        4,47,684,8,47,11,47,12,47,685,1,48,1,48,1,48,1,48,1,48,4,48,693,
        8,48,11,48,12,48,694,1,48,1,48,1,48,3,48,700,8,48,1,48,1,48,1,48,
        1,48,3,48,706,8,48,1,49,1,49,1,49,1,49,1,49,1,49,4,49,714,8,49,11,
        49,12,49,715,1,49,1,49,1,49,3,49,721,8,49,1,50,1,50,1,50,3,50,726,
        8,50,1,50,1,50,1,50,3,50,731,8,50,5,50,733,8,50,10,50,12,50,736,
        9,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,4,51,745,8,51,11,51,12,51,
        746,1,52,1,52,1,52,1,52,1,53,5,53,754,8,53,10,53,12,53,757,9,53,
        1,53,1,53,1,54,1,54,1,55,1,55,1,55,0,3,22,26,60,56,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,
        100,102,104,106,108,110,0,3,1,0,29,30,1,0,52,54,2,0,21,24,57,57,
        850,0,120,1,0,0,0,2,132,1,0,0,0,4,134,1,0,0,0,6,198,1,0,0,0,8,224,
        1,0,0,0,10,226,1,0,0,0,12,247,1,0,0,0,14,249,1,0,0,0,16,253,1,0,
        0,0,18,274,1,0,0,0,20,286,1,0,0,0,22,290,1,0,0,0,24,307,1,0,0,0,
        26,314,1,0,0,0,28,325,1,0,0,0,30,355,1,0,0,0,32,357,1,0,0,0,34,367,
        1,0,0,0,36,373,1,0,0,0,38,380,1,0,0,0,40,383,1,0,0,0,42,389,1,0,
        0,0,44,396,1,0,0,0,46,406,1,0,0,0,48,423,1,0,0,0,50,435,1,0,0,0,
        52,437,1,0,0,0,54,439,1,0,0,0,56,447,1,0,0,0,58,462,1,0,0,0,60,490,
        1,0,0,0,62,557,1,0,0,0,64,595,1,0,0,0,66,597,1,0,0,0,68,600,1,0,
        0,0,70,612,1,0,0,0,72,619,1,0,0,0,74,626,1,0,0,0,76,634,1,0,0,0,
        78,649,1,0,0,0,80,651,1,0,0,0,82,657,1,0,0,0,84,661,1,0,0,0,86,664,
        1,0,0,0,88,667,1,0,0,0,90,670,1,0,0,0,92,675,1,0,0,0,94,677,1,0,
        0,0,96,705,1,0,0,0,98,707,1,0,0,0,100,722,1,0,0,0,102,739,1,0,0,
        0,104,748,1,0,0,0,106,755,1,0,0,0,108,760,1,0,0,0,110,762,1,0,0,
        0,112,121,3,110,55,0,113,115,3,2,1,0,114,116,5,50,0,0,115,114,1,
        0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,121,1,
        0,0,0,119,121,3,8,4,0,120,112,1,0,0,0,120,113,1,0,0,0,120,119,1,
        0,0,0,121,122,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,124,1,
        0,0,0,124,125,5,0,0,1,125,1,1,0,0,0,126,133,3,76,38,0,127,133,3,
        10,5,0,128,133,3,56,28,0,129,133,3,104,52,0,130,133,3,92,46,0,131,
        133,3,78,39,0,132,126,1,0,0,0,132,127,1,0,0,0,132,128,1,0,0,0,132,
        129,1,0,0,0,132,130,1,0,0,0,132,131,1,0,0,0,133,3,1,0,0,0,134,138,
        5,27,0,0,135,137,3,6,3,0,136,135,1,0,0,0,137,140,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,142,
        5,28,0,0,142,5,1,0,0,0,143,145,3,60,30,0,144,146,5,50,0,0,145,144,
        1,0,0,0,146,147,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,199,
        1,0,0,0,149,151,3,56,28,0,150,152,5,50,0,0,151,150,1,0,0,0,152,153,
        1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,199,1,0,0,0,155,199,
        3,110,55,0,156,158,3,46,23,0,157,159,5,50,0,0,158,157,1,0,0,0,159,
        160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,199,1,0,0,0,162,
        164,3,48,24,0,163,165,5,50,0,0,164,163,1,0,0,0,165,166,1,0,0,0,166,
        164,1,0,0,0,166,167,1,0,0,0,167,199,1,0,0,0,168,199,3,4,2,0,169,
        199,3,32,16,0,170,199,3,40,20,0,171,199,3,42,21,0,172,174,3,78,39,
        0,173,175,5,50,0,0,174,173,1,0,0,0,175,176,1,0,0,0,176,174,1,0,0,
        0,176,177,1,0,0,0,177,199,1,0,0,0,178,180,3,62,31,0,179,181,5,50,
        0,0,180,179,1,0,0,0,181,182,1,0,0,0,182,180,1,0,0,0,182,183,1,0,
        0,0,183,199,1,0,0,0,184,199,3,8,4,0,185,199,3,28,14,0,186,188,3,
        92,46,0,187,189,5,50,0,0,188,187,1,0,0,0,189,190,1,0,0,0,190,188,
        1,0,0,0,190,191,1,0,0,0,191,199,1,0,0,0,192,194,3,12,6,0,193,195,
        5,50,0,0,194,193,1,0,0,0,195,196,1,0,0,0,196,194,1,0,0,0,196,197,
        1,0,0,0,197,199,1,0,0,0,198,143,1,0,0,0,198,149,1,0,0,0,198,155,
        1,0,0,0,198,156,1,0,0,0,198,162,1,0,0,0,198,168,1,0,0,0,198,169,
        1,0,0,0,198,170,1,0,0,0,198,171,1,0,0,0,198,172,1,0,0,0,198,178,
        1,0,0,0,198,184,1,0,0,0,198,185,1,0,0,0,198,186,1,0,0,0,198,192,
        1,0,0,0,199,7,1,0,0,0,200,203,3,106,53,0,201,203,3,70,35,0,202,200,
        1,0,0,0,202,201,1,0,0,0,203,204,1,0,0,0,204,205,5,57,0,0,205,207,
        5,25,0,0,206,208,3,22,11,0,207,206,1,0,0,0,207,208,1,0,0,0,208,209,
        1,0,0,0,209,210,5,26,0,0,210,211,3,4,2,0,211,225,1,0,0,0,212,215,
        3,106,53,0,213,215,3,70,35,0,214,212,1,0,0,0,214,213,1,0,0,0,215,
        216,1,0,0,0,216,217,5,57,0,0,217,219,5,25,0,0,218,220,3,22,11,0,
        219,218,1,0,0,0,219,220,1,0,0,0,220,221,1,0,0,0,221,222,5,26,0,0,
        222,223,5,50,0,0,223,225,1,0,0,0,224,202,1,0,0,0,224,214,1,0,0,0,
        225,9,1,0,0,0,226,227,5,1,0,0,227,228,5,57,0,0,228,239,5,27,0,0,
        229,230,3,106,53,0,230,231,3,108,54,0,231,234,1,0,0,0,232,234,3,
        94,47,0,233,229,1,0,0,0,233,232,1,0,0,0,234,235,1,0,0,0,235,236,
        5,50,0,0,236,238,1,0,0,0,237,233,1,0,0,0,238,241,1,0,0,0,239,237,
        1,0,0,0,239,240,1,0,0,0,240,242,1,0,0,0,241,239,1,0,0,0,242,243,
        5,28,0,0,243,11,1,0,0,0,244,248,3,14,7,0,245,248,3,16,8,0,246,248,
        3,20,10,0,247,244,1,0,0,0,247,245,1,0,0,0,247,246,1,0,0,0,248,13,
        1,0,0,0,249,250,5,1,0,0,250,251,5,57,0,0,251,252,5,57,0,0,252,15,
        1,0,0,0,253,254,5,1,0,0,254,255,5,57,0,0,255,256,5,57,0,0,256,257,
        5,2,0,0,257,260,5,27,0,0,258,261,3,60,30,0,259,261,3,18,9,0,260,
        258,1,0,0,0,260,259,1,0,0,0,261,269,1,0,0,0,262,265,5,51,0,0,263,
        266,3,60,30,0,264,266,3,18,9,0,265,263,1,0,0,0,265,264,1,0,0,0,266,
        268,1,0,0,0,267,262,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,
        270,1,0,0,0,270,272,1,0,0,0,271,269,1,0,0,0,272,273,5,28,0,0,273,
        17,1,0,0,0,274,275,5,57,0,0,275,276,5,3,0,0,276,283,5,57,0,0,277,
        278,5,4,0,0,278,279,3,60,30,0,279,280,5,5,0,0,280,282,1,0,0,0,281,
        277,1,0,0,0,282,285,1,0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,
        19,1,0,0,0,285,283,1,0,0,0,286,287,3,18,9,0,287,288,5,2,0,0,288,
        289,3,60,30,0,289,21,1,0,0,0,290,293,6,11,-1,0,291,294,3,70,35,0,
        292,294,3,106,53,0,293,291,1,0,0,0,293,292,1,0,0,0,294,297,1,0,0,
        0,295,298,3,74,37,0,296,298,3,108,54,0,297,295,1,0,0,0,297,296,1,
        0,0,0,298,304,1,0,0,0,299,300,10,1,0,0,300,301,5,51,0,0,301,303,
        3,22,11,2,302,299,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,
        1,0,0,0,305,23,1,0,0,0,306,304,1,0,0,0,307,308,5,57,0,0,308,310,
        5,25,0,0,309,311,3,26,13,0,310,309,1,0,0,0,310,311,1,0,0,0,311,312,
        1,0,0,0,312,313,5,26,0,0,313,25,1,0,0,0,314,315,6,13,-1,0,315,316,
        3,60,30,0,316,322,1,0,0,0,317,318,10,1,0,0,318,319,5,51,0,0,319,
        321,3,26,13,2,320,317,1,0,0,0,321,324,1,0,0,0,322,320,1,0,0,0,322,
        323,1,0,0,0,323,27,1,0,0,0,324,322,1,0,0,0,325,326,5,6,0,0,326,327,
        5,25,0,0,327,328,3,60,30,0,328,329,5,26,0,0,329,333,5,27,0,0,330,
        332,3,30,15,0,331,330,1,0,0,0,332,335,1,0,0,0,333,331,1,0,0,0,333,
        334,1,0,0,0,334,336,1,0,0,0,335,333,1,0,0,0,336,337,5,28,0,0,337,
        29,1,0,0,0,338,339,5,7,0,0,339,340,3,66,33,0,340,344,5,49,0,0,341,
        343,3,6,3,0,342,341,1,0,0,0,343,346,1,0,0,0,344,342,1,0,0,0,344,
        345,1,0,0,0,345,356,1,0,0,0,346,344,1,0,0,0,347,348,5,8,0,0,348,
        352,5,49,0,0,349,351,3,6,3,0,350,349,1,0,0,0,351,354,1,0,0,0,352,
        350,1,0,0,0,352,353,1,0,0,0,353,356,1,0,0,0,354,352,1,0,0,0,355,
        338,1,0,0,0,355,347,1,0,0,0,356,31,1,0,0,0,357,361,3,34,17,0,358,
        360,3,36,18,0,359,358,1,0,0,0,360,363,1,0,0,0,361,359,1,0,0,0,361,
        362,1,0,0,0,362,365,1,0,0,0,363,361,1,0,0,0,364,366,3,38,19,0,365,
        364,1,0,0,0,365,366,1,0,0,0,366,33,1,0,0,0,367,368,5,9,0,0,368,369,
        5,25,0,0,369,370,3,60,30,0,370,371,5,26,0,0,371,372,3,4,2,0,372,
        35,1,0,0,0,373,374,5,10,0,0,374,375,5,9,0,0,375,376,5,25,0,0,376,
        377,3,60,30,0,377,378,5,26,0,0,378,379,3,4,2,0,379,37,1,0,0,0,380,
        381,5,10,0,0,381,382,3,4,2,0,382,39,1,0,0,0,383,384,5,11,0,0,384,
        385,5,25,0,0,385,386,3,60,30,0,386,387,5,26,0,0,387,388,3,4,2,0,
        388,41,1,0,0,0,389,390,5,12,0,0,390,391,5,25,0,0,391,392,3,44,22,
        0,392,393,5,26,0,0,393,394,3,4,2,0,394,43,1,0,0,0,395,397,3,56,28,
        0,396,395,1,0,0,0,396,397,1,0,0,0,397,398,1,0,0,0,398,400,5,50,0,
        0,399,401,3,60,30,0,400,399,1,0,0,0,400,401,1,0,0,0,401,402,1,0,
        0,0,402,404,5,50,0,0,403,405,3,60,30,0,404,403,1,0,0,0,404,405,1,
        0,0,0,405,45,1,0,0,0,406,407,5,13,0,0,407,408,5,25,0,0,408,418,3,
        50,25,0,409,414,5,51,0,0,410,415,3,52,26,0,411,415,3,54,27,0,412,
        415,3,60,30,0,413,415,3,18,9,0,414,410,1,0,0,0,414,411,1,0,0,0,414,
        412,1,0,0,0,414,413,1,0,0,0,415,417,1,0,0,0,416,409,1,0,0,0,417,
        420,1,0,0,0,418,416,1,0,0,0,418,419,1,0,0,0,419,421,1,0,0,0,420,
        418,1,0,0,0,421,422,5,26,0,0,422,47,1,0,0,0,423,424,5,14,0,0,424,
        425,5,25,0,0,425,430,3,50,25,0,426,427,5,51,0,0,427,429,3,74,37,
        0,428,426,1,0,0,0,429,432,1,0,0,0,430,428,1,0,0,0,430,431,1,0,0,
        0,431,433,1,0,0,0,432,430,1,0,0,0,433,434,5,26,0,0,434,49,1,0,0,
        0,435,436,5,55,0,0,436,51,1,0,0,0,437,438,5,54,0,0,438,53,1,0,0,
        0,439,440,5,55,0,0,440,55,1,0,0,0,441,442,3,58,29,0,442,443,5,2,
        0,0,443,444,3,60,30,0,444,448,1,0,0,0,445,448,3,58,29,0,446,448,
        3,104,52,0,447,441,1,0,0,0,447,445,1,0,0,0,447,446,1,0,0,0,448,57,
        1,0,0,0,449,463,3,108,54,0,450,451,3,106,53,0,451,452,3,108,54,0,
        452,463,1,0,0,0,453,454,3,70,35,0,454,455,3,108,54,0,455,463,1,0,
        0,0,456,463,3,72,36,0,457,458,5,25,0,0,458,459,3,58,29,0,459,460,
        5,26,0,0,460,463,1,0,0,0,461,463,3,102,51,0,462,449,1,0,0,0,462,
        450,1,0,0,0,462,453,1,0,0,0,462,456,1,0,0,0,462,457,1,0,0,0,462,
        461,1,0,0,0,463,59,1,0,0,0,464,465,6,30,-1,0,465,491,3,64,32,0,466,
        491,3,108,54,0,467,491,3,72,36,0,468,491,3,74,37,0,469,470,5,48,
        0,0,470,491,3,60,30,31,471,472,5,45,0,0,472,491,3,60,30,30,473,475,
        7,0,0,0,474,473,1,0,0,0,474,475,1,0,0,0,475,476,1,0,0,0,476,477,
        5,25,0,0,477,478,3,60,30,0,478,479,5,26,0,0,479,491,1,0,0,0,480,
        491,3,68,34,0,481,491,3,84,42,0,482,491,3,86,43,0,483,491,3,88,44,
        0,484,491,3,90,45,0,485,491,3,24,12,0,486,491,3,62,31,0,487,491,
        3,102,51,0,488,491,3,54,27,0,489,491,3,18,9,0,490,464,1,0,0,0,490,
        466,1,0,0,0,490,467,1,0,0,0,490,468,1,0,0,0,490,469,1,0,0,0,490,
        471,1,0,0,0,490,474,1,0,0,0,490,480,1,0,0,0,490,481,1,0,0,0,490,
        482,1,0,0,0,490,483,1,0,0,0,490,484,1,0,0,0,490,485,1,0,0,0,490,
        486,1,0,0,0,490,487,1,0,0,0,490,488,1,0,0,0,490,489,1,0,0,0,491,
        548,1,0,0,0,492,493,10,29,0,0,493,494,5,32,0,0,494,547,3,60,30,30,
        495,496,10,28,0,0,496,497,5,33,0,0,497,547,3,60,30,29,498,499,10,
        27,0,0,499,500,5,31,0,0,500,547,3,60,30,28,501,502,10,26,0,0,502,
        503,5,30,0,0,503,547,3,60,30,27,504,505,10,25,0,0,505,506,5,29,0,
        0,506,547,3,60,30,26,507,508,10,24,0,0,508,509,5,40,0,0,509,547,
        3,60,30,25,510,511,10,23,0,0,511,512,5,41,0,0,512,547,3,60,30,24,
        513,514,10,22,0,0,514,515,5,42,0,0,515,547,3,60,30,23,516,517,10,
        21,0,0,517,518,5,43,0,0,518,547,3,60,30,22,519,520,10,20,0,0,520,
        521,5,44,0,0,521,547,3,60,30,21,522,523,10,19,0,0,523,524,5,38,0,
        0,524,547,3,60,30,20,525,526,10,18,0,0,526,527,5,39,0,0,527,547,
        3,60,30,19,528,529,10,17,0,0,529,530,5,46,0,0,530,547,3,60,30,18,
        531,532,10,16,0,0,532,533,5,47,0,0,533,547,3,60,30,17,534,535,10,
        15,0,0,535,536,5,34,0,0,536,547,3,60,30,16,537,538,10,14,0,0,538,
        539,5,35,0,0,539,547,3,60,30,15,540,541,10,13,0,0,541,542,5,36,0,
        0,542,547,3,60,30,14,543,544,10,12,0,0,544,545,5,37,0,0,545,547,
        3,60,30,13,546,492,1,0,0,0,546,495,1,0,0,0,546,498,1,0,0,0,546,501,
        1,0,0,0,546,504,1,0,0,0,546,507,1,0,0,0,546,510,1,0,0,0,546,513,
        1,0,0,0,546,516,1,0,0,0,546,519,1,0,0,0,546,522,1,0,0,0,546,525,
        1,0,0,0,546,528,1,0,0,0,546,531,1,0,0,0,546,534,1,0,0,0,546,537,
        1,0,0,0,546,540,1,0,0,0,546,543,1,0,0,0,547,550,1,0,0,0,548,546,
        1,0,0,0,548,549,1,0,0,0,549,61,1,0,0,0,550,548,1,0,0,0,551,558,5,
        15,0,0,552,558,5,16,0,0,553,555,5,17,0,0,554,556,3,60,30,0,555,554,
        1,0,0,0,555,556,1,0,0,0,556,558,1,0,0,0,557,551,1,0,0,0,557,552,
        1,0,0,0,557,553,1,0,0,0,558,63,1,0,0,0,559,561,7,0,0,0,560,559,1,
        0,0,0,560,561,1,0,0,0,561,565,1,0,0,0,562,566,3,66,33,0,563,566,
        3,108,54,0,564,566,3,72,36,0,565,562,1,0,0,0,565,563,1,0,0,0,565,
        564,1,0,0,0,566,596,1,0,0,0,567,568,5,29,0,0,568,570,5,30,0,0,569,
        567,1,0,0,0,570,571,1,0,0,0,571,569,1,0,0,0,571,572,1,0,0,0,572,
        574,1,0,0,0,573,575,5,29,0,0,574,573,1,0,0,0,574,575,1,0,0,0,575,
        579,1,0,0,0,576,580,3,66,33,0,577,580,3,108,54,0,578,580,3,72,36,
        0,579,576,1,0,0,0,579,577,1,0,0,0,579,578,1,0,0,0,580,596,1,0,0,
        0,581,582,5,30,0,0,582,584,5,29,0,0,583,581,1,0,0,0,584,585,1,0,
        0,0,585,583,1,0,0,0,585,586,1,0,0,0,586,588,1,0,0,0,587,589,5,30,
        0,0,588,587,1,0,0,0,588,589,1,0,0,0,589,593,1,0,0,0,590,594,3,66,
        33,0,591,594,3,108,54,0,592,594,3,72,36,0,593,590,1,0,0,0,593,591,
        1,0,0,0,593,592,1,0,0,0,594,596,1,0,0,0,595,560,1,0,0,0,595,569,
        1,0,0,0,595,583,1,0,0,0,596,65,1,0,0,0,597,598,7,1,0,0,598,67,1,
        0,0,0,599,601,5,25,0,0,600,599,1,0,0,0,601,602,1,0,0,0,602,600,1,
        0,0,0,602,603,1,0,0,0,603,605,1,0,0,0,604,606,3,106,53,0,605,604,
        1,0,0,0,606,607,1,0,0,0,607,605,1,0,0,0,607,608,1,0,0,0,608,609,
        1,0,0,0,609,610,5,26,0,0,610,611,3,60,30,0,611,69,1,0,0,0,612,614,
        3,106,53,0,613,615,5,31,0,0,614,613,1,0,0,0,615,616,1,0,0,0,616,
        614,1,0,0,0,616,617,1,0,0,0,617,71,1,0,0,0,618,620,5,31,0,0,619,
        618,1,0,0,0,620,621,1,0,0,0,621,619,1,0,0,0,621,622,1,0,0,0,622,
        623,1,0,0,0,623,624,3,108,54,0,624,73,1,0,0,0,625,627,5,42,0,0,626,
        625,1,0,0,0,627,628,1,0,0,0,628,626,1,0,0,0,628,629,1,0,0,0,629,
        632,1,0,0,0,630,633,3,108,54,0,631,633,3,102,51,0,632,630,1,0,0,
        0,632,631,1,0,0,0,633,75,1,0,0,0,634,635,5,18,0,0,635,636,5,57,0,
        0,636,637,5,27,0,0,637,642,5,57,0,0,638,639,5,51,0,0,639,641,5,57,
        0,0,640,638,1,0,0,0,641,644,1,0,0,0,642,640,1,0,0,0,642,643,1,0,
        0,0,643,645,1,0,0,0,644,642,1,0,0,0,645,646,5,28,0,0,646,77,1,0,
        0,0,647,650,3,80,40,0,648,650,3,82,41,0,649,647,1,0,0,0,649,648,
        1,0,0,0,650,79,1,0,0,0,651,652,5,18,0,0,652,653,5,57,0,0,653,654,
        5,57,0,0,654,655,5,2,0,0,655,656,5,57,0,0,656,81,1,0,0,0,657,658,
        5,18,0,0,658,659,5,57,0,0,659,660,5,57,0,0,660,83,1,0,0,0,661,662,
        3,58,29,0,662,663,5,58,0,0,663,85,1,0,0,0,664,665,3,58,29,0,665,
        666,5,59,0,0,666,87,1,0,0,0,667,668,5,58,0,0,668,669,3,58,29,0,669,
        89,1,0,0,0,670,671,5,59,0,0,671,672,3,58,29,0,672,91,1,0,0,0,673,
        676,3,94,47,0,674,676,3,98,49,0,675,673,1,0,0,0,675,674,1,0,0,0,
        676,93,1,0,0,0,677,678,3,106,53,0,678,683,3,108,54,0,679,680,5,4,
        0,0,680,681,3,60,30,0,681,682,5,5,0,0,682,684,1,0,0,0,683,679,1,
        0,0,0,684,685,1,0,0,0,685,683,1,0,0,0,685,686,1,0,0,0,686,95,1,0,
        0,0,687,692,3,108,54,0,688,689,5,4,0,0,689,690,3,60,30,0,690,691,
        5,5,0,0,691,693,1,0,0,0,692,688,1,0,0,0,693,694,1,0,0,0,694,692,
        1,0,0,0,694,695,1,0,0,0,695,696,1,0,0,0,696,699,5,2,0,0,697,700,
        3,60,30,0,698,700,3,100,50,0,699,697,1,0,0,0,699,698,1,0,0,0,700,
        706,1,0,0,0,701,702,3,108,54,0,702,703,5,2,0,0,703,704,3,100,50,
        0,704,706,1,0,0,0,705,687,1,0,0,0,705,701,1,0,0,0,706,97,1,0,0,0,
        707,708,3,106,53,0,708,713,3,108,54,0,709,710,5,4,0,0,710,711,3,
        60,30,0,711,712,5,5,0,0,712,714,1,0,0,0,713,709,1,0,0,0,714,715,
        1,0,0,0,715,713,1,0,0,0,715,716,1,0,0,0,716,717,1,0,0,0,717,720,
        5,2,0,0,718,721,3,100,50,0,719,721,3,54,27,0,720,718,1,0,0,0,720,
        719,1,0,0,0,721,99,1,0,0,0,722,725,5,27,0,0,723,726,3,60,30,0,724,
        726,3,100,50,0,725,723,1,0,0,0,725,724,1,0,0,0,726,734,1,0,0,0,727,
        730,5,51,0,0,728,731,3,60,30,0,729,731,3,100,50,0,730,728,1,0,0,
        0,730,729,1,0,0,0,731,733,1,0,0,0,732,727,1,0,0,0,733,736,1,0,0,
        0,734,732,1,0,0,0,734,735,1,0,0,0,735,737,1,0,0,0,736,734,1,0,0,
        0,737,738,5,28,0,0,738,101,1,0,0,0,739,744,3,108,54,0,740,741,5,
        4,0,0,741,742,3,60,30,0,742,743,5,5,0,0,743,745,1,0,0,0,744,740,
        1,0,0,0,745,746,1,0,0,0,746,744,1,0,0,0,746,747,1,0,0,0,747,103,
        1,0,0,0,748,749,5,19,0,0,749,750,3,106,53,0,750,751,5,57,0,0,751,
        105,1,0,0,0,752,754,5,20,0,0,753,752,1,0,0,0,754,757,1,0,0,0,755,
        753,1,0,0,0,755,756,1,0,0,0,756,758,1,0,0,0,757,755,1,0,0,0,758,
        759,7,2,0,0,759,107,1,0,0,0,760,761,5,57,0,0,761,109,1,0,0,0,762,
        763,5,60,0,0,763,111,1,0,0,0,80,117,120,122,132,138,147,153,160,
        166,176,182,190,196,198,202,207,214,219,224,233,239,247,260,265,
        269,283,293,297,304,310,322,333,344,352,355,361,365,396,400,404,
        414,418,430,447,462,474,490,546,548,555,557,560,565,571,574,579,
        585,588,593,595,602,607,616,621,628,632,642,649,675,685,694,699,
        705,715,720,725,730,734,746,755
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'='", "'.'", "'['", "']'", 
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
    RULE_structVariableDefinition = 8
    RULE_structMember = 9
    RULE_structAssignment = 10
    RULE_functionParams = 11
    RULE_functionCall = 12
    RULE_callParams = 13
    RULE_switchStatement = 14
    RULE_switchCase = 15
    RULE_conditional = 16
    RULE_ifStatement = 17
    RULE_elseIfStatement = 18
    RULE_elseStatement = 19
    RULE_whileLoop = 20
    RULE_forLoop = 21
    RULE_forCondition = 22
    RULE_printfStatement = 23
    RULE_scanfStatement = 24
    RULE_formatSpecifier = 25
    RULE_char = 26
    RULE_string = 27
    RULE_variable = 28
    RULE_lvalue = 29
    RULE_rvalue = 30
    RULE_jumpStatement = 31
    RULE_unaryExpression = 32
    RULE_literal = 33
    RULE_explicitConversion = 34
    RULE_pointer = 35
    RULE_deref = 36
    RULE_addr = 37
    RULE_enumDeclaration = 38
    RULE_enumStatement = 39
    RULE_enumVariableDefinition = 40
    RULE_enumVariableDeclaration = 41
    RULE_postFixIncrement = 42
    RULE_postFixDecrement = 43
    RULE_preFixIncrement = 44
    RULE_preFixDecrement = 45
    RULE_arrayStatement = 46
    RULE_arrayDeclaration = 47
    RULE_arrayAssignment = 48
    RULE_arrayDefinition = 49
    RULE_array = 50
    RULE_arrayElement = 51
    RULE_typedef = 52
    RULE_type = 53
    RULE_identifier = 54
    RULE_comment = 55

    ruleNames =  [ "program", "declaration", "scope", "statement", "function", 
                   "structDefinition", "structStatement", "structVariable", 
                   "structVariableDefinition", "structMember", "structAssignment", 
                   "functionParams", "functionCall", "callParams", "switchStatement", 
                   "switchCase", "conditional", "ifStatement", "elseIfStatement", 
                   "elseStatement", "whileLoop", "forLoop", "forCondition", 
                   "printfStatement", "scanfStatement", "formatSpecifier", 
                   "char", "string", "variable", "lvalue", "rvalue", "jumpStatement", 
                   "unaryExpression", "literal", "explicitConversion", "pointer", 
                   "deref", "addr", "enumDeclaration", "enumStatement", 
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
            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 112
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 113
                    self.declaration()
                    self.state = 115 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 114
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 117 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==50):
                            break

                    pass

                elif la_ == 3:
                    self.state = 119
                    self.function()
                    pass


                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1297036694897033218) != 0)):
                    break

            self.state = 124
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


        def enumStatement(self):
            return self.getTypedRuleContext(GrammarParser.EnumStatementContext,0)


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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.enumDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.structDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.variable()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.typedef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.arrayStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 131
                self.enumStatement()
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
            self.state = 134
            self.match(GrammarParser.LBRACE)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                self.state = 135
                self.statement()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
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
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.rvalue(0)
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

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.variable()
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 150
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 153 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.printfStatement()
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

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.scanfStatement()
                self.state = 164 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 163
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 166 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 168
                self.scope()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 169
                self.conditional()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 170
                self.whileLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 171
                self.forLoop()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 172
                self.enumStatement()
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

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 178
                self.jumpStatement()
                self.state = 180 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 179
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 182 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==50):
                        break

                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 184
                self.function()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 185
                self.switchStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 186
                self.arrayStatement()
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

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 192
                self.structStatement()
                self.state = 194 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 193
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 196 
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
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 200
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 201
                    self.pointer()
                    pass


                self.state = 204
                self.match(GrammarParser.IDENTIFIER)
                self.state = 205
                self.match(GrammarParser.LPAREN)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                    self.state = 206
                    self.functionParams(0)


                self.state = 209
                self.match(GrammarParser.RPAREN)
                self.state = 210
                self.scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 212
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 213
                    self.pointer()
                    pass


                self.state = 216
                self.match(GrammarParser.IDENTIFIER)
                self.state = 217
                self.match(GrammarParser.LPAREN)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                    self.state = 218
                    self.functionParams(0)


                self.state = 221
                self.match(GrammarParser.RPAREN)
                self.state = 222
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
            self.state = 226
            self.match(GrammarParser.T__0)
            self.state = 227
            self.match(GrammarParser.IDENTIFIER)
            self.state = 228
            self.match(GrammarParser.LBRACE)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0):
                self.state = 233
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 229
                    self.type_()
                    self.state = 230
                    self.identifier()
                    pass

                elif la_ == 2:
                    self.state = 232
                    self.arrayDeclaration()
                    pass


                self.state = 235
                self.match(GrammarParser.SEMICOLON)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
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


        def structVariableDefinition(self):
            return self.getTypedRuleContext(GrammarParser.StructVariableDefinitionContext,0)


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
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.structVariable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.structVariableDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.structAssignment()
                pass


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


    class StructVariableDefinitionContext(ParserRuleContext):
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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_structVariableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructVariableDefinition" ):
                listener.enterStructVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructVariableDefinition" ):
                listener.exitStructVariableDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructVariableDefinition" ):
                return visitor.visitStructVariableDefinition(self)
            else:
                return visitor.visitChildren(self)




    def structVariableDefinition(self):

        localctx = GrammarParser.StructVariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structVariableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(GrammarParser.T__0)
            self.state = 254
            self.match(GrammarParser.IDENTIFIER)
            self.state = 255
            self.match(GrammarParser.IDENTIFIER)
            self.state = 256
            self.match(GrammarParser.T__1)
            self.state = 257
            self.match(GrammarParser.LBRACE)
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 258
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.state = 259
                self.structMember()
                pass


            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 262
                self.match(GrammarParser.COMMA)
                self.state = 265
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 263
                    self.rvalue(0)
                    pass

                elif la_ == 2:
                    self.state = 264
                    self.structMember()
                    pass


                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            self.match(GrammarParser.RBRACE)
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
        self.enterRule(localctx, 18, self.RULE_structMember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(GrammarParser.IDENTIFIER)
            self.state = 275
            self.match(GrammarParser.T__2)
            self.state = 276
            self.match(GrammarParser.IDENTIFIER)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 277
                    self.match(GrammarParser.T__3)
                    self.state = 278
                    self.rvalue(0)
                    self.state = 279
                    self.match(GrammarParser.T__4) 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_structAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.structMember()
            self.state = 287
            self.match(GrammarParser.T__1)
            self.state = 288
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_functionParams, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 291
                self.pointer()
                pass

            elif la_ == 2:
                self.state = 292
                self.type_()
                pass


            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 295
                self.addr()
                pass
            elif token in [57]:
                self.state = 296
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.FunctionParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParams)
                    self.state = 299
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 300
                    self.match(GrammarParser.COMMA)
                    self.state = 301
                    self.functionParams(2) 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(GrammarParser.IDENTIFIER)
            self.state = 308
            self.match(GrammarParser.LPAREN)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 309
                self.callParams(0)


            self.state = 312
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_callParams, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.rvalue(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CallParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callParams)
                    self.state = 317
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 318
                    self.match(GrammarParser.COMMA)
                    self.state = 319
                    self.callParams(2) 
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(GrammarParser.T__5)
            self.state = 326
            self.match(GrammarParser.LPAREN)
            self.state = 327
            self.rvalue(0)
            self.state = 328
            self.match(GrammarParser.RPAREN)
            self.state = 329
            self.match(GrammarParser.LBRACE)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 330
                self.switchCase()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 336
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
        self.enterRule(localctx, 30, self.RULE_switchCase)
        self._la = 0 # Token type
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(GrammarParser.T__6)
                self.state = 339
                self.literal()
                self.state = 340
                self.match(GrammarParser.COLON)
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                    self.state = 341
                    self.statement()
                    self.state = 346
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(GrammarParser.T__7)
                self.state = 348
                self.match(GrammarParser.COLON)
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229602876903127618) != 0):
                    self.state = 349
                    self.statement()
                    self.state = 354
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
        self.enterRule(localctx, 32, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.ifStatement()
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 358
                    self.elseIfStatement() 
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 364
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
        self.enterRule(localctx, 34, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(GrammarParser.T__8)
            self.state = 368
            self.match(GrammarParser.LPAREN)
            self.state = 369
            self.rvalue(0)
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
        self.enterRule(localctx, 36, self.RULE_elseIfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(GrammarParser.T__9)
            self.state = 374
            self.match(GrammarParser.T__8)
            self.state = 375
            self.match(GrammarParser.LPAREN)
            self.state = 376
            self.rvalue(0)
            self.state = 377
            self.match(GrammarParser.RPAREN)
            self.state = 378
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
        self.enterRule(localctx, 38, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(GrammarParser.T__9)
            self.state = 381
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
        self.enterRule(localctx, 40, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(GrammarParser.T__10)
            self.state = 384
            self.match(GrammarParser.LPAREN)
            self.state = 385
            self.rvalue(0)
            self.state = 386
            self.match(GrammarParser.RPAREN)
            self.state = 387
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
        self.enterRule(localctx, 42, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(GrammarParser.T__11)
            self.state = 390
            self.match(GrammarParser.LPAREN)
            self.state = 391
            self.forCondition()
            self.state = 392
            self.match(GrammarParser.RPAREN)
            self.state = 393
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
        self.enterRule(localctx, 44, self.RULE_forCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115190289924096) != 0):
                self.state = 395
                self.variable()


            self.state = 398
            self.match(GrammarParser.SEMICOLON)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 399
                self.rvalue(0)


            self.state = 402
            self.match(GrammarParser.SEMICOLON)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1076681372161245184) != 0):
                self.state = 403
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
        self.enterRule(localctx, 46, self.RULE_printfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(GrammarParser.T__12)
            self.state = 407
            self.match(GrammarParser.LPAREN)
            self.state = 408
            self.formatSpecifier()
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 409
                self.match(GrammarParser.COMMA)
                self.state = 414
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 410
                    self.char()
                    pass

                elif la_ == 2:
                    self.state = 411
                    self.string()
                    pass

                elif la_ == 3:
                    self.state = 412
                    self.rvalue(0)
                    pass

                elif la_ == 4:
                    self.state = 413
                    self.structMember()
                    pass


                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 421
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
        self.enterRule(localctx, 48, self.RULE_scanfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(GrammarParser.T__13)
            self.state = 424
            self.match(GrammarParser.LPAREN)
            self.state = 425
            self.formatSpecifier()
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 426
                self.match(GrammarParser.COMMA)
                self.state = 427
                self.addr()
                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 433
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
        self.enterRule(localctx, 50, self.RULE_formatSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
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
        self.enterRule(localctx, 52, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
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
        self.enterRule(localctx, 54, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
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
        self.enterRule(localctx, 56, self.RULE_variable)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.lvalue()
                self.state = 442
                self.match(GrammarParser.T__1)
                self.state = 443
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.lvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
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
        self.enterRule(localctx, 58, self.RULE_lvalue)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.type_()
                self.state = 451
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 453
                self.pointer()
                self.state = 454
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 456
                self.deref()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 457
                self.match(GrammarParser.LPAREN)
                self.state = 458
                self.lvalue()
                self.state = 459
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 461
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


        def structMember(self):
            return self.getTypedRuleContext(GrammarParser.StructMemberContext,0)


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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_rvalue, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 465
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.state = 466
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 467
                self.deref()
                pass

            elif la_ == 4:
                self.state = 468
                self.addr()
                pass

            elif la_ == 5:
                self.state = 469
                self.match(GrammarParser.LOGICAL_NOT)
                self.state = 470
                self.rvalue(31)
                pass

            elif la_ == 6:
                self.state = 471
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 472
                self.rvalue(30)
                pass

            elif la_ == 7:
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29 or _la==30:
                    self.state = 473
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 476
                self.match(GrammarParser.LPAREN)
                self.state = 477
                self.rvalue(0)
                self.state = 478
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 480
                self.explicitConversion()
                pass

            elif la_ == 9:
                self.state = 481
                self.postFixIncrement()
                pass

            elif la_ == 10:
                self.state = 482
                self.postFixDecrement()
                pass

            elif la_ == 11:
                self.state = 483
                self.preFixIncrement()
                pass

            elif la_ == 12:
                self.state = 484
                self.preFixDecrement()
                pass

            elif la_ == 13:
                self.state = 485
                self.functionCall()
                pass

            elif la_ == 14:
                self.state = 486
                self.jumpStatement()
                pass

            elif la_ == 15:
                self.state = 487
                self.arrayElement()
                pass

            elif la_ == 16:
                self.state = 488
                self.string()
                pass

            elif la_ == 17:
                self.state = 489
                self.structMember()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 548
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 546
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 492
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 493
                        self.match(GrammarParser.DIV)
                        self.state = 494
                        self.rvalue(30)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 495
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 496
                        self.match(GrammarParser.MOD)
                        self.state = 497
                        self.rvalue(29)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 498
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 499
                        self.match(GrammarParser.MULT)
                        self.state = 500
                        self.rvalue(28)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 501
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 502
                        self.match(GrammarParser.MINUS)
                        self.state = 503
                        self.rvalue(27)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 504
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 505
                        self.match(GrammarParser.PLUS)
                        self.state = 506
                        self.rvalue(26)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 507
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 508
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 509
                        self.rvalue(25)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 510
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 511
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 512
                        self.rvalue(24)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 513
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 514
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 515
                        self.rvalue(23)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 516
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 517
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 518
                        self.rvalue(22)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 519
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 520
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 521
                        self.rvalue(21)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 522
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 523
                        self.match(GrammarParser.EQUALS)
                        self.state = 524
                        self.rvalue(20)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 525
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 526
                        self.match(GrammarParser.NOT_EQUAL)
                        self.state = 527
                        self.rvalue(19)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 528
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 529
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 530
                        self.rvalue(18)
                        pass

                    elif la_ == 14:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 531
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 532
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 533
                        self.rvalue(17)
                        pass

                    elif la_ == 15:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 534
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 535
                        self.match(GrammarParser.GREATER_THAN)
                        self.state = 536
                        self.rvalue(16)
                        pass

                    elif la_ == 16:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 537
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 538
                        self.match(GrammarParser.LESS_THAN)
                        self.state = 539
                        self.rvalue(15)
                        pass

                    elif la_ == 17:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 540
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 541
                        self.match(GrammarParser.GREATER_EQUAL)
                        self.state = 542
                        self.rvalue(14)
                        pass

                    elif la_ == 18:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 543
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 544
                        self.match(GrammarParser.LESS_EQUAL)
                        self.state = 545
                        self.rvalue(13)
                        pass

             
                self.state = 550
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
        self.enterRule(localctx, 62, self.RULE_jumpStatement)
        try:
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.match(GrammarParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.match(GrammarParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 553
                self.match(GrammarParser.T__16)
                self.state = 555
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 554
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
        self.enterRule(localctx, 64, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 595
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29 or _la==30:
                    self.state = 559
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 565
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 562
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 563
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 564
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 569 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 567
                        self.match(GrammarParser.PLUS)
                        self.state = 568
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 571 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

                self.state = 574
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 573
                    self.match(GrammarParser.PLUS)


                self.state = 579
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 576
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 577
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 578
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 583 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 581
                        self.match(GrammarParser.MINUS)
                        self.state = 582
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 585 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

                self.state = 588
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 587
                    self.match(GrammarParser.MINUS)


                self.state = 593
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [52, 53, 54]:
                    self.state = 590
                    self.literal()
                    pass
                elif token in [57]:
                    self.state = 591
                    self.identifier()
                    pass
                elif token in [31]:
                    self.state = 592
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
        self.enterRule(localctx, 66, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
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
        self.enterRule(localctx, 68, self.RULE_explicitConversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 599
                self.match(GrammarParser.LPAREN)
                self.state = 602 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 605 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 604
                self.type_()
                self.state = 607 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188108361728) != 0)):
                    break

            self.state = 609
            self.match(GrammarParser.RPAREN)
            self.state = 610
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
        self.enterRule(localctx, 70, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.type_()
            self.state = 614 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 613
                self.match(GrammarParser.MULT)
                self.state = 616 
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
        self.enterRule(localctx, 72, self.RULE_deref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 618
                self.match(GrammarParser.MULT)
                self.state = 621 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 623
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


        def arrayElement(self):
            return self.getTypedRuleContext(GrammarParser.ArrayElementContext,0)


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
        self.enterRule(localctx, 74, self.RULE_addr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 625
                self.match(GrammarParser.BITWISE_AND)
                self.state = 628 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 632
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 630
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 631
                self.arrayElement()
                pass


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
        self.enterRule(localctx, 76, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            self.match(GrammarParser.T__17)
            self.state = 635
            self.match(GrammarParser.IDENTIFIER)
            self.state = 636
            self.match(GrammarParser.LBRACE)
            self.state = 637
            self.match(GrammarParser.IDENTIFIER)
            self.state = 642
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 638
                self.match(GrammarParser.COMMA)
                self.state = 639
                self.match(GrammarParser.IDENTIFIER)
                self.state = 644
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 645
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
        self.enterRule(localctx, 78, self.RULE_enumStatement)
        try:
            self.state = 649
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 647
                self.enumVariableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 648
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
        self.enterRule(localctx, 80, self.RULE_enumVariableDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            self.match(GrammarParser.T__17)
            self.state = 652
            self.match(GrammarParser.IDENTIFIER)
            self.state = 653
            self.match(GrammarParser.IDENTIFIER)
            self.state = 654
            self.match(GrammarParser.T__1)
            self.state = 655
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
        self.enterRule(localctx, 82, self.RULE_enumVariableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 657
            self.match(GrammarParser.T__17)
            self.state = 658
            self.match(GrammarParser.IDENTIFIER)
            self.state = 659
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
        self.enterRule(localctx, 84, self.RULE_postFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.lvalue()
            self.state = 662
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
        self.enterRule(localctx, 86, self.RULE_postFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            self.lvalue()
            self.state = 665
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
        self.enterRule(localctx, 88, self.RULE_preFixIncrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.match(GrammarParser.INCREMENT)
            self.state = 668
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
        self.enterRule(localctx, 90, self.RULE_preFixDecrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 670
            self.match(GrammarParser.DECREMENT)
            self.state = 671
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
        self.enterRule(localctx, 92, self.RULE_arrayStatement)
        try:
            self.state = 675
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 673
                self.arrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 674
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
        self.enterRule(localctx, 94, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            self.type_()
            self.state = 678
            self.identifier()
            self.state = 683 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 679
                self.match(GrammarParser.T__3)
                self.state = 680
                self.rvalue(0)
                self.state = 681
                self.match(GrammarParser.T__4)
                self.state = 685 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
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
        self.enterRule(localctx, 96, self.RULE_arrayAssignment)
        self._la = 0 # Token type
        try:
            self.state = 705
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 687
                self.identifier()
                self.state = 692 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 688
                    self.match(GrammarParser.T__3)
                    self.state = 689
                    self.rvalue(0)
                    self.state = 690
                    self.match(GrammarParser.T__4)
                    self.state = 694 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                self.state = 696
                self.match(GrammarParser.T__1)
                self.state = 699
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                    self.state = 697
                    self.rvalue(0)
                    pass
                elif token in [27]:
                    self.state = 698
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 701
                self.identifier()
                self.state = 702
                self.match(GrammarParser.T__1)
                self.state = 703
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
        self.enterRule(localctx, 98, self.RULE_arrayDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
            self.type_()
            self.state = 708
            self.identifier()
            self.state = 713 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 709
                self.match(GrammarParser.T__3)
                self.state = 710
                self.rvalue(0)
                self.state = 711
                self.match(GrammarParser.T__4)
                self.state = 715 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 717
            self.match(GrammarParser.T__1)
            self.state = 720
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 718
                self.array()
                pass
            elif token in [55]:
                self.state = 719
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
        self.enterRule(localctx, 100, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
            self.match(GrammarParser.LBRACE)
            self.state = 725
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                self.state = 723
                self.rvalue(0)
                pass
            elif token in [27]:
                self.state = 724
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 734
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 727
                self.match(GrammarParser.COMMA)
                self.state = 730
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 17, 20, 21, 22, 23, 24, 25, 29, 30, 31, 42, 45, 48, 52, 53, 54, 55, 57, 58, 59]:
                    self.state = 728
                    self.rvalue(0)
                    pass
                elif token in [27]:
                    self.state = 729
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 736
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 737
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
        self.enterRule(localctx, 102, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
            self.identifier()
            self.state = 744 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 740
                    self.match(GrammarParser.T__3)
                    self.state = 741
                    self.rvalue(0)
                    self.state = 742
                    self.match(GrammarParser.T__4)

                else:
                    raise NoViableAltException(self)
                self.state = 746 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

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
        self.enterRule(localctx, 104, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 748
            self.match(GrammarParser.T__18)
            self.state = 749
            self.type_()
            self.state = 750
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
        self.enterRule(localctx, 106, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 752
                self.match(GrammarParser.T__19)
                self.state = 757
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 758
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
        self.enterRule(localctx, 108, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 760
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
        self.enterRule(localctx, 110, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 762
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
        self._predicates[11] = self.functionParams_sempred
        self._predicates[13] = self.callParams_sempred
        self._predicates[30] = self.rvalue_sempred
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
                return self.precpred(self._ctx, 29)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 12)
         




