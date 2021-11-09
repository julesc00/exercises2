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

# sort descending order
lst = [100, 10, 10000, 1, 9, 999, 99]
lst.sort(key=lambda x: 100 / x)
print(lst)

# sort ascending order
lst2 = [100, 10, 10000, 1, 9, 999, 99]
lst2.sort(key=lambda x: x * 1)
print(lst2)

# sort  the words in the list based on their second letter from a to z
lst3 = ["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
lst3.sort(key=lambda x: x[1] * 1)
print(lst3)

# Sort tuples in the list based on the second item
lst4 = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California")]
lst4.sort(key=lambda x: x[1])
print(lst4)

# Sort the tuples in the list based on the last character of the second items.
lst4.sort(key=lambda x: x[1][-1])
print(lst4)

# Sort using sorted, reverse parameter and lambda to sort tuples in the list based on the last
# character of the second items in reverse order.
print(sorted(lst4, key=lambda x: x[1][-1], reverse=True))

i = 6
L = lambda x: x + 2

print(L(i))
