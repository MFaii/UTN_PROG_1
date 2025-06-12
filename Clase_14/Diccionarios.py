# alumno
# Nombre, Apellido, Legajo, Nota Final, Genero, Edad

# CREACION DICCIONARIO

# FORMA A

# alumno = dict([
#     ("legajo",11111),
#     ("nombre","Mariano"),
#     ("apellido","Fernandez"),
#     ("genero","Masculino"),
#     ("edad",30),
#     ("nota_final",8)
# ])

# FORMA B

# alumno = {
#     "legajo":11111,
#     "nombre":"Mariano",
#     "apellido":"Fernandez",
#     "genero":"Masculino",
#     "edad":30,
#     "nota_final":8
# }

# FORMA C --> Similar a la forma B, pero partiendo de un diccionario vacio

# alumno = {}
# print(alumno)
# #Cuando se asigna una clave en un diccionario si no existe la crea, si existe la modifica

# alumno["legajo"] = 11111
# alumno["nombre"] = "Mariano"
# alumno["apellido"] = "Fernández"
# alumno["genero"] = "Masculino"
# alumno["edad"] = 30
# alumno["nota_final"] = 8
# #alumno["nombre"] = "Juan" #MODIFICA a Mariano por Juan

# for clave in alumno:
#     print(f"{clave}:{alumno[clave]}")

# # print(f"{alumno['nombre']}")
# # print(f"{alumno['apellido']}")


# alumno = {
#     "legajo":11111,
#     "nombre":"Mariano",
#     "apellido":"Fernandez",
#     "genero":"Masculino",
#     "edad":30,
#     "nota_final":8
# }

# Mostrar elementos en un diccionario

# Metodo get() --> Recomiendo usar este metodo

# nombre = alumno["nombre"]
# apellido = alumno["apellido"]

# nombre = alumno.get("nombre")
# apellido = alumno.get("apellido")
# apellido = alumno.get("apellido","NO EXISTE APELLIDO")

# if nombre != None and apellido != None:
#     print(f"NOMBRE COMPLETO: {nombre} {apellido}")
# else:
#     print("HUBO UN PROBLEMA")

# print(f"NOMBRE COMPLETO: {nombre} {apellido}")

# POP --> Elimina la clave que le especifico en el diccionario

# alumno = {
#     "legajo":11111,
#     "nombre":"Mariano",
#     "apellido":"Fernandez",
#     #"genero":"Masculino",
#     "edad":30,
#     "nota_final":8
# }

# print("ANTES DEL POP")
# for clave in alumno:
#     print(f"{clave}:{alumno[clave]}")

# #elemento_eliminado = alumno.pop("genero") #ROMPE
# # elemento_eliminado = alumno.pop("genero",None) #Gracias al parametro default, el pop no rompe
# elemento_eliminado = alumno.pop("genero","NO EXISTE") #Gracias al parametro default, el pop no rompe


# print("")

# print("DESPUES DEL POP")
# for clave in alumno:
#     print(f"{clave}:{alumno[clave]}")

# print(f"Elemento eliminado: {elemento_eliminado}")

# METODO KEYS(), VALUES(), ITEMS()

alumno = {
    "legajo": 11111,
    "nombre": "Mariano",
    "apellido": "Fernandez",
    "genero": "Masculino",
    "edad": 30,
    "nota_final": 8,
}

# KEYS()

# claves = alumno.keys()
# print(claves)
# print(type(claves))

# for clave in alumno.keys():
#     print(clave)

# for clave in alumno:
#     print(clave)

# VALUES()

# valores = alumno.values()
# print(valores)

# for valor in alumno.values():
#     print(valor)

# for clave in alumno:
#     print(alumno[clave])

# ITEMS()

# items = alumno.items()
# print(items)

# for clave,valor in alumno.items():
#     print(f"{clave} - {valor}")

# for clave in alumno:
#     print(f"{clave} - {alumno[clave]}")
