from src.tests.utils import mips_output_compare

root = "src/tests/test_input_files/custom_tests/project_1/"


def test_p1_bin_op_1():
    source_file = "p1_bin_op_1.c"
    mips_output_compare(root, source_file)


def test_p1_bin_op_2():
    source_file = "p1_bin_op_2.c"
    mips_output_compare(root, source_file)


def test_p1_bitw_op():
    source_file = "p1_bitw_op.c"
    mips_output_compare(root, source_file)


def test_p1_comp_op():
    source_file = "p1_comp_op.c"
    mips_output_compare(root, source_file)


def test_p1_parenthesis():
    source_file = "p1_parenthesis.c"
    mips_output_compare(root, source_file)


def test_p1_shift_op():
    source_file = "p1_shift_op.c"
    mips_output_compare(root, source_file)


def test_p1_unary_op():
    source_file = "p1_unary_op.c"
    mips_output_compare(root, source_file)


def test_complex_binary_modulo_test():
    source_file = "complex_binary_modulo_test.c"
    mips_output_compare(root, source_file)


def test_complex_binary_operations_test():
    source_file = "complex_binary_operations_test.c"
    mips_output_compare(root, source_file)


def test_complex_bitwise_operations_test():
    source_file = "complex_bitwise_operations_test.c"
    mips_output_compare(root, source_file)


def test_complex_comparison_extended_test():
    source_file = "complex_comparison_extended_test.c"
    mips_output_compare(root, source_file)


def test_complex_comparison_operations_test():
    source_file = "complex_comparison_operations_test.c"
    mips_output_compare(root, source_file)


def test_complex_logical_operations_test():
    source_file = "complex_logical_operations_test.c"
    mips_output_compare(root, source_file)


def test_complex_mixed_operations_test():
    source_file = "complex_mixed_operations_test.c"
    mips_output_compare(root, source_file)


def test_complex_parenthesis_test():
    source_file = "complex_parenthesis_test.c"
    mips_output_compare(root, source_file)


def test_complex_shift_operations_test():
    source_file = "complex_shift_operations_test.c"
    mips_output_compare(root, source_file)


def test_complex_unary_operations_test():
    source_file = "complex_unary_operations_test.c"
    mips_output_compare(root, source_file)
