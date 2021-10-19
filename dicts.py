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
# cars[1]["model"] = "Audi"
# print(f"Changed car: {cars[1]}")


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
# print(f"My cars: {cars[0]}")
# pprint.pprint(country.get("India")[-1])
# print(country.get("United States"))
# print(cars)
#
# example_car = cars[0].values()
# pprint.pprint(f"This is an example car: {[item for item in example_car]}")
#
# pprint.pprint(mapper(country))
# print([key for key in country.keys()])

country["Japan"].append("Hiroshima")

for x, y in country.items():
    cities = f"Cities in {x}: {', '.join(y)}."

    print(cities)
