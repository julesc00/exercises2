"""
Logarithmic time

A logarithmic algorithm **halves **the list every time it’s run.
In English this is:
    - Go to the middle of the list
    - Check to see if that element is the answer
    - If it’s not, check to see if that element is more than the item we want to find
    - If it is, ignore the right-hand side (all the numbers higher than the midpoint) of the list and choose a new midpoint.
    - Start over again, by finding the midpoint in the new list.

    The algorithm halves the input every single time it iterates. Therefore it is logarithmic.
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def search_n(lst: list, item: int) -> bool:
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


print(search_n(a, 10))
