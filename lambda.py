from functools import reduce


ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ta_liste = [10, 20, 30]

# We use lambdas for 1 time functions.
print(list(map(lambda item: item * 2, ma_liste)))
print(list(filter(lambda item: item % 2 != 0, ma_liste)))
print(reduce(lambda acc, item: acc + item, ma_liste))
print(list(map(lambda item: item ** 2, ma_liste)))

# List sorting
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)
