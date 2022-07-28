import math
import itertools

# Ugly
filter_modulo = lambda i, m: (i[j] for j in range(len(i)) if i[j] % m)

print(list(filter_modulo(range(10), 2)))


# Rather prettier, with a generator
def filter_modulo2(items, modulo):
    for item in items:
        if item % modulo:
            yield item


print(list(filter_modulo2(range(10), 2)))

"""
Another case for pretty better than ugly
"""


def spam(eggs, *args, **kwargs):
    for arg in args:
        eggs += arg
        for extra_egg in kwargs.get("extra_eggs", []):
            eggs += extra_egg
        return eggs


print(spam(1, 2, 3, extra_eggs=[4, 5]))


# Prettier
def sum_ints(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(sum_ints(1, 2, 3, 4, 5))


"""
Simple is better than complex
"""


def primes_complicated():
    sieved = dict()
    i = 2
    while True:
        if i not in sieved:
            yield i
            sieved[i * i] = [i]
        else:
            for j in sieved:
                sieved.setdefault(i + j, []).append(j)
            del sieved[i]


print(list(itertools.islice(primes_complicated(), 10)))


# Another example that could be improved
def primes_complex():
    nums = itertools.count(2)
    while True:
        yield (prime := next(nums))  # needs the parenthesis else it'll create an error
        nums = filter(prime.__rmod__, nums)


print(list(itertools.islice(primes_complex(), 10)))

#########################################


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for modulo in range(2, num):
        if not num % modulo:
            return False
    else:
        return True


def primes_simple():
    for item in itertools.count():
        if is_prime(item):
            yield item


print(list(itertools.islice(primes_simple(), 10)))
