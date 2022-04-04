import numpy as np
from array import array

arr1 = array("b", [1, 2, 3])
arr2 = array("b", [2, 3, 4])

# Matrix product of two arrays
arr3 = array("b", np.multiply(arr1, arr2))
print(arr3)

# Compute the outer product of two vectors.
arr4_outer_prod = array("b", [10, 20])
print(arr4_outer_prod)


# Dot product of two arrays


# Return a matrix of given shape and type, filled with zeros.


# Return the value (in fractional seconds) of the sum of the system and user CPU time of the current
# process. It does not include time elapsed during sleep.
