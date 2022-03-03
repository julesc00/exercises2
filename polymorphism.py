"""
Polymorphism defines the ability to take different forms. Polymorphism in Python allows us to define methods in
the child class with the same name as defined in their parent class. In this article, we will get into the
details of Polymorphism in Python in the following sequence:

Polymorphism in Python
A child class inherits all the methods from the parent class. However, in some situations, the method
inherited from the parent class doesn’t quite fit into the child class. In such cases, you will have
to re-implement method in the child class.

"""


class User:

    def sign_in(self):
        print("log in")

    def attack(self):  # It'll be overridden.
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        return print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows; {self.num_arrows} arrows left")


wizard1 = Wizard("Merlin", 60)
archer1 = Archer("Robin", 100)

# polymorphism example
for char in [wizard1, archer1]:
    char.attack()

# def player_attack(char):
#     char.attack()
#
#
# player_attack(wizard1)
# player_attack(archer1)
