#!/bin/bash

# Define the paths for rendering AST and symbol table, and compiling to LLVM and MIPS
MAIN_SCRIPT="python -m src.main"
OUTPUT_DIR="output"
INPUT_DIR="tests"  # Default input directory

# Create and activate Python 3 virtual environment
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt

# Function to process each input file
process_file() {
    input_file="$1"
    filename=$(basename -- "$input_file")
    filename_without_extension="${filename%.*}"
    ast_output="$OUTPUT_DIR/${filename_without_extension}_ast.dot"
    symb_output="$OUTPUT_DIR/${filename_without_extension}_symb.dot"
    llvm_output="$OUTPUT_DIR/${filename_without_extension}.ll"
    mips_output="$OUTPUT_DIR/${filename_without_extension}.mips"

    # Rendering the AST
    $MAIN_SCRIPT --input "$input_file" --render_ast_png "$ast_output"

#    # Rendering the symbol table
#    $MAIN_SCRIPT --input "$input_file" --render_symb "$symb_output"
#
#    # Compile to LLVM
#    $MAIN_SCRIPT --input "$input_file" --target_llvm "$llvm_output"
#
#    # Compile to MIPS
#    $MAIN_SCRIPT --input "$input_file" --target_mips "$mips_output"
}

# Recursive function to process files in a directory
process_directory() {
    local dir="$1"
    for file in "$dir"/*; do
        if [ -f "$file" ]; then
            echo "Processing $file"
            process_file "$file"
            echo "Finished processing $file"
            echo
        elif [ -d "$file" ]; then
            process_directory "$file"
        fi
    done
}


# Parse command-line options
while getopts i: flag
do
    # shellcheck disable=SC2220
    case "${flag}" in
        i) INPUT_DIR=${OPTARG};;
    esac
done

# Start processing from the input directory
process_directory "$INPUT_DIR"