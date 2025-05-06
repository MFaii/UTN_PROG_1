lista_numeros = [None, None, None, None, None]
respuesta = "si"

print(lista_numeros)

while respuesta == "si":
    indice = int(input("Ingrese el indice en donde guardar el dato: "))

    while indice >= len(lista_numeros) or indice < 0:
        indice = int(input("ERROR Reingrese el indice en donde guardar el dato: "))

    numero = int(input("Ingrese el dato: "))
    lista_numeros[indice] = numero
    respuesta = input("¿Quiere seguir intentando? si/no")

for i in range(len(lista_numeros)):
    if lista_numeros[i] != None:
        print(f"elemento: {lista_numeros[i]} indice:{i}")
