import random
import string

LETTERS = string.ascii_letters
NUMS = "01234567890"
SPE = "-+*%&$!_"


def generate_password() -> str:
    symbols = LETTERS + NUMS + SPE
    pass_len = int(input("Enter your password length: "))
    password = "".join(random.sample(symbols, pass_len))

    return password


if __name__ == "__main__":
    print(generate_password())
