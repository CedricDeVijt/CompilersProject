import re
import math


def count_mandatory_features(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match the mandatory features
    pattern = r'\[ \]\s\(\*\*mandatory\*\*\)'
    matches = re.findall(pattern, content)

    return len(matches) + count_completed_mandatory_features(file_path)


def count_completed_mandatory_features(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match the completed mandatory features
    pattern = r'\[x\]\s\(\*\*mandatory\*\*\)'
    matches = re.findall(pattern, content)

    return len(matches)


def count_optional_features(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match the optional features
    pattern = r'\[ \]\s\(\*\*optional\*\*\)'
    matches = re.findall(pattern, content)

    return len(matches) + count_completed_optional_features(file_path)


def count_completed_optional_features(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match the completed optional features
    pattern = r'\[x\]\s\(\*\*optional\*\*\)'
    matches = re.findall(pattern, content)

    return len(matches) + count_completed_additional_features(file_path)


def count_completed_additional_features(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match the completed additional features
    pattern = r'\[x\]\s\(\*\*additional\*\*\)'
    matches = re.findall(pattern, content)

    return len(matches)

# AST

file_path_AST = 'TODO_AST.md'
AST_total_mandatory_features = count_mandatory_features(file_path_AST)
AST_completed_mandatory_features = count_completed_mandatory_features(file_path_AST)
AST_percent_mandatory = AST_completed_mandatory_features/AST_total_mandatory_features

AST_total_optional_features = count_optional_features(file_path_AST)
AST_completed_optional_features = count_completed_optional_features(file_path_AST)
AST_percent_optional = AST_completed_optional_features/AST_total_optional_features

AST_score = (AST_percent_mandatory + AST_percent_optional) / 2 if AST_percent_mandatory == 1 else AST_percent_mandatory / 2
print(f"AST Mandatory Features: {AST_completed_mandatory_features}/{AST_total_mandatory_features}")
print(f"AST Optional Features: {AST_completed_optional_features}/{AST_total_optional_features}")
print(f"AST Score: {round(100 * 100 * AST_score) / 100}%")

# LLVM
print("\n")

file_path_LLVM = 'TODO_LLVM.md'
LLVM_total_mandatory_features = count_mandatory_features(file_path_LLVM)
LLVM_completed_mandatory_features = count_completed_mandatory_features(file_path_LLVM)
LLVM_percent_mandatory = LLVM_completed_mandatory_features/LLVM_total_mandatory_features

LLVM_total_optional_features = count_optional_features(file_path_LLVM)
LLVM_completed_optional_features = count_completed_optional_features(file_path_LLVM)
LLVM_percent_optional = LLVM_completed_optional_features/LLVM_total_optional_features

LLVM_score = (LLVM_percent_mandatory + LLVM_percent_optional) / 2 if LLVM_percent_mandatory == 1 else LLVM_percent_mandatory / 2
print(f"LLVM Mandatory Features: {LLVM_completed_mandatory_features}/{LLVM_total_mandatory_features}")
print(f"LLVM Optional Features: {LLVM_completed_optional_features}/{LLVM_total_optional_features}")
print(f"LLVM Score: {round(100 * 100 * LLVM_score) / 100}%")

# MIPS
print("\n")

file_path_MIPS = 'TODO_MIPS.md'
MIPS_total_mandatory_features = count_mandatory_features(file_path_MIPS)
MIPS_completed_mandatory_features = count_completed_mandatory_features(file_path_MIPS)
MIPS_percent_mandatory = MIPS_completed_mandatory_features/MIPS_total_mandatory_features

MIPS_total_optional_features = count_optional_features(file_path_MIPS)
MIPS_completed_optional_features = count_completed_optional_features(file_path_MIPS)
MIPS_percent_optional = MIPS_completed_optional_features/MIPS_total_optional_features

MIPS_score = (MIPS_percent_mandatory + MIPS_percent_optional) / 2 if MIPS_percent_mandatory == 1 else MIPS_percent_mandatory / 2
print(f"MIPS Mandatory Features: {MIPS_completed_mandatory_features}/{MIPS_total_mandatory_features}")
print(f"MIPS Optional Features: {MIPS_completed_optional_features}/{MIPS_total_optional_features}")
print(f"MIPS Score: {round(100*100*MIPS_score) / 100}%")

# TOTAL
print("\n")
percent_of_grade = 60

score = (LLVM_score * 0.4 + MIPS_score * 0.6)
print(f"Total Score: {round(100 * 100 * score) / 100}%")
print(f"Grade From Project: {round(100 * percent_of_grade / 100 * 20 * score) / 100}/20")