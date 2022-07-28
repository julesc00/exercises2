# Nested
def between_and_module(value, a, b, modulo):
    if value >= a:
        if value <= b:
            if value % modulo:
                return True
    return False


# Flatter version
def between_and_modulo2(value, a, b, modulo):
    if value < a:
        return False
    elif value > b:
        return False
    elif not value % modulo:
        return False
    else:
        return True


for item in range(10):
    if between_and_modulo2(item, 2, 9, 2):
        print(item, end=" ")

# sparce is better than dense
# dense
print()
f = lambda x: 0 ** x or x * f(x - 1)
print(f(40))


# rewrite sparce
def factorial(x):
    if 0 ** x:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(40))
