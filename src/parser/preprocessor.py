import os


def pre_processing(path, stdio_found=None):
    lines = []
    if stdio_found is None:
        stdio_found = [False]
    with open(path, 'r') as file:
        lines = file.readlines()

    lines = pre_process_include(lines, stdio_found)
    lines = pre_process_define(lines)
    return lines


def pre_process_include(lines, stdio_found):
    lines = pre_process_include_file(lines, stdio_found)
    lines = pre_process_include_guards(lines)
    return lines


def pre_process_include_file(lines, stdio_found=None):
    macros = []
    for line in lines:
        if line.startswith("#include"):
            # Split in words.
            words = line.split()
            if len(words) == 1:
                raise Exception("#include expects \"FILENAME\" or <FILENAME>!")
            if len(words) > 2:
                raise Exception('extra tokens at end of #include directive!')
            if not ((words[1].startswith('\"') and words[1].endswith('\"')) or (words[1].startswith('<') and words[1].endswith('>'))):
                raise Exception("#include expects \"FILENAME\" or <FILENAME>!")
            if words[1] == '<stdio.h>':
                stdio_found[0] = True
                macros.append(line)
                continue
            # Check if file exists.
            if not os.path.exists(words[1][1:-1]):
                raise Exception(f"File {words[1][1:-1]} not found.")
            # Read file.
            file_lines = pre_processing(path=words[1][1:-1], stdio_found=stdio_found)
            # Insert file content.
            index = lines.index(line) + 1
            for file_line in file_lines:
                lines.insert(index, file_line)
                index += 1
            # Add include to removal
            macros.append(line)
    for line in lines:
        if 'printf(' in line or 'scanf(' in line:
            if not stdio_found[0]:
                raise Exception("<stdio.h> not included.")
    for macro in macros:
        lines.remove(macro)
    return lines


def pre_process_include_guards(lines):
    included_guards = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#ifndef"):
            guard = line.split()[1]
            if guard in included_guards:
                # Remove all lines until #endif
                while not lines[i].startswith("#endif"):
                    lines.pop(i)
                lines.pop(i)
                i += 1
            else:
                included_guards.append(guard)
                while not lines[i].startswith("#endif"):
                    if lines[i].startswith("#ifndef") or lines[i].startswith("#define") or lines[i].startswith("#endif"):
                        lines.pop(i)
                    else:
                        i += 1
                lines.pop(i)
                i -= 1
        else:
            i += 1

    return lines


def pre_process_define(lines):
    macros = []
    for line in lines:
        if line.startswith("#define"):
            # Split in words.
            words = line.split()
            if len(words) >= 3:
                macros.append(line)
            else:
                raise Exception("#define expects MACRO or MACRO VALUE!")
            for line2 in lines:
                if lines.index(line2) > lines.index(line):
                    repl = ''
                    for word in words[2:]:
                        repl += word + ' '
                    repl = repl.removesuffix(' ')
                    lines[lines.index(line2)] = line2.replace(words[1], repl)

    for macro in macros:
        lines.remove(macro)

    return lines