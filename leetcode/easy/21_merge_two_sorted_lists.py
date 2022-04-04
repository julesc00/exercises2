from collections import namedtuple


def merge_sorted_lists(list1: list, list2: list):
    s_lst1 = sorted(list1.copy())
    s_lst2 = sorted(list2.copy())
    final_lst = []
    tups = namedtuple(s_lst1, s_lst2)

    print(final_lst)


if __name__ == "__main__":
    merge_sorted_lists([1, 2, 4], [1, 3, 4])
