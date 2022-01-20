
def map_point(arr, r, c):
    arr[r][c] = 2


def map_ship(arr, r1, c1, r2, c2):
    if c1 == c2:
        for r in range(r1, r2+1):
            arr[r][c1] = 1
    else:
        for c in range(c1, c2+1):
            arr[r1][c] = 1
            arr[r2][c] = 1


def get_index_by_char(char):
    return ord(char) - ord("A")


def get_vals(arr, shift):
    r1, c1, r2, c2 = shift[0], shift[1], shift[2], shift[3]
    items = []

    if c1 == c2:
        for r in range(r1, r2+1):
            items.append(arr[r][c1])
    else:
        for c in range(c1, c2+1):
            items.append(arr[r1][c])
            items.append(arr[r2][c])

    return items


def sunken(arr, shift):
    items = get_vals(arr, shift)
    return all(el == 2 for el in items)


def hit(arr, shift):
    items = get_vals(arr, shift)
    return any(el == 2 for el in items)


def solution(N, S, T):
    data = [[] for _ in range(N)]
    for i in range(N):
        data[i] = [0] * N
        ships = S.split(",")
        tmp_shifts = []
        for ship in ships:
            cells = ship.split()
            first_where = cells[0]
            first_where_r = int(first_where[0:-1]) - 1
            first_where_c = get_index_by_char(first_where[-1])
            second_where = cells[1]
            second_where_r = int(second_where[0:-1]) - 1
            second_where_c = get_index_by_char(second_where[-1])
            map_ship(data, first_where_r, first_where_c, second_where_r, second_where_c)
            tmp_shifts.append((first_where_r, first_where_c, second_where_r, second_where_c))

        for cell in T.split():
            row = int(cell[0:-1]) - 1
            col = get_index_by_char(cell[-1])
            map_point(data, row, col)

        res_1, res_2 = 0, 0
        for shift in tmp_shifts:
            if sunken(data, shift):
                res_1 += 1
            elif hit(data, shift):
                res_2 += 1

        return f"{res_1}{res_2}"


if __name__ == "__main__":
    N = 4
    S = "1B 2C,2D 4D"
    T = "2B 2D 3D 4D 4A"
    print(solution(N, S, T))
