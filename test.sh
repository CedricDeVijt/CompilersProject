#!/bin/bash

# Define the paths for rendering AST and symbol table, and compiling to LLVM and MIPS
MAIN_SCRIPT="python -m src.main"
OUTPUT_DIR="output"
INPUT_DIR="tests/extra_tests"  # Default input directory

# Create and activate Python 3 virtual environment
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt

# Array to store errors
ERRORS=()
FAILED_TESTS=()
SUCCESS_STRING=""
UNSUCCESSFUL_TESTS=0
SUCCESSFUL_TESTS=0

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
    echo "Processing $input_file"
    #
    $MAIN_SCRIPT --input "$input_file" --render_ast "$ast_output" &> /dev/null

    # if output file exists, then the rendering was successful
    if [ -f "$ast_output" ]; then
        SUCCESS_STRING+="."
        ((SUCCESSFUL_TESTS++))
    else
        ERRORS+=("$input_file: rendering AST failed")
        FAILED_TESTS+=("$input_file")
        SUCCESS_STRING+="F"
        ((UNSUCCESSFUL_TESTS++))
    fi

    # Add code to handle other tasks like rendering symbol table, compiling to LLVM, compiling to MIPS
}

# Recursive function to process files in a directory or a single file
process_directory() {
    local path="$1"
    if [ -d "$path" ]; then
        for file in "$path"/*; do
            if [ -f "$file" ] && [[ "$file" == *.c ]]; then
                process_file "$file"
            elif [ -d "$file" ]; then
                process_directory "$file"
            fi
        done
    elif [ -f "$path" ]; then
        if [[ "$path" == *.c ]]; then
            process_file "$path"
        fi
    fi
}

# Parse command-line options
while getopts i: flag; do
    case "${flag}" in
        i) INPUT_DIR=${OPTARG};;
    esac
done

# remove the output directory if it exists with files in
if [ -d "$OUTPUT_DIR" ]; then
    rm -r "$OUTPUT_DIR"
fi


# Start processing from the input directory
process_directory "$INPUT_DIR"

# Calculate total tests
TOTAL_TESTS=$((SUCCESSFUL_TESTS + UNSUCCESSFUL_TESTS))

# Get the width of the terminal
TERMINAL_WIDTH=$(tput cols)


echo ""
echo "collected $TOTAL_TESTS items"

# Print individual test results
echo $SUCCESS_STRING

# Print summary
echo ""
echo " $(printf '=%.0s' $(seq 1 $((TERMINAL_WIDTH/2 - ${#SUCCESSFUL_TESTS} - ${#UNSUCCESSFUL_TESTS} - 8)))) $SUCCESSFUL_TESTS passed, $UNSUCCESSFUL_TESTS failed $(printf '=%.0s' $(seq 1 $((TERMINAL_WIDTH/2 - ${#SUCCESSFUL_TESTS} - ${#UNSUCCESSFUL_TESTS} - 8))))"
echo ""

# Print paths of failed tests
if [ "$UNSUCCESSFUL_TESTS" -gt 0 ]; then
    echo "Failed Tests:"
    for ((i = 0; i < ${#FAILED_TESTS[@]}; i++)); do
        echo "${FAILED_TESTS[$i]}"
    done
fi
