
if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())

    if n < 3:
        num_str = "".join(str(y) for y in range(1, 3+1)) + "".join(str(x) for x in range(4, n+1))
        print(num_str)
    else:
        num_str = "".join(str(y) for y in range(1, 3+1)) + "".join(str(x) for x in range(4, n+1))
        print(num_str)
