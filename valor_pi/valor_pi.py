"Funciones que aproximan el valor de PI utilizando distintos métodos"

import math
import random


def factorial(n):
    "Funcion auxiliar para calcular el factorial"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# --------------------------------------------------------------------

# Serie de Leibniz


def leibniz_pi(n, total):
    """Serie de Leibniz (muy sencilla, pero lenta).
    Usa una serie infinita con sumas y restas alternadas."""
    if n == total:
        return 0
    termino = (-1) ** n / (2 * n + 1)
    return termino + leibniz_pi(n + 1, total)


def valor_pi_uno():
    "Devuelve un aproximado del valor de PI."
    return 4 * leibniz_pi(0, 995)


# --------------------------------------------------------------------

# Serie de Nilakantha


def nilakantha_pi(n, total):
    """Parecida a Leibniz pero más precisa por iteración.
    Implica alternar fracciones de números impares con signos alternados."""
    if n == total:
        return 0
    termino = ((-1) ** (n + 1)) * 4 / ((2 * n) * (2 * n + 1) * (2 * n + 2))
    return termino + nilakantha_pi(n + 1, total)


def valor_pi_dos():
    "Devuelve un aproximado del valor de PI"
    return 3 + nilakantha_pi(1, 995)


# --------------------------------------------------------------------

# Fórmula de Gauss-Legendre


def gauss_legendre_pi(iteraciones):
    """Muy precisa y rápida, pero requiere álgebra con raíces cuadradas y
    medias aritmético-geométricas.
    Se usa en algoritmos de alto rendimiento como los que calcularon millones
    de dígitos."""

    a = 1.0
    b = 1.0 / math.sqrt(2)
    t = 0.25
    p = 1.0

    for _ in range(iteraciones):
        a_nuevo = (a + b) / 2
        b = math.sqrt(a * b)
        t -= p * (a - a_nuevo) ** 2
        a = a_nuevo
        p *= 2

    pi_aprox = ((a + b) ** 2) / (4 * t)
    return pi_aprox


def valor_pi_tres():
    "Devuelve un aproximado del valor de PI"
    return gauss_legendre_pi(995)


# --------------------------------------------------------------------

# Algoritmo de Chudnovsky


def chudnovsky_pi(n, total):
    """El más eficiente para muchos decimales.
    Usa factoriales y raíces cuadradas."""
    if n == total:
        return 0
    num = ((-1) ** n) * factorial(6 * n) * (13591409 + (545140134 * n))
    den = factorial(3 * n) * (factorial(n) ** 3) * (640320 ** ((3 * n)))
    termino = num / den
    return termino + chudnovsky_pi(n + 1, total)


def valor_pi_cuatro():
    "Devuelve un valor aproximado del numero PI"
    return 1 / ((12 / math.sqrt(640320**3)) * chudnovsky_pi(0, 995))


print(valor_pi_tres())


# --------------------------------------------------------------------

# Método de Monte Carlo


def montecarlo_pi(num_puntos):
    """Usa simulación aleatoria de puntos dentro de un cuadrado y un
    círculo."""
    dentro = 0

    for _ in range(num_puntos):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            dentro += 1

    return 4 * dentro / num_puntos


def valor_pi_cinco():
    "Devuelve un aproximado del valor de PI"
    return montecarlo_pi(1000000)


# --------------------------------------------------------------------


def main():
    "Devuelve los resultados aproximados de los métodos"
    print("\nValor por Serie de Leibniz:\n")
    print(f"{valor_pi_uno():.15f}")
    print("\nValor por Serie de Nilakantha:\n")
    print(f"{valor_pi_dos():.15f}")
    print("\nValor por Fórmula de Gauss-Legendre:\n")
    print(f"{valor_pi_tres():.15f}")
    print("\nValor por Algoritmo de Chudnovsky:\n")
    print(f"{valor_pi_cuatro():.15f}")
    print("\nValor por Método de Monte Carlo:\n")
    print(f"{valor_pi_cinco():.15f}\n")


if __name__ == "__main__":
    main()
