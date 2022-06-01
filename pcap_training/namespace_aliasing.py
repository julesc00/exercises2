"""
Aliasing:
    When I rename an import module for convenience.
"""
from math import (sin as my_sin,
                  pi as my_pi)
from array import array
from platform import platform, machine, processor, system


# print(my_sin(my_pi/2))


"""
dir()
"""
# print(dir(my_pi))
# [print(i, end="\t") for i in dir(array)]

print(platform())
print(machine())
print(processor())
print(system())
