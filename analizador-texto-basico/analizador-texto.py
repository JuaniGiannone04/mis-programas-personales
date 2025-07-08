"""
Es un programa que recibe un texto (Ingresado por el usuario) y
genera estadísticas básicas sobre su contenido.

1. Contar palabras
Total de palabras.
Palabras únicas.

2. Contar caracteres
Total de caracteres.
Caracteres sin contar espacios.
"""


def ingresar_texto():
    """Se le solicita al usuario ingresar un texto base
    del que se generaran las estadisticas basicas de su
    contenido"""
    print("Ingresa una palabra/texto")
    texto = input("")
    return texto


def contar_palabras(texto):
    """Se contaran la cantidad total de palabras y se
    determinaran las palabras unicas junto a la de mayor
    y menor apariciones."""
    palabras = texto.split()
    total_palabras = len(palabras)
    dicc_palabras = {}
    palabras_unicas = []
    menores_apariciones = []
    mayores_apariciones = []

    for palabra in palabras:
        if palabra not in dicc_palabras:
            dicc_palabras[palabra] = 1
        else:
            dicc_palabras[palabra] += 1

    menor_aparicion = min(dicc_palabras.values())
    mayor_aparicion = max(dicc_palabras.values())

    for clave, valor in dicc_palabras.items():
        if valor == 1:
            palabras_unicas.append(clave)
        if valor == menor_aparicion:
            menores_apariciones.append(clave)
        if valor == mayor_aparicion:
            mayores_apariciones.append(clave)

    print(f"Total de palabras: {total_palabras}")
    print(f"Mas apariciones: {", ".join(mayores_apariciones)}")
    print(f"Menos apariciones: {", ".join(menores_apariciones)}")
    print(f"Palabras unicas: {", ".join(palabras_unicas)}")


def contar_caracteres(texto):
    """Se contara la cantidad total de caracteres (sin contar espacios)
    y la cantidad de veces que aparece cada caracter."""
    dicc_carac = {}
    palabras = texto.split()
    cant_caracteres = 0
    for palabra in palabras:
        for caracter in palabra:
            cant_caracteres += 1
            if caracter not in dicc_carac:
                dicc_carac[caracter] = 1
            else:
                dicc_carac[caracter] += 1
    print(f"Total caracteres: {cant_caracteres}")
    print(
        f"{
            (", ".join
                ([f"{clave}: {valor}" for clave, valor in dicc_carac.items()]))
            }"
    )


def main():
    "Funcion main"
    texto_usuario = ingresar_texto()
    contar_palabras(texto_usuario)
    contar_caracteres(texto_usuario)


if __name__ == "__main__":
    main()
