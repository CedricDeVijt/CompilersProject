# Compiler Project Team 12

## Team Members

- Cedric De Vijt
- Robbe Stuer
- Thomas Urkens

## Project Description

This project is a compiler for a language called `C`. The compiler is written in python and generates MIPS assembly
code. The compiler is able to parse the input code, generate an abstract syntax tree (AST), perform semantic analysis,
generate intermediate code, and generate MIPS assembly code. The compiler is able to handle the following features:

- Binary operations +, -, *, and /.
- Binary operations >, <, and ==.
- Unary operators + and -.
- Parenthesis to overwrite the order of operations.
- Logical operators &&, ||, and !.
- Comparison operators >=, <=, and !=.
- Binary operator %.
- Shift operators <<, >>.
- Bitwise operators &, |, ~, and ^.
- Add an int main() { ... } function
- Extra reserved keywords need to be supported: const, char, int, and float.
- Literals are now no longer limited to integers: literals of any type (integer, floating point, character) can now be
  part of expressions
- Variables
- Pointers
- Constants
- Explicit conversions
- Implicit conversions of a richer to a poorer type should cause a compiler warning indicating possible loss of
  information.
- Single line comments
- Multi line comments
- Output printf
- Typedef support

## Project Structure

The project is structured as follows:

- `src/` contains the source code for the compiler
- `tests/` contains the test cases for the compiler
- `test.sh` is a shell script that runs all the tests
- `README.md` contains the project description and team members
- `TODO.md` contains the requirements for the project
- `COMPILER.md` contains information on how to run the compiler

## How to Run the Compiler

To run the compiler, follow the steps below:

- Rendering the AST:
  `python -m src.main --input input_file.c --render_ast ast_output.dot`
- - Rendering the AST as png:
  `python -m src.main --input input_file.c --render_ast_png ast_output.dot`
- Rendering the symbol table:
  `python -m src.main --input input_file.c --render_symb symb_output.dot`
- Rendering the symbol table as png:
  `python -m src.main --input input_file.c --render_symb_png symb_output.dot`
- Compile to LLVM:
  `python -m src.main --input input_file.c --target_llvm output_file.ll`
- Compile to MIPS:
  `python -m src.main --input input_file.c --target_mips output_file.mips`

## How to Run the Tests

To run the tests, follow the steps below:

1. Run the shell script by running `./test.sh`

The shell script will run all the tests in the `tests/` directory and print the results to the console. The tests from
project 1 are modified to be compatible with the compiler.

## Conclusion

Overall, the compiler project was a challenging but rewarding experience. We learned a lot about compilers, parsing, and
code generation. We were able to implement most of the features specified in the project requirements and generate
correct assembly code for simple C programs. We hope to continue working on the compiler and improve its functionality
in the future. We would like to thank the professors for their guidance and support throughout the project.