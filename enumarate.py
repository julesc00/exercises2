"""
Enumerate() method adds a counter to an iterable and returns it in a form of enumerating
object. This enumerated object can then be used directly for loops or converted into a
list of tuples using the list() method.
"""
my_list = ["apple", "banana", "peach", "pear", "berry"]

[print(counter, value) for counter, value in enumerate(my_list)]
[print(counter, val) for counter, val in enumerate(my_list)]
