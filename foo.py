import platform

print(__name__)

print(platform.python_implementation())

words = ["hola", "hello"]
print([w[0].upper() for w in words])
