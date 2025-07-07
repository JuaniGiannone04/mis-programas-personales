"Cifrado por libro (con letras). Es una forma clásica de cifrado donde el mensaje se codifica por índices de palabras en un texto llave."

import re


def cifrado_libro(llave, mensaje):
    """La funcion recibe una llave (un texto) y un texto
    que se devolvera cifrado"""
    cifrado = []
    llaves = re.split(r"[ .,]+", llave)
    mensajes = mensaje.split(" ")
    for palabra in mensajes:
        if palabra not in llaves:
            raise ValueError("Mensaje no presente en la llave")
        cifrado.append(llaves.index(palabra))
    return cifrado


def main():
    "Funcion main de ejemplo"
    llave_ej = "La casa oscura. El perro ladraba. El viento movia cortinas."
    cifrado_ej = "perro oscura"
    lista = cifrado_libro(llave_ej, cifrado_ej)
    print(lista)


if __name__ == "__main__":
    main()
