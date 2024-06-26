from src.tests.utils import llvm_output_compare

root = "src/tests/test_input_files/custom_tests/project_2/"


def test_p2_bin_op_1():
    source_file = "p2_bin_op_1.c"
    llvm_output_compare(root, source_file)


def test_p2_bin_op_2():
    source_file = "p2_bin_op_2.c"
    llvm_output_compare(root, source_file)


def test_p2_bitw_op():
    source_file = "p2_bitw_op.c"
    llvm_output_compare(root, source_file)


def test_p2_comp_op():
    source_file = "p2_comp_op.c"
    llvm_output_compare(root, source_file)


def test_p2_const():
    source_file = "p2_const.c"
    llvm_output_compare(root, source_file)


def test_p2_const_casting():
    source_file = "p2_const_casting.c"
    llvm_output_compare(root, source_file)


def test_p2_explicit_conv():
    source_file = "p2_explicit_conv.c"
    llvm_output_compare(root, source_file)


def test_p2_implicit_conv():
    source_file = "p2_implicit_conv.c"
    llvm_output_compare(root, source_file)


def test_p2_inc_dec_op():
    source_file = "p2_inc_dec_op.c"
    llvm_output_compare(root, source_file)


def test_p2_literals():
    source_file = "p2_literals.c"
    llvm_output_compare(root, source_file)


def test_p2_parenthesis():
    source_file = "p2_parenthesis.c"
    llvm_output_compare(root, source_file)


def test_p2_pointers():
    source_file = "p2_pointers.c"
    llvm_output_compare(root, source_file)


def test_p2_shift_op():
    source_file = "p2_shift_op.c"
    llvm_output_compare(root, source_file)


def test_p2_unary_op():
    source_file = "p2_unary_op.c"
    llvm_output_compare(root, source_file)
