"""
1. Realizar una función recursiva que calcule la suma de los primeros números naturales:
"""


def sumar_naturales(numero: int) -> int:
    if numero <= 1:
        return numero
    return numero + sumar_naturales(numero - 1)


res = sumar_naturales(4)
print(f"La suma de los primeros 4 n° naturales es: {res}")


""" 
2. Realizar una función recursiva que calcule la potencia de un número:
"""


def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1

    return base * calcular_potencia(base, exponente - 1)


res = calcular_potencia(2, 3)
print(f"El resultado es: {res}")

""" 
3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
"""


def sumar_digitos(numero: int) -> int:
    if numero == 0:
        return 0

    else:
        return numero % 10 + sumar_digitos(numero // 10)


print(sumar_digitos(12323233))

""" 
4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:
"""


def calcular_fibonacci(numero: int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1

    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)


num = int(input("ingrese numero: "))
print(f"El numero de fibo de {num} es: {calcular_fibonacci(num)}")
