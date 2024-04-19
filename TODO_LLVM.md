# project 1

- [x] (**mandatory**) Binary operations +, -, *, and /.
- [x] (**mandatory**) Binary operations >, <, and ==.
- [x] (**mandatory**) Unary operators + and -.
- [x] (**mandatory**) Parenthesis to overwrite the order of operations.
- [x] (**mandatory**) Logical operators &&, ||, and !.
- [x] (**mandatory**) Comparison operators >=, <=, and !=.
- [x] (**mandatory**) Binary operator %.
- [x] (**mandatory**) Shift operators <<, >>.
- [x] (**mandatory**) Bitwise operators &, |, ~, and ^.

# project 2

- [x] (**mandatory**) Add an int main() { ... } function
- [x] (**mandatory**) Extra reserved keywords need to be supported: const, char, int, and float.
- [x] (**mandatory**) Literals are now no longer limited to integers: literals of any type (integer, floating point,
  character) can now be part of expressions
- [x] (**mandatory**) Variables
- [x] (**mandatory**) Pointers
- [x] (**mandatory**) Constants
- [x] (**mandatory**) Implicit conversions warnings
- [x] (**mandatory**) Explicit conversions
- [ ] (**mandatory**) Pointer arithmetic
- [x] (**mandatory**) Increment/Decrement Operations
- [x] (**optional**) Const casting

# project 3

- [x] (**mandatory**) Single line comments
- [x] (**mandatory**) Multi line comments
- [x] (**mandatory**) Output printf
- [x] (**mandatory**) Typedef support
- [x] (**mandatory**) LLVM definitions
- [x] (**mandatory**) LLVM pointers
- [x] (**mandatory**) LLVM comments

# project 4

- [x] (**mandatory**) Conditional statements
- [x] (**optional**) Else if statements
- [ ] (**mandatory**) Loops
- [ ] (**mandatory**) Anonymous scopes
- [ ] (**mandatory**) Switch statements
- [ ] (**mandatory**) Enumerations

# project 5

- Functionality
  - [ ] (**mandatory**) Function scopes
  - [ ] (**mandatory**) Local and global variables
  - [ ] (**mandatory**) Functions
    - [ ] Defining functions
    - [ ] Calling functions
    - [ ] Function arguments (basic types, pointers, constness, pass-by-value and pass-by-reference)
    - [ ] Return values
    - [ ] Void function
    - [ ] Missing main -> error.
  - [ ] (**optional**) Overloading of functions on the amount and type of parameters
  - [ ] (**mandatory**) Define `#define` 
  - [ ] (**mandatory**) Includes `#include`
  - [ ] (**optional**) Include guards `#ifdef`, `#ifndef`, `#endif`
- Semantic Analysis
  - [ ] (**mandatory**) Function scopes in symbol table
  - [ ] (**mandatory**) Check consistency of return type
  - [ ] (**mandatory**) Check consistency of function arguments
  - [ ] (**mandatory**) Functions can only be called if they are declared/defined earlier
  - [ ] (**mandatory**) Check redefinitions of functions (headers too)
  - [ ] (**optional**) All paths in function body end in return statement (except void functions)
- Optimizations
  - [ ] (**mandatory**) Do not generate code after return statement
  - [ ] (**mandatory**) Do not generate code after continue/break statement
  - [ ] (**mandatory**) Do not generate code for unused variables
  - [ ] (**mandatory**) Do not generate code for conditionals that are never true

# project 6

- Functionality
  - [ ] (**mandatory**) Arrays
  - [ ] (**mandatory**) Multi-dimensional arrays
  - [ ] (**mandatory**) Assignment of complete arrays or array rows
  - [ ] (**mandatory**) Array initialization
  - [ ] (**optional**) Dynamic arrays
  - [ ] (**mandatory**) C-strings
  - [ ] (**mandatory**) Including stdio.h
- Semantical Analysis
  - [ ] (**mandatory**) Type checking arrays
  - [ ] (**mandatory**) Type of specified index is int when accessing arrays
  - [ ] (**mandatory**) When assigning array initializers check that the length matches the array

# project 7

- Functionality
  - [ ] (**mandatory**) Structs
  - [ ] (**optional**) Structs containing other structs
  - [ ] (**optional**) Dynamic allocation of structs
  - [ ] (**optional**) Unions
  - [ ] (**optional**) Function pointers
  - [ ] (**optional**) File reading using fgets
  - [ ] (**optional**) File writing using fputs
  - [ ] (**optional**) Dynamically allocated strings and charracter buffers
- Semantic Analysis
  - [ ] (**optional**) Type checking for function pointers
  - [ ] (**mandatory**) Type checking for accessing and assigning struct members
  - [ ] (**optional**) Type checking for accessing and assigning union members