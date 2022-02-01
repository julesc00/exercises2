"""
There are N nails hammered into the same block of wood. Each nail sticks out of the wood at some length. You can choose at most K nails and
hammer them down to any length between their original lengths and 0. Nails cannot be pulled up. The goal is to have as many nails of the same
length as possible.
You are given an implementation of a function:
def solution(A, K) which, given an array A of N integers representing lengths of the nails sorted in a non-decreasing
order and an integer K, returns the maximal number of nails that can be positioned at the same length after
hammering down at most K nails.
For example, given K = 2 and array A = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5] the function should return 5. One of the
possibilities is to hammer the nails represented by A[8] and A[9] down to length 3.

The attached code is still incorrect for some inputs. Despite the error(s), the code may produce a correct answer
for the example test cases. The goal of the exercise is to find and fix the bug(s) in the implementation.
You can modify at most four lines.
Assume that:
    N is an integer within the range [1..10,000];
    K is an integer within the range [0..N];
    each element of array A is an integer within the range [1..1,000,000,000];
    array A is sorted in non-decreasing order.
    In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""


def solution(A, K):
    n = len(A)
    best = 0
    # count = 1
    count = 0
    for i in range(n-K-1):
        if A[i] == A[i+1]:
            count = count + 1
        else:
            count = 0
        best = max(best, count)
    print(f"Count: {count}")
    print(f"Best: {best}")
    # result = best + 1 + K
    result = best + 1 + K if K < n else n
    return result


if __name__ == "__main__":
    arr = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
    print(solution(arr, 2))
