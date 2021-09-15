"""
Write a  program to get sum of even numbers.
"""

SOME_NUMS = [1, 2, 3, 4, 5, 6]


def sum_of_even_numbers(nums):
    res = [x for x in nums if x % 2 == 0]
    print(sum(res))

    return sum(res)


sum_of_even_numbers(SOME_NUMS)
