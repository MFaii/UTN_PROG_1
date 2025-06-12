

def ordenar_array_menor_mayor(array_a_ordenar:list) -> None:
    #1.For (recorro los indices del numero de la izquierda)
    for i in range(len(array_a_ordenar)-1):
        #2.For secundario (para recorrer los indices del numero de la derecha)
        for j in range(i+1,len(array_a_ordenar)):
            if array_a_ordenar[i] > array_a_ordenar[j]:
                auxiliar = array_a_ordenar[i]
                array_a_ordenar[i] = array_a_ordenar[j]
                array_a_ordenar[j] = auxiliar

def ordenar_array_mayor_menor(array_a_ordenar:list) -> None:
    #1.For (recorro los indices del numero de la izquierda)
    for i in range(len(array_a_ordenar)-1):
        #2.For secundario (para recorrer los indices del numero de la derecha)
        for j in range(i+1,len(array_a_ordenar)):
            if array_a_ordenar[i] < array_a_ordenar[j]:
                auxiliar = array_a_ordenar[i]
                array_a_ordenar[i] = array_a_ordenar[j]
                array_a_ordenar[j] = auxiliar
