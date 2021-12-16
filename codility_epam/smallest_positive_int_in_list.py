

lst = [1, 3, 6, 4, 1, 2]
lst2 = [1, 2, 3]


def solution(A):
    sorted_lst = sorted(lst)
    lst_to_compare = sorted(A)
    for n in range(sorted_lst[0], sorted_lst[-1]):
        for x in lst_to_compare:
            if n not in sorted_lst:
                return n
            elif x not in sorted_lst:
                return lst_to_compare[-1] + 1


print(solution(lst))
