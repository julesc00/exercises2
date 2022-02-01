from itertools import count, product, cycle


# Infinite iterators
def counter(n):
    """Using itertools.count()"""
    for i in count(n, n):
        if i == 35:
            break
        print(i, end=" ")


def use_cycle():
    cnt = 7
    for i in cycle("ABC"):
        if not cnt:
            break
        else:
            print(i, end=" ")
            cnt -= 1


def create_matrix(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
    return list(product(alphabet[:n], [n for n in range(1, len(alphabet[:n])+1)]))


if __name__ == "__main__":
    use_cycle()
