"""
Linear time algorithms mean that every single element from the input is visited exactly once,
O(n) times. As the size of the input, N, grows our algorithm’s run time scales exactly with
the size of the input.

Linear running time algorithms are widespread. Linear runtime means that the program visits
every element from the input. Linear time complexity O(n) means that as the input grows,
the algorithms take proportionally longer to complete.2 Apr 2019
"""
shopping_list = ["Bread", "Butter", "The Nacho Libre soundtrack from the 2006 film Nacho Libre",
                 "Reusable Water Bottle"]

[print(item) for item in shopping_list]


# Largest item in a list
items = [2, 16, 7, 9, 8, 23, 12]


def get_max_item(lst: list) -> int:
    return max(items)


# or
def get_max_item2(lst: list) -> int:
    max_item = lst[0]
    for item in lst:
        if item > max_item:
            max_item = item
    return max_item


if __name__ == "__main__":
    print(get_max_item(items))
    print(get_max_item2(items))
