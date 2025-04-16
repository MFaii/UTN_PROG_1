# El for yo lo voy a usar cuando de antemano sepa la cantidad de vueltas que vaya a dar mi código, yo no voy a poder usar el for para por ejemplo el ultimo ejemplo de adivina el numero ya que no tengo predefinido la cantidad de vueltas que va a dar.

# Range
# lista_numeros = list(range(5))
# print(lista_numeros)

# La función range tiene 3 parametros (inicio,fin,incremento)
# lista_numeros = list(range(inicio,fin,incremento))
# Esto me sirve para generar el rango de numeros que yo quiera

# Mostrar numeros del 1 al 5
# Inicio -> Incluyente (tengo que poner el numero que yo espero que arranque la secuencia)
# Fin -> Excluyente (tengo que poner el numero que yo espero que termine en la secuencia, pero a diferencia del incio ese numero no lo incluye (TENGO QUE PONER UNO MAS))
# Incremento -> Como se va a ir sumando esta secuencia de numeros (de a uno, de a dos, etc). Por defecto es 1

# Si al incremento no le ponen nada, incrementa de a uno por defecto
# lista_numeros = list(range(1,6)) #SON LO MISMO
# lista_numeros = list(range(1,6,1)) #SON LO MISMO
# lista_numeros = list(range(1,6,2))
# print(lista_numeros)


# Cuando usar el for

# Mostrar numeros del 1 al 5

# Variable de control -> Es la variable que va a modificar el for por cada vuelta por un numero diferente en el rango especifica

# A diferencia del for de otros lenguajes, es que el for de python solo sigue una secuencia iterable (rango numero,lista,tupla, archivo,etc)
# En otros lenguajes el for es diferente, el for en otros lenguajes sigue una condicion lógica como la sigue el while
# A diferencias de otros lenguajes, el for de python nunca genera un bucle infinito, porque como sigue una secuencia de algun rango o iterable, estas mismas siempre tienen un fin

# lista = ["Mariano","Jose","Daniel"]

# for nombre in lista:
#     print(nombre)

# for numero in range(1,6,1):
#     print(numero)

# import random

# lista_numeros = list(range(0,random.randint(2,25),1))
# print(lista_numeros)

# Mostrar numeros del 5 al 1

# for numero in range(5,0,-1):
#     print(numero)

# Pedir 5 numeros y mostrar su suma
# No necesariamente vamos a usar la variable de control de for, simplemente vamos a usar un for solo para vueltas
# Normalmente se le pone i a la variable de control del for, ya que la vamos a usar en la clase de arrays como indice.

# acumulador = 0

# for i in range(5):
#     numero = int(input("Ingrese un numero: "))
#     acumulador += numero

# print(f"La suma es {acumulador}")

# Pedir 5 numeros , mostrar su suma y promedio
# Podemos usar la variable de control como contador, pero hay que tener en cuenta el alcance de nuestra secuencia.

# acumulador = 0

# # print(list(range(1,6,1)))

# #En algunos lenguajes la variable de control del for es LOCAL al for, una vez salido del for desaparece
# for contador in range(1,6,1):
#     numero = int(input("Ingrese un numero: "))
#     acumulador += numero

# promedio = acumulador / contador

# print(f"La suma es: {acumulador}")
# print(f"El promedio es: {promedio}")

# Pedir 10 numeros y mostrar su suma, si el usuario ingresa un 0, se detiene el pedido de numeros

# acumulador = 0

# for i in range(10):
#     numero = int(input("Ingrese un numero: "))
#     acumulador += numero

#     if numero == 0:
#         break

# print(f"La suma es: {acumulador}")

# Pedir 5 numeros y sumar solamente los numeros positivos

# acumulador_positivos = 0

# for i in range(5):
#     numero = int(input("Ingrese un numero: "))
#     # if numero < 0:
#     #     continue
#     # acumulador_positivos += numero
#     if numero > 0:
#         acumulador_positivos += numero

# print(f"El resultado de la suma es: {acumulador_positivos}")

# Yo dentro de un for puedo tener otro for
# Los separo en for principal (i)
# For secundario (j)
# Cada vuelta del for principal (i) tiene que dar todas las vueltas el for secundario en j

for i in range(3):
    for j in range(4):
        print(f"for principal (i): {i} for secundario (j): {j}")
    print("TERMINO VUELTA EL FOR PRINCIPAL")
