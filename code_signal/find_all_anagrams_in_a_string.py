from collections import Counter
from typing import List

"""
CodeSignal - Find All Anagrams in a String
Problem Statement:
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
    
    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
    The order of output does not matter.
"""


def is_anagram(s_counter: Counter, p_counter: Counter) -> bool:
    return s_counter == p_counter


def is_anagram_v2(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


def find_all_anagrams_in_a_string(s: str, p: str) -> List:
    p_counter = Counter(p)
    s_counter = Counter(s[:len(p) - 1])
    res = []
    for i in range(len(p) - 1, len(s)):
        s_counter[s[i]] += 1
        if s_counter == p_counter:
            res.append(i - len(p) + 1)
        s_counter[s[i - len(p) + 1]] -= 1
        if s_counter[s[i - len(p) + 1]] == 0:
            del s_counter[s[i - len(p) + 1]]
    return res


if __name__ == "__main__":
    print(find_all_anagrams_in_a_string("cbaebabacd", "abc"))
    print(find_all_anagrams_in_a_string("abab", "ab"))

    print(is_anagram(Counter("abc"), Counter("abc")))

