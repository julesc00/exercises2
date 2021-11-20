"""
Polynomial time is a polynomial function of the input. A polynomial function
looks like n^2n 2 or n^3n 3 and so on.

If one loop through a list is O(n)O(n), 2 loops must be O(n^2)O(n 2). For each loop, we go over the
list once. For each item in that list, we go over the entire list once. Resulting in n2 operations.
"""

LST1 = [64, 34, 25, 12, 22, 11, 90]


# Bubble sort
def bubble_fort(lst):
    n = len(lst)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


print(bubble_fort(LST1))
