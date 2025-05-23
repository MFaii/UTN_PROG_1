from Funciones import *
import os

#En realidad son 5 pero usamos 2 para probar
array_nombres = crear_array(2,"")
matriz_votos = crear_matriz(2,3,0)

bandera_carga_nombres = False
bandera_carga_votos = False

while True:
    print("1.Cargar nombres\n2.Cargar votos\n3.Mostrar votos\n4.Partidos con menos del 5% de votos\n16.Salir")
    opcion = int(input("Su opcion: "))
    while opcion > 16 or opcion < 1:
        opcion = int(input("Reingrese su opcion (1-16): "))
    if opcion == 1:
        if cargar_nombre_partidos(array_nombres) == True:
            print("Carga de nombres exitosa!")
            mostrar_array(array_nombres)
            bandera_carga_nombres = True
        else:
            print("Error en la carga")
    elif opcion == 2:
        if cargar_votos(matriz_votos) == True:
            print("Carga de votos exitosa!")
            mostrar_matriz(matriz_votos)
            bandera_carga_votos = True
        else:
            print("Error al cargar los datos!")
    elif opcion == 3 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        # if mostrar_partido(array_nombres,matriz_votos,0) == False:
        #     print("Hubo un error al mostrar el partido")
        if mostrar_partidos(array_nombres,matriz_votos) == False:
            print("Error al mostrar los datos")
    elif opcion == 4 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        if mostrar_partidos_que_no_superan_porciento(array_nombres,matriz_votos,5) == False:
            print("No existe ningun partido que haya tenido menos del 5% de los votos")
    elif opcion == 16:
        print("Saliendo...")
        break
    else:
        print("No se hicieron las cargas. Acceso denegado")
    input("Toque cualquier boton para continuar...")
    os.system("clear")