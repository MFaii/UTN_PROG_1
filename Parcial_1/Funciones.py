from Validaciones import *
from Inputs import *


def crear_matriz(
    cantidad_filas: int, cantidad_columnas: int, valor_inicial: any
) -> list:
    """
    Crea una matriz de tamaño especificado y la llena con un valor inicial.

    Args:
        cantidad_filas (int): Filas para la matriz.
        cantidad_columnas (int): Columnas para la matriz.
        valor_inicial (any): Valor inicial de todos los elementos de la matriz.

    Returns:
        list: Devuelve la matriz creada con el valor inicial.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz


def crear_array(cantidad_elementos: int, valor_inicial: any) -> list:
    """
    Crea un array de tamaño especificado y lo llena con un valor inicial.

    Args:
        cantidad_elementos (int): Cantidad de elementos para el array.
        valor_inicial (any): Valor inicial de todos los elementos del array.

    Returns:
        list: Devuelve el array creado con el valor inicial.
    """
    array = [valor_inicial] * cantidad_elementos
    return array


def cargar_nombre_participantes(array_nombres: list) -> bool:
    """
    Solicita nombres por consola y los carga en el array recibido como argumento.

    Args:
        array_nombres (list): Lista predefinida con espacios vacíos donde se cargarán los nombres de los participantes.

    Returns:
        bool: Devuelve True si la carga fue exitosa, False si el array no es válido.
    """
    if type(array_nombres) == list and len(array_nombres) > 0:
        for i in range(len(array_nombres)):
            print(f"Ingreso del nombre para el participante {i + 1}:")
            nombre = pedir_nombre()
            array_nombres[i] = nombre
        return True
    else:
        return False


def mostrar_array(array: list):
    """
    Muestra los elementos del array por consola

    Args:
        array (list): Lista de elementos a mostrar
    """
    for i in range(len(array)):
        print(f"{array[i]}")


def mostrar_matriz(matriz: list) -> None:
    """
    Muestra por consola una matriz.

    Args:
        matriz (list): Matriz a mostrar.
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            print(f"{matriz[fila][columna]}", end=" ")
            print("")


def cargar_puntuaciones(matriz_puntos: list) -> bool:
    """
    Solicita las puntuaciones por consola y las carga en la matriz.

    Args:
        matriz_puntos (list): Matriz donde se van a cargar las puntuaciones.

    Returns:
        bool: Devuelve True si la carga fue exitosa, False si la matriz no es válida.
    """
    if type(matriz_puntos) == list and len(matriz_puntos) > 0:
        for fila in range(len(matriz_puntos)):
            for columna in range(len(matriz_puntos[fila])):
                puntaje = pedir_puntaje(
                    columna + 1, "participante " + str(fila + 1) + ":"
                )
                matriz_puntos[fila][columna] = puntaje
        return True
    else:
        return False


def mostrar_puntuacion(array_nombres: list, matriz_puntos: list, indice: int) -> bool:
    """
    Muestra por consola el nombre del participante, sus puntuajes individuales y el promedio, la misma es ejecutada por mostrar_puntuaciones().

    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_puntos (list): Matriz con los puntajes otorgados por los jurados.
        indice (int): Índice del participante a mostrar.

    Returns:
        bool: Devuelve True si se muestra correctamente la información, False si el índice es inválido.
    """
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
    """
    Calcula y devuelve el puntaje promedio de un participante.

    Args:
        matriz (list): Matriz de puntuaciones donde cada fila representa a un participante y cada columna a un jurado.
        indice (int): Índice del participante del cual se quiere calcular el promedio.

    Returns:
        float: Promedio de los puntajes del participante.
    """
    total = 0
    cantidad = len(matriz[indice])

    for j in range(cantidad):
        total += matriz[indice][j]

    promedio = total / cantidad
    return promedio


def mostrar_puntuaciones(array_nombres: list, matriz_puntos: list) -> bool:
    """
    Muestra por consola las puntuaciones de todos los participantes junto con sus promedios.

    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_puntos (list): Matriz con los puntajes otorgados por los jurados a cada participante.

    Returns:
        bool: Devuelve True si se muestran correctamente las puntuaciones, False si los datos son inválidos.
    """
    if (
        type(array_nombres) == list
        and type(matriz_puntos) == list
        and len(array_nombres) > 0
        and len(matriz_puntos) > 0
    ):
        retorno = True
        for i in range(len(array_nombres)):
            mostrar_puntuacion(array_nombres, matriz_puntos, i)
            print("")
    else:
        retorno = False

    return retorno


def promedio_mayor_a_cuatro(array_nombres: list, matriz_puntos: list) -> bool:
    """
    Muestra los participantes cuyo promedio de puntuación sea mayor a 4.

    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_puntos (list): Matriz con las puntuaciones otorgadas por los jurados.

    Returns:
        bool: Devuelve True si al menos un participante tiene promedio mayor a 4, False en caso contrario.
    """
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
    """
    Muestra los participantes cuyo promedio de puntuación sea mayor a 7.

    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_puntos (list): Matriz con las puntuaciones otorgadas por los jurados.

    Returns:
        bool: Devuelve True si al menos un participante tiene promedio mayor a 7, False en caso contrario.
    """
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
    """
    Muestra por consola el promedio de puntuaciones otorgadas por cada jurado.

    Args:
        matriz_puntos (list): Matriz que contiene las puntuaciones de cada jurado a cada participante.

    Returns:
        bool: Devuelve True si se calcularon y mostraron los promedios correctamente, False si la matriz está vacía o no es válida.
    """
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


