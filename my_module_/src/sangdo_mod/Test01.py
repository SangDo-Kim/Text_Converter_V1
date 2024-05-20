import fnmatch
import re


def is_valid_pattern(pattern):
    try:
        fnmatch.translate(pattern)
        return True
    except re.error:
        return False

# Test patterns
patterns = ["*.txt", "x?xx.*", "[a-z]+.png", "[a-z", "abc**"]

# Check if patterns are valid
for pattern in patterns:
    if is_valid_pattern(pattern):
        print(f"'{pattern}' is a valid pattern.")
    else:
        print(f"'{pattern}' is not a valid pattern.")
