
def find_longest_common_prefix(lst: list) -> str:
    """
    1. Define the iterated min-max item range using: min(), max()
    2. Create counter and automatic idx to use as the dynamic item indexing.
    3. Iterate min max chars as long as idx is less than both items, while counter increments to break
        the loop, and as long as both max and min items chars are the same.
    :return: str with only the common prefix iterated chars among the min and max items.
    """
    max_str = max(lst)
    counter = 0

    for i in lst:
        if i[0] == max_str[0]:
            counter += 1
    print(f"Counter: {counter}")
    # Remove items that don't match to max_str delimiter.
    [lst.pop(lst.index(i)) if i[0] != max_str[0] else None for i in lst]

    min_str, idx = min(lst), 0
    common_char = max_str[0]
    if not len(lst) or counter == 1:
        return ""
    while idx < len(max_str) and idx < len(min_str) and max_str[idx] == min_str[idx]:
        counter += 1
        idx += 1
    return max_str[0:idx]


if __name__ == "__main__":
    strs = ["primary", "prix", "print", "prior", "aaaa"]
    strs2 = ["primary", "aaaa"]
    print(find_longest_common_prefix(strs2))
