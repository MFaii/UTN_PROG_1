# matriz = [
#     [3,4,5],
#     [5,-2,4],
#     [7,5,5]
# ]

nombres = [
    ["Mariano","Ana","Ana"],
    ["Mariano","Jose","Mariano"],
    ["Juan","Maria","Nestor"]
]

#GENERAL 
def buscar_dato_matriz(matriz:list,dato_a_buscar:any) -> bool:
    bandera = False

    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if matriz[fil][col] == dato_a_buscar:
                bandera = True
                break
        if bandera == True:
            break
    
    return bandera

#GENERAL
def contar_dato_matriz(matriz:list,dato_a_contar:any) -> int:
    contador = 0

    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if matriz[fil][col] == dato_a_contar:
                contador += 1
    
    return contador

#Ejemplo 1 -> Buscar si un numero ingresado se encuentra en la matriz o no

# numero_ingresado = int(input("Ingrese un numero: "))
# bandera = buscar_dato_matriz(matriz,"Jose")
    
# if bandera == True:
#     print(f"El numero {numero_ingresado} se encuentra en la matriz")
# else:
#     print(f"El numero {numero_ingresado} no se encuentra en la matriz")

#Ejemplo 2 -> Buscar cuantas veces se repite el numero ingresado

# numero_ingresado = int(input("Ingrese un numero: "))
# contador = contar_dato_matriz(matriz,numero_ingresado)

# if contador != 1:
#     print(f"El numero {numero_ingresado} se encuentra {contador} veces en la matriz")
# else:
#     print(f"El numero {numero_ingresado} se encuentra una vez en la matriz")

# print(contar_dato_matriz(nombres,"Mauricio"))