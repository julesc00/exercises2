
while True:
    try:
        age = int(input("What's your age? "))
        10 / age
        raise Exception("hey, calm down niggah!")
    except ValueError as err:
        print(f"Please, enter a number {err}")
    except ZeroDivisionError:
        print("Enter a number hight than zero")
    else:
        print("thank you")
        break
    finally:
        print("ok, I'm finally done")
    print("can you hear me?")
