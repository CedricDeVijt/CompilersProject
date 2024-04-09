import re


def count_mandatory_features(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match the mandatory features
    pattern = r'\[\]\s\(\*\*mandatory\*\*\)'
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
    pattern = r'\[\]\s\(\*\*optional\*\*\)'
    matches = re.findall(pattern, content)

    return len(matches) + count_completed_optional_features(file_path)


def count_completed_optional_features(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match the completed optional features
    pattern = r'\[x\]\s\(\*\*optional\*\*\)'
    matches = re.findall(pattern, content)

    return len(matches)


# Use the function
file_path = 'TODO.md'
total_mandatory_features = count_mandatory_features(file_path)
completed_mandatory_features = count_completed_mandatory_features(file_path)

percent_mandatory = completed_mandatory_features/total_mandatory_features

total_optional_features = count_optional_features(file_path)
completed_optional_features = count_completed_optional_features(file_path)

percent_optional = completed_optional_features/total_optional_features

score = (percent_mandatory + percent_optional) / 2 if percent_mandatory == 1 else percent_mandatory / 2
print(f"Mandatory Features: {completed_mandatory_features}/{total_mandatory_features}")
print(f"Optional Features: {completed_optional_features}/{total_optional_features}")
print(f"Score: {100*score}% (assuming it works in LLVM AND MIPS)")
