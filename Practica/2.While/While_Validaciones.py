# 1. Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

"""contraseña = "gg324"

while True:
    contraseña_ingresada = input("Ingrese la clave: ")
    if contraseña_ingresada == contraseña:
        print("Clave correcta")
        break
    else:
        print("Clave incorrecta")"""


# 2. Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

""" contraseña_correcta = "gg324"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    contraseña_ingresada = input("Ingrese la clave: ")
    intentos += 1

    if contraseña_ingresada == contraseña_correcta:
        print("Clave correcta")
        break
    else:
        print("Clave incorrecta") """


# 3. Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

""" while True:
    nota = int(input("Ingrese nota entre 1 y 10: "))
    if 1 <= nota <= 10:
        print("Nota valida")
        break
    else:
        print("La nota no se encuentra entre 1 y 10") """


# 4. Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

""" while True:
    color = input("Ingrese un color (Rojo, Azul, Verde): ").strip().lower()

    if color == "rojo" or color == "verde" or color == "azul":
        print("Color correcto")
        break
    else:
        print("Color incorrecto") """


# Integrador
""" 
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.
"""

""" apellido = input("Ingresar apellido: ").strip().capitalize()

while True:
    edad = int(input("Ingrese su edad (entre 18 y 90): "))

    if 18 <= edad <= 90:
        break
    else:
        print("Edad incorrecta")

while True:
    estado_civil = (
        input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a)")
        .strip()
        .lower()
    )

    if (
        estado_civil == "soltero/a"
        or estado_civil == "casado/a"
        or estado_civil == "divorciado/a"
        or estado_civil == "viudo/a"
    ):
        break
    else:
        print("Estado civil no valido")

while True:
    legajo = int(input("Ingrese numero de legalo (4 cifras, sin ceros a la izquierda)"))

    if 1000 <= legajo <= 9999:
        break
    else:
        print("El numero debe tener 4 cifras y no comonezar con cero")

print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"Numero de legajo: {legajo}")
 """
