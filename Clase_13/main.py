# APPEND --> Me permite agregar un elemento al final de la lista

# lista_nombres = ["Mariano","Ana","Juan"]
# #lista_nombres = []

# print(f"Antes del append:{lista_nombres}")
# #lista_nombres.append("Maria")
# #lista_nombres.append(50)
# print(f"Despues del append:{lista_nombres}")

# INSERT --> Me permite insertar un elemento en la posición que yo quiera
# lista_nombres = ["Mariano","Ana","Juan"]

# print(f"Antes del insert:{lista_nombres}")
# lista_nombres.insert(1,"Maria")#Agrego a Maria en el segundo elemento
# # lista_nombres.insert(0,"Maria")#Agrego a Maria en el primer elemento
# # lista_nombres.insert(2,"Maria")#Los agrega en el anteúltimo elemento
# # lista_nombres.insert(-1,"Maria")#Los agrega en el anteúltimo elemento
# # lista_nombres.insert(len(lista_nombres),"Maria")#Lo agrega al final (ES LO MISMO QUE EL APPEND)
# # lista_nombres.insert(99999999,"Maria")#Si el indice esta fuera de rango, lo agrega al final (REPLICA EL APPEND)

# print(f"Despues del insert:{lista_nombres}")

# EXTEND --> Une una lista con otra

# lista_a = ["Mariano","Juan","Jose"]
# lista_b = ["Ana","Maria","Juliana"]

# print(f"Lista a : {lista_a}")
# print(f"Lista b : {lista_b}")

# # lista_a.extend(lista_b)
# # lista_b.extend(lista_a)
# lista_a.extend(lista_a)

# print(f"Lista a : {lista_a}")
# print(f"Lista b : {lista_b}")

# REMOVE --> Elimina la primer ocurrencia de un elemento especifico en la lista

# print("HOLA")
# raise ValueError
# print("CHAU")

# dato_a_eliminar = input("Ingrese el dato a eliminar: ")

# try:
#     lista_nombres = ["Mariano","Ana","Juan","Mariano"]
#     print(f"Antes del remove: {lista_nombres}")
#     # lista_nombres.remove("Ana")#Borra a Ana
#     # lista_nombres.remove("Mariano")#Borra al primer Mariano que encuentra
#     lista_nombres.remove(dato_a_eliminar)
#     print(f"Despues del remove: {lista_nombres}")
# except:
#     print("EL DATO A ELIMINAR NO EXISTE")

# print("EL PROGRAMA SIGUE EN CURSO")

# try:
#     division = 10 / 0
#     lista = []
#     print(lista[0])
# except ZeroDivisionError:
#     print("NO SE PUEDE DIVIDIR POR CERO")
# except:
#     print("OTRO ERROR")

# POP --> Elimina un elemento de un indice especifico en la lista, y lo devuelve

# lista_nombres = ["Mariano","Ana","Juan"]
# print(f"Antes del pop: {lista_nombres}")
# #lista_nombres.pop(0)#Borro el elemento del indice 0
# # lista_nombres.pop(1)#Borro el elemento del indice 1
# # lista_nombres.pop()#Borro el último elemento
# # lista_nombres.pop(1000)#ERROR
# elemento_borrado = lista_nombres.pop(0)
# print(f"Despues del pop: {lista_nombres}")
# # print(elemento_borrado)
# lista_nombres.insert(0,elemento_borrado)
# print(f"Despues del pop: {lista_nombres}")

# CLEAR --> Elimina todos los elementos de la lista, dejandola vacia

# lista_nombres = ["Mariano","Ana","Juan"]
# print(f"Antes del clear: {lista_nombres}")
# lista_nombres.clear()
# print(f"Despues del clear: {lista_nombres}")

# INDEX --> Devuelve la posición de la primer ocurrencia del elemento a buscar

# lista_nombres = ["Mariano","Ana","Juan","Mariano"]

# try:
#     indice = lista_nombres.index("Mariano") #0
#     # indice = lista_nombres.index("Ana") #1
#     #indice = lista_nombres.index("Maria") #ERROR
#     #indice = lista_nombres.index("Mariano",1) #3
#     print(f"Indice : {indice} - Dato: {lista_nombres[indice]}")
# except:
#     print("NO SE PUDO ENCONTRAR EL ELEMENTO PORQUE NO EXISTE EN LA LISTA")

# print("EL PROGRAMA SIGUE")

# SORT --> Me permite ordenar una lista de menor a mayor o de mayor a menor

# lista_numeros = [2,4,1,9,5]
# print(f"Antes del sort: {lista_numeros}")
# lista_numeros.sort()#ORDENA DE MENOR A MAYOR
# #lista_numeros.sort(reverse=True)#ORDENA DE MAYOR A MENOR
# print(f"Despues del sort: {lista_numeros}")

# REVERSE --> El metodo me permite ordenar al reves la lista.

# lista_nombres = ["Mariano","Ana","Juan","Maria"]
# print(f"Antes del reverse: {lista_nombres}")
# lista_nombres.reverse()
# print(f"Despues del reverse: {lista_nombres}")

# SHUFFLE --> Funcion que se encarga de ordenar de manera aleatoria los elementos de una lista

# import random

# lista_nombres = ["Mariano","Ana","Juan","Maria"]
# print(f"Antes del shuffle: {lista_nombres}")
# random.shuffle(lista_nombres)
# print(f"Despues del shuffle: {lista_nombres}")

# del --> Es una palabra reservada que me permite eliminar el objeto que yo quiera

# lista_nombres = ["Mariano","Ana","Juan","Maria"]
# print(f"Antes del DEL: {lista_nombres}")
# #del lista_nombres[0] #Elimino el indice 0 de la lista
# #del lista_nombres[1] #Elimino el indice 1 de la lista
# #del lista_nombres[-1] #Elimino el último elemento de la lista
# #del lista_nombres[1000]#ERROR
# #del lista_nombres[1:3]#Elimino lo que hay en el indice 1 y 2
# #print(lista_nombres[-1000:1000])
# #del lista_nombres[-1000:1000] #NO DA ERROR, DEJA LA LISTA VACIA
# #print(id(lista_nombres))
# #print(id(lista_nombres[-1000:1000]))
# del lista_nombres#BORRA TODO RASTRO DE LA LISTA ORIGINAL EN EL SISTEMA

# print(f"Despues del DEL: {lista_nombres}")

lista_nombres = ["Mariano", "Ana", "Jose"]

# for i in range(len(lista_nombres)):
#     print(f"Indice: {i} - Valor: {lista_nombres[i]}")

# OBJETO ENUMERATE --> Objeto que yo puedo iterar en un for para obtener automaticamente el indice y el dato de mi lista (NO ES UNA FUNCION)

# print(enumerate(lista_nombres))
for indice, dato in enumerate(lista_nombres):
    print(f"Indice: {indice} - Valor : {dato}")

# OBJETO ZIP --> Objeto que yo puedo iterar para poder recorrer varias listas a la vez (Util para arrays paralelos)

lista_nombres = ["Mariano", "Ana", "Maria"]
lista_edades = [20, 30, 40]
lista_generos = ["Masculino", "Femenino", "No Binario"]

# for i in range(len(lista_nombres)):
#     print(f"Nombre: {lista_nombres[i]}\nEdad:{lista_edades[i]} años\nGenero:{lista_generos[i]}\n")

for nombre, edad, genero in zip(lista_nombres, lista_edades, lista_generos):
    print(f"Nombre: {nombre}\nEdad:{edad} años\nGenero:{genero}\n")
