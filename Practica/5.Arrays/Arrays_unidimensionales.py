# 1. Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
"""def crear_array(cantidad: int) -> list:
numeros = []
for i in range(cantidad):
    numero = int(input(f"Ingrese el numero {i +1}: "))
    numeros = numeros + [numero]
return numeros"""


""" cantidad_elementos = int(input("Ingrese la cantidad de elementos(numeros): "))
lista = crear_array(cantidad_elementos)
print(f"Array creado: {lista}") """

# 2. Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.


""" def ingresar_y_crear(cantidad: int) -> list:
    return crear_array(cantidad)


cantidad = int(input("Ingrese la cantidad de numeros: "))
array = ingresar_y_crear(cantidad)
print(f"Array creado: {array}") """

# 3. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.


""" def calcular_promedio(lista: list) -> float:
    suma = 0
    cantidad = 0
    for numero in lista:
        suma += numero
        cantidad += 1
    if cantidad == 0:
        return 0
    return suma / cantidad


numeros = [10, 8, 8, 8]
promedio = calcular_promedio(numeros)
print(f"El promedio es: {promedio}") """

# 4. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.


""" def calcular_promedio_positivos(lista: list) -> float:
    suma = 0
    cantidad = 0
    for numero in lista:
        if numero > 0:
            suma += numero
            cantidad += 1
    if cantidad == 0:
        return 0
    return suma / cantidad


numeros = [10, -5, 20, -3, 0]
promedio_positivos = calcular_promedio_positivos(numeros)
print(f"El promedio de los positivos es: {promedio_positivos}") """

# 5. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.


""" def calcular_producto(lista: list) -> int:
    producto = 1
    for numero in lista:
        producto = producto * numero
    return producto


numeros = [2, 3, 4]
resultado = calcular_producto(numeros)
print(f"El producto de los elementos es: {resultado}") """

# 6. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.


""" def indice_valor_maximo(lista: list) -> int:
    if len(lista) == 0:
        return -1

    maximo = lista[0]
    posicion = 0

    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posicion = i

    return posicion


numeros = [5, 8, 12, 3, 7]
indice_max = indice_valor_maximo(numeros)
print(f"La posición del valor máximo es: {indice_max}") """

# 7. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.


""" def indices_valores_maximos(lista: list):
    if len(lista) == 0:
        print("La lista esta vacia")
        return

    maximo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero

    print(f"El valor maximo es: {maximo}")
    print(f"Se encuentra en: ")

    for i in range(len(lista)):
        if lista[i] == maximo:
            print(i)


numeros = [4, 7, 2, 7, 5]
indices_valores_maximos(numeros) """
