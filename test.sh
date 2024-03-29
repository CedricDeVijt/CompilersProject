#!/bin/bash

# Define the paths for rendering AST and symbol table, and compiling to LLVM and MIPS
MAIN_SCRIPT="python -m src.main"
INPUT_DIR="tests"
OUTPUT_DIR="output"

# Function to perform all steps for each input file
process_file() {
    input_file="$1"
    filename=$(basename -- "$input_file")
    filename_without_extension="${filename%.*}"
    ast_output="$OUTPUT_DIR/${filename_without_extension}_ast.dot"
    symb_output="$OUTPUT_DIR/${filename_without_extension}_symb.dot"
    llvm_output="$OUTPUT_DIR/${filename_without_extension}.ll"
    mips_output="$OUTPUT_DIR/${filename_without_extension}.mips"

    # Rendering the AST
    $MAIN_SCRIPT --input "$input_file" --render_ast "$ast_output"

    # Rendering the symbol table
    $MAIN_SCRIPT --input "$input_file" --render_symb "$symb_output"

    # Compile to LLVM
    $MAIN_SCRIPT --input "$input_file" --target_llvm "$llvm_output"

    # Compile to MIPS
    $MAIN_SCRIPT --input "$input_file" --target_mips "$mips_output"
}

# Loop through all test files and process each one
for input_file in $INPUT_DIR/*; do
    if [ -f "$input_file" ]; then
        echo "Processing $input_file"
        process_file "$input_file"
        echo "Finished processing $input_file"
        echo
    fi
done
