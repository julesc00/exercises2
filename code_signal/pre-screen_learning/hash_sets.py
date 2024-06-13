"""
Complexity Analysis of Hash Sets:
- Lookup: O(1) average, O(n) worst case.
- Insertion: O(1) average, O(n) worst case.
- Deletion: O(1) average, O(n) worst case.
- Space complexity: O(n)
"""


def simple_hash(input_str: str) -> int:
    """
    Hash function that takes a string and returns a hash value.
    """
    summation = sum(ord(char) for char in input_str)
    return summation % 10


print(simple_hash("Hello"))


students_ids = set()
students_ids.add(123)
students_ids.add(456)
students_ids.add(789)

print(456 in students_ids)
print(999 in students_ids)
