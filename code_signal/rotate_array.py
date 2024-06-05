from typing import List

"""
CodeSignal - Rotate Array
Problem Statement:
    Rotate an array to the right by a given number of steps.
"""


def rotate_array(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    k %= n
    nums[:] = nums[n - k:] + nums[:n - k]
    return nums


def rotate_array_v2(nums: List[int], k: int) -> List[int]:
    k = k % len(nums)  # Handle cases where k > len(nums)
    return nums[-k:] + nums[:-k]


if __name__ == "__main__":
    print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]
