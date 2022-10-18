"""
For running script: python -m mccabe mastering_python/ch3/using_mccabe.py
"""


def noop():
    pass


def yield_cube_points(matrix):
    for x in matrix:
        for y in x:
            for z in y:
                yield x, y, z


def print_cube(matrix):
    for x in matrix:
        for y in x:
            for z in y:
                print(z, end="")
            print()
        print()
