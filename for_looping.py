
friends = ["Cesar", "Julito", "Jemima"]

# This iterates over the index number and not the value.
"""
Prints:
    0 is my friend.
    1 is my friend.
    2 is my friend.
"""
for friend in range(len(friends)):
    print(f"{friend} is my friend.")

# Example 2
grades = [35, 68, 98, 86, 100]

# It will print only the amount of items in the list.
amount = len(grades)
print(amount)

total = sum(grades)
print(f"Average: {total / amount}")
