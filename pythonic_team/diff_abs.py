
LIST1 = [-1, 5, 10, 20, 28, 3]
LIST2 = [26, 134, 135, 15, 17]

# get 28 y 26


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


print(get_smallest_diff_to_zero(LIST1, LIST2))
