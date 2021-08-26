ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ta_liste = [10, 20, 30]


def multiply_by_2(i):
    return i * 2


def check_odd(item):
    return item % 2 != 0


# Zip packs the items according to their index position.
my_list2 = (list(map(multiply_by_2, ma_liste)))
print(list(zip(ma_liste, ta_liste)))

