from antlr4 import *

from src.antlr_files.Proj_2.Grammar_Project_2Lexer import Grammar_Project_2Lexer as MyGrammarLexer
from src.antlr_files.Proj_2.Grammar_Project_2Parser import Grammar_Project_2Parser as MyGrammarParser

from ASTGenerator import ASTGenerator


def main():
    # Read input from a file
    with open("tests/example1.txt", "r") as file:
        input_string = file.read()

    # Create a CharStream that reads from the input file
    input_stream = InputStream(input_string)

    # Create a CharStream that reads from standard input
    input_stream = InputStream(input_string)

    # Create a lexer that feeds off of input CharStream
    lexer = MyGrammarLexer(input_stream)

    # Create a buffer of tokens pulled from the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that feeds off the tokens buffer
    parser = MyGrammarParser(token_stream)

    # Begin parsing at the start rule
    tree = parser.program()

    generator = ASTGenerator()

    ast = generator.visit(tree)

    ast[0].constantFold()

    ast[0].to_dot_file("output")


if __name__ == '__main__':
    main()
