

arr2 = [4, 7, 2, 6]
target2 = 8


def two_sum(lst: list[int], target: int) -> list[int]:
    values = {}

    for idx, elem in enumerate(lst):
        print(f"index: {idx}, element: {elem}")
        comp = target - elem
        print(f"comp: {comp}")
        if comp in values:
            print(f"values: {values}")
            return [values[comp], idx]
        print(f"other: {values}")
        values[elem] = idx
    return []


print(two_sum(arr2, target2))
