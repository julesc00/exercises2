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

    temp_dict = {}
    for x in a:
        if x in temp_dict:
            temp_dict[x] += 1
        else:
            temp_dict[x] = 1

    print(temp_dict)
    for k, v in temp_dict.items():
        if v % 2 == 1:
            return k


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

    def test_simple1(self):
        """Simple test n=5"""
        arr = gen_array(5, 4)
        assert 4 == match_odd_occurrences(arr)

    def test_simple2(self):
        """Simple test n=11"""
        arr = gen_array(11, 4)
        assert 4 == match_odd_occurrences(arr)

    def test_small1(self):
        """Small random test n=201"""
        arr = gen_array(201, 42)
        assert 42 == match_odd_occurrences(arr)

    def test_small2(self):
        """Small random test n=601"""
        arr = gen_array(601, 4242)
        assert 4242 == match_odd_occurrences(arr)

    def test_medium1(self):
        """Medium random test n=2001"""
        arr = gen_array(2001, 100)
        assert 100 == match_odd_occurrences(arr)

    def test_medium2(self):
        """Medium random test n=100,003"""
        arr = gen_array(100003, 500000)
        assert 500000 == match_odd_occurrences(arr)

    def test_big1(self):
        """Big random test n=999,999, multiple repetitions"""
        arr = gen_array(100003, 700)
        assert 700 == match_odd_occurrences(arr)

    def test_big2(self):
        """Big random test n=999,999"""
        arr = gen_array(999999, 5000111222)
        assert 5000111222 == match_odd_occurrences(arr)
