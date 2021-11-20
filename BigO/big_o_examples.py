"""
Name	    Big O

Constant	O(c)
    The complexity of an algorithm is said to be constant if the steps required to complete
    the execution of an algorithm remain constant, irrespective of the number of inputs.
    The constant complexity is denoted by O(c) where c can be any constant number.

Linear	    O(n)
    The complexity of an algorithm is said to be linear if the steps required to
    complete the execution of an algorithm increase or decrease linearly with the
    number of inputs. Linear complexity is denoted by O(n).

Quadratic	O(n^2)
    The complexity of an algorithm is said to be quadratic when the steps required to
    execute an algorithm are a quadratic function of the number of items in the input.

Cubic	    O(n^3)
Exponential	O(2^n)
Logarithmic	O(log(n))
Log Linear	O(nlog(n))
"""
import matplotlib.pyplot as plt
import numpy as np


def constant_algo(items):
    """Constant Complexity (O(c))"""
    return items[0] * items[0]


print(constant_algo([4, 5, 6, 8]))


x = [2, 4, 6, 8, 10, 12]
y = [2, 2, 2, 2, 2, 2]

plt.plot(x, y, "b")
plt.xlabel("Inputs")
plt.ylabel("Steps")
plt.title("Constant Complexity")
plt.show()


x2 = [2, 4, 6, 8, 10, 12]
y2 = [2, 4, 6, 8, 10, 12]

plt.plot(x2, y2, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Complexity')
plt.show()


def linear_algo(items):
    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])


def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item)


quadratic_algo([4, 5, 6, 8])
