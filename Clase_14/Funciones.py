import random

def mostrar_menu():
    print("1. Cargar Alumno")
    print("2. Mostrar Alumnos")
    print("3. Mostrar Alumnos Promocionados")
    print("4. Mostrar Alumnos con edad entre 18 y 30")
    print("5. Mostrar Alumnos Aprobados")
    print("6. Mostrar Alumnos Desaprobados")
    print("7. Salir")
    
def cargar_alumno(lista_alumnos:list) -> bool:
    alumno = {}
    respuesta = cargar_diccionario_alumno(alumno)
    
    if respuesta == True:
        lista_alumnos.append(alumno)
    
    return respuesta

def cargar_diccionario_alumno(alumno:dict) -> bool:
    retorno = False
    alumno["legajo"] = random.randint(11111,99999)
    alumno["nombre"] = input("Ingrese el nombre: ")
    alumno["apellido"] = input("Ingrese el apellido: ")
    alumno["genero"] = input("Ingrese el genero: ")
    alumno["edad"] = int(input("Ingrese su edad: "))
    alumno["nota_final"] = int(input("Ingrese la nota final (1-10): "))
    
    mostrar_alumno(alumno)
    respuesta = input("Esta seguro de querer cargar este alumno (si/no): ")
    
    if respuesta == "si":
        retorno = True
        
    return retorno

def mostrar_alumno(alumno:dict) -> None:
    print(f"LEGAJO: {alumno.get("legajo","No existe")}")
    print(f"NOMBRE: {alumno.get("nombre","No existe")}")
    print(f"APELLIDO: {alumno.get("apellido","No existe")}")
    print(f"GENERO: {alumno.get("genero","No existe")}")
    print(f"EDAD: {alumno.get("edad","No existe")} años")
    print(f"NOTA FINAL: {alumno.get("nota_final","No existe")}/10")
    
def mostrar_alumnos(lista_alumnos:list) -> bool:
    retorno = False
    
    for i in range(len(lista_alumnos)):
        mostrar_alumno(lista_alumnos[i])
        print("")
        retorno = True
        
    return retorno

def mostrar_alumnos_por_rango(lista_alumnos:list,minimo:int,maximo:int,clave:str) -> bool:
    retorno = False
    
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        dato = alumno.get(clave)
        if dato != None and dato >= minimo and dato <= maximo:
            mostrar_alumno(alumno)
            print("")
            retorno = True
            
    return retorno