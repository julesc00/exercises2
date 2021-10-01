def multiply_by_2(i):
    return i * 2


# Map loops through an iterable and executes a function on it.
my_list = (list(map(multiply_by_2, [1, 2, 3])))


print(my_list)
