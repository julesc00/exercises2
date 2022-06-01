
def pass_check(var1):
    if var1 == "5678":
        print("Welcome")
        return True
    else:
        print("Wrong password!!!")


def user_input():
    for x in range(4):
        if x == 3:
            print("Your wrong password limit is exceeded.")
            break
        else:
            v1 = input("Enter your ATM PIN: ")
            v2 = pass_check(v1)
            if v2:
                break


if __name__ == "__main__":
    user_input()
