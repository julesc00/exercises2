"""
Generators
"""


def make_list(num):
    result = []
    result = (result.append(((i * 2), (i * i))) for i in range(num))  # returns none instead
    # for i in range(100):
    #     result.append(((i * 2), (i * i)))
    return result


my_list = make_list(100)
print(my_list)
