LIST1 = [-1, 5, 10, 20, 28, 3]
LIST2 = [26, 134, 135, 15, 17]


def get_nums_diff(arr_a, arr_b):
    if not arr_a or not arr_b:
        return []
    arr_a.sort()
    arr_b.sort()
    output_nums = [arr_a[0], arr_b[0]]
    min_diff = abs(arr_a[0] - arr_b[0])

    ind_a, ind_b = 0, 0
    while ind_a < len(arr_a) and ind_b < len(arr_b):
        a = arr_a[ind_a]
        b = arr_b[ind_b]

        next_a = arr_a[ind_a + 1] if ind_a + 1 < len(arr_a) else a
        next_b = arr_b[ind_b + 1] if ind_b + 1 < len(arr_b) else b

        diff_a_next_b = abs(a - next_b)
        diff_b_next_a = abs(b - next_a)

        if diff_a_next_b < diff_b_next_a:
            potential_min_diff = diff_a_next_b
            potential_output_nums = [a, next_b]
            ind_b += 1
        else:
            potential_min_diff = diff_b_next_a
            potential_output_nums = [next_a, b]
            ind_a += 1

        if potential_min_diff < min_diff:
            min_diff = potential_min_diff
            output_nums = potential_output_nums
            if min_diff == 0:
                return output_nums
    return output_nums


print(get_nums_diff(LIST1, LIST2))
