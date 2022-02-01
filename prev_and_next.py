
from itertools_practice import tee, islice, chain, zip_longest

alphabet = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"


def prev_and_next(i):
    prevs, items, nexts = tee(alphabet, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip_longest(prevs, items, nexts)


mylist = ['banana', 'orange', 'apple', 'kiwi', 'tomato']

for previous, item, nxt in prev_and_next(alphabet):
    print(f"Item is now {item}, next is {nxt} previous is {previous}")

