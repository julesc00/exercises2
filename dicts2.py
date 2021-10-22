"""
Python Dictionaries

    Características:
        1. Los diccionarios se usan para guardar valores de datos en pares clave:valor
        2. Desde python 3.7 son ordenados (los índices fijados en memoria).
        3. Son mutables, y no permite duplicados

"""


products = {
    "fruits": ["mango", "banana"],
    "veggies": ["apio", "papa"],
    "nuts": "peanuts"
}
print(f"Panchito las productos que llevas son: {products.values()}")

# Crear un diccionario con claves duplicadas
print("1. Diccionario duplicado")
dict_duplicado = {
    "2": 2,
    "2": 5
}
print(dict_duplicado)
print(f"{'*' * 20}\n")
###################################################################


# Crear un diccionario variado
print("2. Diccionario variado")
varied_dict = {
    "integer": 1,
    "string": "hola",
    "boolean": True,
    "float": 35.99,
    "list": [1, 2.5, "tres", False],
    "tuple": ("hello",),
    "another_dict": {"month": "Enero", "year": 2021},
    "set": {"apple", "banana", "cherry"}
}
print(varied_dict)

print(f"{'*' * 20}\n")
###################################################################


# Vaciar un diccionario
empty_dict = {
    "producto": "Compu"
}
empty_dict.clear()
print("3. Diccionario vacio")
print(f"Campos: {empty_dict}")

print(f"{'*' * 20}\n")
###################################################################


# Copiar un diccionario
dict1 = {
    "2": "dos",
    "3": "tres",
    "4": "cuatro"
}

print("4. Diccionario copiado")
dict2 = dict1.copy()
print("Copiado")
print(dict2)

print(f"{'*' * 20}\n")
###################################################################


# Acceder a un valor por su clave
print("5. Acceder un valor por su clave")
value2 = dict1["2"]

print(value2)  # ejemplo 1

print(dict1.get("9", "nada aquí"))  # ejemplo 2

print(f"{'*' * 20}\n")
###################################################################


# Mostrar valores
print("6. Imprimir solo valores")
dict_keys = dict1.keys()
dict_values = dict1.values()
print(dict_values)

print(f"{'*' * 20}\n")
###################################################################


# Imprimir clave y valor
print("7. Imprimir clave y valor")

for key, value in dict1.items():
    print(key, value)

print(f"{'*' * 20}\n")
###################################################################


# Ejercicio: Checar si existen una clave y valor específicos en el diccionario
print("8. Checando si están la clave:valor específicos")


print(f"{'*' * 20}\n")
###################################################################


# Insertar clave y valor, si no existen
print("9. Insertar clave y valor, si no existe")
dict1.update({"5": "cinco"})
print(dict1)

print(f"{'*' * 20}\n")
###################################################################


# Editar valor
print("10. Editar valor")
dict1.update({"2": "doss"})
print(dict1)

print(f"{'*' * 20}\n")
###################################################################


# Insertar clave y valor si no existe, si existe lo retorna, no lo edita
print("11. Insertar clave y valor si no existe, si existe lo retorna, no lo edita")
dict1.setdefault("7", "siete")
dict1.setdefault("7", "manzana")
print(dict1)

print(f"{'*' * 20}\n")
###################################################################


# Insertar clave y valor si no existe, si existe lo retorna, no lo edita
print("12. Insertar clave y valor si no existe, si existe lo retorna, no lo edita")
dict1 = {**dict1, **{"6": "seis"}}
print(dict1)

print(f"{'*' * 20}\n")
###################################################################


# Editar clave
print("13. Editar clave")
dict1["2s"] = dict1.pop("2")

print(dict1)

print(f"{'*' * 20}\n")
###################################################################


# Retornar un diccionario agregando con claves y valores declarados
print("14. Retornando un diccionario de los valores declarados")
campo = ["key1", "key2"]
valor = ""
dict3 = dict.fromkeys(campo, valor)
print(dict3)

print(f"{'*' * 20}\n")
###################################################################
