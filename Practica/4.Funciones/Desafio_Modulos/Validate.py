def validate_number(cadena: str, es_float: bool) -> bool:
    decimal = 0

    for i in range(len(cadena)):
        caracter = cadena[i]

        if caracter == ".":
            if not es_float:
                return False
            decimal += 1
            if decimal > 1:
                return False

        elif caracter == "-":
            if i != 0:
                return False

        elif caracter < "0" and caracter > "9":
            return False

    return True


def validate_length(cadena: str, longitud: int) -> bool:
    return len(cadena) == longitud
