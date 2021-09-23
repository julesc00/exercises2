print([(x, y ** 2) for x in range(3) for y in range(3)])
print([x ** 2 for x in range(10) if x % 2 > 0])
print([x.lower() for x in ["I", "AM", "NOT", "SHOUTING!"]])

# Lambda functions
txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

mark = map(lambda s: (True, s) if "anonymous" in s else (False, s), txt)
mark2 = map(lambda s: (True, s) if "functions" in s else (False, s), txt)
print(list(mark))
print(list(mark2))
