"""
Usuario ingresa una grilla.

Se revisa en una sopa de letras si conjunto de palabras:

Aparecen en horizontal (de izquierda a derecha).

Aparecen en vertical (de arriba hacia abajo).

Aparecen en diagonal (en ambas diagonales).

Aparecen en sentido inverso.

"""


def armar_grilla():
    """El usuario ingresa las medidas de la grilla y va ingresando
    como esta compuesta."""
    print("Ingresa la cantidad de filas de la grilla")
    filas = int(input(""))
    print("Ingresa la cantidad de columnas de la grilla")
    columnas = int(input(""))
    lista = []
    for i in range(filas):
        sublista = []
        for j in range(columnas):
            while True:
                print(f"Ingresa el valor de la posicion {[i + 1], [j + 1]}")
                letra = input("").lower()
                if len(letra) == 1 and letra.isalpha():
                    sublista.append(letra)
                    break
                print("Se debe ingresar una letra")
        lista.append(sublista)
    return lista


def imprimir_grilla(grilla):
    "Imprime por pantalla la grilla ingresada"
    print("\n")
    for fila in grilla:
        print(" ".join(fila))
    print("")


def ingresar_palabra():
    """El usuario ingresa la palabra que desea buscar
    en la sopa de letras"""
    while True:
        print("Ingresa la palabra que se desea buscar (-1 para terminar)")
        busqueda = input("")
        if busqueda == "-1":
            return None
        if len(busqueda) > 0:
            return busqueda.lower()
        print("Ingreso invalido")


def buscar_horizontal_normal(grilla, palabra):
    """Se busca la palabra de derecha a izquierda
    de manera horizontal"""
    for fila in range(len(grilla)):
        for columna in range((len(grilla[0]) - (len(palabra) - 1))):
            if grilla[fila][columna] == palabra[0]:
                for i, letra in enumerate(palabra[1:], start=1):
                    if letra != grilla[fila][columna + i]:
                        break
                else:
                    return fila + 1, columna + 1
    return None


def buscar_vertical_normal(grilla, palabra):
    """Se busca la palabra de arriba hacia abajo"""
    for columna in range(len(grilla[0])):
        for fila in range(len(grilla) - (len(palabra) - 1)):
            if grilla[fila][columna] == palabra[0]:
                for i, letra in enumerate(palabra[1:], start=1):
                    if letra != grilla[fila + i][columna]:
                        break
                else:
                    return fila + 1, columna + 1
    return None


def buscar_diagonal_normal(grilla, palabra):
    """Se busca la palabra diagonalmente de izquierda
    a derecha"""
    for fila in range(len(grilla) - (len(palabra) - 1)):
        for columna in range(len(grilla[0]) - (len(palabra) - 1)):
            if grilla[fila][columna] == palabra[0]:
                for i, letra in enumerate(palabra[1:], start=1):
                    if letra != grilla[fila + i][columna + i]:
                        break
                else:
                    return fila + 1, columna + 1
    return None


def buscar_horizontal_invertida(grilla, palabra):
    """Se busca la palabra de izquierda a derecha
    de manera horizontal"""
    for fila in range(len(grilla)):
        for columna in range(len(grilla[0]) - 1, (len(palabra) - 1), -1):
            if grilla[fila][columna] == palabra[0]:
                for i, letra in enumerate(palabra[1:], start=1):
                    if letra != grilla[fila][columna - i]:
                        break
                else:
                    return fila + 1, columna + 1
    return None


def buscar_vertical_invertida(grilla, palabra):
    """Se busca la palabra de abajo hacia arriba"""
    for columna in range(len(grilla[0])):
        for fila in range((len(grilla) - 1), (len(palabra) - 2), -1):
            if grilla[fila][columna] == palabra[0]:
                for i, letra in enumerate(palabra[1:], start=1):
                    if letra != grilla[fila - i][columna]:
                        break
                else:
                    return fila + 1, columna + 1
    return None


def buscar_diagonal_invertida(grilla, palabra):
    """Se busca la palabra diagonalmente de derecha a
    izquierda"""
    for fila in range(len(grilla) - 1, len(palabra) - 2, -1):
        for columna in range(len(grilla[0]) - 1, len(palabra) - 2, -1):
            if grilla[fila][columna] == palabra[0]:
                for i, letra in enumerate(palabra[1:], start=1):
                    if letra != grilla[fila - i][columna - i]:
                        break
                else:
                    return fila + 1, columna + 1
    return None


def main():
    "Funcion principal main"
    sopa_letras = armar_grilla()
    imprimir_grilla(sopa_letras)
    while True:
        palabra = ingresar_palabra()
        if palabra is None:
            print("Programa finalizado")
            break
        busquedas = [
            ("horizontal normal", buscar_horizontal_normal),
            ("vertical normal", buscar_vertical_normal),
            ("diagonal normal", buscar_diagonal_normal),
            ("horizontal invertida", buscar_horizontal_invertida),
            ("vertical invertida", buscar_vertical_invertida),
            ("diagonal invertida", buscar_diagonal_invertida),
        ]

        for nombre, funcion in busquedas:
            posicion = funcion(sopa_letras, palabra)
            if posicion is not None:
                print(f"FILA: {posicion[0]} COLUMNA: {posicion[1]}")
                print(f"DIRECCION: {nombre}")
                break
        else:
            print("La palabra no fue encontrada.")


if __name__ == "__main__":
    main()
