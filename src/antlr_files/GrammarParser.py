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
        4,1,59,645,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,1,0,1,0,4,0,100,8,0,11,0,12,0,101,1,0,1,0,4,0,
        106,8,0,11,0,12,0,107,1,0,1,0,4,0,112,8,0,11,0,12,0,113,1,0,4,0,
        117,8,0,11,0,12,0,118,1,0,1,0,1,1,1,1,5,1,125,8,1,10,1,12,1,128,
        9,1,1,1,1,1,1,2,1,2,4,2,134,8,2,11,2,12,2,135,1,2,1,2,4,2,140,8,
        2,11,2,12,2,141,1,2,1,2,1,2,4,2,147,8,2,11,2,12,2,148,1,2,1,2,1,
        2,1,2,1,2,1,2,4,2,157,8,2,11,2,12,2,158,1,2,1,2,4,2,163,8,2,11,2,
        12,2,164,1,2,1,2,1,2,1,2,4,2,171,8,2,11,2,12,2,172,3,2,175,8,2,1,
        3,1,3,3,3,179,8,3,1,3,1,3,1,3,3,3,184,8,3,1,3,1,3,1,3,1,3,1,3,3,
        3,191,8,3,1,3,1,3,1,3,3,3,196,8,3,1,3,1,3,1,3,3,3,201,8,3,1,4,1,
        4,1,4,3,4,206,8,4,1,4,1,4,3,4,210,8,4,1,4,1,4,1,4,5,4,215,8,4,10,
        4,12,4,218,9,4,1,5,1,5,1,5,3,5,223,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,6,5,6,233,8,6,10,6,12,6,236,9,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,
        244,8,7,10,7,12,7,247,9,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,255,8,8,10,
        8,12,8,258,9,8,1,8,1,8,1,8,5,8,263,8,8,10,8,12,8,266,9,8,3,8,268,
        8,8,1,9,1,9,5,9,272,8,9,10,9,12,9,275,9,9,1,9,3,9,278,8,9,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,15,3,15,309,8,15,1,15,1,15,3,15,313,8,15,1,15,1,15,3,15,317,
        8,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,325,8,16,5,16,327,8,16,10,
        16,12,16,330,9,16,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,
        19,1,19,1,19,3,19,344,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,3,20,354,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,377,
        8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        5,21,417,8,21,10,21,12,21,420,9,21,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,3,22,434,8,22,1,23,1,23,1,23,1,23,
        3,23,440,8,23,3,23,442,8,23,1,24,3,24,445,8,24,1,24,1,24,1,24,3,
        24,450,8,24,1,24,1,24,4,24,454,8,24,11,24,12,24,455,1,24,3,24,459,
        8,24,1,24,1,24,1,24,3,24,464,8,24,1,24,1,24,4,24,468,8,24,11,24,
        12,24,469,1,24,3,24,473,8,24,1,24,1,24,1,24,3,24,478,8,24,3,24,480,
        8,24,1,25,1,25,1,26,4,26,485,8,26,11,26,12,26,486,1,26,4,26,490,
        8,26,11,26,12,26,491,1,26,1,26,1,26,1,27,1,27,4,27,499,8,27,11,27,
        12,27,500,1,28,4,28,504,8,28,11,28,12,28,505,1,28,1,28,1,29,4,29,
        511,8,29,11,29,12,29,512,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,
        5,30,523,8,30,10,30,12,30,526,9,30,1,30,1,30,1,31,1,31,3,31,532,
        8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,
        1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,
        3,38,559,8,38,1,39,1,39,1,39,1,39,1,39,4,39,566,8,39,11,39,12,39,
        567,1,40,1,40,1,40,1,40,4,40,574,8,40,11,40,12,40,575,1,40,1,40,
        1,40,3,40,581,8,40,1,40,1,40,1,40,1,40,3,40,587,8,40,1,41,1,41,1,
        41,1,41,1,41,4,41,594,8,41,11,41,12,41,595,1,41,1,41,1,41,3,41,601,
        8,41,1,42,1,42,1,42,3,42,606,8,42,1,42,1,42,1,42,3,42,611,8,42,5,
        42,613,8,42,10,42,12,42,616,9,42,1,42,1,42,1,43,1,43,1,43,1,43,1,
        43,4,43,625,8,43,11,43,12,43,626,1,44,1,44,1,44,1,44,1,45,5,45,634,
        8,45,10,45,12,45,637,9,45,1,45,1,45,1,46,1,46,1,47,1,47,1,47,0,3,
        8,12,42,48,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,
        84,86,88,90,92,94,0,3,1,0,26,27,1,0,49,51,2,0,18,21,54,54,717,0,
        116,1,0,0,0,2,122,1,0,0,0,4,174,1,0,0,0,6,200,1,0,0,0,8,202,1,0,
        0,0,10,219,1,0,0,0,12,226,1,0,0,0,14,237,1,0,0,0,16,267,1,0,0,0,
        18,269,1,0,0,0,20,279,1,0,0,0,22,285,1,0,0,0,24,292,1,0,0,0,26,295,
        1,0,0,0,28,301,1,0,0,0,30,308,1,0,0,0,32,318,1,0,0,0,34,333,1,0,
        0,0,36,335,1,0,0,0,38,343,1,0,0,0,40,353,1,0,0,0,42,376,1,0,0,0,
        44,433,1,0,0,0,46,441,1,0,0,0,48,479,1,0,0,0,50,481,1,0,0,0,52,484,
        1,0,0,0,54,496,1,0,0,0,56,503,1,0,0,0,58,510,1,0,0,0,60,516,1,0,
        0,0,62,531,1,0,0,0,64,533,1,0,0,0,66,539,1,0,0,0,68,543,1,0,0,0,
        70,546,1,0,0,0,72,549,1,0,0,0,74,552,1,0,0,0,76,558,1,0,0,0,78,560,
        1,0,0,0,80,586,1,0,0,0,82,588,1,0,0,0,84,602,1,0,0,0,86,619,1,0,
        0,0,88,628,1,0,0,0,90,635,1,0,0,0,92,640,1,0,0,0,94,642,1,0,0,0,
        96,117,3,94,47,0,97,99,3,60,30,0,98,100,5,47,0,0,99,98,1,0,0,0,100,
        101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,117,1,0,0,0,103,105,
        3,38,19,0,104,106,5,47,0,0,105,104,1,0,0,0,106,107,1,0,0,0,107,105,
        1,0,0,0,107,108,1,0,0,0,108,117,1,0,0,0,109,111,3,88,44,0,110,112,
        5,47,0,0,111,110,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,
        1,0,0,0,114,117,1,0,0,0,115,117,3,6,3,0,116,96,1,0,0,0,116,97,1,
        0,0,0,116,103,1,0,0,0,116,109,1,0,0,0,116,115,1,0,0,0,117,118,1,
        0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,121,5,
        0,0,1,121,1,1,0,0,0,122,126,5,24,0,0,123,125,3,4,2,0,124,123,1,0,
        0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,129,1,0,
        0,0,128,126,1,0,0,0,129,130,5,25,0,0,130,3,1,0,0,0,131,133,3,42,
        21,0,132,134,5,47,0,0,133,132,1,0,0,0,134,135,1,0,0,0,135,133,1,
        0,0,0,135,136,1,0,0,0,136,175,1,0,0,0,137,139,3,38,19,0,138,140,
        5,47,0,0,139,138,1,0,0,0,140,141,1,0,0,0,141,139,1,0,0,0,141,142,
        1,0,0,0,142,175,1,0,0,0,143,175,3,94,47,0,144,146,3,32,16,0,145,
        147,5,47,0,0,146,145,1,0,0,0,147,148,1,0,0,0,148,146,1,0,0,0,148,
        149,1,0,0,0,149,175,1,0,0,0,150,175,3,2,1,0,151,175,3,18,9,0,152,
        175,3,26,13,0,153,175,3,28,14,0,154,156,3,62,31,0,155,157,5,47,0,
        0,156,155,1,0,0,0,157,158,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,
        0,159,175,1,0,0,0,160,162,3,46,23,0,161,163,5,47,0,0,162,161,1,0,
        0,0,163,164,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,175,1,0,
        0,0,166,175,3,6,3,0,167,175,3,14,7,0,168,170,3,76,38,0,169,171,5,
        47,0,0,170,169,1,0,0,0,171,172,1,0,0,0,172,170,1,0,0,0,172,173,1,
        0,0,0,173,175,1,0,0,0,174,131,1,0,0,0,174,137,1,0,0,0,174,143,1,
        0,0,0,174,144,1,0,0,0,174,150,1,0,0,0,174,151,1,0,0,0,174,152,1,
        0,0,0,174,153,1,0,0,0,174,154,1,0,0,0,174,160,1,0,0,0,174,166,1,
        0,0,0,174,167,1,0,0,0,174,168,1,0,0,0,175,5,1,0,0,0,176,179,3,90,
        45,0,177,179,3,54,27,0,178,176,1,0,0,0,178,177,1,0,0,0,179,180,1,
        0,0,0,180,181,5,54,0,0,181,183,5,22,0,0,182,184,3,8,4,0,183,182,
        1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,186,5,23,0,0,186,187,
        3,2,1,0,187,201,1,0,0,0,188,191,3,90,45,0,189,191,3,54,27,0,190,
        188,1,0,0,0,190,189,1,0,0,0,191,192,1,0,0,0,192,193,5,54,0,0,193,
        195,5,22,0,0,194,196,3,8,4,0,195,194,1,0,0,0,195,196,1,0,0,0,196,
        197,1,0,0,0,197,198,5,23,0,0,198,199,5,47,0,0,199,201,1,0,0,0,200,
        178,1,0,0,0,200,190,1,0,0,0,201,7,1,0,0,0,202,205,6,4,-1,0,203,206,
        3,54,27,0,204,206,3,90,45,0,205,203,1,0,0,0,205,204,1,0,0,0,206,
        209,1,0,0,0,207,210,3,58,29,0,208,210,3,92,46,0,209,207,1,0,0,0,
        209,208,1,0,0,0,210,216,1,0,0,0,211,212,10,1,0,0,212,213,5,48,0,
        0,213,215,3,8,4,2,214,211,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,
        0,216,217,1,0,0,0,217,9,1,0,0,0,218,216,1,0,0,0,219,220,5,54,0,0,
        220,222,5,22,0,0,221,223,3,12,6,0,222,221,1,0,0,0,222,223,1,0,0,
        0,223,224,1,0,0,0,224,225,5,23,0,0,225,11,1,0,0,0,226,227,6,6,-1,
        0,227,228,3,42,21,0,228,234,1,0,0,0,229,230,10,1,0,0,230,231,5,48,
        0,0,231,233,3,12,6,2,232,229,1,0,0,0,233,236,1,0,0,0,234,232,1,0,
        0,0,234,235,1,0,0,0,235,13,1,0,0,0,236,234,1,0,0,0,237,238,5,1,0,
        0,238,239,5,22,0,0,239,240,3,42,21,0,240,241,5,23,0,0,241,245,5,
        24,0,0,242,244,3,16,8,0,243,242,1,0,0,0,244,247,1,0,0,0,245,243,
        1,0,0,0,245,246,1,0,0,0,246,248,1,0,0,0,247,245,1,0,0,0,248,249,
        5,25,0,0,249,15,1,0,0,0,250,251,5,2,0,0,251,252,3,50,25,0,252,256,
        5,46,0,0,253,255,3,4,2,0,254,253,1,0,0,0,255,258,1,0,0,0,256,254,
        1,0,0,0,256,257,1,0,0,0,257,268,1,0,0,0,258,256,1,0,0,0,259,260,
        5,3,0,0,260,264,5,46,0,0,261,263,3,4,2,0,262,261,1,0,0,0,263,266,
        1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,268,1,0,0,0,266,264,
        1,0,0,0,267,250,1,0,0,0,267,259,1,0,0,0,268,17,1,0,0,0,269,273,3,
        20,10,0,270,272,3,22,11,0,271,270,1,0,0,0,272,275,1,0,0,0,273,271,
        1,0,0,0,273,274,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,276,278,
        3,24,12,0,277,276,1,0,0,0,277,278,1,0,0,0,278,19,1,0,0,0,279,280,
        5,4,0,0,280,281,5,22,0,0,281,282,3,42,21,0,282,283,5,23,0,0,283,
        284,3,2,1,0,284,21,1,0,0,0,285,286,5,5,0,0,286,287,5,4,0,0,287,288,
        5,22,0,0,288,289,3,42,21,0,289,290,5,23,0,0,290,291,3,2,1,0,291,
        23,1,0,0,0,292,293,5,5,0,0,293,294,3,2,1,0,294,25,1,0,0,0,295,296,
        5,6,0,0,296,297,5,22,0,0,297,298,3,42,21,0,298,299,5,23,0,0,299,
        300,3,2,1,0,300,27,1,0,0,0,301,302,5,7,0,0,302,303,5,22,0,0,303,
        304,3,30,15,0,304,305,5,23,0,0,305,306,3,2,1,0,306,29,1,0,0,0,307,
        309,3,38,19,0,308,307,1,0,0,0,308,309,1,0,0,0,309,310,1,0,0,0,310,
        312,5,47,0,0,311,313,3,42,21,0,312,311,1,0,0,0,312,313,1,0,0,0,313,
        314,1,0,0,0,314,316,5,47,0,0,315,317,3,42,21,0,316,315,1,0,0,0,316,
        317,1,0,0,0,317,31,1,0,0,0,318,319,5,8,0,0,319,320,5,22,0,0,320,
        328,3,34,17,0,321,324,5,48,0,0,322,325,3,42,21,0,323,325,3,36,18,
        0,324,322,1,0,0,0,324,323,1,0,0,0,325,327,1,0,0,0,326,321,1,0,0,
        0,327,330,1,0,0,0,328,326,1,0,0,0,328,329,1,0,0,0,329,331,1,0,0,
        0,330,328,1,0,0,0,331,332,5,23,0,0,332,33,1,0,0,0,333,334,5,52,0,
        0,334,35,1,0,0,0,335,336,5,52,0,0,336,37,1,0,0,0,337,338,3,40,20,
        0,338,339,5,9,0,0,339,340,3,42,21,0,340,344,1,0,0,0,341,344,3,40,
        20,0,342,344,3,88,44,0,343,337,1,0,0,0,343,341,1,0,0,0,343,342,1,
        0,0,0,344,39,1,0,0,0,345,354,3,92,46,0,346,347,3,90,45,0,347,348,
        3,92,46,0,348,354,1,0,0,0,349,350,3,54,27,0,350,351,3,92,46,0,351,
        354,1,0,0,0,352,354,3,56,28,0,353,345,1,0,0,0,353,346,1,0,0,0,353,
        349,1,0,0,0,353,352,1,0,0,0,354,41,1,0,0,0,355,356,6,21,-1,0,356,
        377,3,48,24,0,357,377,3,92,46,0,358,377,3,56,28,0,359,377,3,58,29,
        0,360,361,5,45,0,0,361,377,3,42,21,24,362,363,5,42,0,0,363,377,3,
        42,21,23,364,365,5,22,0,0,365,366,3,42,21,0,366,367,5,23,0,0,367,
        377,1,0,0,0,368,377,3,52,26,0,369,377,3,68,34,0,370,377,3,70,35,
        0,371,377,3,72,36,0,372,377,3,74,37,0,373,377,3,10,5,0,374,377,3,
        46,23,0,375,377,3,86,43,0,376,355,1,0,0,0,376,357,1,0,0,0,376,358,
        1,0,0,0,376,359,1,0,0,0,376,360,1,0,0,0,376,362,1,0,0,0,376,364,
        1,0,0,0,376,368,1,0,0,0,376,369,1,0,0,0,376,370,1,0,0,0,376,371,
        1,0,0,0,376,372,1,0,0,0,376,373,1,0,0,0,376,374,1,0,0,0,376,375,
        1,0,0,0,377,418,1,0,0,0,378,379,10,22,0,0,379,380,5,29,0,0,380,417,
        3,42,21,23,381,382,10,21,0,0,382,383,5,30,0,0,383,417,3,42,21,22,
        384,385,10,20,0,0,385,386,5,28,0,0,386,417,3,42,21,21,387,388,10,
        19,0,0,388,389,5,27,0,0,389,417,3,42,21,20,390,391,10,18,0,0,391,
        392,5,26,0,0,392,417,3,42,21,19,393,394,10,17,0,0,394,395,5,37,0,
        0,395,417,3,42,21,18,396,397,10,16,0,0,397,398,5,38,0,0,398,417,
        3,42,21,17,399,400,10,15,0,0,400,401,5,39,0,0,401,417,3,42,21,16,
        402,403,10,14,0,0,403,404,5,40,0,0,404,417,3,42,21,15,405,406,10,
        13,0,0,406,407,5,41,0,0,407,417,3,42,21,14,408,409,10,12,0,0,409,
        410,5,43,0,0,410,417,3,42,21,13,411,412,10,11,0,0,412,413,5,44,0,
        0,413,417,3,42,21,12,414,415,10,4,0,0,415,417,3,44,22,0,416,378,
        1,0,0,0,416,381,1,0,0,0,416,384,1,0,0,0,416,387,1,0,0,0,416,390,
        1,0,0,0,416,393,1,0,0,0,416,396,1,0,0,0,416,399,1,0,0,0,416,402,
        1,0,0,0,416,405,1,0,0,0,416,408,1,0,0,0,416,411,1,0,0,0,416,414,
        1,0,0,0,417,420,1,0,0,0,418,416,1,0,0,0,418,419,1,0,0,0,419,43,1,
        0,0,0,420,418,1,0,0,0,421,422,5,31,0,0,422,434,3,42,21,0,423,424,
        5,32,0,0,424,434,3,42,21,0,425,426,5,33,0,0,426,434,3,42,21,0,427,
        428,5,34,0,0,428,434,3,42,21,0,429,430,5,35,0,0,430,434,3,42,21,
        0,431,432,5,36,0,0,432,434,3,42,21,0,433,421,1,0,0,0,433,423,1,0,
        0,0,433,425,1,0,0,0,433,427,1,0,0,0,433,429,1,0,0,0,433,431,1,0,
        0,0,434,45,1,0,0,0,435,442,5,10,0,0,436,442,5,11,0,0,437,439,5,12,
        0,0,438,440,3,42,21,0,439,438,1,0,0,0,439,440,1,0,0,0,440,442,1,
        0,0,0,441,435,1,0,0,0,441,436,1,0,0,0,441,437,1,0,0,0,442,47,1,0,
        0,0,443,445,7,0,0,0,444,443,1,0,0,0,444,445,1,0,0,0,445,449,1,0,
        0,0,446,450,3,50,25,0,447,450,3,92,46,0,448,450,3,56,28,0,449,446,
        1,0,0,0,449,447,1,0,0,0,449,448,1,0,0,0,450,480,1,0,0,0,451,452,
        5,26,0,0,452,454,5,27,0,0,453,451,1,0,0,0,454,455,1,0,0,0,455,453,
        1,0,0,0,455,456,1,0,0,0,456,458,1,0,0,0,457,459,5,26,0,0,458,457,
        1,0,0,0,458,459,1,0,0,0,459,463,1,0,0,0,460,464,3,50,25,0,461,464,
        3,92,46,0,462,464,3,56,28,0,463,460,1,0,0,0,463,461,1,0,0,0,463,
        462,1,0,0,0,464,480,1,0,0,0,465,466,5,27,0,0,466,468,5,26,0,0,467,
        465,1,0,0,0,468,469,1,0,0,0,469,467,1,0,0,0,469,470,1,0,0,0,470,
        472,1,0,0,0,471,473,5,27,0,0,472,471,1,0,0,0,472,473,1,0,0,0,473,
        477,1,0,0,0,474,478,3,50,25,0,475,478,3,92,46,0,476,478,3,56,28,
        0,477,474,1,0,0,0,477,475,1,0,0,0,477,476,1,0,0,0,478,480,1,0,0,
        0,479,444,1,0,0,0,479,453,1,0,0,0,479,467,1,0,0,0,480,49,1,0,0,0,
        481,482,7,1,0,0,482,51,1,0,0,0,483,485,5,22,0,0,484,483,1,0,0,0,
        485,486,1,0,0,0,486,484,1,0,0,0,486,487,1,0,0,0,487,489,1,0,0,0,
        488,490,3,90,45,0,489,488,1,0,0,0,490,491,1,0,0,0,491,489,1,0,0,
        0,491,492,1,0,0,0,492,493,1,0,0,0,493,494,5,23,0,0,494,495,3,42,
        21,0,495,53,1,0,0,0,496,498,3,90,45,0,497,499,5,28,0,0,498,497,1,
        0,0,0,499,500,1,0,0,0,500,498,1,0,0,0,500,501,1,0,0,0,501,55,1,0,
        0,0,502,504,5,28,0,0,503,502,1,0,0,0,504,505,1,0,0,0,505,503,1,0,
        0,0,505,506,1,0,0,0,506,507,1,0,0,0,507,508,3,92,46,0,508,57,1,0,
        0,0,509,511,5,39,0,0,510,509,1,0,0,0,511,512,1,0,0,0,512,510,1,0,
        0,0,512,513,1,0,0,0,513,514,1,0,0,0,514,515,3,92,46,0,515,59,1,0,
        0,0,516,517,5,13,0,0,517,518,5,54,0,0,518,519,5,24,0,0,519,524,5,
        54,0,0,520,521,5,48,0,0,521,523,5,54,0,0,522,520,1,0,0,0,523,526,
        1,0,0,0,524,522,1,0,0,0,524,525,1,0,0,0,525,527,1,0,0,0,526,524,
        1,0,0,0,527,528,5,25,0,0,528,61,1,0,0,0,529,532,3,64,32,0,530,532,
        3,66,33,0,531,529,1,0,0,0,531,530,1,0,0,0,532,63,1,0,0,0,533,534,
        5,13,0,0,534,535,5,54,0,0,535,536,5,54,0,0,536,537,5,9,0,0,537,538,
        5,54,0,0,538,65,1,0,0,0,539,540,5,13,0,0,540,541,5,54,0,0,541,542,
        5,54,0,0,542,67,1,0,0,0,543,544,3,40,20,0,544,545,5,55,0,0,545,69,
        1,0,0,0,546,547,3,40,20,0,547,548,5,56,0,0,548,71,1,0,0,0,549,550,
        5,55,0,0,550,551,3,40,20,0,551,73,1,0,0,0,552,553,5,56,0,0,553,554,
        3,40,20,0,554,75,1,0,0,0,555,559,3,78,39,0,556,559,3,80,40,0,557,
        559,3,82,41,0,558,555,1,0,0,0,558,556,1,0,0,0,558,557,1,0,0,0,559,
        77,1,0,0,0,560,561,3,90,45,0,561,565,3,92,46,0,562,563,5,14,0,0,
        563,564,5,49,0,0,564,566,5,15,0,0,565,562,1,0,0,0,566,567,1,0,0,
        0,567,565,1,0,0,0,567,568,1,0,0,0,568,79,1,0,0,0,569,573,3,92,46,
        0,570,571,5,14,0,0,571,572,5,49,0,0,572,574,5,15,0,0,573,570,1,0,
        0,0,574,575,1,0,0,0,575,573,1,0,0,0,575,576,1,0,0,0,576,577,1,0,
        0,0,577,580,5,9,0,0,578,581,3,42,21,0,579,581,3,84,42,0,580,578,
        1,0,0,0,580,579,1,0,0,0,581,587,1,0,0,0,582,583,3,92,46,0,583,584,
        5,9,0,0,584,585,3,84,42,0,585,587,1,0,0,0,586,569,1,0,0,0,586,582,
        1,0,0,0,587,81,1,0,0,0,588,589,3,90,45,0,589,593,3,92,46,0,590,591,
        5,14,0,0,591,592,5,49,0,0,592,594,5,15,0,0,593,590,1,0,0,0,594,595,
        1,0,0,0,595,593,1,0,0,0,595,596,1,0,0,0,596,597,1,0,0,0,597,600,
        5,9,0,0,598,601,3,84,42,0,599,601,3,36,18,0,600,598,1,0,0,0,600,
        599,1,0,0,0,601,83,1,0,0,0,602,605,5,24,0,0,603,606,3,42,21,0,604,
        606,3,84,42,0,605,603,1,0,0,0,605,604,1,0,0,0,606,614,1,0,0,0,607,
        610,5,48,0,0,608,611,3,42,21,0,609,611,3,84,42,0,610,608,1,0,0,0,
        610,609,1,0,0,0,611,613,1,0,0,0,612,607,1,0,0,0,613,616,1,0,0,0,
        614,612,1,0,0,0,614,615,1,0,0,0,615,617,1,0,0,0,616,614,1,0,0,0,
        617,618,5,25,0,0,618,85,1,0,0,0,619,624,3,92,46,0,620,621,5,14,0,
        0,621,622,3,42,21,0,622,623,5,15,0,0,623,625,1,0,0,0,624,620,1,0,
        0,0,625,626,1,0,0,0,626,624,1,0,0,0,626,627,1,0,0,0,627,87,1,0,0,
        0,628,629,5,16,0,0,629,630,3,90,45,0,630,631,5,54,0,0,631,89,1,0,
        0,0,632,634,5,17,0,0,633,632,1,0,0,0,634,637,1,0,0,0,635,633,1,0,
        0,0,635,636,1,0,0,0,636,638,1,0,0,0,637,635,1,0,0,0,638,639,7,2,
        0,0,639,91,1,0,0,0,640,641,5,54,0,0,641,93,1,0,0,0,642,643,5,57,
        0,0,643,95,1,0,0,0,70,101,107,113,116,118,126,135,141,148,158,164,
        172,174,178,183,190,195,200,205,209,216,222,234,245,256,264,267,
        273,277,308,312,316,324,328,343,353,376,416,418,433,439,441,444,
        449,455,458,463,469,472,477,479,486,491,500,505,512,524,531,558,
        567,575,580,586,595,600,605,610,614,626,635
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'switch'", "'case'", "'default'", "'if'", 
                     "'else'", "'while'", "'for'", "'printf'", "'='", "'break'", 
                     "'continue'", "'return'", "'enum'", "'['", "']'", "'typedef'", 
                     "'const'", "'int'", "'float'", "'char'", "'void'", 
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
    RULE_arrayStatement = 38
    RULE_arrayDeclaration = 39
    RULE_arrayAssignment = 40
    RULE_arrayDefinition = 41
    RULE_array = 42
    RULE_arrayElement = 43
    RULE_typedef = 44
    RULE_type = 45
    RULE_identifier = 46
    RULE_comment = 47

    ruleNames =  [ "program", "scope", "statement", "function", "functionParams", 
                   "functionCall", "callParams", "switchStatement", "switchCase", 
                   "conditional", "ifStatement", "elseIfStatement", "elseStatement", 
                   "whileLoop", "forLoop", "forCondition", "printfStatement", 
                   "formatSpecifier", "string", "variable", "lvalue", "rvalue", 
                   "conditionalExpression", "jumpStatement", "unaryExpression", 
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
            self.state = 116 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 96
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 97
                    self.enumDeclaration()
                    self.state = 99 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 98
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 101 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==47):
                            break

                    pass

                elif la_ == 3:
                    self.state = 103
                    self.variable()
                    self.state = 105 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 104
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 107 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==47):
                            break

                    pass

                elif la_ == 4:
                    self.state = 109
                    self.typedef()
                    self.state = 111 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 110
                        self.match(GrammarParser.SEMICOLON)
                        self.state = 113 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==47):
                            break

                    pass

                elif la_ == 5:
                    self.state = 115
                    self.function()
                    pass


                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 162129586857910272) != 0)):
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
            self.state = 122
            self.match(GrammarParser.LBRACE)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274196759985470930) != 0):
                self.state = 123
                self.statement()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
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


        def arrayStatement(self):
            return self.getTypedRuleContext(GrammarParser.ArrayStatementContext,0)


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
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.rvalue(0)
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 132
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 135 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.variable()
                self.state = 139 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 138
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 141 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.comment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.printfStatement()
                self.state = 146 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 145
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 148 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.scope()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 152
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 153
                self.forLoop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 154
                self.enumStatement()
                self.state = 156 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 155
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 158 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 160
                self.jumpStatement()
                self.state = 162 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 161
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 164 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
                        break

                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 166
                self.function()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 167
                self.switchStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 168
                self.arrayStatement()
                self.state = 170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 169
                    self.match(GrammarParser.SEMICOLON)
                    self.state = 172 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==47):
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
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 176
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 177
                    self.pointer()
                    pass


                self.state = 180
                self.match(GrammarParser.IDENTIFIER)
                self.state = 181
                self.match(GrammarParser.LPAREN)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398513545216) != 0):
                    self.state = 182
                    self.functionParams(0)


                self.state = 185
                self.match(GrammarParser.RPAREN)
                self.state = 186
                self.scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 188
                    self.type_()
                    pass

                elif la_ == 2:
                    self.state = 189
                    self.pointer()
                    pass


                self.state = 192
                self.match(GrammarParser.IDENTIFIER)
                self.state = 193
                self.match(GrammarParser.LPAREN)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398513545216) != 0):
                    self.state = 194
                    self.functionParams(0)


                self.state = 197
                self.match(GrammarParser.RPAREN)
                self.state = 198
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
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 203
                self.pointer()
                pass

            elif la_ == 2:
                self.state = 204
                self.type_()
                pass


            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 207
                self.addr()
                pass
            elif token in [54]:
                self.state = 208
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.FunctionParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParams)
                    self.state = 211
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 212
                    self.match(GrammarParser.COMMA)
                    self.state = 213
                    self.functionParams(2) 
                self.state = 218
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
            self.state = 219
            self.match(GrammarParser.IDENTIFIER)
            self.state = 220
            self.match(GrammarParser.LPAREN)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130081571892763648) != 0):
                self.state = 221
                self.callParams(0)


            self.state = 224
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
            self.state = 227
            self.rvalue(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CallParamsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callParams)
                    self.state = 229
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 230
                    self.match(GrammarParser.COMMA)
                    self.state = 231
                    self.callParams(2) 
                self.state = 236
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
            self.state = 237
            self.match(GrammarParser.T__0)
            self.state = 238
            self.match(GrammarParser.LPAREN)
            self.state = 239
            self.rvalue(0)
            self.state = 240
            self.match(GrammarParser.RPAREN)
            self.state = 241
            self.match(GrammarParser.LBRACE)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 242
                self.switchCase()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 248
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
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(GrammarParser.T__1)
                self.state = 251
                self.literal()
                self.state = 252
                self.match(GrammarParser.COLON)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274196759985470930) != 0):
                    self.state = 253
                    self.statement()
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(GrammarParser.T__2)
                self.state = 260
                self.match(GrammarParser.COLON)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274196759985470930) != 0):
                    self.state = 261
                    self.statement()
                    self.state = 266
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
            self.state = 269
            self.ifStatement()
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 270
                    self.elseIfStatement() 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 276
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
            self.state = 279
            self.match(GrammarParser.T__3)
            self.state = 280
            self.match(GrammarParser.LPAREN)
            self.state = 281
            self.rvalue(0)
            self.state = 282
            self.match(GrammarParser.RPAREN)
            self.state = 283
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
            self.state = 285
            self.match(GrammarParser.T__4)
            self.state = 286
            self.match(GrammarParser.T__3)
            self.state = 287
            self.match(GrammarParser.LPAREN)
            self.state = 288
            self.rvalue(0)
            self.state = 289
            self.match(GrammarParser.RPAREN)
            self.state = 290
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
            self.state = 292
            self.match(GrammarParser.T__4)
            self.state = 293
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
            self.state = 295
            self.match(GrammarParser.T__5)
            self.state = 296
            self.match(GrammarParser.LPAREN)
            self.state = 297
            self.rvalue(0)
            self.state = 298
            self.match(GrammarParser.RPAREN)
            self.state = 299
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
            self.state = 301
            self.match(GrammarParser.T__6)
            self.state = 302
            self.match(GrammarParser.LPAREN)
            self.state = 303
            self.forCondition()
            self.state = 304
            self.match(GrammarParser.RPAREN)
            self.state = 305
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
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398782046208) != 0):
                self.state = 307
                self.variable()


            self.state = 310
            self.match(GrammarParser.SEMICOLON)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130081571892763648) != 0):
                self.state = 311
                self.rvalue(0)


            self.state = 314
            self.match(GrammarParser.SEMICOLON)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130081571892763648) != 0):
                self.state = 315
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
            self.state = 318
            self.match(GrammarParser.T__7)
            self.state = 319
            self.match(GrammarParser.LPAREN)
            self.state = 320
            self.formatSpecifier()
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 321
                self.match(GrammarParser.COMMA)
                self.state = 324
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 11, 12, 17, 18, 19, 20, 21, 22, 26, 27, 28, 39, 42, 45, 49, 50, 51, 54, 55, 56]:
                    self.state = 322
                    self.rvalue(0)
                    pass
                elif token in [52]:
                    self.state = 323
                    self.string()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 331
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
            self.state = 333
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
            self.state = 335
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
        self.enterRule(localctx, 38, self.RULE_variable)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.lvalue()
                self.state = 338
                self.match(GrammarParser.T__8)
                self.state = 339
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.lvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 342
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
        self.enterRule(localctx, 40, self.RULE_lvalue)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.type_()
                self.state = 347
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.pointer()
                self.state = 350
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 352
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


        def arrayElement(self):
            return self.getTypedRuleContext(GrammarParser.ArrayElementContext,0)


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
            self.state = 376
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
                self.rvalue(24)
                pass

            elif la_ == 6:
                self.state = 362
                self.match(GrammarParser.BITWISE_NOT)
                self.state = 363
                self.rvalue(23)
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


            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 416
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 378
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 379
                        self.match(GrammarParser.DIV)
                        self.state = 380
                        self.rvalue(23)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 381
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 382
                        self.match(GrammarParser.MOD)
                        self.state = 383
                        self.rvalue(22)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 384
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 385
                        self.match(GrammarParser.MULT)
                        self.state = 386
                        self.rvalue(21)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 387
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 388
                        self.match(GrammarParser.MINUS)
                        self.state = 389
                        self.rvalue(20)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 390
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 391
                        self.match(GrammarParser.PLUS)
                        self.state = 392
                        self.rvalue(19)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 393
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 394
                        self.match(GrammarParser.SHIFT_LEFT)
                        self.state = 395
                        self.rvalue(18)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 396
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 397
                        self.match(GrammarParser.SHIFT_RIGHT)
                        self.state = 398
                        self.rvalue(17)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 399
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 400
                        self.match(GrammarParser.BITWISE_AND)
                        self.state = 401
                        self.rvalue(16)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 402
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 403
                        self.match(GrammarParser.BITWISE_OR)
                        self.state = 404
                        self.rvalue(15)
                        pass

                    elif la_ == 10:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 405
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 406
                        self.match(GrammarParser.BITWISE_XOR)
                        self.state = 407
                        self.rvalue(14)
                        pass

                    elif la_ == 11:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 408
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 409
                        self.match(GrammarParser.LOGICAL_AND)
                        self.state = 410
                        self.rvalue(13)
                        pass

                    elif la_ == 12:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 411
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 412
                        self.match(GrammarParser.LOGICAL_OR)
                        self.state = 413
                        self.rvalue(12)
                        pass

                    elif la_ == 13:
                        localctx = GrammarParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 414
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 415
                        self.conditionalExpression()
                        pass

             
                self.state = 420
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
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(GrammarParser.GREATER_THAN)
                self.state = 422
                self.rvalue(0)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.match(GrammarParser.LESS_THAN)
                self.state = 424
                self.rvalue(0)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.match(GrammarParser.GREATER_EQUAL)
                self.state = 426
                self.rvalue(0)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
                self.match(GrammarParser.LESS_EQUAL)
                self.state = 428
                self.rvalue(0)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 5)
                self.state = 429
                self.match(GrammarParser.EQUALS)
                self.state = 430
                self.rvalue(0)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 6)
                self.state = 431
                self.match(GrammarParser.NOT_EQUAL)
                self.state = 432
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
            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(GrammarParser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.match(GrammarParser.T__10)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(GrammarParser.T__11)
                self.state = 439
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 438
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
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26 or _la==27:
                    self.state = 443
                    _la = self._input.LA(1)
                    if not(_la==26 or _la==27):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 449
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [49, 50, 51]:
                    self.state = 446
                    self.literal()
                    pass
                elif token in [54]:
                    self.state = 447
                    self.identifier()
                    pass
                elif token in [28]:
                    self.state = 448
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 451
                        self.match(GrammarParser.PLUS)
                        self.state = 452
                        self.match(GrammarParser.MINUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 455 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 457
                    self.match(GrammarParser.PLUS)


                self.state = 463
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [49, 50, 51]:
                    self.state = 460
                    self.literal()
                    pass
                elif token in [54]:
                    self.state = 461
                    self.identifier()
                    pass
                elif token in [28]:
                    self.state = 462
                    self.deref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 467 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 465
                        self.match(GrammarParser.MINUS)
                        self.state = 466
                        self.match(GrammarParser.PLUS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 469 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

                self.state = 472
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 471
                    self.match(GrammarParser.MINUS)


                self.state = 477
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [49, 50, 51]:
                    self.state = 474
                    self.literal()
                    pass
                elif token in [54]:
                    self.state = 475
                    self.identifier()
                    pass
                elif token in [28]:
                    self.state = 476
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
            self.state = 481
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
            self.state = 484 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 483
                self.match(GrammarParser.LPAREN)
                self.state = 486 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 489 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 488
                self.type_()
                self.state = 491 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398513545216) != 0)):
                    break

            self.state = 493
            self.match(GrammarParser.RPAREN)
            self.state = 494
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
            self.state = 496
            self.type_()
            self.state = 498 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 497
                self.match(GrammarParser.MULT)
                self.state = 500 
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
            self.state = 503 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 502
                self.match(GrammarParser.MULT)
                self.state = 505 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==28):
                    break

            self.state = 507
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
            self.state = 510 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 509
                self.match(GrammarParser.BITWISE_AND)
                self.state = 512 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 514
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
            self.state = 516
            self.match(GrammarParser.T__12)
            self.state = 517
            self.match(GrammarParser.IDENTIFIER)
            self.state = 518
            self.match(GrammarParser.LBRACE)
            self.state = 519
            self.match(GrammarParser.IDENTIFIER)
            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 520
                self.match(GrammarParser.COMMA)
                self.state = 521
                self.match(GrammarParser.IDENTIFIER)
                self.state = 526
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 527
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
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.enumVariableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
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
            self.state = 533
            self.match(GrammarParser.T__12)
            self.state = 534
            self.match(GrammarParser.IDENTIFIER)
            self.state = 535
            self.match(GrammarParser.IDENTIFIER)
            self.state = 536
            self.match(GrammarParser.T__8)
            self.state = 537
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
            self.state = 539
            self.match(GrammarParser.T__12)
            self.state = 540
            self.match(GrammarParser.IDENTIFIER)
            self.state = 541
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
            self.state = 543
            self.lvalue()
            self.state = 544
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
            self.state = 546
            self.lvalue()
            self.state = 547
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
            self.state = 549
            self.match(GrammarParser.INCREMENT)
            self.state = 550
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
            self.state = 552
            self.match(GrammarParser.DECREMENT)
            self.state = 553
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
        self.enterRule(localctx, 76, self.RULE_arrayStatement)
        try:
            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.arrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.arrayAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 557
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
        self.enterRule(localctx, 78, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.type_()
            self.state = 561
            self.identifier()
            self.state = 565 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 562
                self.match(GrammarParser.T__13)
                self.state = 563
                self.match(GrammarParser.INT)
                self.state = 564
                self.match(GrammarParser.T__14)
                self.state = 567 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
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
        self.enterRule(localctx, 80, self.RULE_arrayAssignment)
        self._la = 0 # Token type
        try:
            self.state = 586
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 569
                self.identifier()
                self.state = 573 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 570
                    self.match(GrammarParser.T__13)
                    self.state = 571
                    self.match(GrammarParser.INT)
                    self.state = 572
                    self.match(GrammarParser.T__14)
                    self.state = 575 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==14):
                        break

                self.state = 577
                self.match(GrammarParser.T__8)
                self.state = 580
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 11, 12, 17, 18, 19, 20, 21, 22, 26, 27, 28, 39, 42, 45, 49, 50, 51, 54, 55, 56]:
                    self.state = 578
                    self.rvalue(0)
                    pass
                elif token in [24]:
                    self.state = 579
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.identifier()
                self.state = 583
                self.match(GrammarParser.T__8)
                self.state = 584
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
        self.enterRule(localctx, 82, self.RULE_arrayDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.type_()
            self.state = 589
            self.identifier()
            self.state = 593 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 590
                self.match(GrammarParser.T__13)
                self.state = 591
                self.match(GrammarParser.INT)
                self.state = 592
                self.match(GrammarParser.T__14)
                self.state = 595 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 597
            self.match(GrammarParser.T__8)
            self.state = 600
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 598
                self.array()
                pass
            elif token in [52]:
                self.state = 599
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
        self.enterRule(localctx, 84, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(GrammarParser.LBRACE)
            self.state = 605
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 17, 18, 19, 20, 21, 22, 26, 27, 28, 39, 42, 45, 49, 50, 51, 54, 55, 56]:
                self.state = 603
                self.rvalue(0)
                pass
            elif token in [24]:
                self.state = 604
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 614
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 607
                self.match(GrammarParser.COMMA)
                self.state = 610
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 11, 12, 17, 18, 19, 20, 21, 22, 26, 27, 28, 39, 42, 45, 49, 50, 51, 54, 55, 56]:
                    self.state = 608
                    self.rvalue(0)
                    pass
                elif token in [24]:
                    self.state = 609
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 616
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 617
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
        self.enterRule(localctx, 86, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.identifier()
            self.state = 624 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 620
                    self.match(GrammarParser.T__13)
                    self.state = 621
                    self.rvalue(0)
                    self.state = 622
                    self.match(GrammarParser.T__14)

                else:
                    raise NoViableAltException(self)
                self.state = 626 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self.match(GrammarParser.T__15)
            self.state = 629
            self.type_()
            self.state = 630
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
        self.enterRule(localctx, 90, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 632
                self.match(GrammarParser.T__16)
                self.state = 637
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 638
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398513414144) != 0)):
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
        self.enterRule(localctx, 92, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
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
        self.enterRule(localctx, 94, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
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
                return self.precpred(self._ctx, 22)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 4)
         




