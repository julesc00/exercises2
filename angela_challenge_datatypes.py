
"""
INSTRUCTIONS:
1. Write a program that adds the digits in a 2 digit number, eg. if the input was 35, then the
    output should be: 3 + 5 = 8

Warning: Don't change the code on lines 1-3, the program should work for different inputs eg. any
    two-digit number.
"""


def two_digit_add():
    """Sum a two-digit string"""
    user_input = input("Enter a 2-digit number: ")
    num1, num2 = int(user_input[0]), int(user_input[1])

    return print(f"{num1} + {num2} is: {num1 + num2}")


two_digit_add()
