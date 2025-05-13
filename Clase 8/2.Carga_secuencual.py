def mostrar_matriz(mi_matriz:list) -> None:
    for fil in range(len(mi_matriz)):
        for col in range(len(mi_matriz[fil])): #len(mi_matriz[0])
            #print(f"{fil},{col}")
            print(f"{mi_matriz[fil][col]}",end=" ")
        print("")
        
def crear_matriz(cantidad_filas:int,cantidad_columnas,valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def cargar_matriz(mi_matriz:list) -> None:
    for fil in range(len(mi_matriz)):
        for col in range(len(mi_matriz[fil])):
            #Pido el dato
            numero = int(input(f"Ingrese un numero (fila: {fil}) (columna: {col}): "))
            #Lo meto en la matriz
            mi_matriz[fil][col] = numero

#3x3
# matriz_a = crear_matriz(3,3,0)
# mostrar_matriz(matriz_a)

#3x2
# matriz_b = crear_matriz(3,2,0)
# mostrar_matriz(matriz_b)

#2x3
matriz_c = crear_matriz(2,3,0)
print("ANTES DE LA CARGA")
mostrar_matriz(matriz_c)

#Carga Secuencial
cargar_matriz(matriz_c)
        
print("DESPUES DE LA CARGA")
mostrar_matriz(matriz_c)
