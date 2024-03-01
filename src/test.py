import antlr4
from src.antlr_files.mathematical_expressionsLexer import mathematical_expressionsLexer as ExpressionLexer
from src.antlr_files.mathematical_expressionsParser import mathematical_expressionsParser as ExpressionParser
from src.antlr_files.mathematical_expressionsVisitor import mathematical_expressionsVisitor as ExpressionVisitor


class MyVisitor(ExpressionVisitor):
    def visitExpression(self, ctx:ExpressionParser.ExpressionContext):
        print("Expression:", ctx.getText())

    def visitAdditiveExpression(self, ctx:ExpressionParser.AdditiveExpressionContext):
        print("Additive Expression:", ctx.getText())

    def visitMultiplicativeExpression(self, ctx:ExpressionParser.MultiplicativeExpressionContext):
        print("Multiplicative Expression:", ctx.getText())

    def visitUnaryExpression(self, ctx:ExpressionParser.UnaryExpressionContext):
        print("Unary Expression:", ctx.getText())

    def visitPrimaryExpression(self, ctx:ExpressionParser.PrimaryExpressionContext):
        print("Primary Expression:", ctx.getText())

    # Define visit methods for logicalExpression, equalityExpression, relationalExpression if needed


def main():
    input_file = "../tests/proj_1/proj1_man_pass_operators.c"  # Specify the path to your input file
    input_stream = antlr4.FileStream(input_file)
    lexer = ExpressionLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ExpressionParser(stream)
    tree = parser.expression()

    # Create a visitor instance
    visitor = MyVisitor()
    visitor.visit(tree)
    print('t')

if __name__ == '__main__':
    main()