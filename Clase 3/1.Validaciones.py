# Nosostros necesitamos que los datos que entren en nuestro sistema esten bien verificados, o sea que el usuario no se equivoque al ingresar, su nombre, edad, etc, para ello realizamos validaciones

# ¿Como funciona? -> Nosotros vamos a usar un bucle while para validar, que lo que me va a permitir que si la información no coincide con lo que el sistema espera, se le pide al usuario un reingreso de datos.
# while ERROR -> Dentro del while la condicion tiene que ser el error esperado por el sistema.

# La contraseña para ingresar es 'utn678'

# clave = input("Ingrese su clave: ")

# #if -> El if me permite validar algo una sola vez (El usuario se puede equivocar infinitas veces)
# while clave != "utn678":
#     print("CLAVE INCORRECTA")
#     clave = input("Reingrese su clave: ")

# print("CLAVE CORRECTA")

# Ingresar la edad de una persona (la misma tiene que estar en 1 y 120 años)

# edad = int(input("Ingrese su edad: "))

# while edad < 1 or edad > 120:
#     print("EDAD INVALIDA , SE ESPERA ENTRE 1 y 120 AÑOS")
#     edad = int(input("Reingrese su edad: "))

# while not (edad >= 1 and edad <= 120):
#     print("EDAD INVALIDA , SE ESPERA ENTRE 1 y 120 AÑOS")
#     edad = int(input("Reingrese su edad: "))

# print(f"Su edad es: {edad} años")

# El genero de una persona (M - F - NB)

# genero = input("Ingrese su genero (M/F/NB): ")

# while genero != "M" and genero != "F" and genero != "NB":
#     print("GENERO INVALIDO (M-F-NB)")
#     genero = input("Reingrese su genero (M/F/NB): ")

# print(f"Su genero es {genero}")

# Pidamos el tipo de usuario (normal-admin-invitado)

# tipo_usuario = input("Ingrese el tipo de usuario: (normal-admin-invitado) ")

# while tipo_usuario != "normal" and tipo_usuario != "admin" and tipo_usuario != "invitado":
#     print("USUARIO INCORRECTO, debe ser normal, invitado o admin")
#     tipo_usuario = input("Reingrese el tipo de usuario: (normal-admin-invitado) ")

# # while not (tipo_usuario == "normal" or tipo_usuario == "admin" or tipo_usuario == "invitado"):
# #     print("USUARIO INCORRECTO, debe ser normal, invitado o admin")
# #     tipo_usuario = input("Reingrese el tipo de usuario: (normal-admin-invitado) ")

# print(f"Usuario logueado: {tipo_usuario}")

# La contraseña para ingresar es 'utn678' (TIENE 3 INTENTOS)

# clave = input("Ingrese su clave: ")
# intentos = 0

# if -> El if me permite validar algo una sola vez (El usuario se puede equivocar infinitas veces)
# while clave != "utn678":
#     intentos += 1
#     if intentos == 3:
#         break
#     print("CLAVE INCORRECTA")
#     clave = input("Reingrese su clave: ")


# if intentos == 3:
#     print("AGOTO LOS 3 INTENTOS POSIBLES NO PUEDE INGRESAR AL SISTEMA")
# else:
#     print("CLAVE CORRECTA\nBIENVENIDO AL SISTEMA")
#     print(f"Tuvo {intentos} errores")

# Pedir numeros y sumarlos hasta que el usuario ingrese el numero 0

# acumulador = 0
# contador = 0

# while True:
#     numero = int(input("Ingrese un numero: "))
#     acumulador += numero
#     contador += 1

#     if numero == 0:
#         break

# print(f"La suma es : {acumulador}")
# print(f"Pedimos {contador} numeros")

# ADIVINA EL NUMERO (Yo voy a ingresar un numero por consola y tengo que adivinar el numero random que la maquina esta pensando), tiene 3 intentos
# import random

# numero_random = random.randint(1,10)
# intentos = 0

# while True:
#     numero = int(input("Ingrese un numero: "))
#     intentos += 1

#     if numero == numero_random:
#         print("GANO")
#         break

#     if intentos == 3:
#         print("PERDIO")
#         break
