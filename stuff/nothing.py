

def card_payments():
    total = 0
    charges = (
        ("refri_y_estufa", 1520),
        ("tenis_lucien_y_gigitte", 986),
        ("mis_audifonos", 949),
        # ("cel_samsung_galaxy", 1882),
        ("cel_mio", 1467),
        ("monitor_benq", 438)
    )
    for charge in charges:
        total += charge[1]
    return total


if __name__ == "__main__":
    print(card_payments())
