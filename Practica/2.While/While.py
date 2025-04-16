# 1. Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

"""repeticion = 0

while repeticion < 10:
    num = 1
    while num <= 10:
        print(num, end=" ")
        num += 1
    print()
    repeticion += 1"""


# 2. Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

""" repeticion = 0
while repeticion < 10:
    num = 10
    while num >= 1:
        print(num, end=" ")
        num -= 1
    print()
    repeticion += 1 """


# 3. Mostrar la suma de los números desde el 1 hasta el 10.

""" suma = 0
num = 1

while num <= 10:
    suma += num
    num += 1

print(f"La suma es: {suma}") """


# 4. Mostrar la suma de los números pares desde el 1 hasta el 10.

""" suma_pares = 0
num_pares = 1

while num_pares <= 10:
    if num_pares % 2 == 0:
        suma_pares += num_pares
    num_pares += 1

print(f"La suma de los pares es {suma_pares}") """


# 5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

""" contador = 0
suma = 0

while contador < 5:
    num = float(input("Ingrese un numero: "))
    suma += num
    contador += 1

promedio = suma / contador

print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}") """


# 6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

""" suma = 0
contador = 0
checkpoint = "s"
promedio = 0

while checkpoint == "s":
    num = float(input("Ingrese un numero: "))
    suma += num
    contador += 1
    checkpoint = input("Desea ingresar otro numero? (s/n): ").lower()

if contador > 0:
    promedio = suma / contador

print(f"La suma de los numeros es: {suma}")
print(f"El promedio es: {promedio}") """

# 7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

""" suma_positivos = 0
producto_negativos = 1
checkpoint = "s"

while checkpoint == "s":
    numero = float(input("Ingrese un numero: "))

    if numero >= 0:
        suma_positivos += numero
    else:
        producto_negativos *= numero

    checkpoint = input("Desea ingresar otro numero? (s/n): ").lower()

print("Suma de los numeros positivos:", suma_positivos)
print("Producto de los numeros negativos:", producto_negativos) """


# 8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.

""" minimo = None
maximo = None
contador = 0

while contador < 10:
    contador += 1
    num = int(input("Ingrese 10 numeros enteros: "))

    if minimo is None or num < minimo:
        minimo = num
    if maximo is None or num > maximo:
        maximo = num

print(f"El minimo es: {minimo}")
print(f"El maximo es: {maximo}") """


# ANEXO

# 9. Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

""" suma = 0
contador = 0

while True:
    num = float(input("Ingrese como minimo 5 numeros: "))
    suma += num
    contador += 1

    if contador >= 5:
        continuar = input("Desea ingresar mas numeros? s/n").lower()
        if continuar != "s":
            break

promedio = suma / contador

print(f"Cantidad de numeros ingresados: {contador}")
print(f"Suma total: {suma}")
print(f"Promedio: {promedio}") """

# 10. Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

""" suma = 0
contador = 0

while True:
    num = float(input("Ingrese como minimo 5 numeros y como maximo 10: "))
    suma += num
    contador += 1

    if contador >= 5:
        if contador == 10:
            print("Se alcanzo el maximo de 10 numeros")
            break
        continuar = input("Desea ingresar mas numeros? s/n").lower()
        if continuar != "s":
            break

promedio = suma / contador
print(f"Cantidad de numeros ingresados: {contador}")
print(f"Suma total: {suma}")
print(f"Promedio: {promedio}") """

# Integrador While

"""
1. Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
A. La suma acumulada de los números negativos.
B. La suma acumulada de los números positivos.
C. La cantidad de números negativos ingresados.
D. El promedio de los números positivos.
E. El número positivo más grande.
F. El porcentaje de números negativos ingresados, respecto del total de ingresos. 
"""

""" suma_negativos = 0  # A
suma_positivos = 0  # B
contador_negativos = 0  # C
contador_positivos = 0  # Para el promedio de los positivos
contador_total = 0
mayor_positivo = None  # E

while True:
    num = float(input("Ingrese un numero: "))
    contador_total += 1

    if num > 0:
        suma_positivos += num
        contador_positivos += 1

        if mayor_positivo is None or num > mayor_positivo:
            mayor_positivo = num

    elif num < 0:
        suma_negativos += num
        contador_negativos += 1

    continuar = input("Desea ingresar otro numero? (s/n): ").lower()
    if continuar != "s":
        break

promedio_positivos = suma_positivos / contador_positivos
porcentaje_negativos = (contador_negativos / contador_total) * 100

print(f"Suma de negativos: {suma_negativos}")  # A
print(f"Suma de positivos: {suma_positivos}")  # B
print(f"Cantidad de numeros negativos: {contador_negativos}")  # C
print(f"Promedio positivos: {promedio_positivos}")  # D
print(f"Positivo mas grande: {mayor_positivo}")  # E
print(f"Porcentaje negativos: {porcentaje_negativos}%")  # F """
