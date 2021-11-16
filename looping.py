
num = 7
user_input = input("Would like to play? (Y/n): ").lower()

if user_input == "y":
    user_num = int(input("Guess a number: "))
    if user_num == num:
        print("Got it!")
    elif abs(num - user_num) == 1:
        print("Off by one.")
    else:
        print("Sorry, it's wrong")
print("Thanks")
