from src.tests.utils import llvm_output_compare

root = "src/tests/test_input_files/extra_tests_with_print/project_4/"


def test_p4_anon_scope():
    source_file = "p4_anon_scope.c"
    llvm_output_compare(root, source_file)


def test_p4_cond_statem():
    source_file = "p4_cond_statem.c"
    llvm_output_compare(root, source_file)


def test_p4_else_if():
    source_file = "p4_else_if.c"
    llvm_output_compare(root, source_file)


def test_p4_enum_1():
    source_file = "p4_enum_1.c"
    llvm_output_compare(root, source_file)


def test_p4_enum_2():
    source_file = "p4_enum_2.c"
    llvm_output_compare(root, source_file)


def test_p4_example_input():
    source_file = "p4_example_input.c"
    llvm_output_compare(root, source_file)


def test_p4_for_loop():
    source_file = "p4_for_loop.c"
    llvm_output_compare(root, source_file)


def test_p4_switch():
    source_file = "p4_switch.c"
    llvm_output_compare(root, source_file)


def test_p4_while_loop():
    source_file = "p4_while_loop.c"
    llvm_output_compare(root, source_file)
