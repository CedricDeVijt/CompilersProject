#!/bin/bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 grammars/Grammar.g4 -visitor
mv grammars/*.py src/antlr_files/Proj_$proj/
mv grammars/*.interp src/antlr_files/
mv grammars/*.tokens src/antlr_files/