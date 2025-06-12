# Cargar nuestro array (5 elementos)
lista_numeros = [0, 0, 0, 0, 0]
# lista_numeros = [0] * 5 -> SOLO FUNCIONA EN PYTHON -> PUNTO 1 DE GUIA

print(lista_numeros)

for i in range(len(lista_numeros)):
    numero = int(input("Ingrese un numero: "))
    lista_numeros[i] = numero

print(lista_numeros)

lista_numeros = [1, 2, 5, 5, 8]
