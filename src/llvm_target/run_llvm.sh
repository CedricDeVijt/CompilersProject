#!/bin/bash

# Check if the input file exists
if [ ! -f "output_file.ll" ]; then
    echo "Error: output_file.ll does not exist."
    exit 1
fi

# Compile the LLVM IR file to an executable
clang output_file.ll -o testExe

# Check if the compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful, running the program..."
    ./testExe
else
    echo "Compilation failed."
    exit 1
fi
