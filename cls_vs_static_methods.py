from datetime import date
import sys


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A class method to create a Person object by birth year.
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    # A static method to check if a Person is an adult or not.
    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person("benito", 4)
person2 = Person.from_birth_year("charbel", 2021)
person3 = Person.from_birth_year("Cari", 2001)

print(person1.age)
print(person2.age)
print(f"{person3.name} is {person3.age} years old.")
print(sys.getrefcount(person3))
