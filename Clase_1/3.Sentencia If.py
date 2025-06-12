#Ejemplo -> Deberiamos decir la palabra "Hola" si el que ingreso al sistema es "Mariano"

# #1.Entrada -> Pedir el nombre
# nombre = input("Ingrese su nombre: ")

# #2.Proceso -> Esta vez tenemos que tomar una decision
# if nombre == "Mariano":
#     print("Hola")
#     #print("Entra al if")

# #3.Salida 
# print(f"El nombre es {nombre}")

#Ejemplo -> Deberiamos decir la palabra "Hola" si el que ingreso al sistema es "Mariano" sino debemos decir "Chau"

# nombre = input("Ingrese su nombre: ")

# # if nombre == "Mariano":
# #     print("Hola")
    
# # if nombre != "Mariano":
# #     print("Chau")

# if nombre == "Mariano":
#     print("Hola")
# else:
#     print("Chau")

#Ejemplo -> Deberiamos decir 'sos adulto' si la persona tiene 18 años o más (VERIFICADO)
#Deberiamos decir sos adolescente si la persona tiene entre 13 y 17 años
#Deberiamos decir sos niño si la persona es menor de 13 años

edad = int(input("Ingrese su edad: "))

#Este if verifica si sos adulto
# if edad >= 18:
#     print("Sos adulto")
# else:
#     #Pueden ser niños o adolescentes
#     if edad >= 13 and edad <= 17:
#         print("Sos adolescente")
#     else:
#         print("Sos niño")

if edad >= 18: 
    print("Sos adulto")
elif edad >= 13 and edad <=17:
    print("Sos adolescente")
else:
    print("Sos un niño")