#GENERAL
def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(f"{matriz[fil][col]}",end=" ")
        print("")

#GENERAL
def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        #matriz.append(fila)
        matriz += [fila]
        
    return matriz

#GENERAL
def crear_array(cantidad_elementos:int,valor_inicial:any) -> list:
    array = [valor_inicial] * cantidad_elementos
    return array

#ESPECIFICA
def cargar_nombres_alumnos(array_nombres:list) -> None:
    for i in range(len(array_nombres)):
        #Pido el dato
        nombre = input(f"Ingrese nombre alumno {i+1}: ")
        #Lo guardo en el array
        array_nombres[i] = nombre
        
#GENERAL 
def cargar_array_string(array:list,mensaje:str) -> None:
    for i in range(len(array)):
        #Pido el dato
        nombre = input(f"{mensaje} {i+1}: ")
        #Lo guardo en el array
        array[i] = nombre
       
#ESPECIFICA 
def cargar_notas_trimestre(matriz_notas:list) -> None:
    for fil in range(len(matriz_notas)):
        for col in range(len(matriz_notas[0])):
            #Pedir el dato
            nota = int(input(f"Ingrese la nota del alumno {fil+1} para el trimestre {col+1} "))
            #VALIDARLA (1-10)
            #Guardarlo en la matriz
            matriz_notas[fil][col] = nota

#ESPECIFICA
def mostrar_alumno(array_nombres:list,matriz_notas:list,indice_alumno:int) -> None:
    #VALIDAR -> Esto puede generar un indice fuera de rango, evitar que los arrays/matrices esten vacios y sean realmente de tipo list
    print(f"Nombre: {array_nombres[indice_alumno]}")
    print(f"Nota Trimestre 1: {matriz_notas[indice_alumno][0]}")
    print(f"Nota Trimestre 2: {matriz_notas[indice_alumno][1]}")
    print(f"Nota Trimestre 3: {matriz_notas[indice_alumno][2]}")

#ESPECIFICA
def mostrar_alumnos(array_nombres:list,matriz_notas:list) -> None:
    for i in range(len(array_nombres)):
        mostrar_alumno(array_nombres,matriz_notas,i)
        print("")
        
#def mostrar_alumnos()

#GENERAL
def sumar_matriz(matriz_numerica:list) -> int | float:
    suma = 0
    
    for fil in range(len(matriz_numerica)):
        for col in range(len(matriz_numerica[fil])):
            if type(matriz_numerica[fil][col]) == int or type(matriz_numerica[fil][col]) == float:
                suma += matriz_numerica[fil][col]
                
    return suma

#GENERAL
def calcular_promedio(acumulador:float | int, contador:int) -> float | None:
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None
        
    return promedio

#ESPECIFICA
def mostrar_promedio_alumnos(matriz_notas:list) -> None:
    suma_notas = sumar_matriz(matriz_notas)
    cantidad_filas = len(matriz_notas)
    cantidad_columnas = len(matriz_notas[0])
    cantidad_elementos = cantidad_filas * cantidad_columnas
    promedio_notas = calcular_promedio(suma_notas,cantidad_elementos)
    print(f"El promedio total de notas es de {promedio_notas}/10")

#GENERAL
def sumar_fila(matriz_numerica:list,indice_fila:int) -> int | float:
    suma_fila = 0
    
    for col in range(len(matriz_numerica[0])):
        if type(matriz_numerica[indice_fila][col]) == int or type(matriz_numerica[indice_fila][col]) == float :
            suma_fila += matriz_numerica[indice_fila][col]
    
    return suma_fila
#ESPECIFICA
def mostrar_alumnos_no_superan_nota_promedio(array_nombres:list,matriz_notas:list,promedio:float) -> None:
    for fil in range(len(matriz_notas)):
        suma_nota = sumar_fila(matriz_notas,fil)
        cantidad_trimestres = len(matriz_notas[0])
        promedio_nota = calcular_promedio(suma_nota,cantidad_trimestres)
        
        if promedio_nota < promedio:
            mostrar_alumno(array_nombres,matriz_notas,fil)
            print("")

#ESPECIFICA 
def ordenar_alumnos_por_nombre(array_nombres:list,matriz_notas:list) -> None:
    for i in range(len(array_nombres)-1):
        for j in range(i+1,len(array_nombres)):
            if array_nombres[i] > array_nombres[j]:
                auxiliar = array_nombres[i]
                array_nombres[i] = array_nombres[j]
                array_nombres[j] = auxiliar
                
                auxiliar_dos = matriz_notas[i]
                matriz_notas[i] = matriz_notas[j]
                matriz_notas[j] = auxiliar_dos
                
def ordenar_alumnos_por_nota_primer_trimestre(array_nombres:list,matriz_notas:list) -> None:
    for i in range(len(matriz_notas)-1):
        for j in range(i+1,len(matriz_notas)):
            if matriz_notas[i][0] < matriz_notas[j][0]:
                auxiliar = matriz_notas[i]
                matriz_notas[i] = matriz_notas[j]
                matriz_notas[j] = auxiliar
                
                auxiliar_dos = array_nombres[i]
                array_nombres[i] = array_nombres[j]
                array_nombres[j] = auxiliar_dos