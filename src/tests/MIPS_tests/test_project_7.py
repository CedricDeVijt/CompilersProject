from src.tests.utils import mips_output_compare, mips_output_compare_with_expected_output

root = "src/tests/test_input_files/custom_tests/project_7/"


def test_p7_struct():
    source_file = "p7_struct.c"
    mips_output_compare(root, source_file)


def test_p7_struct_2():
    source_file = "p7_struct_2.c"
    mips_output_compare(root, source_file)


def test_p7_struct_assignment():
    source_file = "p7_struct_assignment.c"
    mips_output_compare(root, source_file)


def test_p7_struct_assignment2():
    source_file = "p7_struct_assignment2.c"
    mips_output_compare(root, source_file)


def test_p7_struct_definition():
    source_file = "p7_struct_definition.c"
    mips_output_compare(root, source_file)


def test_p7_struct_operations():
    source_file = "p7_struct_operations.c"
    mips_output_compare(root, source_file)


def test_p7_struct_var_assignment():
    source_file = "p7_struct_var_assignment.c"
    mips_output_compare(root, source_file)