def jurado_mas_estricto(matriz_puntos: list) -> bool:
    """
    Determina cuál de los tres jurados fue el más estricto. -> Cambios, determina cuales fueron los dos mas estrictos

    Args:
        matriz_puntos (list): Matriz de puntuaciones, donde cada fila representa a un participante y cada columna representa a un jurado.

    Returns:
        bool: Devuelve True si se pudo determinar el jurado más estricto, False si la matriz no es válida.
    """
    if type(matriz_puntos) == list and len(matriz_puntos) > 0:
        suma_jurado_1 = 0
        suma_jurado_2 = 0
        suma_jurado_3 = 0
        cantidad = len(matriz_puntos)

        for i in range(cantidad):
            suma_jurado_1 += matriz_puntos[i][0]
            suma_jurado_2 += matriz_puntos[i][1]
            suma_jurado_3 += matriz_puntos[i][2]

        promedio_1 = suma_jurado_1 / cantidad
        promedio_2 = suma_jurado_2 / cantidad
        promedio_3 = suma_jurado_3 / cantidad

        menor_promedio = promedio_1
        if promedio_2 < menor_promedio:
            menor_promedio = promedio_2
        if promedio_3 < menor_promedio:
            menor_promedio = promedio_3

        print("\nJurado/s más estricto/s:")
        if promedio_1 == menor_promedio:
            print(f"JURADO 1 con promedio: {round(promedio_1, 2)}")
        if promedio_2 == menor_promedio:
            print(f"JURADO 2 con promedio: {round(promedio_2, 2)}")
        if promedio_3 == menor_promedio:
            print(f"JURADO 3 con promedio: {round(promedio_3, 2)}")

        return True
    else:
        return False


def buscar_participante_por_nombre(
    array_nombres: list, matriz_puntos: list, nombre: str
) -> bool:
    """
    Busca un participante por nombre en una lista y muestra sus puntajes y promedio.

    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_puntos (list): Matriz de puntuaciones, donde cada fila representa a un participante y cada columna representa a un jurado.
        nombre (str): Nombre del participante a buscar.

    Returns:
        bool: True si el participante fue encontrado, False en caso contrario.
    """
    encontrado = False

    for i in range(len(array_nombres)):
        if array_nombres[i].lower() == nombre.lower():
            print(f"NOMBRE PARTICIPANTE: {array_nombres[i]}")
            print(f"PUNTAJE JURADO 1: {matriz_puntos[i][0]}")
            print(f"PUNTAJE JURADO 2: {matriz_puntos[i][1]}")
            print(f"PUNTAJE JURADO 3: {matriz_puntos[i][2]}")

            promedio = (
                matriz_puntos[i][0] + matriz_puntos[i][1] + matriz_puntos[i][2]
            ) / 3
            print(f"PUNTAJE PROMEDIO: {round(promedio,2)}/ 10")

            encontrado = True
            break

    return encontrado


def top_3_participantes(array_nombres: list, matriz_puntos: list) -> bool:
    """
    Muestra los 3 participantes con mayor puntaje promedio, ordenandolos con el metodo de bubble sort

    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_puntos (list): Matriz de puntuaciones, donde cada fila representa a un participante y cada columna representa a un jurado.

    Returns:
        bool: True si se pudo mostrar el top, False si no hay participantes cargados.
    """
    cantidad = len(array_nombres)

    if cantidad == 0:
        print("No hay participantes cargados.")
        return False

    promedios = [0] * cantidad
    indices = [0] * cantidad

    for i in range(cantidad):
        promedios[i] = calcular_promedio_participante(matriz_puntos, i)
        indices[i] = i

    for i in range(cantidad - 1):
        for j in range(i + 1, cantidad):
            if promedios[i] < promedios[j]:
                aux_promedios = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = aux_promedios

                aux_indices = indices[i]
                indices[i] = indices[j]
                indices[j] = aux_indices

    print("\n--- TOP 3 PARTICIPANTES CON MAYOR PROMEDIO ---")

    for i in range(3):
        idx = indices[i]
        print(f"{i +1}. {array_nombres[idx]} - PROMEDIO: {round(promedios[i],2)}/10")

    return True


def ordenar_alfabeticamente(array_nombres: list, matriz_puntos: list) -> bool:
    """
    Muestra los participantes ordenados de la A-Z

    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_puntos (list): Matriz de puntuaciones, donde cada fila representa a un participante y cada columna representa a un jurado.

    Returns:
        bool: True si la operación fue exitosa, False si los datos no son válidos.
    """
    if type(array_nombres) == list and type(matriz_puntos) == list:

        cantidad = len(array_nombres)

        copia_nombres = [0] * cantidad
        copia_puntos = [0] * cantidad

        for i in range(cantidad):
            copia_nombres[i] = array_nombres[i]
            copia_puntos[i] = [
                matriz_puntos[i][0],
                matriz_puntos[i][1],
                matriz_puntos[i][2],
            ]

        for i in range(cantidad - 1):
            for j in range(i + 1, cantidad):
                if copia_nombres[i].lower() > copia_nombres[j].lower():
                    aux_nombre = copia_nombres[i]
                    copia_nombres[i] = copia_nombres[j]
                    copia_nombres[j] = aux_nombre

                    aux_puntos = copia_puntos[i]
                    copia_puntos[i] = copia_puntos[j]
                    copia_puntos[j] = aux_puntos

        print("\n--- Datos ordenados ---")

        for i in range(cantidad):
            nombre = copia_nombres[i]
            puntos = copia_puntos[i]
            promedio = calcular_promedio_participante(copia_puntos, i)
            print(
                f"{i + 1}. {nombre} | Puntajes: {puntos[0]}, {puntos[1]}, {puntos[2]} | Promedio: {round(promedio, 2)}"
            )

        return True

    else:
        return False
