
class User:

    def sign_in(self):
        print("log in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        return print(f"attacking with arrows of {self.num_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
print(isinstance(wizard1, object))

