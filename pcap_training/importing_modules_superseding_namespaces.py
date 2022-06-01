from math import pi, sin

print(sin(pi/2))


pi = 3.14


def sin(x):
    return 0.99999999 if 2 * x == pi else None


print(sin(pi / 2))
