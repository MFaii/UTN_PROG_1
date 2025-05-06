from Validate import *

"""
1. Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:
def get_int(
    mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int
) -> int | None:
    pass

En donde:
mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
mínimo: valor mínimo admitido (inclusive)
máximo: valor máximo admitido (inclusive)
reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
"""


def get_int(
    mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int
) -> int | None:

    intentos = 0
    while intentos < reintentos:
        entrada = input(mensaje)

        if validate_number(entrada, es_float=False):
            numero = int(entrada)
            if minimo <= numero <= maximo:
                return numero

        print(mensaje_error)
        intentos += 1

    return None


numero = get_int(
    mensaje="Ingrese un numero entre 1 y 50: ",
    mensaje_error="Numero no valido. Ingrese nuevamente.",
    minimo=1,
    maximo=50,
    reintentos=3,
)

if numero != None:
    print(f"El numero ingresado es: {numero}")
else:
    print("No se ingreso un numero valido luego de 3 intentos")

""" 
Repetir el mismo procedimiento para un dato de tipo float
"""


def get_float(
    mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int
) -> float | None:

    intentos = 0
    while intentos < reintentos:
        entrada = input(mensaje)

        if validate_number(entrada, es_float=True):
            numero = float(entrada)
            if minimo <= numero <= maximo:
                return numero

        print(mensaje_error)
        intentos += 1

    return None


numero = get_float(
    mensaje="Ingrese un numero entre -10.5 y 50.5: ",
    mensaje_error="Numero no valido. Ingrese nuevamente.",
    minimo=-10.5,
    maximo=50.5,
    reintentos=3,
)

if numero != None:
    print(f"El numero ingresado es: {numero}")
else:
    print("No se ingreso un numero valido luego de 3 intentos")

""" 
Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):
def get_string(longitud: int) -> str | None:
    pass
"""


def get_string(longitud: int) -> str | None:
    cadena = input(f"Ingrese una cadena de {longitud} caracteres: ")

    if validate_length(cadena, longitud):
        return cadena
    else:
        print("La cadena no tiene la longitud correcta")
        return None


res = get_string(3)

if res != None:
    print(f"Cadena: {res}")
else:
    print("No se ingreso una cadena valida")
