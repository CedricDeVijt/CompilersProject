from antlr4 import *

from src.antlr_files.Grammar_Project_1Lexer import Grammar_Project_1Lexer as MyGrammarLexer
from src.antlr_files.Grammar_Project_1Parser import Grammar_Project_1Parser as MyGrammarParser
from src.antlr_files.Grammar_Project_1Visitor import Grammar_Project_1Visitor as MyGrammerVisitor

from ASTGenerator import ASTGenerator


def main():
    # Your input string to parse
    input_string = ("(5+5)/3+8*(5+2);\n8+8;")

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

    ast.constantFold()

    ast.to_dot_file("output.dot")


if __name__ == '__main__':
    main()
