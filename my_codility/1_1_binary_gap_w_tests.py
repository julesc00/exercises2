import pytest

# The largest integer we have to deal with
MAX_INT = 2147483647


def solution(nums: int):
    """
    Determines the maximal 'binary gap' in an integer
    :param nums: a positive integer (between 1 and maxint or 2 million odd)
    :return: a count of the longest sequence of zeros in the binary representation of the integer.
    """
    # sanitize against crazy inputs
    if not isinstance(nums, int):
        raise TypeError("Input must be an integer")
    if nums < 1:
        raise ValueError("Input must be a positive integer.")
    if nums > MAX_INT:
        raise ValueError("Input must be a positive integer less than 2,147,483,647")

    # convert the number to a str containing '0' and '1' chars
    bin_string = str(bin(nums))[2:]

    # The longest binary gap: use None to indicate no 'gap' yet found (set to zero at the first flip)
    max_count = None
    # count the bits in a sequence
    this_count = 0
    # true if the last bit was a zero
    was_zero = None

    # loop over all the 0/1 chars in the string
    for bit in bin_string:
        is_zero = bit == '0'

        # If the bit value has flipped
        if bool(was_zero) != bool(is_zero):
            # The first sequence doesn't count eg: 1111001 has a result of 2
            if max_count is None:
                max_count = 0
            # Save the biggest gap
            elif this_count > max_count:
                max_count = this_count
            # Reset counter
            this_count = 1
        else:
            # Increment the length of the sequence
            this_count += 1

        # Track what the last bit was
        was_zero = is_zero

    # print "%s: %s = %s" % (N, binary_string, max_count)
    if max_count is not None:
        return max_count
    # No binary gaps found
    return 0


class TestBinaryGap:

    def test_example1(self):
        assert 5 == solution(1041)

    def test_example2(self):
        assert 0 == solution(15)

    def test_extremes(self):
        assert 0 == solution(1)
        assert 1 == solution(5)
        assert 0 == solution(MAX_INT)

    def test_trailing_zeros(self):
        assert solution(6) == 0
        assert solution(328) == 2

    def test_simple1(self):
        assert solution(9) == 2
        assert solution(11) == 1

    def test_simple2(self):
        assert solution(19) == 2
        assert solution(42) == 1

    def test_simple3(self):
        assert solution(1162) == 3
        assert solution(5) == 1

    def test_medium1(self):
        assert solution(51712) == 2
        assert solution(20) == 1

    def test_medium2(self):
        assert solution(561892) == 3
        assert solution(9) == 2

    def test_medium3(self):
        assert solution(66561) == 9

    def test_large1(self):
        assert solution(6291457) == 20

    def test_large2(self):
        assert solution(74901729) == 4

    def test_large4(self):
        assert solution(1376796946) == 5

    def test_large5(self):
        assert solution(1073741825) == 29

    def test_large6(self):
        assert solution(1610612737) == 28

    def test_no_int(self):
        with pytest.raises(TypeError) as e_info:
            solution(1.0)

    def test_zero(self):
        with pytest.raises(ValueError) as e_info:
            solution(0)

    def test_max_int_plus_one(self):
        with pytest.raises(ValueError) as e_info:
            solution(2147483648)


if __name__ == "__main__":
    print(solution(1))
