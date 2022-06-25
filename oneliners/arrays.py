import numpy as np

a1 = np.array([
    [1, 0, 0],
    [1, 1, 1],
    [2, 0, 0]
])

a2 = np.array([
    [1, 1, 1],
    [1, 1, 2],
    [1, 1, 2]
])

print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)

print(np.max(a1))
print(np.min(a2))
print(np.average(a1))
