"""
Explanation:

Since D class has no implemented same name method, it will call the first parent-class which is B(), then
the following C(), and at last the super-class method from A().
"""
class A:
    def rk(self):
        print("In class A")


class B:
    def rk(self):
        print("In class B")


class C:
    def rk(self):
        print("In class C")


# Class ordering
class D(B, C):
    pass


r = D()
print(r.rk())
