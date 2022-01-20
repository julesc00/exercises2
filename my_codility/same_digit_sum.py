"""
Write a function:
def solution(A)
that, given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to
an equal sum. If there are no two numbers whose digits have an equal sum, the function should return -1.
Examples:
1. Given A = [51, 71, 17, 42], the function should return 93. There are two pairs of numbers whose digits add up to
an equal sum: (51, 42) and (17, 71). The first pair sums up to 93.
2. Given A = [42, 33, 60], the function should return 102. The digits of all numbers in A add up to the same sum,
and choosing to add 42 and 60 gives the result 102.
3. Given A = [51, 32, 43], the function should return -1, since all numbers in A have digits that add up to different,
unique sums.
Write an efficient algorithm for the following assumptions: N is an integer within the range [1..200,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""
import collections


def solution(a):
    additions, gst_addition = collections.defaultdict(list), 0
    for i in a:
        sum_of_nums = sum(int(num) for num in str(i))
        additions[sum_of_nums].append(i)
    print(additions)

    for item in additions.values():
        if len(item) > 1:
            ordered_add = sorted(item)
            add_two_nums = ordered_add[len(ordered_add) - 2] + ordered_add[len(ordered_add) - 1]
            gst_addition = add_two_nums if add_two_nums > gst_addition else gst_addition

        return gst_addition if gst_addition > 0 else -1


if __name__ == "__main__":
    arr1 = [51, 71, 17, 42]
    arr2 = [42, 33, 60]
    arr3 = [51, 32, 43]
    print(solution(arr3))
