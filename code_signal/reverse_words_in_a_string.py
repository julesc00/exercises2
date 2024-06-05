"""
CodeSignal - Reverse Words in a String
Problem Statement:
    Given an input string, reverse the order of the words.
"""


def reverse_words_in_a_string(s: str) -> str:
    return " ".join(s.split()[::-1])


def reverse_words_in_a_string_v2(s: str) -> str:
    return " ".join(reversed(s.split()))


if __name__ == "__main__":
    print(reverse_words_in_a_string("The cat in the hat"))
    print(reverse_words_in_a_string("The quick brown fox"))
