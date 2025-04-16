# 1. Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

"""for i in range(1, 11):
print(i, end=" ")"""

# 2. Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

""" for i in range(10, 0, -1):
    print(i, end=" ") """

# 3. Mostrar la suma de los números desde el 1 hasta el 10.

""" suma = 0

for i in range(1, 11):
    suma += i

print(f"La suma es:{suma}") """

# 4. Mostrar la suma de los números pares desde el 1 hasta el 10.

""" suma = 0

for i in range(1, 11):
    if i % 2 == 0:
        suma += i

print(f"La suma es:{suma}") """

# 5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

""" suma = 0

for i in range(5):
    num = float(input(f"Ingrese los 5 numeros: "))
    suma += num

promedio = suma / 5

print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}") """

# 6. Ingresar 10 números enteros. Determinar el máximo y el mínimo.

""" minimo = None
maximo = None

for i in range(10):
    num = int(input("Ingrese los 10 numeros: "))

    if minimo is None or num < minimo:
        minimo = num
    if maximo is None or num > maximo:
        maximo = num

print(f"El minimo es: {minimo}")
print(f"El maximo es: {maximo}") """
