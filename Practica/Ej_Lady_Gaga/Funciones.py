def mostrar_playlist(playlist: list):
    for i in range(len(playlist)):
        cancion = playlist[i]
        for clave in cancion:
            print(f"{clave} : {cancion[clave]}")
        print("")


def normalizar_playlist(playlist: list) -> None:
    for i in range(len(playlist)):
        cancion = playlist[i]
        normalizar_cancion(cancion)


def normalizar_cancion(cancion: dict) -> None:
    cancion["Titulo"] = obtener_titulo(cancion["Tema"])
    cancion["Colaboradores"] = obtener_colaboradores(cancion["Tema"])
    cancion.pop("Tema")


def obtener_titulo(tema: str) -> str:
    titulo = ""
    bandera_colaborador = False
    bandera_guion = False
    for i in range(len(tema)):
        if tema[i] == "|":
            bandera_colaborador = True
        if bandera_colaborador == True and tema[i - 2] == "-":
            bandera_guion = True
        if bandera_guion == True:
            titulo += tema[i]

    if bandera_colaborador == False:
        titulo = tema

    return titulo


def obtener_colaboradores(tema: str) -> list:
    lista_colaboradores = []
    colaborador = ""
    for i in range(len(tema)):
        if (
            tema[i] == " "
            and tema[i + 1] == "|"
            or tema[i] == " "
            and tema[i + 1] == "-"
        ):
            lista_colaboradores.append(colaborador)

        if tema[i - 2] == "|" and tema[i - 1] == " ":
            colaborador = ""
        colaborador += tema[i]

    return lista_colaboradores
