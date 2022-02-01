"""
Smallest Difference
Sample solution: [28, 26]
"""
import heapq
from heapq import nsmallest, heappop
import itertools_practice

LIST1 = [-1, 5, 10, 20, 28, 3]
LIST2 = [26, 134, 135, 15, 17]


def get_smallest_diff(lst1, lst2):
    smallest_diff = []

    val1 = heappop(nsmallest(1, lst1, key=abs))
    val2 = heappop(nsmallest(1, lst2, key=abs))
    print(val1)
    smallest_diff.extend((val1, val2))

    return smallest_diff


print(get_smallest_diff(LIST1, LIST2))  # Output: [-1, 15]



