""" 
1. Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
a. Si es invierno: solo se viaja a Bariloche.
b. Si es verano: se viaja a Mar del plata y Cataratas.
c. Si es otoño: se viaja a todos los lugares.
d. Si es primavera: se viaja a todos los lugares menos Bariloche.

"""

estacion = input("Ingrese la estacion: ").lower()
destino = input ("Ingrese el destino: ").lower()

mensaje = ""

match estacion:
  case "invierno":
    if destino == "bariloche":
      mensaje = "Se viaja"
    else: 
      mensaje = "No se viaja"
  case "verano":
    if destino == "mar del plata" or destino == "cataratas":
      mensaje = "Se viaja"
    else: 
      mensaje = "No se viaja"
  case "otoño":
    mensaje = "Se viaja"
  case "primavera":
    if destino != "bariloche":
      mensaje = "Se viaja"
    else: 
      mensaje = "No se viaja"
  case _:
    mensaje = "No se viaja"
    
print(f"El destino es {destino}, en la estacion: {estacion}, por lo tanto: {mensaje}")
  