
"""
CodeSignal - First Non-Repeating Character
Problem Statement:
    Give a string, find and return the first non-repeating character. If there is no such character, return '_'.
"""


def first_non_repeating_character(s: str) -> str:
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return '_'


if __name__ == "__main__":
    print(first_non_repeating_character("abacabad"))  # Output: c
    