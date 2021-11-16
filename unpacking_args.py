"""
Unpacking arguments using *.
"""


def multiply(*args):
    """Example 1"""
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(1, 2, 3))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 5, 7, operator="*"))


def add(x: int, y: int) -> int:
    """Example 2"""
    return x + y


nums = [3, 5]  # Have the same number of parameters, else it'll create an error.
nums2 = (8, 9)
print(add(*nums2))


# Example 3
nums3 = {"x": 15, "y": 30}
print(add(x=nums3["x"], y=nums3["y"]))  # or
print(add(**nums3))
