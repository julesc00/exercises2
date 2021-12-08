# Linear example
count = 10**5
nums = []
for i in range(count):
    nums.append(i)

nums.reverse()


# Quadratic example, slower
nums2 = []
for i in range(count):
    nums2.insert(0, i)
