from typing import List
"""
CodeSignal - Merge Two Sorted Lists
Problem Statement:
    Given two sorted lists, merge them into one sorted list.
"""


def merge_sorted_lists(lst1: List[int], lst2: List[int]) -> List[int]:
    merged_list = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    while i < len(lst1):
        merged_list.append(lst1[i])
        i += 1
    while j < len(lst2):
        merged_list.append(lst2[j])
        j += 1
    return merged_list


if __name__ == "__main__":
    print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
