
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


player1 = PlayerCharacter("julito", 14)
player2 = PlayerCharacter("michele", 9)
player1.attack = 50
player1.health = 95

print(player1.name)
print(player2.name)
print(f"Player1 membership status: {player1.membership}")
print(f"Player2 membership status: {player2.membership}")
print(f"Attack: {player1.attack}")
print(f"Player 1 health: {player1.health}")
print(f"{player1.name} is {player1.age} years old.".title())
print(f"{player2.name} is {player2.age} years old.".title())
print(player1.run())
