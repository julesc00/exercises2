"""
Short Problem Definition:
Minimize the value |(A[0] + … + A[P-1]) – (A[P] + … + A[N-1])|.

Link
TapeEquilibrium

Complexity:
expected worst-case time complexity is O(N);

expected worst-case space complexity is O(N)

Execution:
    In the first run I compute the left part up to the point i and the overall sum last.
    Then I compute the minimal difference between 0..i and i+1..n.
"""
import sys


def solution(A):
    # 1st pass
    parts = [0] * len(A)
    parts[0] = A[0]

    for idx in range(1, len(A)):
        parts[idx] = A[idx] + parts[idx-1]

    # 2nd pass
    solution = max()

