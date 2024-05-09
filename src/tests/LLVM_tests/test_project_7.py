from src.tests.utils import llvm_output_compare, llvm_output_compare_with_expected_output

root = "src/tests/test_input_files/custom_tests/project_7/"

#class TestProject1:
#    @staticmethod
#    def testPrintf():
#        source_file = "p1_printf.c"
#        test_llvm(root, source_file)
#
#
#
#
#
#class TestProject3:
#    @staticmethod
#    def testPrintf():
#        source_file = "p3_printf.c"
#        test_llvm(root, source_file)


def test_p7_struct():
    source_file = "p7_struct.c"
    llvm_output_compare(root, source_file)


def test_p7_struct_assignment():
    source_file = "p7_struct_assignment.c"
    llvm_output_compare(root, source_file)

def test_p7_struct_assignment2():
    source_file = "p7_struct_assignment2.c"
    llvm_output_compare(root, source_file)