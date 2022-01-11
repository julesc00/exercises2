import random

N_RANGE = (2, 100000)
ELEMENT_RANGE = (-1000, 1000)


def solution(a):
    """
    Minimize the value |(A[0] + ... + A[P-1]) = (A[P] + ... + A[N-1])|
    :param a: Non-empty list of integers
    :return: An integer - the index value where the smallest difference occurs
    """
    assert len(a) > 1

    best, before, after = None, 0, sum(a)

    for i in range(0, len(a)-1):
        before += a[i]
        after -= a[i]
        difference = abs(before - after)
        if best is None or difference < best:
            best = difference
    return best


class TestExercise:
    def test_example1(self):
        assert solution([3, 1, 2, 4, 3]) == 1

    def test_simple(self):
        assert solution([1, 2]) == 1

    def test_double(self):
        assert solution([-1000, 1000]) == 2000

    def test_random(self):
        n = random.randint(*N_RANGE)
        arr = [random.randint(*ELEMENT_RANGE) for _ in range(n)]
        print(n, solution(arr), arr)

    def test_maximum(self):
        arr = [random.randint(*ELEMENT_RANGE) for _ in range(100000)]
        print(100000, solution(arr), arr)
