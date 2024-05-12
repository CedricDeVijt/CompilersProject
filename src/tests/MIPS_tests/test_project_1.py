from src.tests.utils import llvm_output_compare

root = "src/tests/test_input_files/custom_tests/project_1/"


def test_p1_bin_op_1():
    source_file = "p1_bin_op_1.c"
    llvm_output_compare(root, source_file)


def test_p1_bin_op_2():
    source_file = "p1_bin_op_2.c"
    llvm_output_compare(root, source_file)


def test_p1_bitw_op():
    source_file = "p1_bitw_op.c"
    llvm_output_compare(root, source_file)


def test_p1_comp_op():
    source_file = "p1_comp_op.c"
    llvm_output_compare(root, source_file)


def test_p1_parenthesis():
    source_file = "p1_parenthesis.c"
    llvm_output_compare(root, source_file)


def test_p1_shift_op():
    source_file = "p1_shift_op.c"
    llvm_output_compare(root, source_file)


def test_p1_unary_op():
    source_file = "p1_unary_op.c"
    llvm_output_compare(root, source_file)
