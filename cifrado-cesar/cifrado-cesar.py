"""Se hara un programa que imite el comportamiento del cifrado cesar.
Se pedira una palabra a cifrar y la cantidad de tabulaciones que se le
hara a los digitos para cambiarlos, utilizando todos los digitos presentes
en el ASCII."""

 
def armar_diccionario_ascii():
    "Diccionario con todos los caracteres del codigo ASCII"
    ascii_dict = {}
    for i in range(128):
        ascii_dict[chr(i)] = i
    return ascii_dict


def cifrar_cesar(message, tabulations):
    """Se utilizara el cifrado cesar para cifrar un conjunto
    de caracteres dados"""
    encryption = []
    dicc = armar_diccionario_ascii()
    for letra in message:
        if letra not in dicc:
            encryption.append("?")
        else:
            codigo = chr((dicc[letra] + tabulations) % 128)
            encryption.append(codigo)
    result = "".join(encryption)
    return result


def main():
    "Main function"
    ex_message = "HOLA COMO ESTAS"
    ex_encriptation = cifrar_cesar(ex_message, 2)
    print(ex_encriptation)


if __name__ == "__main__":
    main()
