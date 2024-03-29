#!/bin/bash
echo "What Project are you working on?"
read proj
reg='^[0-9]+$'
if [[ $proj == $reg ]]; then
    echo "Project name must be an integer"
    exit 1
fi
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 grammars/Grammar_Project_${proj}.g4 -visitor
mv grammars/*.py src/antlr_files/Proj_$proj/
mv grammars/*.interp src/antlr_files/Proj_$proj/
mv grammars/*.tokens src/antlr_files/Proj_$proj/