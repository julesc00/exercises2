
def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    max_occurrence = 1
    index = 0

    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]] + 1
            if tmp > max_occurrence:
                max_occurrence = tmp
                index = i
            count[A[i]] += 1
        else:
            count[A[i]] = 1
    return A[index]


if __name__ == "__main__":
    print(solution(3, [1, 2, 3, 3, 1, 3, 1]))
