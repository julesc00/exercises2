from functools import reduce
"""
Practicality beats purity
"""
# Way 1
fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)

print(fib(10))

# Way 2
fib2 = lambda n: reduce(lambda x, y: (x[0]+x[1], x[0]), [(1, 1)] * (n-1))[0]
print(fib2(10))


# Way 3, more readable
def fib3(n):
    if n < 2:
        return n
    else:
        return fib3(n - 1) + fib3(n - 2)


print(fib3(10))


# Way 4, also readable
def fib4(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib4(10))
