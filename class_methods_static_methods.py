
"""Blueprint"""


class NameOfClass:
    class_attribute = "value"

    def __init__(self, param1, param2):
        """A constructor"""
        self.param1 = param1
        self.param2 = param2

    def method(self):
        # code
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        # code
        pass

    @staticmethod
    def static_method(param1, param2):
        # code
        pass


class PlayerCharacter:
    """Player blueprint."""

    membership = True  # Class object attribute, it's static

    def __init__(self, name, age):
        if self.membership:

            self.name = name
            self.age = age

    def run(self):
        print("run")
        return "done"

    @classmethod
    def add_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(n1, n2):  # Use staticmethod when we don't care about the class state.
        return n1 - n2


player1 = PlayerCharacter("julito", 14)
player2 = PlayerCharacter("michele", 9)
player1.attack = 50
player1.health = 95

print(f"Adding: {player1.add_things(2, 3)}")

# Class methods can be called without instantiating.
print(f"No instantiating: {PlayerCharacter.add_things(2, 3)}")
