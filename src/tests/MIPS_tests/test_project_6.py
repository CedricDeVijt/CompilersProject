# from src.tests.utils import llvm_output_compare, llvm_output_compare_with_expected_output
#
# root = "src/tests/test_input_files/custom_tests/project_6/"
#
#
# def test_p6_array():
#     source_file = "p6_array.c"
#     llvm_output_compare(root, source_file)
#
#
# def test_p6_array_assignment_complete():
#     source_file = "p6_array_assignment_complete.c"
#     llvm_output_compare_with_expected_output(root, source_file, "src/tests/LLVM_tests/expected_output/p6_array_assignment_complete_expected_output.txt")
#
#
# def test_p6_array_assignment_partial():
#     source_file = "p6_array_assignment_partial.c"
#     llvm_output_compare_with_expected_output(root, source_file, "src/tests/LLVM_tests/expected_output/p6_array_assignment_partial_expected_output.txt")
#
#
# def test_p6_array_init():
#     source_file = "p6_array_init.c"
#     llvm_output_compare_with_expected_output(root, source_file, "src/tests/LLVM_tests/expected_output/p6_array_init_expected_output.txt")
#
#
# def test_p6_array_multi_dim():
#     source_file = "p6_array_multi_dim.c"
#     llvm_output_compare(root, source_file)
#
#
# def test_p6_c_string():
#     source_file = "p6_c_string.c"
#     llvm_output_compare(root, source_file)
#
#
# def test_p6_example_input():
#     source_file = "p6_example_input.c"
#     llvm_output_compare(root, source_file)
