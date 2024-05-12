from src.tests.utils import mips_output_compare, mips_output_compare_with_expected_output

root = "src/tests/test_input_files/custom_tests/project_6/"


def test_p6_array():
    source_file = "p6_array.c"
    mips_output_compare(root, source_file)


def test_p6_array_assignment_complete():
    source_file = "p6_array_assignment_complete.c"
    mips_output_compare_with_expected_output(root, source_file, "src/tests/mips_tests/expected_output/p6_array_assignment_complete_expected_output.txt")


def test_p6_array_assignment_partial():
    source_file = "p6_array_assignment_partial.c"
    mips_output_compare_with_expected_output(root, source_file, "src/tests/mips_tests/expected_output/p6_array_assignment_partial_expected_output.txt")


def test_p6_array_init():
    source_file = "p6_array_init.c"
    mips_output_compare_with_expected_output(root, source_file, "src/tests/mips_tests/expected_output/p6_array_init_expected_output.txt")


def test_p6_array_multi_dim():
    source_file = "p6_array_multi_dim.c"
    mips_output_compare(root, source_file)


def test_p6_c_string():
    source_file = "p6_c_string.c"
    mips_output_compare(root, source_file)


def test_p6_example_input():
    source_file = "p6_example_input.c"
    mips_output_compare(root, source_file)
