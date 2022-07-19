from collections import namedtuple as nt


class Solution:
    def __init__(self, lst, k):
        self.lst = lst
        self.k = k

    def swap_nodes(self):
        self.lst = [1, 2, 3, 4, 5]
        self.k = 2

        node_front = self.lst[self.k]
        rear_node = self.lst[-self.k]

        for item in self.lst:

