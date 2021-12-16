
lst = [9, 3, 9, 3, 9, 8, 9]


def match_odd_occurrences():
    """Complexity: O(N) or O(N*log(N))"""
    temp_dict = {}
    for x in lst:
        if x in temp_dict:
            temp_dict[x] += 1
        else:
            temp_dict[x] = 1

    print(temp_dict)
    for k, v in temp_dict.items():
        if v % 2 == 1:
            return k


if __name__ == "__main__":
    print(match_odd_occurrences())
