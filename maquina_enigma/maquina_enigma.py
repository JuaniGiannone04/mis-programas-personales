"""La máquina Enigma fue un dispositivo de cifrado electromecánico utilizado
principalmente por la Alemania nazi durante la Segunda Guerra Mundial para
proteger sus comunicaciones militares. Era conocida por su complejidad y por
generar un cifrado polialfabético, que cambiaba con cada pulsación de tecla,
lo que la hacía aparentemente difícil de romper."""


class Rotor:
    """
    Clase Rotor que es como un disco con 26 posiciones, una por cada letra
    del alfabeto. Internamente, cada una de esas letras se mapea a otra letra,
    como una especie de sustitución cifrada. Cada vez que se cifra una letra,
    el rotor gira una posición, lo cual cambia completamente cómo se hace la
    sustitución la próxima vez. Por eso, aunque escribas la misma letra dos
    veces, el resultado cifrado puede ser diferente, porque el rotor gira
    entre una y otra.
    """

    def __init__(self):
        "Constructor de la clase rotor"
        self.mapeo = {
            "A": "E",
            "B": "K",
            "C": "M",
            "D": "F",
            "E": "L",
            "F": "G",
            "G": "D",
            "H": "Q",
            "I": "V",
            "J": "Z",
            "K": "N",
            "L": "T",
            "M": "O",
            "N": "W",
            "O": "Y",
            "P": "H",
            "Q": "X",
            "R": "U",
            "S": "S",
            "T": "P",
            "U": "A",
            "V": "I",
            "W": "B",
            "X": "R",
            "Y": "C",
            "Z": "J",
        }
        self.mapeo_inverso = {v: k for k, v in self.mapeo.items()}
        self.posicion = 0

    def codificar(self, letra):
        """Toma una letra de entrada, ajusta según la posición actual,
        aplica el mapeo y devuelve la letra de salida.
        El desplazamiento se hace sumando la
        posición antes de mirar el diccionario."""
        if not letra.isalpha():
            raise ValueError("Solo se pueden ingresar letras")
        letra = letra.upper()
        # Convertir letra a índice numérico 0-25
        indice = ((ord(letra) - ord("A")) + self.posicion) % 26
        # Convertir índice rotado a letra (mayúscula)
        letra_rotada = chr(indice + ord("A"))
        # Buscar la letra codificada en el mapeo
        salida = self.mapeo[letra_rotada]
        return salida

    def decodificar(self, letra):
        """Lo inverso de codificar: aplica el mapeo inverso ajustado a
        la posición."""
        if not letra.isalpha():
            raise ValueError("Solo se pueden ingresar letras")
        letra = letra.upper()
        # Letra de entrada se "desmapea" primero
        letra_intermedia = self.mapeo_inverso[letra]
        # Luego se corrige el desplazamiento inverso
        indice = ((ord(letra_intermedia) - ord("A")) - self.posicion) % 26
        salida = chr(indice + ord("A"))
        return salida

    def rotar(self):
        "El rotor avanza una posicion"
        self.posicion = (self.posicion + 1) % 26

    def resetear(self):
        """Para volver la posición a 0 si se quiere cifrar el
        mismo mensaje de nuevo."""
        self.posicion = 0


class Reflector:
    """Su función es reflejar la señal que viene desde los rotores de
    forma que vuelva por otro camino. Esta reflexión permite que el
    cifrado sea simétrico, es decir: si A se convierte en M, entonces
    M se convierte en A al pasar por el reflector."""

    def __init__(self):
        "Constructor de clase Reflector"
        self.mapeo_reflector = {
            "A": "Y",
            "Y": "A",
            "B": "R",
            "R": "B",
            "C": "U",
            "U": "C",
            "D": "H",
            "H": "D",
            "E": "Q",
            "Q": "E",
            "F": "S",
            "S": "F",
            "G": "L",
            "L": "G",
            "I": "Z",
            "Z": "I",
            "J": "N",
            "N": "J",
            "K": "V",
            "V": "K",
            "M": "W",
            "W": "M",
            "O": "X",
            "X": "O",
            "P": "T",
            "T": "P",
        }

    def reflejar(self, letra):
        "Devuelve valor reflejado"
        return self.mapeo_reflector[letra.upper()]


class MaquinaEnigma:
    """Esta clase va a ser el "cerebro" del sistema, ya que orquesta cómo se
    cifran o descifran letras y mensajes completos"""

    def __init__(self):
        "Constructor de Clase MaquinaEnigma"
        self.reflector = Reflector()
        self.rotor1 = Rotor()
        self.rotor2 = Rotor()
        self.rotor3 = Rotor()

    def cifrar_letra(self, letra):
        """Se encarga de tomar una sola letra, procesarla completamente y
        devolver su versión cifrada. Pasa por 3 rotores"""
        letra_codificada = self.rotor1.codificar(letra)
        letra_codificada = self.rotor2.codificar(letra_codificada)
        letra_codificada = self.rotor3.codificar(letra_codificada)

        letra_reflejada = self.reflector.reflejar(letra_codificada)

        letra_final = self.rotor3.decodificar(letra_reflejada)
        letra_final = self.rotor2.decodificar(letra_final)
        letra_final = self.rotor1.decodificar(letra_final)

        self.rotor1.rotar()
        if self.rotor1.posicion == 0:
            self.rotor2.rotar()  # Metodo de STEPPING para que un rotor rote
            # solo si el anterior dio la vuelta completa
            if self.rotor2.posicion == 0:
                self.rotor3.rotar()

        return letra_final

    def cifrar_mensaje(self, mensaje):
        """Se encarga de tomar las letras de un mensaje, procesarlas
        completamente y devolver su versión cifrada."""
        mensaje_final = ""
        for letra in mensaje:
            if letra != " ":
                mensaje_final += self.cifrar_letra(letra)
            else:
                mensaje_final += letra
        return mensaje_final

    def resetear(self):
        """Vuelve los tres rotores a la posición inicial 0."""
        self.rotor1.resetear()
        self.rotor2.resetear()
        self.rotor3.resetear()


def main():
    "Funcion principal main"
    maquina = MaquinaEnigma()

    mensaje = "HOLA como ESTAS"
    print("Mensaje original:", mensaje)

    mensaje_cifrado = maquina.cifrar_mensaje(mensaje)
    print("Mensaje cifrado:", mensaje_cifrado)

    maquina.resetear()

    mensaje_descifrado = maquina.cifrar_mensaje(mensaje_cifrado)
    print("Mensaje descifrado:", mensaje_descifrado)

    print("PROCESO COMPLETADO")


if __name__ == "__main__":
    main()
