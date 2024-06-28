import time

LIST1 = [-1, 5, 10, 20, 28, 3]
LIST2 = [26, 134, 135, 15, 17]


def get_smallest_diff_to_zero(lst1, lst2):
    lst1.sort()
    lst2.sort()
    diff = [lst1[0], lst2[0]]
    for x in lst1:
        for y in lst2:
            if x < y:
                diff[0] = min(x, y, key=abs)
            else:
                diff[1] = min(y, x, key=abs)
    return diff


def get_smallest_diff_to_zero_optimized(lst1, lst2):
    lst1.sort()
    lst2.sort()
    i, j = 0, 0
    diff = [lst1[0], lst2[0]]
    smallest_diff = abs(lst1[0] - lst2[0])

    while i < len(lst1) and j < len(lst2):
        current_diff = abs(lst1[i] - lst2[j])
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            diff = [lst1[i], lst2[j]]

        if lst1[i] < lst2[j]:
            i += 1
        else:
            j += 1

    return diff


start_time = time.time()
print(get_smallest_diff_to_zero(LIST1, LIST2), time.time() - start_time)


start_time = time.time()
print(get_smallest_diff_to_zero_optimized(LIST1, LIST2), time.time() - start_time)
