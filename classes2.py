
class Aircraft:
    print("Welcome to class")


aircraft_obj = Aircraft()
aircraft_obj.c1 = 35
aircraft_obj.c2 = 60

print(aircraft_obj.c1)


class Test:
    var1 = 3
    print("Calling from inside the class: ", var1)


t1 = Test()
print("Calling class variable threw first instance the class: ", t1.var1)
print("class variable id: ", id(t1.var1))

t1.var1 = 5
print("Calling after assigning the value: ", t1.var1)
print("outside variable id: ", id(t1.var1))

t2 = Test()
print("Calling class variable threw second instance of the class: ", t2.var1)

extracted_var = t2.var1
print("extracted var: ", extracted_var)


class Cal(object):
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def sum(self):
        return self.val1 + self.val2

    def sub(self):
        return self.val1 - self.val2

    def prod(self):
        return self.val1 * self.val2


# Create cal instance
c1 = Cal(20, 10)
print(c1.sum())
print(c1.sub())
print(c1.prod())
