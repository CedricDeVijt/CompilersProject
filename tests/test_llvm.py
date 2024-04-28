import os
import pytest

from src.main.__main__ import Generator, compile_llvm


class TestProject3:
    def __init__(self):
        self.visitor = Generator()
        self.file_dir = "tests/test_input_files/extra_tests/project_3/"

    def testPrintf(self):
        source_file = "p3_printf.c"

        llvm_generated_code = "p3_printf_generated.ll"
        llvm_test_code = "p3_printf_test.ll"
        llvm_generated_output = "p3_printf_generated_output.txt"
        llvm_test_output = "p3_printf_test_output.txt"

        # compile to llvm and run with clang
        os.system("clang -S -emit-llvm " + self.file_dir + source_file + " -o " + self.file_dir + llvm_generated_code)
        os.system("lli " + self.file_dir + llvm_generated_code + " > " + self.file_dir + llvm_generated_output)


        # compile to llvm and run with our compiler
        compile_llvm(input_file=self.file_dir + source_file, visitor=self.visitor, output_file=self.file_dir + llvm_test_code, run_code=False)
        os.system("lli " + self.file_dir + llvm_test_code + " > " + self.file_dir + llvm_test_output)

        # compare the output
        with open(self.file_dir + llvm_generated_output, 'r') as f:
            generated_output = f.read()
        with open(self.file_dir + llvm_test_output, 'r') as f:
            test_output = f.read()

        assert generated_output == test_output
