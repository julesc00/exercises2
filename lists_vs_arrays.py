import array as arr

my_list = ["hello", 2, True]

my_array = arr.array("i", [1, 2, 3, 4, 5])
f_array = arr.array("f", [2, 3, 5])

print(my_list)
print(my_array)
print(f_array)

print(my_array.count(my_list))

# Reverse sequence by indexing
print(my_array[::-1])
for i in my_array:
    print(i)
