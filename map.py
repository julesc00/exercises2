"""
As the name proposed, filter() creates a new list that only contains elements
that satisfy the conditions we provide.

Syntax : filter(function, iterable(s))
"""
from functools import reduce


def multiply_by_2(i):
    return i * 2


def odd(n: int) -> bool:
    return n % 3 == 0


# Map loops through an iterable and executes a function on it.
my_list = (list(map(multiply_by_2, [1, 2, 3])))
numbers = [23, 22, 16, 28, 14, 36, 12, 99]
odd2 = list(filter(odd, numbers))
print(odd2)
print(my_list)

# With lambda
odd = list(filter(lambda n: n % 3 == 0, numbers))
print(odd)

"""
2. Map()

The map function iterates through all the elements in a given iterable 
and executes the function by the arguments we pass.

Syntax : map(function, iterable(s))
"""


def double_nums(n: int) -> int:
    return n * 2


doubles = list(map(double_nums, odd))
print(doubles)

# With lambda
doubles2 = list(map(double_nums, odd))
print(doubles2)


"""
3. Reduce()

Reduce function is different from map() and filter(). It returns only a single
value based on the function and iterables we pass.

Syntax : reduce(function, sequence[, initial])
"""


def add_all(x, y) -> int:
    return x + y


sum1 = reduce(add_all, odd)
print(sum1)

# Using lambda
sum2 = reduce(lambda a, b: a+b, odd)
print(sum2)
