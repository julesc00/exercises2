
ROMAN = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]


def num_to_roman(num):
    result = ""
    for (a, r) in ROMAN:
        (factor, num) = divmod(num, a)
        result += r * factor

    return result


print(num_to_roman(56))
