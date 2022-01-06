

str_list = ["primary", "prison", "prior"]


def find_longest_common_prefix(strs: list):
    if not len(strs):
        return ""
    else:
        s1 = max(strs)
        s2 = min(strs)
        i, match = 0, 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1
            match += 1
        return s1[0:match]


if __name__ == "__main__":
    print(find_longest_common_prefix(str_list))
