import itertools

"""
Write a function that takes in a non-empty list of distinct integers, and an integer representing a target
sum. If any two numbers in the input list sum up to the target sum, the function should return them in a
list, in any order. If no two numbers sum up to the target sum, the function should return an empty list.

Note that the target sum has to be obtained by summing two different integers in the list; you can't add a
single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.
"""


# Approach 1
def target_sum(my_list, my_target_sum):
    for nums in itertools.combinations(my_list, 2):
        if sum(nums) == my_target_sum:
            print(sorted(list(nums)))
            break


lst = [3, 5, -4, 8, 11, 1, -1, 6]
targ_sum = 10

if __name__ == "__main__":
    target_sum(lst, targ_sum)
