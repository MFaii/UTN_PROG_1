# variable_global = 10


def sumar(numero_uno: int, numero_dos: int) -> int:
    """Se encarga de sumar dos numeros

    Args:
        numero_uno (int): Primer Numero
        numero_dos (int): Segundo Numero

    Returns:
        int: El resultado de la suma
    """
    resultado = numero_uno + numero_dos
    return resultado


def saludar(nombre: str) -> None:
    """Se encarga de saludar

    Args:
        nombre (str): Recibe el nombre de la persona
    """
    print(f"Hola {nombre}")
