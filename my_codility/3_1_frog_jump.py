import pytest
import random


INT_RANGE = (1, 1000000000)


def solution(X, Y, D):
    """
    Calculate the minimum number of jumps from X to Y
    :param X: start integer
    :param Y: minimum end integer
    :param D: size of the jump
    :return: minimum number of jumps in 0(1) time and space complexity
    """
    assert X <= Y

    quot, rem = divmod(Y-X, D)
    return quot if rem == 0 else quot + 1


class TestFrogJump:

    def test_example1(self):
        assert solution(10, 85, 30) == 3

    def test_one(self):
        assert solution(0, 10, 1) == 10

    def test_big_steps(self):
        assert solution(0, 10, 20) == 1

    def test_even_steps(self):
        assert solution(10, 100, 10) == 9

    def test_equal_steps(self):
        assert solution(10, 10, 10) == 0

    def test_odd_steps(self):
        assert solution(9, 29, 10) == 2


if __name__ == "__main__":
    pytest.main()
