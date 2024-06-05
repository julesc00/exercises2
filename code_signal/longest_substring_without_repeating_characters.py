"""
CodeSignal - Longest Substring Without Repeating Characters
Problem Statement:
    Given a string, find the length of the longest substring without repeating characters.
"""


def length_of_longest_substring(s: str) -> int:
    char_index = {}
    start = max_length = 0
    for i, char in enumerate(s):
        if char in char_index:
            start = max(start, char_index[char] + 1)
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # Output: 3
    