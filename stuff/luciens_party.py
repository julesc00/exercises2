
my_guests = (
    ("nous", 11),
    ("Rbk", 4),
    ("Oscar", 4),
    ("Cristian", 3),
    ("Juan Pablo", 5),
    ("Beni", 2),
    ("Paty", 3),
    ("Don Beni", 1)
)
gym_guests = (
    ("Carlitos", 2),
    ("Roberto", 1),
    ("Oscar", 2),
    ("Angel", 1),
    ("Vero", 2),
    ("Raul", 2),
    ("Lic Carlos", 2),
    ("Gerus", 2),
    ("Flavio", 1),
    ("Uriel", 1),
    ("Eduardo", 2)
)


def sum_guests() -> str:
    my_total_guests, gym_total_guests, both_sides_guests, guests_removed = 0, 0, 0, 0
    both_sides_guests_names = ("Carlitos", "Oscar", "Eduardo",)
    for guest in my_guests:
        my_total_guests += guest[1]
    for guest in gym_guests:
        gym_total_guests += guest[1]
        if guest[0] in both_sides_guests_names:
            guests_removed += guest[1]
            gym_total_guests -= guest[1]
    total_guests = (my_total_guests + gym_total_guests) + guests_removed
    return f"""
    My total guests cleaned: {my_total_guests + gym_total_guests}
    Both sides guests: {guests_removed}
    Total: {total_guests}
    """


if __name__ == "__main__":
    print(sum_guests())
