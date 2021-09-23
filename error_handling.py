age = None
while True:
    try:
        age = int(input("What's your age?: "))
        result = 10 / age
        print(f"Your age is: {result}")
    except ValueError:
        print("Please, enter a number")
    except ZeroDivisionError:
        print("Enter a number higher than zero")
    else:
        print("Danke!")
        break
