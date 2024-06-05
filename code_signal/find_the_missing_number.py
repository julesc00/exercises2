from typing import List
"""
CodeSignal - Find the Missing Number
Problem Statement:
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is
    missing from the array.
"""


def find_missing_number(nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    print(find_missing_number([3, 0, 1]))  # Output: 2
    print(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8
