"""
OOP: Intro to Object Oriented Programming

Functions and Methods:
    Characteristics:
        A function is a block of code which only runs when it is called.
        You can pass data, known as parameters, into a function.
        A function can return data as a result.

    1. DRY - Do not Repeat Yourself.
    2. Encapsulation
    3. Re-usability

    4. Function declaration
        - Un parámetro es la variable enlistada dentro del paréntesis en la definición
            de la función.
        - Un argumento es el valor que es enviado a la función cuando es invocada.
        - El número de parámetros en la función pide el mismo número de argumentos
            cuando sea invocada.
    5.
"""

NAMES = ["lupita", "paco"]


def saludar_a_alguien():
    """Saludar a alguien."""

    name = "Panchito"
    return name


def sumar_numeros():
    """Sumar dos números."""

    result = 20 + 20
    return result


def dar_nombre(name):  # name es un parámetro, valor pasado a una función en su declaración.
    return name


def restar_nums(x, y):
    """Restar dos números."""

    result = x - y
    return result


def hello_world(name):
    return f"Hello {name.title()}"
