
def pyramid_levels():
    """Pending complete"""
    blocks = int(input("Enter the number of blocks: "))
    counter, row_iterations = blocks, []

    for num in range(blocks, 0, -1):
        print(num)
        row_iterations.append(num - 2 if num > 1 else None)
        counter -= 1
    print(row_iterations)
    print(f"The height of the pyramid: {len(row_iterations)}")


print(pyramid_levels())
