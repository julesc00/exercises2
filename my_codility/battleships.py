from itertools import tee, islice, chain, zip_longest


def solution(N, S, T):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
    tmp_ships, hits = S.split(","), T.split(" ")
    print(tmp_ships)
    sunken_ships, hit_ships = 0, 0
    cleaned_ships = []

    # Create matrix
    x_area = [ltr for ltr in alphabet[:N]]
    y_area = [n for n in range(1, len(x_area) + 1)]
    matrix = [[f"{str(y)}{str(x)}" for x in x_area] for y in y_area]

    def prev_current_next(i):
        prevs, items, nexts = tee(i, 3)
        prevs = chain([None], prevs)
        nexts = chain(islice(nexts, 1, None), [None])

        return zip_longest(prevs, items, nexts)

    # Ships sanitization
    for ship in tmp_ships:
        # One-space ship with NL format
        if ship[:2] == ship[3:5]:
            cleaned_ship = [ship[:2]]
            cleaned_ships.append(cleaned_ship)
        # One-space ship with NNL format
        elif ship[:3] == ship[4:7]:
            cleaned_ship2 = [ship[:3]]
            cleaned_ships.append(cleaned_ship2)
        # two-dimensional ship
        elif ship[0] != ship[3] and ship[1] != ship[4]:
            for previous, item, nxt in prev_current_next(alphabet):
                if ship[1] == item:
                    v1, v2 = int(ship[0]) + 1, int(ship[3]) - 1
                    t = f"{v1}{item}"
                    c = f"{v1}{nxt}"
                    h = f"{v2}{previous}"
                    two_dim_ship = [t, c, h, ship[:3]]
                    cleaned_ships.append(sorted(two_dim_ship))

        else:
            cleaned_ships.append(ship.split(" "))
    print(f"Cleaned ships: {cleaned_ships}")
    print(f"Hits: {hits}")

    # Battle status
    exact_hit_match = []
    for ship in cleaned_ships:
        if hits == ship:
            sunken_ships += 1
        else:
            for hit in hits:
                if hit in ship and len(hit) < len(ship):
                    hit_ships += 1
                elif hit in ship:
                    exact_hit_match.append(hit)
                    if exact_hit_match == ship:
                        sunken_ships += 1

    print(f"Exact hit match: {exact_hit_match}")
    return f"{sunken_ships},{hit_ships}"


if __name__ == "__main__":
    N = 3
    S = "1A 1B,2C 2C"
    T = "1B"
    print(solution(N, S, T))
