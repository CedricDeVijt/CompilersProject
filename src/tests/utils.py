def llvm_output_compare(root: str, input_file: str):
    import os
    from src.main.__main__ import compile_llvm, Generator

    visitor = Generator()
    file_dir = root
    source_file = input_file

    # remove the file extension
    filename = source_file.split(".")[0]

    llvm_generated_code = filename + "_generated.ll"
    llvm_test_code = filename + "_test.ll"
    llvm_generated_output = filename + "_generated_output.txt"
    llvm_test_output = filename + "_test_output.txt"

    # compile to llvm and run with clang
    os.system("clang -S -emit-llvm " + file_dir + source_file + " -o " + file_dir + llvm_generated_code)
    os.system("lli " + file_dir + llvm_generated_code + " > " + file_dir + llvm_generated_output)

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
