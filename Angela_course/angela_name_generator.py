"""
1. Create a greeting for your program.
2. Ask the user for the city they grew up in.
3. Ask the user for the name of a pet.
4. Combine the name of their city and pet and show them their band name.
Note: Make sure the input cursor shows on a new line.
"""


def band_name_generator():
    city = input("Enter the city you grew up in: \n")
    pet_name = input("Enter a pet name: \n")

    return print(f"This is band name: {pet_name.title()} {city.title()}")


band_name_generator()
