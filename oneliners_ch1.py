squares = [i ** 2 for i in range(10)]
print(squares)

# Arithmetic Operations
x, y = 3, 2
print(x + y)  # 5
print(x - y)  # 1
print(x * y)  # 6
print(x / y)  # 1.5
print(x // y)  # 1 - performs an integer division, the result is rounded.
print(x % y)  # 1
print(abs(-x))  # Absolute value -3
print(f"Absolute: {abs(x + 5j)}")
print(int(3.9))  # 3
print(float(x))  # 3.0
print(x ** y)  # 9

"""Booleans """
# Booleans
x = 1 > 2
y = 2 > 1
print(x)
print(y)

# keywords: and, or, not
x, y = True, False

print((x or y) == True)
print((x and y) == False)
print((not y) == True)
if None or 0 or 0.0 or "" or [] or {} or set():
    print("Dead code")

# Strings
y = "   This is lazy\t\n   "
print(y.strip())
print("DrDre".lower())
print("attention".upper())
print("smartphone".startswith("smart"))
print("smartphone".endswith("phone"))
print("another".find("other"))
print("cheat".replace("ch", "m"))
print(",".join(["F", "B", "I"]))
print(len("Caricia"))
print("ear" in "earth")

# The Keyword None
def f():
    x = 2

print(f() is None)


# Container Data Structures
# Lists
y = x = 3
print(x is y)
print(x)
print(y)

lst = [1, 2, 2]
lst.append(4)
print(lst)

lst2 = [1, 2, 4]
lst2.insert(2, 3)
print(lst2)

print([1, 2, 2] + [4])

fruits = ["apple", "banana", "cherry"]
cars = ["BMW", "Audi", "Tesla"]
fruits.extend(cars)
print(fruits)

fruits.remove("apple")
print(fruits)

lst2.reverse()
print(lst2)
fruits.sort()
print(fruits)

stack = [3]
stack.append(42)
print(stack)
stack.pop()
stack.pop()
print(stack)

# hero = "Jesuschrist"
# heroine = "Virgin Mary"
# print(hash(hero))
# heroes = {"hero", "heroine"}
# print(hash(heroes))

calories = {"apple": 52, "banana": 89, "chocolate": 548}

print(calories["apple"] < calories["banana"])

calories["cappu"] = 75
print(calories)

for k, v in calories.items():
    print(k) if v > 500 else None

print(52 in [2, 39, 52])
print("list" in {"list": [1, 2, 3], "set": {1, 2, 3}})

# List and  comprehension
nums = [x for x in range(3)]
print(nums)

# (name, $-income)
customers = [("Charbelito", 2400000),
             ("Benito", 145500),
             ("Jules", 543434),
             ("Michelina", 9832300)]

# your high value customers earning >$1M
whales = [x for x, y in customers if y > 1000000]
print(whales)

cars = [("BMW", 760000),
        ("Audi", 567000),
        ("Mercedes-Benz", 890000)]

most_expensive_car = [x for x, y in cars if y > 800000]
print(most_expensive_car)
cheapest = min(cars)
caro = max(cars)
print(f"The cheapest is the {cheapest[0]} at $\
{cheapest[1]} pesos, and the most expensive is {caro[0]}\
 at ${caro[1]} pesos.")

# if, else, elif list comprehension
# x = int(input("your value: "))
if x > 3:
    print("Big")
elif x == 3:
    print("Medium")
else:
    print("Small")

# Loop declarations
for i in [0, 1, 2]:
    print(i)

# while loop - same semantics
j = 0
while j < 3:
    print(j)
    j = j + 1


# functions
# Add percentage
def appreciate(x, percentage):
    return x + x * percentage / 100  # return x plus x divided by percentage and then x divided by 100


print(appreciate(200, 5))

# Lambda functions
print((lambda x: x + 3)(5))

