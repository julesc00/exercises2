"""
Example with no namespace collision.
"""
import math

pi = 3.14


def sin(x):
    return 0.99999999 if 2 * x == pi else None
    # same but in oneliner.
    # if 2 * x == pi:
    #     return 0.99999999
    # else:
    #     return None


if __name__ == "__main__":
    print(sin(pi/2))
    print(math.sin(math.pi/2))
