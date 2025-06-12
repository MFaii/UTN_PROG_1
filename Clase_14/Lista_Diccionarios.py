import os
from Funciones import *

# Tenemos que crear un sistema para agregar alumnos
# 1.Cargar Alumno
# 2.Mostrar Alumnos
# 3.Mostrar Alumnos Promocionados
# 4.Mostrar Alumnos con edad entre 18 y 30
# 5.Mostrar Alumnos Aprobados
# 6.Mostrar Alumnos Desaprobados
# 7.Salir

# Mostrar alumnos entre 18 y 30 años

lista_alumnos = []

while True:
    mostrar_menu()
    opcion = int(input("Su opcion: "))
    while opcion > 7 or opcion < 1:
        opcion = int(input("Reingrese su opcion (1-7): "))
    if opcion == 1:
        if cargar_alumno(lista_alumnos) == True:
            print("Alumno cargado con exito")
        else:
            print("El usuario cancelo la carga")
    elif opcion == 2:
        if mostrar_alumnos(lista_alumnos) == False:
            print("No hay alumnos cargados")
    elif opcion == 3:
        if mostrar_alumnos_por_rango(lista_alumnos, 6, 10, "nota_final") == False:
            print("No hay alumnos promocionados")
    elif opcion == 4:
        if mostrar_alumnos_por_rango(lista_alumnos, 18, 30, "edad") == False:
            print("No hay alumnos entre los 18 y 30 años")
    elif opcion == 5:
        if mostrar_alumnos_por_rango(lista_alumnos, 4, 5, "nota_final") == False:
            print("No hay alumnos aprobados")
    elif opcion == 6:
        if mostrar_alumnos_por_rango(lista_alumnos, 1, 3, "nota_final") == False:
            print("No hay alumnos desaprobados")
    elif opcion == 7:
        print("Saliendo...")
        break
    input("Toque cualquier boton para continuar...")
    os.system("clear")
