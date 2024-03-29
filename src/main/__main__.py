import sys

import antlr4
from antlr4.error.ErrorListener import ErrorListener

import src.parser.AST as AST
from src.antlr_files.Proj_2.Grammar_Project_2Lexer import Grammar_Project_2Lexer as Lexer
from src.antlr_files.Proj_2.Grammar_Project_2Parser import Grammar_Project_2Parser as Parser
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

    try:
        visit = visitor.visit(tree)
        ast = visit[0]
        symbolTable = visit[1]
        ast.constantFold()
        return ast, symbolTable
    except Exception as e:
        print(e)
        return None, None


def compile_llvm(input_file, visitor):
    ast, symbol_table = generate_ast(input_file, visitor)
    if ast is None:
        print("Failed to generate AST.")
        return

    # Open a file to write LLVM code
    with open('src/llvm_target/output.ll', 'w') as llvm_file:
        # Write LLVM header
        llvm_file.write("; ModuleID = 'output.ll'\n")
        llvm_file.write("source_filename = \"output.ll\"\n")
        llvm_file.write("\n")

        generateLLVMcode(ast, llvm_file, symbol_table)


def generateLLVMcode(node, llvm_file, symbol_table):
    if isinstance(node, AST.Node):
        if isinstance(node, AST.ProgramNode):
            for child in node.children:
                generateLLVMcode(child, llvm_file, symbol_table)
        elif isinstance(node, AST.MainNode):
            llvm_file.write("define i32 @main() {\n")
            llvm_file.write("entry:\n")
            for child in node.children:
                generateLLVMcode(child, llvm_file, symbol_table)
            llvm_file.write("    ret i32 0\n")
            llvm_file.write("}\n")
        elif isinstance(node, AST.DefinitionNode):
            if node.rvalue.value.isalpha():
                operation(node, llvm_file, symbol_table)
            else:
                pointer = False
                # Get variable name, value, and type from node
                var_name = f"%{node.lvalue.value}"
                value = node.rvalue.value
                c_type = "" # type as in c code
                if node.type[0].value == "int":
                    var_type = 'i32'
                elif node.type[0].value == "float":
                    var_type = 'float'
                elif node.type[0].value == "char":
                    var_type = 'i8'
                    value = ord(value[1])
                else:
                    # Handle pointers
                    if isinstance(value, str):
                        var_type = symbol_table[f"%{value}"]
                    else:
                        var_type = symbol_table[f"%{value.value}"]
                        c_type = var_type
                        if c_type == "i32":
                            c_type = "int"
                        elif c_type == "i8":
                            c_type = "char"
                    for i in range(int(node.type[0].value)):
                        if i != 0:
                            var_type += '*'
                            c_type += '*'
                    pointer = True

                # Write to output file
                if pointer:
                    llvm_file.write(f"    {var_name} = alloca {var_type}*")
                    llvm_file.write(f"  ; {c_type}* {node.lvalue.value} = &{value.value};\n")
                    llvm_file.write(f"    %addr_{value.value} = alloca {var_type}\n")
                    llvm_file.write(f"    store {var_type}* %{value.value}, {var_type}** %addr_{value.value}\n")
                    llvm_file.write(f"    %ptr_{value.value} = load {var_type}*, {var_type}** %addr_{value.value}\n")
                    llvm_file.write(f"    store {var_type}* %ptr_{value.value}, {var_type}** {var_name}\n\n")
                else:
                    llvm_file.write(f"    {var_name} = alloca {var_type}")
                    llvm_file.write(f"  ; {node.type[0].value} {node.lvalue.value} = {value};\n")
                    llvm_file.write(f"    store {var_type} {value}, {var_type}* {var_name}\n\n")
                symbol_table[var_name] = var_type

        elif isinstance(node, AST.AssignmentNode):
            # Get variable name, value, and type from node
            var_name = f"%{node.lvalue.value}"
            value = node.rvalue.value
            var_type = symbol_table[var_name]

            # Write to output file
            llvm_file.write(f"    store {var_type} {value}, {var_type}* {var_name}")
            llvm_file.write(f"  ; {node.lvalue.value} = {value};\n\n")
        elif isinstance(node, AST.PostFixNode) or isinstance(node, AST.PreFixNode):

            # Get variable name and type from node
            var_name = f"%{node.value}"
            var_type = symbol_table[var_name]

            # Write to output file
            llvm_file.write(f"    {var_name}_val = load {var_type}, {var_type}* {var_name}")
            if node.op == "inc":
                llvm_file.write(f"  ; {node.value}++\n")
                llvm_file.write(f"    {var_name}_inc = add {var_type} {var_name}_val, 1\n")
                llvm_file.write(f"    store {var_type} {var_name}_inc, {var_type}* {var_name}\n\n")
            else:
                llvm_file.write(f"  ; {node.value}--\n")
                llvm_file.write(f"    {var_name}_dec = sub {var_type} {var_name}_val, 1\n")
                llvm_file.write(f"    store {var_type} {var_name}_dec, {var_type}* {var_name}\n\n")
        elif isinstance(node, AST.CommentNode):
            # Multiline comments
            if node.value[1] == '*':
                comment = node.value[3:-6]
                c = ""
                for i in comment:
                    if i == '\n':
                        c = c[4:]
                        llvm_file.write(f"    ; {c}\n")
                        c = ""
                    else:
                        c += i
                llvm_file.write("\n")
            # Single line comments
            else:
                comment = node.value[2:]
                llvm_file.write(f"    ;{comment}\n")
        elif isinstance(node, AST.IdentifierNode):
            # No action needed for identifiers in LLVM code generation
            pass
        elif isinstance(node, AST.TypeNode):
            # No action needed for types in LLVM code generation
            pass


