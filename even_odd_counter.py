
def count_even_odd_nums():
    usr_num = int(input("Enter a number from 1 to 1000: "))
    evens, odds, counter = 0, 0, usr_num
    while counter:
        for num in range(1, usr_num+1):
            if num % 2 == 0:
                evens += 1
                counter -= 1
            elif num % 2 != 0:
                odds += 1
                counter -= 1

    return f"Evens: {evens} and Odds: {odds}"


if __name__ == "__main__":
    print(count_even_odd_nums())
