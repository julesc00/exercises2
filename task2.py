
my_list = [4, 2, 5, 8, 7, 3, 7]


def find_max_neighbors(lst):
    even_pairs = []
    for idx, val in enumerate(lst):
        if (val + val) % 2 == 0:
            even_pairs.append(val)
    print(len(even_pairs))


if __name__ == "__main__":
    find_max_neighbors(my_list)
