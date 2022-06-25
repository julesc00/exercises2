
def my_capital():
    tax = 34  # Approx on 1.6 % off 213 million
    capital_in_million_pesos = 213 - tax

    # Outcomes
    outcomes = (
        # Million pesos
        ("ma_fame", 33),
        ("notre_ranch", 30),
        ("ranch_machinery", 10),
        ("mon_bmw", 2),
        ("ma_femme_bmw", 2),
        ("mes_enfants", 30),  # These would be managed by us for those underage (less than 18 years old) children
        ("ma_mere_maison", 5),
        ("ma_mere_aide", 1),
        ("mon_pere_aide", 1),
        ("mes_freres_aide", 9)  # 3 million/sibling
    )

    total_expenses = 0

    for item in outcomes:
        total_expenses += item[1]
    print(f"Total expenses in millions: ${total_expenses}")
    millions_left = capital_in_million_pesos - total_expenses

    return f"Total millions left: ${millions_left}"


if __name__ == "__main__":
    print(my_capital())
