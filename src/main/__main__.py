import sys
import os

import antlr4

from src.antlr_files.Grammar_Project_1Lexer import Grammar_Project_1Lexer as Lexer
from src.antlr_files.Grammar_Project_1Parser import Grammar_Project_1Parser as Parser
from src.antlr_files.Grammar_Project_1Visitor import Grammar_Project_1Visitor as Visitor
from src.antlr_files.Grammar_Project_1Visitor import Grammar_Project_1Visitor as Listener

from src.parser.ASTGenerator import ASTGenerator as Generator


def generate_ast(path, visitor):
    input_stream = antlr4.FileStream(path)
    lexer = Lexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.program()

    ast = visitor.visit(tree)
    return ast


def compile_llvm(input_file, visitor):
    ast = generate_ast(input_file, visitor)
    # TODO: CONVERT TO LLVM
    raise Exception("NOT IMPLEMENTED YET!")


def compile_mips(input_file, visitor):
    ast = generate_ast(input_file, visitor)
    # TODO: CONVERT TO MIPS
    raise Exception("NOT IMPLEMENTED YET!")


def run(language, path):
    visitor = Generator()
    if os.path.isdir(path):
        # compile all in directory
        print('directory')
        if language == 'LLVM':
            print('LLVM')
            return
        print('MIPS')
        return
    print('file')
    if language == "LLVM":
        print('LLVM')
        compile_llvm(path, visitor)
        return
    print('MIPS')
    compile_mips(path, visitor)


def main(argv):
    arg_len = 2
    if len(argv) != arg_len+1 or (argv[1] != 'LLVM' and argv[1] != 'MIPS') or not (os.path.isdir(argv[2]) or os.path.isfile(argv[2])):
        print('Usage: test.py [\'LLVM\' | \'MIPS\'] [INPUT_FILE | INPUT_DIRECTORY]')
        exit(1)
    run(argv[1], argv[2])


if __name__ == '__main__':
    main(sys.argv)