
# Frozen set example
frozen_set_example = frozenset(["this", "is", "a", "frozen", "set", "set"])

print(frozen_set_example)
vegetables = ["Spinach", "Carrots", "Kale", "Garlic", "Potatoes", "Tomatoes", "Cabbage"]
print(vegetables[-4])

my_list = [1, 2, 3, 4, 4, 5, 5, 6]
print(set(my_list))

# Another way to create a set
my_set = set([1, 2, 3, 4, 4])
print(my_set)

fruits1 = {"apple", "grapes", "mango"}
fruits2 = {"watermelon", "apples", "mango"}
fruits1.add("papaya")
print(fruits1)

total_fruits = fruits1.union(fruits2)
print(total_fruits)

print(fruits1.difference(fruits2))
print(fruits1.intersection(fruits2))
print(fruits1.isdisjoint(fruits2))
print(fruits1.issubset(fruits2))
