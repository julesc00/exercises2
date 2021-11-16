
num = 7

while True:
    user_input = input("Would like to play? (Y/n): ").lower()
    if user_input == "n":
        print("Thanks :(")
        break
    else:
        user_num = int(input("Guess a number: "))
        if user_num == num:
            print("Got it!")
        elif abs(num - user_num) == 1:
            print("Off by one.")
        else:
            print("Sorry, it's wrong")

