import antlr4
from src.antlr_files.grammarCLexer import grammarCLexer as Lexer
from src.antlr_files.grammarCParser import grammarCParser as Parser
from src.antlr_files.grammarCVisitor import grammarCVisitor as Visitor
from src.antlr_files.grammarCListener import grammarCListener as Listener


class MyVisitor(Visitor):
    def visitStart(self, ctx:Parser.StartContext):
        print("Start:", ctx.getText())

    def visitProgramLine(self, ctx:Parser.ProgramLineContext):
        print("ProgramLine:", ctx.getText())

    def visitExpression(self, ctx:Parser.ExpressionContext):
        print("Expression:", ctx.getText())

    def visitOperation(self, ctx:Parser.OperationContext):
        print("Operation:", ctx.getText())

    def visitTerm(self, ctx:Parser.TermContext):
        print("Term:", ctx.getText())



def main():
    input_file = "../tests/proj_1/proj1_man_pass_constantFolding.c"  # Specify the path to your input file
    input_stream = antlr4.FileStream(input_file)
    lexer = Lexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.start()

    # Create a visitor instance
    visitor = MyVisitor()
    visitor.visitChildren(tree)


if __name__ == '__main__':
    main()