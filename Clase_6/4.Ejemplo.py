# Necesitamos un sistema que me permita cargas las notas de 5 alumnos en la universidad (1 al 10)
# Necesitamos mostrar la suma y el promedio de esas notas, al final mostrar cada una de esas notas

notas_alumnos = [0, 0, 0, 0, 0]
# notas_alumnos = [None,None,None,None,None]
suma_notas = 0

print(f"Array antes de la carga {notas_alumnos}")

for i in range(len(notas_alumnos)):
    nota_alumno = int(input("Ingrese la nota del alumno (1-10): "))

    while nota_alumno > 10 or nota_alumno < 1:
        print("ERROR, la nota debe estar entre 1 y 10")
        nota_alumno = int(input("Reingrese la nota del alumno (1-10): "))

    # Lo guardo en mi arreglo
    notas_alumnos[i] = nota_alumno
    suma_notas += nota_alumno

print(f"Array despues de la carga {notas_alumnos}")
promedio_notas = suma_notas / len(notas_alumnos)

print(f"La suma de notas es de {suma_notas}")
print(f"El promedio de notas es de {promedio_notas}")
