
"""
Calculate body mass index
"""
from decimal import Decimal


def cal_body_mass_index():
    """Calculate body mass index."""
    weight = Decimal(input("Enter your weight in kilos format: "))
    height = Decimal(input("Enter your height in this meters format: "))
    result = weight / (height * height)

    return print(f"Your BMI is: {int(result)}")


cal_body_mass_index()
