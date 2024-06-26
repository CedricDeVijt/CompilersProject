from src.tests.utils import llvm_output_compare, llvm_output_compare_with_expected_output

root = "src/tests/test_input_files/custom_tests/project_5/"


def test_p5_define_value():
    source_file = "p5_define_value.c"
    llvm_output_compare(root, source_file)


def test_p5_function_overloading():
    source_file = "p5_function_overloading.c"
    llvm_output_compare_with_expected_output(root, source_file, "src/tests/LLVM_tests/expected_output/p5_function_overloading_expected_output.txt")


def test_p5_functions_1():
    source_file = "p5_functions_1.c"
    llvm_output_compare(root, source_file)


def test_p5_include():
    source_file = "p5_include.c"
    llvm_output_compare(root, source_file)


def test_p5_include_guards():
    source_file = "p5_include_guards_1.c"
    llvm_output_compare(root, source_file)


def test_p5_local_global_var():
    source_file = "p5_local_global_var.c"
    llvm_output_compare(root, source_file)
