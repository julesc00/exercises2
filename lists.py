"""
Colecciones de Python

Tema: Tipos de datos (Data Types) Lists & tuples - iterables

1. Las listas en Python son ordenadas, mutables, y permiten duplicados.

1.1. Los tuples en Python son ordenados, inmutables y permiten duplicados.
    Tuple Note: Si solo tenemos un valor en el tuple, tiene que terminar
    con una trailing comma ej. mi_tuple = (1,)


2. Acceder a los valores de la lista

3. list methods:
    list()
    tuple(())

    len()

    append()
    clear()
    copy()
    insert()
    pop()

3.1 tuple methods:
    count()
    index()

4. Convertir un string a una list
    string.split()

5. Convertir una list a un string
    string.join(lista)
"""
import sys


# Acceder a los valores de la lista/tuple
lista = []
mi_tuple = ()
#
# print(type(lista))
# print(type(mi_tuple))


# """Saber el tamaño de una lista o un tuple"""
# print(f"Tamaño en memoria de la lista: {sys.getsizeof(lista)}")
# print(f"Tamaño en memoria del tuple: {sys.getsizeof(mi_tuple)}")
#
#
# """Acceder a los valores de una lista o un tuple por medio de su índice."""
# lista2 = [1, 2, 3, 4, 5]
# tuple2 = (6, 7, 7, 5, 3)  # El índice en python inicia de 0 1 2 3...
#
# print(lista2[2])
# print(tuple2[4])

# Acceder al último valor de una lista o tuple
# print(lista2[-2])
# print(tuple2[-2])


# len() es lo extenso de un object.
# print(len(lista2))
# print(len(tuple2))


# Editar valores de una lista.
lista3 = [9, 8, 7, 6, 5]
tuple3 = (7, 7, 6, 1)

lista3[0] = 10
lista3.insert(1, 5)
lista3.append("el último")

print(lista3)

nombre = "Panchito"
print(nombre)

# Agregar un valor a una lista







# my_list = [1, 2, 3, 4, 5]
# my_tuple = (1, 2, 3, 4, 5)
# my_tuple2 = (1, 1, 8, 3, 4, 4, 4)
#
# generated_list = [i for i in range(1, 21)]
# print(generated_list)
#
# print(f"Tamaño en memoria de la lista: {sys.getsizeof(my_list)}")
# print(f"Tamaño en memoria del tuple: {sys.getsizeof(my_tuple)}")
#
# print(f"Veces el número {my_tuple[2]}: {my_tuple.count(3)}")
# print(f"Primera ocurrencia de {my_tuple2[2]} en index: {my_tuple2.index(8)}")

# Métodos de listas


# Iterar los valores de una lista


# Challenge 1: Convertir un mensaje(string) a una list
# nombre = "Panchito"
#
# msg = "Hola como estás Panchito."
# print(len(msg))
# msg_list = list(msg.split(" "))
# print(msg_list)

# Challenge 2: 1. Cambiar nombre y 2. convertir una list a un string, 3. imprimir el resultado
# segundo_nombre = "Fulanito"

# msg_list[3] = segundo_nombre
# print(msg_list)
# msg_string = ""
# msg_string.join(msg_list)
# print(f"Mensaje: {msg_string}")
# print(type(msg_string))


# msg_list.pop()
# msg_list.append(segundo_nombre)
# print(msg_list)
# msg_list.pop()
# msg_list.insert(3, segundo_nombre)
# print(msg_list)
# new_string = " "
# msg = new_string.join(msg_list)
#
# print(new_string.join(msg_list))
# print(msg)
# my_list2 = [1, "hola", 2.30, {"msg": "hello"}]
#
#
# inp_list = ['John', 'Bran', 'Grammy', 'Norah']
# out_str = " "
# print("Converting list to string using join() method:\n")
# print(out_str.join(inp_list))
#
# this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
#
# x = this_tuple.index(8)

