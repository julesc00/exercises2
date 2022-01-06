

def solution(lst):
    n = len(lst)
    max_e_pairs = 0
    for _ in range(2):
        prev_n = lst[-1]
        i, e_pair, l_taken = 0, 0, False

        while i < n:
            current_n = lst[i]
            s = prev_n + current_n
            if s % 2 == 0:
                if i == 0:
                    l_taken = True
                if not i == n-1 and l_taken:
                    e_pair += 1
                    i += 1
            if i < n:
                prev_n = lst[i]
            i += 1

        if e_pair > max_e_pairs:
            max_e_pairs = e_pair
        lst = lst[-1:] + lst[:-1]
    return max_e_pairs


if __name__ == "__main__":
    nums = [4, -4, 8, 2, -4, -4, 2, 8, -4, 4]
    nums2 = [4, 2, 5, 8, 7, 3, 7]
    print(solution(nums2))
