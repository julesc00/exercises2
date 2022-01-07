
str_list = ["primary", "prison", "prior", "prix", "prick"]


def find_longest_common_prefix(strs: list):
    if not len(strs):
        return ""
    else:
        # Define smallest and biggest strings range
        s1 = max(strs)
        s2 = min(strs)
        print(s1, s2)
        idx, match = 0, 0

        # Create a counter-trigger based on smallest-biggest index range
        # and apply this as the comparable index in the min max items.
        while idx < len(s1) and idx < len(s2) and s1[idx] == s2[idx]:
            idx += 1
            match += 1

        # Base the string chars on the longest item using the iterated found index range
        return s1[0:match]


if __name__ == "__main__":
    print(find_longest_common_prefix(str_list))
