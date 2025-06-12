# int = 10
# cadena = "50"
# entero = int(cadena)
# print(entero)

# conjunto = {3,5,9,5,3,4,3}
# print(type(conjunto))
# print(conjunto)

# DECLARAR CONJUNTO VACIO
# # conjunto = {} #NO ES UN SET ES UN DICCIONARIO
# conjunto = set()
# print(type(conjunto))
# print(conjunto)

# lista_nombres = ["Mariano","Mariano","Mariano","Ana","Ana","Juan","Jose","Maria"]

# print(f"Lista antes: {lista_nombres}")
# conjunto = set(lista_nombres)
# lista_nombres = list(conjunto)
# # print(conjunto[0])
# # conjunto[0] = "Jose"
# print(f"Lista despues: {lista_nombres}")

# conjunto_a = {1,2,3}
# conjunto_b = {3,4,5}
# conjunto_union = conjunto_a.union(conjunto_b)

# print(f"a U b = {conjunto_union}")

# conjunto_a = {1,2,3}
# conjunto_b = {3,4,5}

# Se puede hacer a-b en los conjuntos
# conjunto_resultado = conjunto_a - conjunto_b
# print(conjunto_resultado)

# METODO ADD --> Agrega un elemento al conjunto
# conjunto = {1,2,3}
# #conjunto = set()

# print(f"Antes del add {conjunto}")
# print(f"Antes del add {id(conjunto)}")
# conjunto.add(10)#Agrega el 10
# #conjunto.add(3)#No hace nada
# print(f"Despues del add {conjunto}")
# print(f"Despues del add {id(conjunto)}")

# METODO REMOVE --> Quita el elemento pasado por parametro, si este no existe rompe.

# conjunto = {1,2,3}

# print(f"Antes del remove: {conjunto}")
# #conjunto.remove(2)  Borro el elemento 2
# #conjunto.remove(10) ERROR
# print(f"Despues del remove: {conjunto}")

# METODO DISCARD --> Igual al remove pero no rompe

# conjunto = {1,2,3}

# print(f"Antes del discard: {conjunto}")
# conjunto.discard(2)  #Borro el elemento 2
# conjunto.discard(10) #No hace nada
# print(f"Despues del discard: {conjunto}")

# METODO POP --> Elimina el primer elemento del conjunto y lo devuelve

# conjunto = {1,2,3,"Mariano"}

# print(f"Antes del pop: {conjunto}")
# elemento_eliminado = conjunto.pop()
# print(f"Despues del pop: {conjunto}")
# print(f"Elemento eliminado: {elemento_eliminado}")


# METODO CLEAR --> Limpia el conjunto, lo deja vacio

# conjunto = {1,2,3}

# print(f"Antes del clear: {conjunto}")
# conjunto.clear()
# print(f"Despues del clear: {conjunto}")

# INTERCEPTION --> Realiza la intercepcion entre dos conjuntos

# conjunto_a = {1,2,3}
# conjunto_b = {3,4,5}

# conjunto_intercepcion = conjunto_a.intersection(conjunto_b)

# print(f"La intercepcion entre a y b es {conjunto_intercepcion}")

# UPDATE --> Une cualquier iterable al conjunto

# conjunto = {1,2,3}
# lista_numeros = [2,4,5,6,7,2,5,7,8,9]

# print(f"Antes del update: {conjunto}")
# # conjunto.update("Hola")
# conjunto.update(lista_numeros)
# print(f"Despues del update: {conjunto}")

# conjunto = {3,5,9,5,3,4,3}

# for elemento in conjunto:
#     print(elemento)
