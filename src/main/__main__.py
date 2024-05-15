import os
import sys

import antlr4
from antlr4.error.ErrorListener import ErrorListener

from src.antlr_files.GrammarLexer import GrammarLexer as Lexer
from src.antlr_files.GrammarParser import GrammarParser as Parser
from src.llvm_target.LLVMGenerator import LLVMVisitor
from src.mips_target.MIPSGenerator import MIPSVisitor
from src.parser.ASTGenerator import ASTGenerator as Generator
from src.parser.dotGenerator import DotGenerator
from src.parser.preprocessor import pre_processing


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Syntax error at line {line}:{column}")


def generate_ast(path, visitor, constant_fold=True):
    # Preprocessor
    stdio_found = [False]
    new_code = pre_processing(path, stdio_found)
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

    # Print Errors
    err_str = ''
    if not genAST.has_main:
        err_str += "Error: No main function found!"
    for error in errors:
        err_str += f"\nError at {error}"
    if err_str != '':
        print(err_str)
        return None, None, None

    # Print Warnings
    warnings = genAST.warnings
    for warning in warnings:
        print(f"Warning: {warning}")

    # Constant folding of expressions
    if constant_fold:
        ast.constant_fold(errors=errors, warnings=warnings)

    # remove forward declarations
    ast.remove_forward_declarations()

    return ast, symbolTable, stdio_found


def compile_llvm(input_file, visitor, output_file, run_code):
    ast, symbol_table, stdio_found = generate_ast(input_file, visitor)
    if ast is None:
        print("Failed to generate AST.")
        return

    # Open a file to write LLVM code
    path = f'{output_file}'
    with open(path, 'w') as llvm_file:
        visitor = LLVMVisitor(stdio=stdio_found)

        visitor.visit(ast)
        llvm_code = visitor.module

        llvm_file.write(str(llvm_code))

    if run_code:
        os.system(f'lli {path}')


def compile_mips(input_file, visitor, output_file, run_code):
    ast, symbol_table, stdio_found = generate_ast(input_file, visitor)
    if ast is None:
        print("Failed to generate AST.")
        return

    # Open a file to write MIPS code
    path = f'{output_file}'
    with open(path, 'w') as mips_file:
        visitor = MIPSVisitor(stdio=stdio_found)

        visitor.visit(ast)
        mips_data = visitor.data
        mips_code = visitor.code

        if len(mips_data) > 0:
            mips_file.write(".data\n")

        for line in mips_data:
            mips_file.write(f"\t{line}\n")

        if len(mips_data) > 0:
            mips_file.write("\n\t.text\n")
            mips_file.write("\t.globl main\n")

        for line in mips_code:
            if line.endswith(":"):
                mips_file.write(f"{line}\n")
            else:
                mips_file.write(f"\t{line}\n")

    if run_code:
        os.system(f'spim -quiet -file {output_file}')


def render_ast(input_file, output_file):
    ast, _, _ = generate_ast(input_file, Generator())
    if ast is not None:
        DotGenerator.generateASTDot(AST_tree=ast, output_filename=output_file)


def render_ast_png(input_file, output_file):
    ast, _, _ = generate_ast(input_file, Generator())
    if ast is not None:
        DotGenerator.generateASTDot(AST_tree=ast, output_filename=output_file, format='png')


def render_symbol_table(input_file, output_file):
    _, symbol_table, _ = generate_ast(input_file, Generator())
    if symbol_table is not None:
        DotGenerator.generateSymbolTableDot(symbol_table, output_file, file_format='dot')


def render_symbol_table_png(input_file, output_file):
    _, symbol_table, _ = generate_ast(input_file, Generator())
    if symbol_table is not None:
        DotGenerator.generateSymbolTableDot(symbol_table, output_file, file_format='png')


def run(args):
    if args.input:
        if args.render_ast:
            render_ast(input_file=args.input, output_file=args.render_ast)
        elif args.render_ast_png:
            render_ast_png(input_file=args.input, output_file=args.render_ast_png)
        elif args.render_symb:
            render_symbol_table(input_file=args.input, output_file=args.render_symb)
        elif args.render_symb_png:
            render_symbol_table_png(input_file=args.input, output_file=args.render_symb_png)
        elif args.target_llvm:
            compile_llvm(input_file=args.input, visitor=Generator(), output_file=args.target_llvm, run_code=True)
        elif args.target_mips:
            compile_mips(input_file=args.input, visitor=Generator(), output_file=args.target_mips, run_code=True)
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
