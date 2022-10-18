
def sub(v1, v2):
    return v1 - v2


print(sub(20, 5))

"""
Decorators explanation according to geeksforgeeks.org
"""


def decorators(*args, **kwargs):
    """
    Decorator with parameters implementation
    """
    def inner(func):
        """do operations with func"""
        return func
    return inner


@decorators
def func():
    """
    Function implementation
    """
    pass


def decorator_func(func):
    print("Inside decorator")

    def inner(*args, **kwargs):
        print("Inside inner function")
        print("Decorated the function")

        func()
    return inner


@decorator_func
def func_to():
    print("Inside actual function")


func_to()


"""Another way"""


def decorator_func2(func):
    print("Inside decorator2")

    def inner(*args, **kwargs):
        print("Inside inner function2")
        print("Decorated the function2")

        func()
    return inner


def func_to():
    print("Inside actual function2")


decorator_func2(func_to)()
