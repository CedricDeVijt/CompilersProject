from src.tests.utils import llvm_output_compare

root = "src/tests/test_input_files/extra_tests_with_print/project_3/"


def test_p3_comments():
    source_file = "p3_comments.c"
    llvm_output_compare(root, source_file)


def test_p3_example_input_file():
    source_file = "p3_example_input_file.c"
    llvm_output_compare(root, source_file)


def test_p3_printf():
    source_file = "p3_printf.c"
    llvm_output_compare(root, source_file)


def test_p3_typedef_1():
    source_file = "p3_typedef_1.c"
    llvm_output_compare(root, source_file)


def test_p3_typedef_2():
    source_file = "p3_typedef_2.c"
    llvm_output_compare(root, source_file)


def test_p3_typedef_3():
    source_file = "p3_typedef_3.c"
    llvm_output_compare(root, source_file)
