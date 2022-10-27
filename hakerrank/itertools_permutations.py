from itertools import permutations
import re


def permutate(text, size):
    cleaned_txt = re.sub(r"^\d+\s|\s\d+\s|\s\d+$", "", text.strip().upper())
    s_size = len(cleaned_txt)
    if size < 2 or size > s_size:
        p = permutations(cleaned_txt, 2)
        for i in sorted(p):
            print("".join(i))
    else:
        p = permutations(cleaned_txt, size)
        for i in sorted(p):
            print("".join(i))
    return ""


if __name__ == "__main__":
    print(permutate("ABCD", 3))
