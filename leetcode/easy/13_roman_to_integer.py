
ROMANS = [
    ("I", 1),
    ("V", 5),
    ("IX", 9),
    ("X", 10),
    ("XL", 40),
    ("L", 50),
    ("C", 100),
    ("M", 1000)
]


def roman_to_int(r: str) -> str:
    rom_lst = [char.capitalize() for char in r]
    for rom in rom_lst:
        room = ROMANS[]
    print(rom_lst)


if __name__ == "__main__":
    roman_to_int("XX")
