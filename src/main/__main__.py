import sys

import antlr4
from antlr4.error.ErrorListener import ErrorListener

from src.antlr_files.Proj_2.Grammar_Project_2Lexer import Grammar_Project_2Lexer as Lexer
from src.antlr_files.Proj_2.Grammar_Project_2Parser import Grammar_Project_2Parser as Parser
from src.llvm_target.toLLVM import generateLLVMcode
from src.parser.ASTGenerator import ASTGenerator as Generator
from src.parser.dotGenerator import DotGenerator


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Syntax error at line {line}:{column}")


def generate_ast(path, visitor):
    input_stream = antlr4.FileStream(path)
    lexer = Lexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = Parser(stream)
    parser.addErrorListener(ThrowingErrorListener())  # Add the custom listener
    tree = parser.program()

    genAST = visitor.visit(tree)

    ast = genAST.node
    symbolTable = genAST.scope
    errors = genAST.errors
    warnings = genAST.warnings
    for warning in warnings:
        print(f"Warning: {warning}")
    if len(errors) == 0:
        ast.constantFold()
        return ast, symbolTable
    err_str = ''
    for error in errors:
        err_str += f"Error at {error}\n"
    raise Exception(err_str)


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

        generateLLVMcode(ast, llvm_file, symbol_table)


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
