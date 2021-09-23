import pprint

cars = [
    {
        "model": "Mercedez",
        "year": 1995,
        "doors": 5,
        "fuel": "Electric"
    },
    {
        "model": "Mercedez",
        "year": 1995,
        "doors": 5,
        "fuel": "Electric"
    },
]
country = {
    "India": ["Delhi", "Maharastra", "Haryana",
              "Uttar Pradesh", "Himachal Pradesh"],
    "Japan": ["Hokkaido", "Chubu", "Tohoku", "Shikoku"],
    "United States": ["New York", "Texas", "Indiana",
                      "New Jersey", "Hawaii", "Alaska"]
}


def mapper(obj):
    return obj.values()


results = list(map(mapper, cars))
print(results)
print(f"My cars: {cars[0]}")
pprint.pprint(country.get("India")[0])
print(country.get("United States"))
print(cars)

example_car = cars[0].values()
pprint.pprint(f"This is an example car: {example_car}")
