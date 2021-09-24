"""
Convert Celsius to Fahrenheit
"""


def celsius_to_fahrenheit(value):
    """Change from °C to °F"""

    celsius = float(value)
    fahrenheit = 33.8
    result = celsius * fahrenheit

    print(f"Conversion is: {round(result, 2)} °F")

    return result
