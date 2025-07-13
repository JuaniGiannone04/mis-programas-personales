"""

Recibe un Sudoku incompleto de tamaño tal que los subcuadros queden
cuadrados (por ejemplo, se ingresa uno de tamaño 9x9 para que los subcuadros
sean de 3x3).

Lo resuelve automaticamente usando backtracking (Tecnica algoritmica
para resolver problemas mediante la experimentacion sistematica de diversas
posibilidades y la reversion de las decisiones previas. Se utiliza la
recursion)

Imprime el resultado (el Sudoku completo).

"""


def ingresar_tablero():
    """Se ingresan los datos del tablero. Primero se ingresa la
    dimension. Y luego se ingresan los numeros que corresponden a
    cada casillero."""
    print("Ingresa el numero de filas y columnas del tablero")
    while True:
        try:
            dimension = int(input(""))
            break
        except ValueError:
            print("Debe ser un numero entero valido")

    tablero = []
    for i in range(dimension):
        subtablero = []
        for j in range(dimension):
            valor = ingreso_valor(dimension, i, j)
            subtablero.append(valor)
        tablero.append(subtablero)

    return tablero, dimension


def ingreso_valor(dimension, fila, columna):
    """
    El usuario ingresa un valor.
    Valida que, si es numerico, el valor sea entre 1 y la dimension.
    En caso contrario, que solo pueda ingresarse "-" para representar vacio.
    """
    while True:
        print(f"Ingresa valor de {[fila + 1], [columna + 1]} '-' PARA VACIO")
        valor = input("")
        if valor.isdigit():
            valor = int(valor)
            if 1 <= valor <= dimension:
                return valor
        elif valor == "-":
            return 0
        print("Se debe ingresar un valor valido para el tablero")


def validar_ingreso(tablero, dimension):
    """Se valida que los datos ingresados sean compatibles
    con el sudoku.
    Valida que sea compatible en las filas, columnas y
    subcuadros."""
    for fila in range(len(tablero)):
        for col in range(len(tablero[0])):
            if tablero[fila][col] != 0:
                num = tablero[fila][col]
                if (
                    not validar_fila(tablero, fila, dimension, num, col)
                    or not validar_columna(tablero, fila, dimension, num, col)
                    or not validar_recuadro(tablero, fila, dimension, num, col)
                ):
                    return False
    return True


def validar_fila(tablero, fila, dimension, num, col):
    """Se valida que no hayan valores iguales en las filas"""
    for i in range(dimension):
        if col != i:
            if num == tablero[fila][i]:
                return False
    return True


def validar_columna(tablero, fila, dimension, num, col):
    """Se valida que no hayan valores iguales en las columnas"""
    for i in range(dimension):
        if fila != i:
            if num == tablero[i][col]:
                return False
    return True


def validar_recuadro(tablero, fila, dimension, num, col):
    """Se valida que no hayan valores iguales en las columnas y filas
    en los recuadros formados por la dimension"""
    subcuadro = int(dimension**0.5)
    fila_inicio = (fila // subcuadro) * subcuadro
    col_inicio = (col // subcuadro) * subcuadro
    for i in range(fila_inicio, fila_inicio + subcuadro):
        for j in range(col_inicio, col_inicio + subcuadro):
            if i != fila or j != col:
                if tablero[i][j] == num:
                    return False
    return True


def resolver_sudoku(dimension, tablero):
    "Resuelve el sudoku usando el algoritmo de backtracking"
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if tablero[fila][columna] == 0:
                for numero in range(1, dimension + 1):
                    tablero[fila][columna] = numero
                    if validar_ingreso(tablero, dimension):
                        if resolver_sudoku(dimension, tablero):
                            return True
                    tablero[fila][columna] = 0
                return False
    return True


def imprimir_tablero(tablero):
    """Imprime el tablero de Sudoku."""
    dimension = len(tablero)
    subcuadro = int(dimension**0.5)

    for i in range(dimension):
        if i % subcuadro == 0 and i != 0:
            print("-" * (dimension * 2 + subcuadro - 1))

        fila = ""
        for j in range(dimension):
            if j % subcuadro == 0 and j != 0:
                fila += "| "
            valor = tablero[i][j]
            fila += f"{valor if valor != 0 else '-'} "
        print(fila)


def main():
    "Funcion principal main"
    tablero, dimension = ingresar_tablero()

    print("\nTablero ingresado:")
    imprimir_tablero(tablero)

    if resolver_sudoku(dimension, tablero):
        print("\nSudoku resuelto:")
        imprimir_tablero(tablero)
    else:
        print("\nNo se pudo resolver el Sudoku (no tiene solucion valida).")


if __name__ == "__main__":
    main()
