from functools import reduce


msg = ["Python", "programming", "is", "awesome!"]
print(list(map(lambda x: x.upper(), msg)))
print(list(filter(lambda x: len(x) < 8, msg)))

print(reduce(lambda x, y: x + y, msg))
