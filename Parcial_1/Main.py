from Funciones import *
import os

array_nombres = crear_array(5, "")
matriz_puntos = crear_matriz(5, 3, 0)

print("Matriz", matriz_puntos)

bandera_carga_nombres = False
bandera_carga_puntos = False

while True:
    print(
        "1.Cargar nombres\n2.Cargar puntos\n3.Mostrar puntos\n4.Participantes con promedio mayor a 4\n5.Participantes con promedio mayor a 7\n11.Salir"
    )
    opcion = int(input("Su opcion: "))

    while opcion > 11 or opcion < 1:
        opcion = int(input("Reingrese su opcion(1-10): "))

    if opcion == 1:
        if cargar_nombre_participantes(array_nombres) == True:
            print("Carga de nombres exitosa!")
            mostrar_array(array_nombres)
            bandera_carga_nombres = True
        else:
            print("Error en la carga")

    elif opcion == 2:
        if cargar_puntuaciones(matriz_puntos) == True:
            print("Carga de puntos exitosa!")
            mostrar_matriz(matriz_puntos)
            bandera_carga_puntos = True
        else:
            print("Error al cargar los datos!")

    elif opcion == 3 and (
        bandera_carga_puntos == True and bandera_carga_nombres == True
    ):
        if mostrar_puntuaciones(array_nombres, matriz_puntos) == False:
            print("Error al mostrar los datos")

    elif opcion == 4:
        if bandera_carga_nombres == True and bandera_carga_puntos == True:
            promedio_mayor_a_cuatro(array_nombres, matriz_puntos)
        else:
            print("Error al buscar participantes.")

    elif opcion == 5:
        if bandera_carga_nombres == True and bandera_carga_puntos == True:
            promedio_mayor_a_siete(array_nombres, matriz_puntos)
        else:
            print("Error al buscar participantes.")

    elif opcion == 11:
        print("Saliendo")
        break
    else:
        print("No se hicieron las cargas. Acceso denegado")
    input("Toque cualquier boton para continuar...")
    os.system("clear")
