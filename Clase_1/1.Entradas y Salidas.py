#1.Entradas: Son datos que entran al sistema para realizar determina acción, normalmente son hechos por personas fisicas
#Un ejemplo de entrada es ingresar los dos números

#2.Procesos: Son las acciones que realiza nuestro programa con los datos que recibio de entrada.
#Un ejemplo de proceso es realizar una suma.

#3.Salidas: Es lo que el sistema nos devuelve luego de culminar el proceso, normalmente lo expresamos con la función print
#Un ejemplo es el resultado de una suma.

#Variable -> Es una porción de memoria en la que el sistema va a guardar la información necesaria para su funcionamiento.
#Se escriben siempre en minuscula, y en caso de nombres compuestos, con guiones bajos (_)
#nombre 
#edad_usuario
#Como el nombre lo indica, son datos que pueden variar en el tiempo.

#Ejemplo 1 -> Hola Mundo
#Salida
#print("Hola Mundo")

#Ejemplo 2 -> Ingresar un nombre y devolverlo

#Entrada (El ingreso del nombre)
#Las entradas por ahora las vamos a pedir por input()
# nombre = input("Ingrese su nombre: ")
# numero = 10

# #Salida (Mostrar ese nombre)
# print("Su nombre es: " + nombre)
# print("Su nombre es:",nombre)
# #f-string
# print(f"Su nombre es: {nombre}")
# #El metodo format
# print("Su nombre es: {0} {1}".format(nombre,numero))

#Ejemplo 3: Ingreso dos numeros, hago la suma y muestro el resultado

#1.Entradas
numero_uno = int(input("Ingrese el numero 1: "))
numero_dos = int(input("Ingrese el numero 2: "))

#2.Procesos
resultado = numero_uno + numero_dos

#3.Salidas
print(f"La suma entre {numero_uno} y {numero_dos} es = {resultado}")

