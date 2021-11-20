
def non_constructible_change(coins):
    """Eliseo's approach"""
    coins.sort()
    current_change = 0

    for i in coins:
        if i > current_change + 1:
            return current_change + 1
        current_change += 1
    return current_change + 1


print(non_constructible_change([1, 3, 4, 6]))


def get_non_buildable_change(coin_list: list):
    """Norberto's approach was the best this time."""
    coin_list.sort()
    ncc = 1
    i = 0

    while i < len(coin_list) and coin_list[i] <= ncc:
        ncc += coin_list[i]
        i += 1
    return ncc
