from itertools import product


def list_combinations() -> list:
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    z = int(input("Enter z coordinate: "))
    n = int(input("Enter delimiter: "))

    return [list(i) for i in product(range(x+1), range(y+1), range(z+1)) if sum(i) != n]


if __name__ == "__main__":
    print(list_combinations())
