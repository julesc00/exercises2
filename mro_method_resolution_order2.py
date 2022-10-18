"""
Explanation:

The method called first will be the one defined within the child class and then the parent's
since both have the same name.
"""
class A:
    def rk(self):
        print("In class A")


class B:
    def rk(self):
        print("In class B")


r = B()
print(r.rk())
