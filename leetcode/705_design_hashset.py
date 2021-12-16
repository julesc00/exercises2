"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
"""
from typing import List, Any


class MyHashSet:
    """
    Note: if I only oneline the 'contains' code it will perform better than if
    I online eveything as it is.
    """
    hashset = []

    def __init__(self):
        pass

    def add(self, key: int) -> None:
        self.hashset.append(key)if key not in self.hashset else None

    def remove(self, key: int) -> None:
        print("value not in hashset") if key not in self.hashset else self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashset else False


my_hashset = MyHashSet()
print(my_hashset.add(1))
my_hashset.add(2)
print(my_hashset.contains(2))
my_hashset.remove(1)
param_3 = my_hashset.contains(2)
print(param_3)
