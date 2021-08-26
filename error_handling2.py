
def sum(n1, n2):
    try:
        return n1 + n2
    except TypeError as err:
        print(f"Enter a number, {err}")


print(sum(3, "3"))


def division2(n1, n2):
    try:
        return n1 / n2
    except (TypeError, ZeroDivisionError) as err:
        print(f"ooops, {err}")


division2(3, 0)
