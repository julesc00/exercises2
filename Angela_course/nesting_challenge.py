"""
Instructions:
    Your are going to write a programa that adds to a travel log. You
    can see a travel_log which is a list that contains 2 dictionaries.

    Write a function that will work with the following line od code on
    line 21 to add the entry for Russia to the travel_log.
"""
TRAVEL_LOG = [
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Frankfurt", "Stuttgart"]
    },
    {
        "country": "France",
        "visits": 12,
        "cities": ["Marseille", "Paris", "Dijon"]
    }
]


def add_new_country(country: str, visits: int, cities: list):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    TRAVEL_LOG.append(new_country)

    print(f"You've visited {country} {visits} times.")
    print(f"You've been to {cities[0]} and {cities[-1]}.")
    return TRAVEL_LOG


print(add_new_country("Russia", 10, ["Moscow", "Saint Petersburg"]))


# Ginseng Calculator
def get_ginseng_total(treatment_days):
    cost_per_box = 80
    units_per_box = 10
    daily_dose = 2
    total = {}
    one_box_last = int(units_per_box / daily_dose)  # 5 days
    boxes_per_three_months = int(treatment_days / one_box_last)
    total_cost = boxes_per_three_months * 80

    total["total_boxes"] = boxes_per_three_months
    total

    print(f"la caja dura: {one_box_last} días")
    print(f"Boxes total {boxes_per_three_months}")
    print(f"Total cost in pesos: ${total_cost}")
    return

get_ginseng_total(5)
