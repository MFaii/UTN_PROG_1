#El match es una estructura condicional que me permite evaluar solo por igualdad, funciona de manera similar al if-elif

#Enero - Febrero - Marzo -> Verano
#Abril - Mayo - Junio -> Otoño
#Julio - Agosto - Septiembre -> Invierno
#Octubre - Noviembre - Diciembre -> Primavera

#En caso de ponen un mes incorrecto, dar error.

mes = input("Ingrese el mes del año: ")

match mes:
    case "Enero" | "Febrero" | "Marzo" :
        print("Verano")
    case "Abril" | "Mayo" | "Junio":
        print("Otoño")
    case "Julio" | "Agosto" | "Septiembre":
        print("Invierno")
    case "Octubre" | "Noviembre" | "Diciembre":
        print("Primavera")
    case _:
        print(f"{mes} es un mes invalido")