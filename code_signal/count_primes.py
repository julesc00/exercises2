"""
CodeSignal - Count Primes
Problem Statement:
    Count the number of prime numbers less than a non-negative number, n.
"""


def count_primes(n: int) -> int:
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)


if __name__ == "__main__":
    print(count_primes(10))  # Output: 4
    print(count_primes(0))  # Output: 0
    print(count_primes(1))  # Output: 0
