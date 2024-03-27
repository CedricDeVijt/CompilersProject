import sys
import os

import antlr4

from src.antlr_files.Proj_2.Grammar_Project_2Lexer import Grammar_Project_2Lexer as Lexer
from src.antlr_files.Proj_2.Grammar_Project_2Parser import Grammar_Project_2Parser as Parser

import src.parser.AST as AST

from src.parser.ASTGenerator import ASTGenerator as Generator
from src.parser.dotGenerator import DotGenerator


def generate_ast(path, visitor):
    input_stream = antlr4.FileStream(path)
    lexer = Lexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.program()

    try:
        visit = visitor.visit(tree)
        ast = visit[0]
        symbolTable = visit[1]
        ast.constantFold()
        DotGenerator.generateDotImage(AST_tree=ast, output_filename="ast")
    except Exception as e:
        raise Exception(e)
        print(e)
        return None
    return ast


def compile_llvm(input_file, visitor):
    ast = generate_ast(input_file, visitor)
    if ast is None:
        print("Failed to generate AST.")
        return

    # Open a file to write LLVM code
    with open('src/mips_target/output.ll', 'w') as llvm_file:
        # Write LLVM header
        llvm_file.write("; ModuleID = 'output.ll'\n")
        llvm_file.write("source_filename = \"output.ll\"\n")
        llvm_file.write("\n")

        generateLLVMcode(ast, llvm_file, {})


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
        elif isinstance(node, AST.StatementNode):
            if len(node.children) == 4:
                value = node.children[3].value
                var_name = f"%{node.children[1].value}"
                type = ""
                if node.children[0].value == "int":
                    type = 'i32'
                elif node.children[0].value == "float":
                    type = 'float'
                elif node.children[0].value == "char":
                    type = 'i8'
                    value = ord(value[1])
                llvm_file.write(f"    {var_name} = alloca {type}\n")
                llvm_file.write(f"    store {type} {value}, {type}* {var_name}\n\n")
                symbol_table[var_name] = type
            else:
                value = node.children[2].value
                var_name = f"%{node.children[0].value}"
                type = symbol_table[var_name]
                var_name = f"%{node.children[0].value}"
                llvm_file.write(f"    store {type} {value}, {type}* {var_name}\n\n")

        elif isinstance(node, AST.IdentifierNode):
            # No action needed for identifiers in LLVM code generation
            pass
        elif isinstance(node, AST.TypeNode):
            # No action needed for types in LLVM code generation
            pass
        """
        elif isinstance(node, AST.IntNode) or isinstance(node, AST.FloatNode):
            pass
            value = node.value
            var_name = f"%{value}"
            if var_name not in symbol_table:
                llvm_type = "i32" if isinstance(node, AST.IntNode) else "double"
                llvm_file.write(f"{var_name} = alloca {llvm_type}\n")
                llvm_file.write(f"store {llvm_type} {value}, {llvm_type}* {var_name}\n")
                symbol_table[var_name] = True  # Mark variable as allocated and stored
        else:
            # Handle other node types as needed
            pass

        # Recursively emit LLVM code for children nodes
        for child in node.children:
            emit_llvm_code(child, llvm_file, symbol_table)
        """


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
