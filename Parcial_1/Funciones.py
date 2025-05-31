from Validaciones import *


def crear_matriz(
    cantidad_filas: int, cantidad_columnas: int, valor_inicial: any
) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz


def crear_array(cantidad_elementos: int, valor_inicial: any) -> list:
    array = [valor_inicial] * cantidad_elementos
    return array


def cargar_nombre_participantes(array_nombres):
    if type(array_nombres) == list and len(array_nombres) > 0:
        retorno = True
        for i in range(len(array_nombres)):
            valido = False
            while not valido:
                nombre = input(f"Ingrese el nombre del participante {i + 1}: ")
                if nombre_valido(nombre):
                    array_nombres[i] = nombre
                    valido = True
                else:
                    print(
                        "Nombre inválido. Debe tener al menos 3 letras y solo letras y espacios."
                    )
    else:
        retorno = False

    return retorno


def mostrar_array(array: list):
    for i in range(len(array)):
        print(f"{array[i]}")


def mostrar_matriz(matriz: list) -> None:
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            print(f"{matriz[fila][columna]}", end=" ")
            print("")


def cargar_puntuaciones(matriz_puntos: list) -> bool:
    if type(matriz_puntos) == list and len(matriz_puntos) > 0:
        retorno = True
        for fila in range(len(matriz_puntos)):
            for columna in range(len(matriz_puntos[fila])):
                valido = False
                while not valido:
                    punto = int(
                        input(
                            f"Ingrese la cantidad de puntos del jurado {columna +1} para el participante {fila +1}: "
                        )
                    )
                    if puntuacion_valida(punto):
                        matriz_puntos[fila][columna] = punto
                        valido = True
                    else:
                        print("Puntaje inválido. Debe ser un número entre 1 y 10.")
    else:
        retorno = False

    return retorno


def mostrar_puntuacion(array_nombres: list, matriz_puntos: list, indice: int) -> bool:
    if len(array_nombres) > indice and indice >= 0:
        promedio = calcular_promedio_participante(matriz_puntos, indice)
        print(f"NOMBRE PARTICIPANTE: {array_nombres[indice]}")
        print(f"PUNTAJE JURADO 1: {matriz_puntos[indice][0]}")
        print(f"PUNTAJE JURADO 2: {matriz_puntos[indice][1]}")
        print(f"PUNTAJE JURADO 3: {matriz_puntos[indice][2]}")
        print(f"PUNTAJE PROMEDIO: {round(promedio, 2)}/10")
        return True
    else:
        return False


def calcular_promedio_participante(matriz: list, indice: int) -> float:
    total = 0
    cantidad = len(matriz[indice])

    for j in range(cantidad):
        total += matriz[indice][j]

    promedio = total / cantidad
    return promedio


def mostrar_puntuaciones(array_nombres: list, matriz_votos: list) -> bool:
    if (
        type(array_nombres) == list
        and type(matriz_votos) == list
        and len(array_nombres) > 0
        and len(matriz_votos) > 0
    ):
        retorno = True
        for i in range(len(array_nombres)):
            mostrar_puntuacion(array_nombres, matriz_votos, i)
            print("")
    else:
        retorno = False

    return retorno


def promedio_mayor_a_cuatro(array_nombres: list, matriz_puntos: list) -> bool:
    mayor_a_cuatro = False

    for i in range(len(array_nombres)):
        promedio = calcular_promedio_participante(matriz_puntos, i)
        if promedio > 4:
            print(f"NOMBRE PARTICIPANTE: {array_nombres[i]}")
            print(f"PROMEDIO: {round(promedio, 2)}\n")
            mayor_a_cuatro = True

    if not mayor_a_cuatro:
        print("No se encontraron participantes con promedio mayor a 4.")
        return False

    return True


def promedio_mayor_a_siete(array_nombres: list, matriz_puntos: list) -> bool:
    mayor_a_siete = False

    for i in range(len(array_nombres)):
        promedio = calcular_promedio_participante(matriz_puntos, i)
        if promedio > 7:
            print(f"NOMBRE PARTICIPANTE: {array_nombres[i]}")
            print(f"PROMEDIO: {round(promedio, 2)}\n")
            mayor_a_siete = True

    if not mayor_a_siete:
        print("No se encontraron participantes con promedio mayor a 7.")
        return False

    return True


def mostrar_promedio_jurados(matriz_puntos: list) -> bool:
    if type(matriz_puntos) == list and len(matriz_puntos) > 0:
        cantidad_participantes = len(matriz_puntos)
        cantidad_jurados = len(matriz_puntos[0])

        for jurado in range(cantidad_jurados):
            suma = 0
            for participante in range(cantidad_participantes):
                suma += matriz_puntos[participante][jurado]
            promedio = suma / cantidad_participantes
            print(f"PROMEDIO JURADO {jurado + 1}: {round(promedio, 2)}")
        return True
    else:
        return False
