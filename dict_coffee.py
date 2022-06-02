
VENDING_MACHINE = {
    1: "coffee",
    2: "masala tea",
    3: "lemon tea",
    4: "latte",
    5: "black tea",
    6: "cappuccino"
}


def user_input():
    [print(k, v) for k, v in VENDING_MACHINE.items()]
    user_choice = int(input("Please select a choice number from the list: "))
    if user_choice:
        choice = VENDING_MACHINE.get(user_choice)
        if choice:
            print(f"Machine is releasing: {choice}")
        else:
            print("Please select from given choices: ")
            user_input()
    else:
        print("Please enter a valid choice: ")
        user_input()


if __name__ == "__main__":
    user_input()
