import os
import re
import subprocess

from src.main.__main__ import compile_mips, Generator


def llvm_output_compare(root: str, input_file: str):
    import os
    from src.main.__main__ import compile_llvm, Generator

    visitor = Generator()
    file_dir = root
    source_file = input_file

    # remove the file extension
    filename = source_file.split(".")[0]

    llvm_test_code = filename + "_test.ll"
    llvm_generated_output = filename + "_generated_output.txt"
    llvm_test_output = filename + "_test_output.txt"

    # compile the .c file using gcc
    os.system("gcc " + file_dir + source_file + " -o " + file_dir + filename)
    # run the executable and save the output to the text file
    os.system(file_dir + filename + " > " + file_dir + llvm_generated_output)

    # compile to llvm and run with our compiler
    compile_llvm(input_file=file_dir + source_file, visitor=visitor, output_file=file_dir + llvm_test_code,
                 run_code=False)
    os.system("lli " + file_dir + llvm_test_code + " > " + file_dir + llvm_test_output)

    # compare the output
    with open(file_dir + llvm_generated_output, 'r') as f:
        generated_output = f.read()
    with open(file_dir + llvm_test_output, 'r') as f:
        test_output = f.read()

    print("GCC Output:")
    print(generated_output)

    print("LLVM Output:")
    print(test_output)

    assert generated_output == test_output


def llvm_output_compare_with_expected_output(root: str, input_file: str, expected_output: str):
    import os
    from src.main.__main__ import compile_llvm, Generator

    visitor = Generator()
    file_dir = root
    source_file = input_file

    # remove the file extension
    filename = source_file.split(".")[0]

    llvm_test_code = filename + "_test.ll"
    llvm_test_output = filename + "_test_output.txt"

    # compile to llvm and run with our compiler
    compile_llvm(input_file=file_dir + source_file, visitor=visitor, output_file=file_dir + llvm_test_code,
                 run_code=False)
    os.system("lli " + file_dir + llvm_test_code + " > " + file_dir + llvm_test_output)

    # compare the output
    with open(file_dir + llvm_test_output, 'r') as f:
        generated_output = f.read()

    with open(expected_output, 'r') as f:
        expected_output = f.read()

    assert generated_output == expected_output


def round_floats(text, decimal_places=6):
    # This function finds all floating-point numbers in the text and rounds them to the specified decimal places
    def replacer(match):
        return f"{float(match.group()):.{decimal_places}f}"

    # The regex matches floating-point numbers
    float_pattern = re.compile(r'[-+]?\d*\.\d+|\d+')
    return float_pattern.sub(replacer, text)


def mips_output_compare(root: str, input_file: str):
    visitor = Generator()
    file_dir = root
    source_file = input_file

    # remove the file extension
    filename = source_file.split(".")[0]

    # create the file names
    mips_code = filename + "_test.mips"
    mips_output = filename + "_test_output.txt"
    gcc_output = filename + "_generated_output.txt"

    # compile the .c file using gcc
    os.system(f"gcc {os.path.join(file_dir, source_file)} -o {os.path.join(file_dir, filename)}")
    # run the executable and save the output to the text file
    # os.system(f"{os.path.join(file_dir, filename)} > {os.path.join(file_dir, gcc_output)}")

    gcc = subprocess.run(f"{os.path.join(file_dir, filename)}", shell=True, capture_output=True, text=True)
    gcc_output_text = gcc.stdout

    # compile to mips and run mips file with Spim
    # compile_mips(input_file=os.path.join(file_dir, source_file), visitor=visitor,
    #              output_file=os.path.join(file_dir, mips_code), run_code=False)
    # os.system(f"spim -quiet -file {os.path.join(file_dir, mips_code)} > {os.path.join(file_dir, mips_output)}")

    # Print working directory
    print(os.getcwd())
    # run the mips code with our compiler
    compiler = subprocess.run(f"python3 -m src.main --input {os.path.join(file_dir, source_file)} --target_mips {os.path.join(file_dir, mips_code)}", shell=True, capture_output=True, text=True)
    mips_output_text = compiler.stdout

    # Round the floating-point numbers to ensure consistency
    gcc_output_text = round_floats(gcc_output_text)
    mips_output_text = round_floats(mips_output_text)

    print("GCC Output:")
    print(gcc_output_text)

    print("MIPS Output:")
    print(mips_output_text)

    # assert that the exit codes are the same
    assert gcc.returncode == compiler.returncode

    # assert that the outputs are the same
    assert gcc_output_text.strip() == mips_output_text.strip()


def mips_output_compare_with_expected_output(root: str, input_file: str, expected_output: str):
    import os
    from src.main.__main__ import compile_mips, Generator

    visitor = Generator()
    file_dir = root
    source_file = input_file

    # remove the file extension
    filename = source_file.split(".")[0]

    mips_code = filename + "_test.mips"
    mips_output = filename + "_test_output.txt"

    # compile to mips and run with our compiler
    compile_mips(input_file=file_dir + source_file, visitor=visitor, output_file=file_dir + mips_code,
                 run_code=False)
    os.system("spim -quiet -file " + file_dir + mips_code + " > " + file_dir + mips_output)

    # compare the output with the expected output
    with open(file_dir + mips_output, 'r') as f:
        generated_output = f.read()

    with open(expected_output, 'r') as f:
        expected_output = f.read()

    # assert that the outputs are the same
    assert generated_output == expected_output
