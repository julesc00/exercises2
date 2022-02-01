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


def solution(A):
    sums, max_sum = collections.defaultdict(list), 0
    for i in A:
        sum_of_digits = sum(int(num) for num in str(i))
        sums[sum_of_digits].append(i)
    for item in sums.values():
        if len(item) > 1:
            ordered_sum = sorted(item)
            print(ordered_sum)
            print(f"Sum: {sum(max(ordered_sum, ordered_sum))}")
            add_two_nums = ordered_sum[len(ordered_sum) - 2] + ordered_sum[len(ordered_sum) - 1]
            max_sum = add_two_nums if add_two_nums > max_sum else max_sum

        return max_sum if max_sum > 0 else -1


if __name__ == "__main__":
    arr1 = [51, 71, 17, 42]
    arr2 = [42, 33, 60]
    arr3 = [51, 32, 43]
    print(solution(arr2))
