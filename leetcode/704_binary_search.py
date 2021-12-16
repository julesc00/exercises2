"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to
search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Benchmark:
Success
Details
Runtime: 244 ms, faster than 43.19% of Python3 online submissions for Binary Search.
Memory Usage: 15.6 MB, less than 30.54% of Python3 online submissions for Binary Search.
"""


def search(nums: list[int], target: int) -> int:
    for i, v in enumerate(nums):
        if target == v:
            return i
    else:
        return -1


if __name__ == "__main__":
    nums2 = [-1, 0, 3, 5, 9, 12]
    print(search(nums2, 9))
