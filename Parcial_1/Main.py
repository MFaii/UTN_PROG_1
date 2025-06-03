from Funciones import *
import os
from Inputs import *

array_nombres = crear_array(5, "")
matriz_puntos = crear_matriz(5, 3, 0)

bandera_carga_nombres = False
bandera_carga_puntos = False

while True:
    print(
        "1.Cargar nombres\n2.Cargar puntos\n3.Mostrar puntos\n4.Participantes con promedio mayor a 4\n5.Participantes con promedio mayor a 7\n6.Promedio de cada jurado\n7.Jurado/s mas estricto/s\n8.Buscar participante por nombre\n9.Top 3 participantes\n10.Ordenar A-Z\n11.Salir"
    )
    opcion = pedir_opcion(1, 11)

    if opcion == 1:
        if cargar_nombre_participantes(array_nombres) == True:
            print("Carga de nombres exitosa!")
            mostrar_array(array_nombres)
            bandera_carga_nombres = True
        else:
            print("Error en la carga")

    elif opcion == 2 and bandera_carga_nombres == True:
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

    elif opcion == 6:
        if bandera_carga_puntos == True:
            mostrar_promedio_jurados(matriz_puntos)
        else:
            print("Primero debe cargar las puntuaciones.")

    elif opcion == 7:
        if bandera_carga_puntos == True:
            jurado_mas_estricto(matriz_puntos)
        else:
            print("Error al mostrar al jurado mas estricto.")

    elif opcion == 8:
        if bandera_carga_nombres == True and bandera_carga_puntos == True:
            nombre_a_buscar = pedir_nombre()

            if nombre_valido(nombre_a_buscar):
                encontrado = buscar_participante_por_nombre(
                    array_nombres, matriz_puntos, nombre_a_buscar
                )
                if not encontrado:
                    print("El participante no fue encontrado")
            else:
                print("Nombre inválido. Debe contener solo letras y al menos 3 letras.")
        else:
            print("Primero debe cargar los datos.")

    elif opcion == 9:
        if bandera_carga_nombres == True and bandera_carga_puntos == True:
            top_3_participantes(array_nombres, matriz_puntos)
        else:
            print("Primero debe cargar los datos")

    elif opcion == 10:
        if bandera_carga_nombres == True and bandera_carga_puntos == True:
            ordenar_alfabeticamente(array_nombres, matriz_puntos)
        else:
            print("Primero debe cargar los datos.")

    elif opcion == 11:
        print("Saliendo")
        break
    else:
        print("No se hicieron las cargas. Acceso denegado")
    input("Toque cualquier boton para continuar...")
    os.system("clear")
