"""
Ask name a print it in reverse
"""


def reversing():
    name = input("Enter your name: ")
    rev = name[::-1]
    print(f"Name in reverse: {rev}")

    return rev


reversing()


def reversing2():
    lst1 = ["a", "b", "c", "d"]
    rlst1 = reversed(lst1)

    print([x for x in rlst1])


reversing2()
