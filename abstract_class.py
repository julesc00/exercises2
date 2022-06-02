
"""
Abstract class
It is a different kind of class, where we create the blank class into base class. Then in the drive class we give the
functionality to those classes. Let's see an example for better understanding.

If we want to use an abstract class concept, then it is not allowed to be used directly in the Python programming
language. It has a special module to achieve an abstract class that is ABC. An example is classes (ABC).
"""
from abc import ABC, abstractmethod


# Abstract class example
class TestAbstractBaseClass(ABC):

    # Abstract method example
    @abstractmethod
    def show(self):
        print("It is a declaration of an abstract class.")


class AbstractDriveClass(TestAbstractBaseClass):
    def show(self):
        super().show()  # Referring to the base class show method.
        print("It is an implementation of an abstract class.")


abstract_obj = AbstractDriveClass()
print(abstract_obj.show())
