
import random

INT_RANGE = (0, 100000)


def solution(a: list):
    """
    Find the missing element in a given permutation
    :param a: list of integers
    :return: the integer that is missing in O(n) time and O(1) space complexity
    """
    # An empty list so the missing element must be "1"
    if not len(a):
        return 1

    return sum(range(1, len(a)+2)) - sum(a)


class TestFindMissingElement:

    def test_example1(self):
        assert solution([2, 3, 1, 5]) == 4

    def test_single(self):
        assert solution([2]) == 1

    def test_random(self):
        arr = [n for n in range(1, random.randint(*INT_RANGE))]
        missing = random.randint(0, len(arr))
        arr.remove(missing)

        assert solution(arr) == missing

    def test_maximum(self):
        arr = [n for n in range(1, INT_RANGE[1]+1)]
        arr.pop()

        assert solution(arr) == INT_RANGE[1]
