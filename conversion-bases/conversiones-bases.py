"""
Programa que convierte numeros decimales (base 10) entre diferentes sistemas
numericos.
Se utilizara con los sistemas mas comunes:
binario (base 2),
octal (base 8) y
hexadecimal (base 16)
Esto se hara para numeros enteros positivos (suponiendo que los numeros
ingresados por el usuario seran de este tipo).
Para llevar a cabo estas funciones, se utilizaran un tipo de funciones llamadas
"RECURSIVAS" que se llaman a si mismas dentro de su propia definicion.
"""

# --------------------------------------------------------------------------------------------------

# CONVERSION DE DECIMAL A BINARIO


def _decimal_a_binario(numero):
    """La conversion a binario consiste en dividir el numero
    original por 2 sucesivamente y registrar los restos (0 o 1)
    en orden inverso."""
    if numero == 0:  # Caso base
        return ""
    return _decimal_a_binario(numero // 2) + str(numero % 2)  # Caso recursivo


def decimal_a_binario(numero):
    """Esta funcion wrapped devuelve '0' explicitamente si
    el número ingresado es cero, para mantener la representación
    binaria correcta."""
    if numero == 0:  # Caso numero ingresado 0
        return "0"
    return _decimal_a_binario(numero)


# --------------------------------------------------------------------------------------------------

# CONVERSION DE DECIMAL A OCTAL


def decimal_a_octal(numero):
    """La conversion de decimal a octal consiste en dividir por 8
    el numero original hasta que este sea menor a dicho numero. En ese caso,
    el octal se conforma por el ultimo cociente y todos los restos"""
    if numero < 8:  # Caso base
        return str(numero)
    return decimal_a_octal(numero // 8) + str(numero % 8)  # Caso recursivo


# --------------------------------------------------------------------------------------------------

# CONVERSION DE DECIMAL A HEXADECIMAL


def decimal_a_hexa(numero):
    """La conversion decimal a hexagonal consiste en dividir por 16 hasta
    que el numero original sea menor a 16. Se va componiendo el numero con
    los restos y, si algun resto es mayor a 10 y menor a 16 se coloca una
    letra de la A a la F, sino, se coloca simplemente el numero del resto"""
    dicc_hexa = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    if numero < 16:
        if numero < 10:
            return str(numero)
        return dicc_hexa[numero]
    if (numero % 16) >= 10:
        return decimal_a_hexa(numero // 16) + dicc_hexa[numero % 16]
    return decimal_a_hexa(numero // 16) + str(numero % 16)
