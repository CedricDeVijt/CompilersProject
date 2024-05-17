from src.tests.utils import mips_output_compare

root = "src/tests/test_input_files/custom_tests/project_2/"


def test_p2_bin_op_1():
    source_file = "p2_bin_op_1.c"
    mips_output_compare(root, source_file)


def test_p2_bin_op_2():
    source_file = "p2_bin_op_2.c"
    mips_output_compare(root, source_file)


def test_p2_bitw_op():
    source_file = "p2_bitw_op.c"
    mips_output_compare(root, source_file)


def test_p2_comp_op():
    source_file = "p2_comp_op.c"
    mips_output_compare(root, source_file)


def test_p2_const():
    source_file = "p2_const.c"
    mips_output_compare(root, source_file)


def test_p2_const_casting():
    source_file = "p2_const_casting.c"
    mips_output_compare(root, source_file)


def test_p2_explicit_conv():
    source_file = "p2_explicit_conv.c"
    mips_output_compare(root, source_file)


def test_p2_implicit_conv():
    source_file = "p2_implicit_conv.c"
    mips_output_compare(root, source_file)


def test_p2_inc_dec_op():
    source_file = "p2_inc_dec_op.c"
    mips_output_compare(root, source_file)


def test_p2_literals():
    source_file = "p2_literals.c"
    mips_output_compare(root, source_file)


def test_p2_parenthesis():
    source_file = "p2_parenthesis.c"
    mips_output_compare(root, source_file)


def test_p2_pointer_arithmetic():
    source_file = "p2_pointer_arithmetic.c"
    mips_output_compare(root, source_file)


def test_p2_pointers():
    source_file = "p2_pointers.c"
    mips_output_compare(root, source_file)


def test_p2_shift_op():
    source_file = "p2_shift_op.c"
    mips_output_compare(root, source_file)


def test_p2_unary_op():
    source_file = "p2_unary_op.c"
    mips_output_compare(root, source_file)


def test_p2_constants_test():
    source_file = "p2_constants_test.c"
    mips_output_compare(root, source_file)


def test_p2_explicit_conversions_test():
    source_file = "p2_explicit_conversions_test.c"
    mips_output_compare(root, source_file)


def test_p2_implicit_conversions_test():
    source_file = "p2_implicit_conversions_test.c"
    mips_output_compare(root, source_file)


def test_p2_increment_decrement_test():
    source_file = "p2_increment_decrement_test.c"
    mips_output_compare(root, source_file)


def test_p2_literals_test():
    source_file = "p2_literals_test.c"
    mips_output_compare(root, source_file)


def test_p2_main_function_test():
    source_file = "p2_main_function_test.c"
    mips_output_compare(root, source_file)


def test_p2_pointer_arithmetic_test():
    source_file = "p2_pointer_arithmetic_test.c"
    mips_output_compare(root, source_file)


def test_p2_reserved_keywords_test():
    source_file = "p2_reserved_keywords_test.c"
    mips_output_compare(root, source_file)
