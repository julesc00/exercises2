"""
Print area of a square
A = side * side
"""


# def get_square():
#     side = int(input("Enter an integer value: "))
#     area = side * side
#     print("This is the: {}".format(area))
#
#     return area
#
#
# get_square()


def celsius_to_fahrenheit():
    """Change from C to F"""

    celsius = int(input("Enter a celsius: "))
    fahrenheit = 33.8
    result = celsius * fahrenheit

    print(f"Conversion is: {round(result, 2)} °F")

    return result


celsius_to_fahrenheit()
