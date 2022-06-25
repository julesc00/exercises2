import numpy as np

# Data: yearly salary in ($1000) [2017, 2018, 2019]
alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]

salaries = np.array([alice, bob, tim])
taxation = np.array([
    [0.2, 0.25, 0.22],
    [0.4, 0.5, 0.5],
    [0.1, 0.2, 0.1]
])

# Oneliner
max_income = np.max(salaries - salaries * taxation)
print(max_income)

print("*" * 20)
print(("*"*20) + " Numpy Slicing " + ("*"*20))

arr1 = np.array([55, 56, 57, 58, 59, 60, 61])
print(arr1)
print(arr1[:])  # Prints all items in the array.
print(arr1[2:])  # Starts from index 2, skips 0-1
print(arr1[1:4])  # Starts from index 1, and stops before index 4 [56 57 58]
print(arr1[2:-2])  # Starts from index 2, and backwards stops at index -2, [57 58 59]
print(arr1[::-1])  # Prints items backwards.
print(arr1[::2])  # Prints skipping one item [55 57 59 61] = [55 - 57 - 59 - 61]
print(arr1[1::2])  # Skips index 0, and starts from index 1 and skips one every other.
# [61 59 57] Starts with the last item as the 1st, then skips backwards every other, but stops -2 items backwards.
print(arr1[:1:-2])
#  The same as above
print(arr1[-1:1:-2])
print()
"""
Multi-dimensional slicing
"""
print(("*"*20) + " Numpy Multi-dimensional Slicing " + ("*"*20))
arr2 = np.array([
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [12, 13, 14, 15]
])
print(arr2[:, 2])  # Prints index-2 column: [ 2  6 14] and all items in it.
print(arr2[1, :])  # Prints index-1 column: [4 5 6 7] and all items in it.
print(arr2[1, ::2])  # Prints index-1 column and skips every other item. [4 6]
print(arr2[:, :-1])  # Prints all columns, and except the last item in the last column.
print(arr2[:-2])  # Same as :-2, :
print()

"""
Broadcasting
    Broadcasting describes the automatic process of bringing two NumPy arrays
    into the same shape so that you can apply certain element-wise operations
    (see “Slicing and Indexing” on page 46). Broadcasting is closely related
    to the shape attribute of NumPy arrays, which in turn is closely related to the
    concept of axes.
"""
print(("*"*20) + " Broadcasting " + ("*"*20))
arr3 = np.array([1, 2, 3, 4])
print(f"Array dimensions: {arr3.ndim}")  # Prints 1
arr4 = np.array([
    [2, 1, 2],
    [3, 2, 3],
    [4, 3, 4]
])
print(f"Array dimensions: {arr4.ndim}")  # Prints 2

arr5 = np.array([
    [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]
    ],
    [
        [1, 2, 4],
        [2, 3, 5],
        [3, 4, 6]
    ]
])
print(f"Array dimensions: {arr5.ndim}")  # Prints 3

"""
Note:
    If you increase the dimensionality of an array (for example, you move from 2D to 3D
    arrays), the new axis becomes axis 0, and the i-th axis of the low-dimensional array
    becomes the (i + 1)-th axis of the high-dimensional array.
    
    Giving the shape attribute to arrays:
"""
print(f"Array shape: {arr3.shape}")  # (4,)
print(f"Array shape: {arr4.shape}")  # (3, 3)
print(f"Array shape: {arr5.shape}")  # (2, 3, 3)
