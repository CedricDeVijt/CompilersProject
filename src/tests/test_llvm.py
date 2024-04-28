import os

import src.main.__main__ as main


class TestProject3:
    def testPPPrintf(self):
        visitor = main.Generator()
        file_dir = "src/tests/test_input_files/extra_tests/project_3/"
        source_file = "p3_printf.c"

        llvm_generated_code = "p3_printf_generated.ll"
        llvm_test_code = "p3_printf_test.ll"
        llvm_generated_output = "p3_printf_generated_output.txt"
        llvm_test_output = "p3_printf_test_output.txt"

        # compile to llvm and run with clang
        os.system("clang -S -emit-llvm " + file_dir + source_file + " -o " + file_dir + llvm_generated_code)
        os.system("lli " + file_dir + llvm_generated_code + " > " + file_dir + llvm_generated_output)


        # compile to llvm and run with our compiler
        main.compile_llvm(input_file=file_dir + source_file, visitor=visitor, output_file=file_dir + llvm_test_code, run_code=False)
        os.system("lli " + file_dir + llvm_test_code + " > " + file_dir + llvm_test_output)

        # compare the output
        with open(file_dir + llvm_generated_output, 'r') as f:
            generated_output = f.read()
        with open(file_dir + llvm_test_output, 'r') as f:
            test_output = f.read()

        assert generated_output == test_output
