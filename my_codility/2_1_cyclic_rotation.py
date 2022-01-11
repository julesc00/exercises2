"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

Note: I only get 89% correct and test for empty values does not pass.
"""
import random

import pytest

ARRAY_RANGE = (-1000, 1000)
INT_RANGE = (0, 100)


def cyclic_rotation(a: list, k: int) -> list:
    """
    Rotate the array 'a' by 'k' times step
    :param a: an array of integers
    :param k: number of times to shift right
    :return: the rotated array
    """
    lst = a[:]

    if not len(lst):
        return []

    for _ in range(k):
        popped = lst.pop()
        lst.insert(0, popped)
    return lst


class TestCyclicRotation:

    def test_zero(self):
        assert cyclic_rotation([6, 3, 8, 9, 7], 0) == [6, 3, 8, 9, 7]

    def test_one(self):
        assert cyclic_rotation([6, 3, 8, 9, 7], 1) == [7, 6, 3, 8, 9]

    def test_example1(self):
        assert cyclic_rotation([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]

    def test_full(self):
        assert cyclic_rotation([6, 3, 8, 9, 7], 5) == [6, 3, 8, 9, 7]

    def test_empty(self):
        assert cyclic_rotation([], 5) == []

    def test_random(self):
        n = random.randint(*INT_RANGE)
        k = random.randint(*INT_RANGE)
        a = [random.randint(*INT_RANGE) for _ in range(0, n)]
        print(n, k, a)
        print(cyclic_rotation(a, k))
