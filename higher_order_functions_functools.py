
import functools
import statistics


@functools.cache
def factorial(n):
    return n * factorial(n-1) if n else 1


class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)

    @functools.cached_property
    def stdev(self):
        return statistics.stdev(self._data)


"""
functools.wraps
"""


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling decorated function")
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print("Called example function")


if __name__ == "__main__":
    print(factorial(10))  # no previously cached result, makes 11 recursive calls
    print(factorial(5))  # just looks up cached value result
    print(factorial(12))  # makes two new recursive calls, the other 10 are cached
    example()
    print(example.__name__)
    print(example.__doc__)
