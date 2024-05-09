from src.tests.utils import llvm_output_compare

root = "src/tests/test_input_files/finished_proj/CorrectCode/"


def test_binaryOperations1():
    source_file = "binaryOperations1.c"
    llvm_output_compare(root, source_file)


def test_binaryOperations2():
    source_file = "binaryOperations2.c"
    llvm_output_compare(root, source_file)


def test_breakAndContinue():
    source_file = "breakAndContinue.c"
    llvm_output_compare(root, source_file)


def test_comparisons1():
    source_file = "comparisons1.c"
    llvm_output_compare(root, source_file)


def test_comparisons2():
    source_file = "comparisons2.c"
    llvm_output_compare(root, source_file)


def test_dereferenceAssignment():
    source_file = "dereferenceAssignment.c"
    llvm_output_compare(root, source_file)


def test_fibonacciRecursive():
    source_file = "fibonacciRecursive.c"
    llvm_output_compare(root, source_file)


def test_floatToIntConversion():
    source_file = "floatToIntConversion.c"
    llvm_output_compare(root, source_file)


def test_for():
    source_file = "for.c"
    llvm_output_compare(root, source_file)


def test_forwardDeclaration():
    source_file = "forwardDeclaration.c"
    llvm_output_compare(root, source_file)


def test_if():
    source_file = "if.c"
    llvm_output_compare(root, source_file)


def test_ifElse():
    source_file = "ifElse.c"
    llvm_output_compare(root, source_file)


def test_intToFloatConversion():
    source_file = "intToFloatConversion.c"
    llvm_output_compare(root, source_file)


def test_modulo():
    source_file = "modulo.c"
    llvm_output_compare(root, source_file)


def test_pointerArgument():
    source_file = "pointerArgument.c"
    llvm_output_compare(root, source_file)


def test_prime():
    source_file = "prime.c"
    llvm_output_compare(root, source_file)


def printf1():
    source_file = "printf1.c"
    llvm_output_compare(root, source_file)


def test_printf2():
    source_file = "printf2.c"
    llvm_output_compare(root, source_file)


def test_printf3():
    source_file = "printf3.c"
    llvm_output_compare(root, source_file)


def test_scanf1():
    source_file = "scanf1.c"
    llvm_output_compare(root, source_file)


def test_scanf2():
    source_file = "scanf2.c"
    llvm_output_compare(root, source_file)


def test_scoping():
    source_file = "scoping.c"
    llvm_output_compare(root, source_file)


def test_unaryOperations():
    source_file = "unaryOperations.c"
    llvm_output_compare(root, source_file)


def test_variables1():
    source_file = "variables1.c"
    llvm_output_compare(root, source_file)


def test_variables2():
    source_file = "variables2.c"
    llvm_output_compare(root, source_file)


def test_variables3():
    source_file = "variables3.c"
    llvm_output_compare(root, source_file)


def test_variables4():
    source_file = "variables4.c"
    llvm_output_compare(root, source_file)


def test_variables5():
    source_file = "variables5.c"
    llvm_output_compare(root, source_file)


def test_variables6():
    source_file = "variables6.c"
    llvm_output_compare(root, source_file)


def test_variables7():
    source_file = "variables7.c"
    llvm_output_compare(root, source_file)


def test_variables8():
    source_file = "variables8.c"
    llvm_output_compare(root, source_file)


def test_while():
    source_file = "while.c"
    llvm_output_compare(root, source_file)


