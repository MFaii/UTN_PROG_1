# EJEMPLO 1 -> Ingreso un nombre por input y me dice si ese nombre esta en la lista

# lista_nombres = ["Mariano","Juan","Gabriel","Maria","Ana"]

# #1. For in range

# nombre = input("Ingrese su nombre: ")
# bandera = False

# for i in range(len(lista_nombres)):
#     if lista_nombres[i] == nombre:
#         bandera = True
#         break
#     # else:
#     #     print("NO SE ENCONTRO EL DATO")

# #2. Foreach
# for dato in lista_nombres:
#     if dato == nombre:
#         bandera = True
#         break

# if bandera == True:
#     print(f"El nombre {nombre} esta en la lista")
# else:
#     print(f"El nombre {nombre} no esta en la lista")


# EJEMPLO 2 -> Contar la cantidad de veces que un nombre aparece en la lista

lista_nombres = [
    "Mariano",
    "David",
    "David",
    "Juan",
    "Mariano",
    "Ana",
    "Mariano",
    "Yanina",
]
contador = 0
nombre = input("Ingrese su nombre: ")

for i in range(len(lista_nombres)):
    if nombre == lista_nombres[i]:
        contador += 1

if contador == 1:
    print(f"El nombre {nombre} se repite una vez")
else:
    print(f"El nombre {nombre} se repite {contador} veces")
