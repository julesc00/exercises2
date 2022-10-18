"""
Explanation:

"""


class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var


foo = MyClass(2)
bar = MyClass(3)

print(foo.class_var, foo.i_var)
print(bar.class_var, bar.i_var)


class ExampleClass(object):
    class_attr = 0

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr


foo2 = ExampleClass(1)
bar2 = ExampleClass(2)

# Print the instance attribute of the object foo
print(foo2.instance_attr)

# Print the instance attribute of the object bar
print(bar2.instance_attr)


# Print the class attribute of the class ExampleClass as a property of the class itself
print(bar2.class_attr)

# Print the class attribute of the class as a property of the objects foo and bar
print(foo2.class_attr)

# Try to print instance attribute as a class property
print(ExampleClass.instance_attr)


class Memorie(object):

    def __init__(self, a):
        self.a = a

    def __slots__(self):
        pass


