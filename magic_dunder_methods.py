
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Optional, When I want to turn my object into a string."""
        return f"{self.name}, {self.age}"

    def __repr__(self):
        """Either one, option. To be unambiguous in the representation of an object."""
        return f"<Person('{self.name}', {self.age})>"


bob = Person("Bob", 35)
print(bob)
