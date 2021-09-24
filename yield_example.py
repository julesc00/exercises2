"""
"return" returns a value and "yield" returns a generator and
it iterates or has to be iterated to access its values.
"""


def generator():
    yield "Welcome"
    yield "Me the Gee!"
    yield "is in the House!"


gen_obj = generator()

print(type(gen_obj))
for i in gen_obj:
    print(i)
