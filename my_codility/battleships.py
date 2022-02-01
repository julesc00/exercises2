from itertools import tee, islice, chain, zip_longest


def solution(N, S, T):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
    tmp_ships, hits = S.split(","), T.split(" ")
    sunken_ships, hit_ships = 0, 0
    cleaned_ships = []

    # Create matrix
    matrix = [[f"{str(y)}{str(x)}" for x in alphabet[:N]] for y in range(1, len(alphabet[:N])+1)]

    def prev_current_next(i):
        """Format two-dimensional ships."""
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
                    h = f"{v2}{previous}"
                    t = f"{v1}{item}"
                    c = f"{v1}{nxt}"
                    two_dim_ship = [t, c, h, ship[:3]]
                    cleaned_ships.append(sorted(two_dim_ship))
        else:
            cleaned_ships.append(ship.split(" "))

    # Battle status
    print(f"Cleaned ships: {cleaned_ships}")
    exact_hit_match = []
    print(f"Hits: {hits}")
    for idx, ship in enumerate(cleaned_ships):
        if hits == ship[idx] and len(ship[idx]) == hits:
            sunken_ships += 1
        elif hits in ship[idx] and 

    return f"{sunken_ships},{hit_ships}"


if __name__ == "__main__":
    N = 4
    S = "1B 2C,2D 4D"
    T = "2B 2D 3D 4D 4A"
    print(solution(N, S, T))
