"""
Importing a function
"""

from functions1 import hello_world


NAMES = ["lupita", "marc", "joe"]


def my_function():
    name = NAMES[0]
    print(hello_world(name))


my_function()

