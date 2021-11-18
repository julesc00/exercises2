

arr2 = [4, 7, 2, 6]
target2 = 13


def two_sum(lst: list[int], target: int) -> list[int]:
    values = {}

    for idx, elem in enumerate(lst):
        comp = target - elem
        if comp in values:
            return [values[comp], idx]
        values[elem] = idx

    return []


print(two_sum(arr2, target2))
