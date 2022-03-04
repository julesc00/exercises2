from collections import Counter

c = Counter()


def count_occurrences() -> dict:
    names = ["Julio", "Claudia", "Julio", "Brigitte", "Jemima", "Cesar"]

    for i in names:
        c[i] += 1
    return c


if __name__ == "__main__":
    print(count_occurrences())
