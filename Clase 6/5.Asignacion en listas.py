# def copiar_lista(lista_numeros:int,cantidad_elementos:int) -> list:
#     #lista_creada = funcion_punto_uno()
#     for i in range(cantidad_elementos):
#         lista_creada[i] = lista_numeros[i]

#     return lista_creada

lista_numeros = [1, 3, 5]


# Hacer esto lo que hace es solo copiar la direccion de memoria (id) de la primer lista que cree en la linea 1
# lista_numeros_dos = lista_numeros
# A
# lista_numeros_dos = [1,3,5]
# B
lista_numeros_dos = lista_numeros.copy()

# C = Hacer nuestra propia funcion que haga esto


print(f"lista_numeros = {lista_numeros}")
print(f"lista_numeros_dos = {lista_numeros_dos}")

print(f"id lista_numeros = {id(lista_numeros)}")
print(f"lista_numeros_dos = {id(lista_numeros_dos)}")

lista_numeros[0] = 10
# lista_numeros_dos[0] = 20

print(f"lista_numeros = {lista_numeros}")
print(f"lista_numeros_dos = {lista_numeros_dos}")
