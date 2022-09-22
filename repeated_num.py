import numpy.ma

arr1 = [4, 5, 2, 4, 5, 9, 9, 4, 4]


def detect_repeated_num(arr: list, detect_num: int, times: int) -> int:
    counter = 0
    for number in arr:
        if number == detect_num:
            counter += 1
    print(counter)
    return True if counter >= times else False


print(detect_repeated_num(arr1, 4, 3))


def major_difference(arr: list):
    smallest_num, highest_num = min(arr), max(arr)
    return highest_num - smallest_num


print(major_difference([9, 8]))

import numpy as np


def same_difference_separation(arr: list) -> bool:
    sorted_arr = sorted(arr)
    counter1, counter2 = 0, 0
    f_counter1, f_counter2 = 0.0, 0.0
    if isinstance(sorted_arr[0], float):
        for _ in np.arange(sorted_arr[0], sorted_arr[1]):
            f_counter1 += 1
        for _ in np.arange(sorted_arr[1], sorted_arr[2]):
            f_counter2 += 1
    else:
        for _ in range(sorted_arr[0], sorted_arr[1]):
            counter1 += 1
        for _ in range(sorted_arr[1], sorted_arr[2]):
            counter2 += 1

    if isinstance(sorted_arr[0], float):
        return True if f_counter1 == f_counter2 else False
    return True if counter1 == counter2 else False


print(same_difference_separation([-2.3, -1.1, 0.1, 1.3, 2.5, 3.7]))

