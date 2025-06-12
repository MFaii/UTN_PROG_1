#Un array bidimensional es una estructura de datos que contiene elementos separados en filas y columnas formando una tabla, se lo conoce como matriz.
#A las matrices en python se las representa como listas anidadas (una lista que dentro de si tiene varias listas)

def mostrar_matriz(mi_matriz:list) -> None:
    for fil in range(len(mi_matriz)):
        for col in range(len(mi_matriz[fil])): #len(mi_matriz[0])
            #print(f"{fil},{col}")
            print(f"{mi_matriz[fil][col]}",end=" ")
        print("")

# # 3x3
# matriz_a = [
#     [3,4,8],
#     [5,-2,10],
#     [7,-4,-1]
# ]
# matriz_a = [[3,4,8],[5,-2,10],[7,-4,1]]

# #3x2
# matriz_b = [
#     [3,6],
#     [-4,0],
#     [1,-1]
# ]

# #2x3
# matriz_c = [
#     [3,6,9],
#     [-2,0,7]
# ]

matriz_a = [
    [3,4,8],
    [5,-2,10],
    [7,-4,-1]
]

#print(matriz_a)

#Para acceder a los elementos de una matriz hay que tener en cuenta su fila y su columna 
#Yo puedo acceder solo a la fila, o puedo acceder tanto a la fila como a la columno

#Acceso
# #Quiero mostrar todos los elementos de la primer fila
# print(matriz_a[0])
# #Quiero mostrar todos los elementos de la segunda fila
# print(matriz_a[1])
# #Quiero mostrar todos los elementos de la última fila
# print(matriz_a[2])

# #La funcion len a la matriz me trae la cantidad de filas de la matriz
# cantidad_filas = len(matriz_a)
# #Quiero mostrar todos los elementos de la última fila
# print(matriz_a[cantidad_filas - 1])
# #Quiero mostrar todos los elementos de la última fila
# # print(matriz_a[-1]) #SOLO FUNCIONA EN PYTHON

# cantidad_filas = len(matriz_a)
# cantidad_columnas = len(matriz_a[0])

#Quiero mostrar el elemento que se guarda en la fila 1 columna 1
#print(matriz_a[0][0])
#Quiero mostrar el elemento que se guarda en la fila 1 columna 2
#print(matriz_a[0][1])
#Quiero mostrar el elemento que se guarda en la fila 1 columna 3
#print(matriz_a[0][2])
#Quiero mostrar el elemento que se guarda en la fila 2 columna 2
#print(matriz_a[1][1])
#Quiero mostrar el elemento que se guarda en la fila 3 columna 3
#print(matriz_a[2][2])
#Quiero mostrar el elemento que se guarda en la fila 3 columna 3
#print(matriz_a[cantidad_filas - 1][cantidad_columnas - 1])
#Quiero mostrar el elemento que se guarda en la fila 3 columna 3
#print(matriz_a[-1][-1])

#PARA ACCEDER A UN VALOR DE MI MATRIZ 
#mi_matriz[FIL][COL]

#Mostrar una matriz
#print(matriz_a) -> NO
#mostrar_matriz(matriz_a)

#MODIFICACION DE LA MATRIZ

print("ANTES")
mostrar_matriz(matriz_a)

cantidad_filas = len(matriz_a)
cantidad_columnas = len(matriz_a[0])

#Modificando el elemento de la fila 1 columna 1
matriz_a[0][0] = 10
#Modificando el elemento de la fila 2 columna 1
matriz_a[1][0] = 20
#Modificando el elemento de la fila 2 columna 2
matriz_a[1][1] = 30
#Modificando el elemento de la fila 3 columna 3
matriz_a[2][2] = 40
#matriz_a[cantidad_filas - 1][cantidad_columnas - 1] = 40
#matriz_a[-1][-1] = 40 #SOLO FUNCIONA EN PYTHON

print("DESPUES")
mostrar_matriz(matriz_a)