def operation(node, llvm_file, symbol_table):
    # load variables for operation
    op = node.rvalue.value
    var_name = node.lvalue.value
    var_type = node.type[0].value
    c_type = node.type[0].value
    if var_type == "int":
        var_type = "i32"
    x = node.rvalue.children[0].value
    y = node.rvalue.children[1].value

    # check operation
    opSymbol = ""
    opText = ""
    if op == "Plus":
        opSymbol = '+'
        opText = "add"
    elif op == "Minus":
        opSymbol = '-'
        opText = "sub"
    elif op == "Mul":
        opSymbol = '*'
        opText = "mul"
    elif op == "Div":
        opSymbol = '/'
        opText = "div"

    # write to file
    llvm_file.write(f"    %{var_name} = alloca {var_type}")
    llvm_file.write(f"  ; {c_type} {var_name} = {x}{opSymbol}{y};\n")

    # differentiate between vars and literals
    if x.isalpha():
        llvm_file.write(f"    %{x}_val = load {var_type}, {var_type}* %{x}\n")
        x = f"%{x}_val"
    if y.isalpha():
        llvm_file.write(f"    %{y}_val = load {var_type}, {var_type}* %{y}\n")
        y = f"%{y}_val"
    llvm_file.write(f"    %{opText} = {opText} {var_type} {x}, {y}\n")
    llvm_file.write(f"    store {var_type} %{opText}, {var_type}* %{var_name}\n\n")




def compile_mips(input_file, visitor):
    # Implement MIPS compilation
    pass


def render_ast(input_file, output_file):
    ast, _ = generate_ast(input_file, Generator())
    if ast is not None:
        DotGenerator.generateDot(AST_tree=ast, output_filename=output_file)


def render_ast_png(input_file, output_file):
    ast, _ = generate_ast(input_file, Generator())
    if ast is not None:
        DotGenerator.generateDot(AST_tree=ast, output_filename=output_file, format='png')


def render_symbol_table(input_file, output_file):
    # Implement symbol table rendering
    pass


def run(args):
    if args.input:
        if args.render_ast:
            render_ast(args.input, args.render_ast)
        elif args.render_ast_png:
            render_ast_png(args.input, args.render_ast_png)
        elif args.render_symb:
            render_symbol_table(args.input, args.render_symb)
        elif args.target_llvm:
            compile_llvm(args.input, args.target_llvm, Generator())
        elif args.target_mips:
            compile_mips(args.input, args.target_mips, Generator())
    else:
        print("No input file provided.")


def main(argv):
    import argparse

    parser = argparse.ArgumentParser(description="Your program description here")
    parser.add_argument("--input", help="Input C file")
    parser.add_argument("--render_ast", help="Render AST to DOT file")
    parser.add_argument("--render_ast_png", help="Render AST to DOT png file")
    parser.add_argument("--render_symb", help="Render symbol table to DOT file")
    parser.add_argument("--target_llvm", help="Compile to LLVM output file")
    parser.add_argument("--target_mips", help="Compile to MIPS output file")
    args = parser.parse_args(argv[1:])

    run(args)


if __name__ == '__main__':
    main(sys.argv)
