import os
import sys

import antlr4
from antlr4.error.ErrorListener import ErrorListener

from src.llvm_target.toLLVM import generateLLVMcodePython
from src.llvm_target.toLLVM import generateLLVMcodeLite
from src.antlr_files.GrammarLexer import GrammarLexer as Lexer
from src.antlr_files.GrammarParser import GrammarParser as Parser
from src.parser.ASTGenerator import ASTGenerator as Generator
from src.parser.dotGenerator import DotGenerator


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Syntax error at line {line}:{column}")


def pre_processing(path, stdio_found=None):
    if stdio_found is None:
        stdio_found = [False]
    with open(path, 'r') as file:
        lines = file.readlines()
    macros = []
    for line in lines:
        if line.startswith("#include"):
            # Split in words.
            words = line.split()
            if len(words) == 1:
                raise Exception("#include expects \"FILENAME\" or <FILENAME>!")
            if len(words) > 2:
                raise Exception('extra tokens at end of #include directive!')
            if not ((words[1].startswith('\"') and words[1].endswith('\"')) or (words[1].startswith('<') and words[1].endswith('>'))):
                raise Exception("#include expects \"FILENAME\" or <FILENAME>!")
            if words[1] == '<stdio.h>':
                stdio_found[0] = True
                macros.append(line)
                continue
            # Check if file exists.
            if not os.path.exists(words[1][1:-1]):
                raise Exception(f"File {words[1][1:-1]} not found.")
            # Read file.
            file_lines = pre_processing(path=words[1][1:-1], stdio_found=stdio_found)
            # Insert file content.
            index = lines.index(line) + 1
            for file_line in file_lines:
                lines.insert(index, file_line)
                index += 1
            # Add include to removal
            macros.append(line)
    for line in lines:
        if 'printf(' in line or 'scanf(' in line:
            if not stdio_found[0]:
                raise Exception("<stdio.h> not included.")
    for macro in macros:
        lines.remove(macro)
    return lines


def generate_ast(path, visitor):
    # Preprocessor
    new_code = pre_processing(path)
    # Save new code to file
    new_path = 'temp.c'
    i = 2
    while os.path.exists(new_path):
        new_path = f'temp_{i}.c'
        i += 1
    with open(new_path, 'w') as file:
        file.writelines(new_code)

    # Generate CST
    input_stream = antlr4.FileStream(new_path)
    os.remove(new_path)
    lexer = Lexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = Parser(stream)
    parser.addErrorListener(ThrowingErrorListener())
    tree = parser.program()

    # Generate AST
    genAST = visitor.visit(tree)

    ast = genAST.node
    symbolTable = genAST.scope
    errors = genAST.errors
    warnings = genAST.warnings
    # Print Warnings
    for warning in warnings:
        print(f"Warning: {warning}")
    ast.constantFold(errors=errors, warnings=warnings)
    # Print Errors
    err_str = ''
    if not genAST.has_main:
        err_str += "Error: No main function found!"
    for error in errors:
        err_str += f"\nError at {error}"
    if err_str != '':
        print(err_str)
        return None, None
    return ast, symbolTable


def compile_llvm(input_file, visitor, output_file):
    ast, symbol_table = generate_ast(input_file, visitor)
    if ast is None:
        print("Failed to generate AST.")
        return

    # Open a file to write LLVM code
    with open('src/llvm_target/output.ll', 'w') as llvm_file:
        # Write LLVM header
        llvm_file.write(f"; ModuleID = '{output_file}'\n")
        llvm_file.write(f"source_filename = \"{output_file}\"\n")
        llvm_file.write("\n")

        generateLLVMcodeLite(ast, llvm_file)


def compile_mips(input_file, visitor, output_file):
    # Implement MIPS compilation
    pass


def render_ast(input_file, output_file):
    ast, _ = generate_ast(input_file, Generator())
    if ast is not None:
        DotGenerator.generateASTDot(AST_tree=ast, output_filename=output_file)


def render_ast_png(input_file, output_file):
    ast, _ = generate_ast(input_file, Generator())
    if ast is not None:
        DotGenerator.generateASTDot(AST_tree=ast, output_filename=output_file, format='png')


def render_symbol_table(input_file, output_file):
    _, symbol_table = generate_ast(input_file, Generator())
    if symbol_table is not None:
        DotGenerator.generateSymbolTableDot(symbol_table, output_file, format='dot')


def render_symbol_table_png(input_file, output_file):
    _, symbol_table = generate_ast(input_file, Generator())
    if symbol_table is not None:
        DotGenerator.generateSymbolTableDot(symbol_table, output_file, format='png')


def run(args):
    if args.input:
        if args.render_ast:
            render_ast(args.input, args.render_ast)
        elif args.render_ast_png:
            render_ast_png(args.input, args.render_ast_png)
        elif args.render_symb:
            render_symbol_table(args.input, args.render_symb)
        elif args.render_symb_png:
            render_symbol_table_png(args.input, args.render_symb_png)
        elif args.target_llvm:
            compile_llvm(args.input, Generator(), args.target_llvm)
        elif args.target_mips:
            compile_mips(args.input, Generator(), args.target_mips)
    else:
        print("No input file provided.")


def main(argv):
    import argparse

    parser = argparse.ArgumentParser(description="Your program description here")
    parser.add_argument("--input", help="Input C file")
    parser.add_argument("--render_ast", help="Render AST to DOT file")
    parser.add_argument("--render_ast_png", help="Render AST to DOT png file")
    parser.add_argument("--render_symb", help="Render symbol table to DOT file")
    parser.add_argument("--render_symb_png", help="Render symbol table to DOT file")
    parser.add_argument("--target_llvm", help="Compile to LLVM output file")
    parser.add_argument("--target_mips", help="Compile to MIPS output file")
    args = parser.parse_args(argv[1:])

    run(args)


if __name__ == '__main__':
    main(sys.argv)
