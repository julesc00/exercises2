import itertools

counter = itertools.count(start=5, step=-2.5)


def count2():
    print(next(counter))
    print(next(counter))


def map_data():
    data = [100, 200, 300, 400]
    # daily_data = list(zip(counter, data))
    data_dict = dict(zip(counter, data))
    # print(daily_data)
    print(data_dict)


if __name__ == "__main__":
    count2()
    map_data()
