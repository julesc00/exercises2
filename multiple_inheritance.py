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

    def check_arrows(self):
        print(f"{self.num_arrows} arrows remaining.")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg("Borgie", 50, 100)
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
print(isinstance(wizard1, object))