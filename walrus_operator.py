# w = False
#
# print((w := True))
#
#
# def do_something(txt):
#     return txt
#
#
# with open("test.txt", "r") as f:
#     text = f.readline()
#
#     while text := f.readline():
#         do_something(text)


# With lists and dicts


numbers = [2, 8, 0, 1, 1, 9, 7, 7]
num_length = len(numbers)
num_sum = sum(numbers)

description = {
    "length": num_length,
    "sum": num_sum,
    "mean": num_sum / num_length
}
print(description)

"""
The variables num_length and num_sum are only used to optimize the calculations inside the dictionary. 
With the walrus operator this role can be made more clear.
"""
description2 = {
    "length": (num_length := len(numbers)),
    "sum": (num_sum := sum(numbers)),
    "mean": num_sum / num_length,
}
print(description2)

numbers2 = [7, 6, 1, 4, 1, 8, 0, 6]

try:
    print(5//9)
except ZeroDivisionError:
    print("Not this way")
