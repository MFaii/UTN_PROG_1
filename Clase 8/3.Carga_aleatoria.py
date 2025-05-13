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

matriz = crear_matriz(3,2,None)
print("ANTES DE LA CARGA")
mostrar_matriz(matriz)

respuesta = "si"

while respuesta == "si":
    #Pedimos el indice de la fila (VALIDAR)
    indice_fila = int(input("Ingrese el indice de la fila: "))
    #Pedimos el indice de la columna (VALIDAR)
    indice_columna = int(input("Ingrese el indice de la columna: "))
    #Pedimos el dato
    numero = int(input("Ingrese un numero"))
    #Agregar el dato a la matriz
    matriz[indice_fila][indice_columna] = numero
    #Preguntar si seguir
    respuesta = input("¿Desea seguir? si/no")

print("DESPUES DE LA CARGA")
mostrar_matriz(matriz)                          