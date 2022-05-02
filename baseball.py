from itertools import tee, islice, chain, zip_longest



OPS = ["5", "2", "C", "D", "+"]


def cal_points():
    line = input("Enter score: ")
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    abc = ("C", "D", "+")
    ops = []
    total = []
    format_vals(line, nums, abc, ops)
    print(ops)

    # Remove previous value
    for i in ops:
        if i == "C":
            ops.pop(ops.index(i) - 1)
    print(ops)

    # Multiple * 2 the previous value and add it to the list
    for i in ops:
        if i == "D":
            temp_val = int(ops.pop(ops.index(i) - 1))
            print(f"Val: ", temp_val)
            val = int(temp_val * 2)
            ops.append(val)
    print(ops)


def prev_and_nxt(lst):
    prevs, items, nexts = tee(lst, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip_longest(prevs, items, nexts)


def format_vals(line, nums, abcs, ops):
    for i in line:
        if i in nums:
            ops.append(int(i))
        if i in abcs:
            ops.append(i)
    return ops


if __name__ == "__main__":
    cal_points()
