"""
CodeSignal - Palindrome Check
Problem Statement:
    Write a function that checks if a given string is a palindrome (a string that reads the same
    forwards and backwards).
"""


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome("racecar"))  # Output: True
    