# list, set, dictionary

msg = [i for i in "hello"]
msg.pop()

my_list2 = [num for num in range(0, 100)]
my_list3 = [num * 2 for num in range(0, 100)]

my_list_even4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

my_ls2 = [1, 2, 2, 3, 4]
my_set = set(my_ls2)

print(my_set)
print(msg)
print(my_list2)
print(my_list3)
print(my_list_even4)


def get_age(age: list) -> str:
    return f"Your age: {age}"


print(get_age([118]))
