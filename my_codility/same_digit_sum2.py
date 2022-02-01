import collections


def solution(a):
    additions = collections.defaultdict(list)
    for i in a:
        sum_of_each_digit = sum(int(num) for num in str(i))
        additions[sum_of_each_digit].append(i)
    print(additions)
    for item in additions.values():
        if len(item) > 1:
            max_pair = sum(item + item)
            print(f"Max pair: {max_pair}")


if __name__ == "__main__":
    arr = [51, 71, 17, 42]
    print(solution(arr))
