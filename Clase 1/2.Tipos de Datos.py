#Operador +
# resultado = 5 + 10
# print(resultado)

#Operador -
# resultado = 5 - 10
# print(resultado)

#Operador *
# resultado = 5 * 10
# print(resultado)

#Operador / -> No importa los numeros que elija, este operador siempre va a devolver un flotante.
# resultado = 10 / 5
# print(resultado)

#Operador // -> Me realiza la division entera entre dos numeros

# resultado = 9 // 5
# print(resultado)

#Resto % -> Esto me es muy util para calcular la paridad de un número 

# resultado = 9 % 5
# print(resultado)

#Potencia ** -> Calcular la potencia de un numero de manera rápida

# resultado = 2 ** 5
# print(resultado)

#OPERADORES RELACIONALES

#Mayor (>) -> Me indica que si el número que tengo a la izquierda es mayor al de la derecha me da verdadero, caso contrario me da falso

# print(10 > 5) #TRUE
# print(5 > 10) #FALSE
# print(10 > 10) #FALSE

#Menor (<) -> Me indica que si el número que tengo a la izquierda es menor al de la derecha me da verdadero, caso contrario me da falso

# print(5 < 10) #True
# print(10 < 5) #False
# print(10 < 10) #False

#Mayor/Igual (>=) -> Me indica que si el número que tengo a la izquierda es mayor o igual al de la derecha me da verdadero, caso contrario me da falso

# print(10 >= 5)#True
# print(5 >= 10)#False
# print(10 >= 10)#True

#Igualdad (==) -> Me indica si el dato de la izquierda es igual al de la derecha
# print(5 == 5) #True
# print(5 == 10) #False
# print("Mariano" == "Mariano") #True
# print("Mariano" == "Jose") #False

#Distinto (!=) -> Me indica si el dato de la izquierda es distinto al de la derecha

# print(5 != 5)#False
# print(5 != 10)#True
# print("Mariano" != "Mariano")#False
# print("Mariano" != "Jose")#True

#OPERADORES LOGICOS

#and -> La condicion de la izquierda y de la derecha tienen que ser verdaderas, caso contrario no se cumple la condicion

# print(True and True) #True
# print(True and False) #False
# print(False and True) #False
# print(False and False) #False

#or -> Al menos alguna de las condiciones ya sea la derecha o izquierda deben ser verdad , o las dos

# print(True or True) #True
# print(True or False) #True
# print(False or True) #True
# print(False or False) #False

#Operador not -> Niega la condicion actual

#print(not True) # False
#print(not False) # True

#OPERADORES DE ASIGNACION

#numero = 10
#numero = numero + 5
#numero += 5
#numero -= 5
#numero *= 5
#numero /= 5
#numero %= 5

#print(numero)

#Para saber de que tipo de dato es mi variable voy a usar la función type()

# nombre = "Mariano"
# numero = 10
# numero_flotante = 3.14

# print(type(nombre))
# print(type(numero))
# print(type(numero_flotante))

#Caso 1: Convertir un entero a un str y a un flotante

# numero_entero = 10
# numero_string = str(numero_entero)
# numero_flotante = float(numero_entero)

# print(f"{numero_entero} - {type(numero_entero)}")
# print(f"{numero_string} - {type(numero_string)}")
# print(f"{numero_flotante} - {type(numero_flotante)}")

#Caso 2: Convertir un flotante a str o a entero

# numero_flotante = 3.99
# numero_entero = int(numero_flotante)
# numero_string = str(numero_flotante)

# print(f"{numero_flotante} - {type(numero_flotante)}")
# print(f"{numero_entero} - {type(numero_entero)}")
# print(f"{numero_string} - {type(numero_string)}")

#Caso 3: Convertir un str a un flotante o entero -> Tienen que tener cuidado que lo que esten por pasar de string a numerico sea realmente un numero

# numero_string = input("Ingrese un numero: ")
# numero_flotante = float(numero_string)
# numero_entero = int(numero_string)

# print(f"{numero_string} - {type(numero_string)}")
# print(f"{numero_flotante} - {type(numero_flotante)}")
# print(f"{numero_entero} - {type(numero_entero)}")
