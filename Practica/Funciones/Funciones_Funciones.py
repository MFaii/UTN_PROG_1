# 1.Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
"""def pedir_numero_entero() -> int:
    numero = int(input("Ingrese un numero entero: "))
    return numero


numero_punto_1 = pedir_numero_entero()
print(f"El numero ingresado es: {numero_punto_1}")"""


# 2. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
""" def pedir_numero_flotante() -> float:
    numero = float(input("Ingrese un numero flotante: "))
    return numero


numero_punto_2 = pedir_numero_flotante()
print(f"El numero ingresado es: {numero_punto_2}") """


# 3. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.
""" def pedir_cadena() -> str:
    cadena = str(input("Ingrese cadena de caracteres: "))
    return cadena


cadena = pedir_cadena()
print(f"{cadena}") """


# 4. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.
""" def calcular_area_rectangulo(base: float, altura: float) -> float:
    area = base * altura
    return area


base_ingresada = float(input("Ingrese la base: "))
altura_ingresada = float(input("Ingrese la altura: "))
area = calcular_area_rectangulo(base_ingresada, altura_ingresada)
print(f"El area del rectangulo es: {area}") """


# 5. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
""" def calcular_area_circulo(radio: float) -> float:
    pi = 3.14
    area = pi * (radio**2)
    return area


radio_ingresado = float(input("Ingrese el radio: "))
area = calcular_area_circulo(radio_ingresado)
print(f"El area del circulo: {area}") """


# 6. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
""" def verificar_par_impar(numero: int) -> None:
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")


num = int(input("Ingrese un numero: "))
verificar_par_impar(num) """


# 7.Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
""" def es_par_impar(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False


num = int(input("Ingrese un numero: "))
es_par_impar(num) """


# 8. Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
""" def encontrar_maximo(numero_1: int, numero_2: int, numero_3: int) -> int:
    return max(numero_1, numero_2, numero_3)


n1 = int(input("Ingrese el numero 1: "))
n2 = int(input("Ingrese el numero 2: "))
n3 = int(input("Ingrese el numero 3: "))
maximo = encontrar_maximo(n1, n2, n3)
print(f"El numero mas grande es: {maximo}") """


# 9. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
""" def calcular_potencia(base: float, exponente: int) -> float:
    return base**exponente


base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = calcular_potencia(base, exponente)
print(f"El resultado es {resultado}") """


# 10. Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
""" def es_primo(numero: int) -> bool:
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True """


# 11. Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

# Utilizando el punto 10 ->

""" def numeros_primos_hasta(numero_final: int) -> int:
    contador = 0
    for numero in range(1, numero_final + 1):
        if es_primo(numero):
            print(numero, end=" ")
            contador += 1
    return contador


numero_final = int(input("Ingrese el numero parametro: "))
cantidad = numeros_primos_hasta(numero_final)
print(f"\nLa cantidad de numeros primos encontrados es: {cantidad}") """


# 12. Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

""" def tabla_multiplicar(numero: int, inicio: int = 1, fin: int = 1) -> None:
    for i in range(inicio, fin + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


tabla_multiplicar(5)
tabla_multiplicar(7, inicio=3, fin=5)
tabla_multiplicar(3, fin=8) """


# 13. Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.


# Funcion 1
""" def pedir_numero_entero() -> int:
    es_valido = False
    while not es_valido:
        numero = input("Ingrese un numero entero: ")
        if numero != "":
            es_valido = True
            for caracter in numero:
                if caracter < "0" or caracter > "9":
                    es_valido = False
            if es_valido:
                numero = int(numero)
            else:
                print("Debe ingresar solo numeros")
        else:
            print("No puede dejar el campo vacio")
    return numero


numero = pedir_numero_entero()
print(numero) """


# Funcion 2
""" def pedir_numero_flotante() -> float:
    es_valido = False
    while not es_valido:
        numero = input("Ingrese un numero flotante: ")
        tiene_punto = 0
        if numero != "":
            es_valido = True
            for caracter in numero:
                if caracter == ".":
                    tiene_punto += 1
                elif caracter < "0" or caracter > "9":
                    es_valido = False
            if tiene_punto > 1:
                es_valido = False
            if es_valido:
                numero = float(numero)
            else:
                print("Ingrese un numero valido")
        else:
            print("No puede dejar el campo vacio")
    return numero


numero = pedir_numero_flotante()
print(numero) """


# Funcion 3
""" def pedir_cadena() -> str:
    texto = input("Ingresar cadena:")
    while texto == "":
        print("No puede dejarlo vacio")
        texto = input("Ingresar cadena:")
    return texto


texto = pedir_cadena()
print(texto) """
