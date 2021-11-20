"""
Functions
    1. Default values
"""

# 1. Declarando parámetros por default.
# def add(x=10, y=8):
#     return f"Suma: {x + y}"
#
#
# print(add())


# 2. Declarando parámetros requerido y por default.
# def multiply(x, y, z=30):
#     return f"El producto es: {x * y + z}"
#
#
# print(multiply(10, 20, 50))
#
#
# def get_user_fullname(firstname, lastname, age=18, location="", blood_type=""):
#     pass


"""
3. Precedencia de parámetros: los parámetros sin valor por default son "parámetros requeridos"
y tienen precedencia sobre los por defecto.
"""


# def subtract(x=10, y):
#     return x - y
#
#
# print(subtract(20, 20))


# 4. Evitar predefinir variables y usarlas como parámetros, una vez definido un parámetro
# por defecto, la función lo conserva.


# def calc_year_born(x, y=2021):
#     year_born = y - x
#     return f"Usted nació en el año: {year_born}😱!"
#
#
# print(calc_year_born(30))
#
#
# print(calc_year_born(30, 2025))


# 5. Funciones como variables
def add2(x, y):
    return x + y


# print(add2(8, 5))
result = add2(8, 8)
print(result)

# Double: x * 2
# def double(x):
#     return x * 2


"""
List Comprehension
"""


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
mi_list = []

# for numero in sequence:
#     mi_list.append(numero)
#     print(mi_list)

doubled = [numero * 2 for numero in sequence]  # or

print(doubled)
