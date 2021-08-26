
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def multiply_by_2(i):
    return i * 2


def check_odd(item):
    return item % 2 != 0


# Map loops through an iterable.
my_list2 = (list(map(multiply_by_2, ma_liste)))
print(list(filter(check_odd, ma_liste)))

print(ma_liste)
print(my_list2)
