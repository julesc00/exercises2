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


class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    @classmethod
    def tech_detail(cls, name, technology):
        return cls(name, technology)

    @staticmethod
    def check_into_db(emp_id):
        emp_db = ['emp0010', 'emp0011', 'emp0012', 'emp0013', 'emp0014']
        if emp_id in emp_db:
            print("This employee is part of the organization.")
        else:
            print("This employee is new to our organization.")
        return "Execution completed"


emp_obj1 = Employee("Benito", "Technology")
emp_obj2 = Employee.tech_detail("Charbelito", "Python")
print(emp_obj1.department)
print(emp_obj2.department)
print(emp_obj1.name)
print(emp_obj2.name)
print(emp_obj1.check_into_db("emp0010"))
