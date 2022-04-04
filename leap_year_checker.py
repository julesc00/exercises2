
def check_leap_year():
    year = int(input("Enter year: "))
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(year, " is a Leap year.")
    elif year % 100 == 0:
        print(year, " is not a Leap year.")
    elif year % 400 == 0:
        print(year, " is a Leap year.")
    else:
        print(year, " is a common year.")

    return "Thanks niggah!"


if __name__ == "__main__":
    check_leap_year()
