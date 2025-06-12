# Una función recursiva es una función que se llama a si misma

# def funcion(contador:int):
#     print(contador)
#     contador+=1
#     funcion(contador)

# def contar_numeros(contador:int,maximo:int) -> None:
#     if contador < maximo:
#         print(f"{contador}")
#         contador+=1
#         contar_numeros(contador,maximo)


def calcular_factorial(numero: int) -> int | str:
    """Se encarga de calcular el factorial de un numero

    Args:
        numero (int | str): El numero al que le debo calcular el factorial y en caso de numero negativo retorna un string diciendo que no existe

    Returns:
        int: El resultado de ese factorial
    """

    if numero == 0:
        resultado = 1
    else:
        if numero > 0:
            resultado = numero * calcular_factorial(numero - 1)
        else:
            resultado = "No existe factorial negativo"

    return resultado


# funcion(1)

# contador = 0
# while True:
#     contador+=1
#     print(contador)

# contar_numeros(0,5)

numero = int(input("Ingrese un numero: "))
factorial = calcular_factorial(numero)
print(f"El factorial de {numero}! es {factorial}")
