#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 4:
        print("USO: calculadora.py num1 operador num2")
        print("EJEMPLO: calculadora.py 5 + 3")
        return

    num1 = sys.argv[1]
    operador = sys.argv[2]
    num2 = sys.argv[3]

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("ERROR: los operandos deben ser numeros.")
        return

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 == 0:
            print("ERROR: división por cero.")
            return
        resultado = num1 / num2
    else:
        print("OPERADOR NO VALIDO. Usa +, -, * o /.")
        return

    print(f"RESULTADO: {resultado}")

if __name__ == "__main__":
    main()
