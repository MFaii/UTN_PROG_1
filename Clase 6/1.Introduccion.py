# Un arreglo es una estructura de datos que organiza un conjunto de elementos bajo un mismo nombre
# En programacion tenemos dos tipos de arreglos

# Unidimensionales -> Sus elementos se organizan uno tras otro bajo una misma dimensión -> Vectores
# Bidimensionales -> Los elementos se organizan uno tras otro en dos dimensiones -> Matrices (Filas/Columnas)

# Los arreglos distinguen cada uno de los elementos mediante un indice
# Los arreglos los vamos a expresar con el tipo de dato list


def contar_elementos(mi_arreglo: list) -> int:
    contador = 0
    for elemento in mi_arreglo:
        contador += 1

    return contador


# Inicializar arrays vacios
# mi_arreglo = []
# mi_arreglo = list()

mi_arreglo = [5, 3, 2, 1, 9]
# print(mi_arreglo)

# ACCESO A CADA UNO DE LOS ELEMENTOS

# Primer elemento
# print(mi_arreglo[0])
# Segundo elemento
# print(mi_arreglo[1])

# Ultimo elemento
# print(mi_arreglo[4])
# SOLO FUNCIONA EN PYTHON (CUIDADO AL USARLO EN OTRO LENGUAJE)
# print(mi_arreglo[-1])

# ERROR -> Indice fuera de rango
# print(mi_arreglo[5])

# La funcion me permite saber la cantidad de ELEMENTOS en mi array
# cantidad_elementos = len(mi_arreglo)
# print(mi_arreglo[cantidad_elementos - 1])

# print(contar_elementos(mi_arreglo))

# Mostrando un array

# print(mi_arreglo)

# For in range
# for i in range(len(mi_arreglo)):
#     print(f"Elemento: {mi_arreglo[i]} - Indice: {i}")

# mi_arreglo[0] = 10
# mi_arreglo[4] = 20

# ERROR
# mi_arreglo[5] = 100

# for i in range(len(mi_arreglo)):
#     if mi_arreglo[i] % 2 == 1:
#         mi_arreglo[i] = 0
#     print(f"Elemento: {mi_arreglo[i]} - Indice: {i}")

# Foreach

# for elemento in mi_arreglo:
#     print(f"Elemento: {elemento}")
