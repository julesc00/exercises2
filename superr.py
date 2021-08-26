
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("log in")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
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


wizard1 = Wizard("Merlin", 60, "merlin@gmail.com")
archer1 = Archer("Robin", 100)

print(wizard1.email)

# introspection
print(dir(wizard1))
