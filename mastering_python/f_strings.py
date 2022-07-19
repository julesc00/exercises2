
NAME = "Julito"

val = 1 / 3

print("Hello {0}, value: {1:.3f}. Bye {0}".format(NAME, val))

# Named variables
print("Hi %(NAME)s" % dict(NAME=NAME))
print(f"Hi {NAME}".format(**globals()))

# Arbitrary expressions
username = "Charbelito"
a = 123
b = 456

some_dict = dict(a=a, b=b)
print(f"a: {some_dict.get('a')}")
print(f"sum: {some_dict.get('a') + some_dict.get('b')}")

# Python expressions, specifically an inline if statement
print(f"If statement: {a if a > b else b}")

# Function calls
print(f"Min: {min(a, b)}")
print(f"Hi {username.title()}. Uppercase: {username.upper()}")

# Loops
print(f"Square: { [x ** 2 for x in range(5)]}")
