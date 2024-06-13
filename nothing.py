import time
import random
my_set = set()
for i in range(10):
    my_set.add(i)


def sort_set():
    large_set = {random.randint(0, 1000000) for _ in range(1000000)}
    print(type(large_set))
    # Measure the time taken to sort the set
    start_time = time.time()
    sorted_list = sorted(large_set, reverse=True)
    print(type(sorted_list))
    end_time = time.time()

    print(f"Time taken to sort: {end_time - start_time} seconds")
    print(f"Number of records: {len(sorted_list)}")


sort_set()


def sort_list():
    large_list = [random.randint(0, 1000000) for _ in range(1000000)]

    # Measure the time taken to sort the list
    start_time = time.time()
    sorted_list = sorted(large_list, reverse=True)
    end_time = time.time()

    print(f"Time taken to sort: {end_time - start_time} seconds")
    print(f"Number of records: {len(sorted_list)}")


sort_list()


def solution(n):
    nums = []
    str_n = str(n)

    for i in str_n:
        nums.extend([int(i)])
    n_sum = sum(nums)
    return n_sum


print(solution(29))
