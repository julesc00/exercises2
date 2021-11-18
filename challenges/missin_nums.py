"""
Write a program to find a missing number, and from a list.
"""


def missing_numbers(nums: list):
    return sum(range(nums[0], nums[-1] + 1)) - sum(nums)


print(missing_numbers([1, 2, 3, 5, 6, 7, 8]))


# Get difference of two lists, using set()
def missing_nums(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) - set(nums2)) + list(set(nums2) - set(nums1))


li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
print(missing_nums(li1, li2))


# Get the missing numbers within a list.
def missing_nums2(nums1: list[int]) -> list[int]:
    cleaned_lst = list(set(nums1))
    range_list = range(cleaned_lst[0], cleaned_lst[-1] + 1)
    diff_items = sorted(list(set(range_list) - set(cleaned_lst)) + list(set(cleaned_lst) - set(range_list)))

    return diff_items


print(missing_nums2([1, 2, 3, 5, 6, 7, 8, 11]))
