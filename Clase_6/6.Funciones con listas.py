def reemplazar_pares(lista_numeros: list, valor: int) -> bool:
    """Se encarga de reemplazar los pares de la lista que recibe como parametro

    Args:
        lista_numeros (list): Lista de numeros
        valor (int): Valor a reemplazar

    Returns:
        bool: True en caso de que la lista correcta, False en caso contrario
    """

    if type(lista_numeros) == list:
        retorno = True
        print(f"id dentro {id(lista_numeros)}")
        for i in range(len(lista_numeros)):
            if lista_numeros[i] % 2 == 0:
                lista_numeros[i] = valor
    else:
        retorno = False

    # A menos de que la funcion cree una nueva lista, retornar listas en funciones no tiene sentido alguno.
    # Cuando la lista viene por parametro en el main no tiene sentido retornarla.
    return retorno


lista_numeros = [1, 5, 2, 4, 9]

print(lista_numeros)
retorno = reemplazar_pares("lalala", 7)

if retorno:
    print("Todo salio bien")
else:
    print("No se le paso una lista, algo fallo")

print(f"id fuera {id(lista_numeros)}")
print(lista_numeros)
