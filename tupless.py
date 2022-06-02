
my_lst = ["hello", "hi", "whats up"]

for row in my_lst:
    tuple_row = tuple(row)

    print(tuple_row)

my_tuple = ("a", "b", "c", "d")
my_other_tuple = my_tuple + ("m",)
print(my_other_tuple)
