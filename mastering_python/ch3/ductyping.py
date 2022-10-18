import datetime
import pathlib

"""
Checking whether a variable is a type of.
That same goes for a float or an integer; instead of enforcing a certain type,
just require certain features.
"""
timestamp = datetime.date(2021, 10, 5)
filename = f"{timestamp}.csv"
print(f"Filename from date: {filename}")

# Str instead of a date
timestamp2 = "2021-10-05"
filename2 = f"{timestamp2}.csv"
print(f"Filename from str: {filename2}")


# Being careful with None
def some_unsafe_function(arg=None):
    if not arg:
        arg = 123
    return arg


def some_safe_function(arg=None):
    if arg is None:
        arg = 123
    return arg


print(some_safe_function(0))
print(some_safe_function(None))

for i, item in enumerate(range(10)):
    print(i, item, end=", ")  # 0 0, 1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 9 9,

print()
my_range = range(5)
print([(i, item) for i, item in enumerate(my_range)])


# Avoid backslashes
with open("/path/to/some/file/you/want/to/read") as file_1, \
        open("open('/path/to/some/file/being/written", "w") as file_2:
    file_2.write(file_1.read())

# better approach
filename = "/path/to/some/file/you/want/to/read"
filename2 = "/path/to/some/file/being/written"
with open(filename) as file1, open(filename2) as file2:
    file2.write(file1.read())

# With pathlib, nice approach too
filename1 = pathlib.Path("/path/to/some/file/you/want/to/read")
filename2 = pathlib.Path("/path/to/some/file/being/written")
with filename1.open() as file_1, filename2.open() as file_2:
    file_2.write(file_1.read())
