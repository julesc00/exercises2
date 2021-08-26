
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
