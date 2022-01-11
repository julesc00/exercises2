import pytest
import random

lst = [9, 3, 9, 3, 9, 8, 9]
# The largest length array we have to handle
MAX_LENGTH = 1000000


def match_odd_occurrences(a):
    """
    Complexity: O(N) or O(N*log(N))
    Fi
    """
    if not isinstance(a, list):
        raise TypeError("Input must be a list of integers")
    if not len(a):
        raise ValueError("Input list must not be empty")
    if len(a) > MAX_LENGTH:
        raise ValueError(f"Input list must not be longer than {MAX_LENGTH}")

    unmatched = dict()

    # For every element
    for el in a:
        # Try removing it's match
        try:
            del unmatched[el]
        except KeyError:
            # else add it
            unmatched[el] = True

    # If one unmatched item
    if len(unmatched) == 1:
        return unmatched.keys()[0]
    else:
        raise Exception(f"Expected one unmatched item, but these {unmatched} unmatched")


def gen_array(L, odd):
    """
    Generate a list of sample data: random integers in pairs
    :param L: the length of the list is double this int
    :param odd: the odd integer out
    """
    arr = []
    for _ in range(int((L-1) / 2)):
        val = random.randint(1, MAX_LENGTH)
        arr.extend((val, val))
    arr.append(odd)
    random.shuffle(arr)
    return arr


class TestOddOccurrencesInArray:

    def test_sample_generation(self):
        print(gen_array(5, 1))

    def test_example1(self):
        arr = [9, 3, 9, 3, 9, 7, 9]
        assert 7 == match_odd_occurrences(arr)
