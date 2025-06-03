from Validaciones import *


def pedir_opcion(min: int, max: int) -> int:
    valor = ""
    while True:
        valor = input(f"Ingrese una opción ({min}-{max}): ")
        if es_entero(valor):
            numero = int(valor)

            if min <= numero <= max:
                return numero

            else:
                print(f"La opcion debe estar entre {min} y {max}. Intentelo nuevamente")

        else:
            print("Ingrese una opcion valida")


def pedir_nombre() -> str:
    while True:
        nombre = input("Ingrese nombre: ")
        if nombre_valido(nombre):
            return nombre
        else:
            print("Error: el nombre debe tener al menos 3 letras")


def pedir_puntaje(jurado: int, participante: str) -> int:
    while True:
        valor = input(f"Ingrese el puntaje del jurado {jurado} para el {participante}")
        if es_entero(valor):
            puntaje = int(valor)
            if puntuacion_valida(puntaje):
                return puntaje
            else:
                print("Error: El puntaje debe estar entre 1 y 10.")
        else:
            print("Error: Debe ingresar un numero entero")
