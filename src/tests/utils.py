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


def mips_output_compare(root: str, input_file: str):
    import os
    from src.main.__main__ import compile_mips, Generator

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
    os.system("gcc " + file_dir + source_file + " -o " + file_dir + filename)
    # run the executable and save the output to the text file
    os.system(file_dir + filename + " > " + file_dir + gcc_output)

    # compile to mips and run mips file with Spim
    compile_mips(input_file=file_dir + source_file, visitor=visitor, output_file=file_dir + mips_code, run_code=False)
    os.system("spim -quiet -file " + file_dir + mips_code + " > " + file_dir + mips_output)

    # compare the output files
    with open(file_dir + gcc_output, 'r') as f:
        gcc_output_text = f.read()
    with open(file_dir + mips_output, 'r') as f:
        mips_output_text = f.read()
        if mips_output_text.startswith("SPIM"):
            mips_output_lines = mips_output_text.splitlines()
            cleaned_lines = mips_output_lines[5:]
            mips_output_text = '\n'.join(cleaned_lines)

    print("GCC Output:")
    print(gcc_output_text)
    print('\n')

    print("MIPS Output:")
    print(mips_output_text)

    # assert that the outputs are the same
    assert gcc_output_text.__str__() == mips_output_text.__str__()


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
