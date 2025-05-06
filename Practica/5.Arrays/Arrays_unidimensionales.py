# 1.Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
def crear_array(cantidad: int) -> list:
    numeros = []
    for i in range(cantidad):
        numero = int(input(f"Ingrese el numero {i +1}: "))
        numeros = numeros + [numero]
    return numeros


cantidad_elementos = int(input("Ingrese la cantidad de elementos(numeros): "))
lista = crear_array(cantidad_elementos)
print(f"Array creado: {lista}")
