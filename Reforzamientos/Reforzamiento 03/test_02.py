"""2. Crear una clase en python que contenga un método que revierta una cadena de palabras
Input: Hola Pythonista, seguimos adelante
Output: adelante seguimos Pythonista, Hola"""

class RevierteCadena:
    def __init__(self, cadena):
        self.cadena = cadena
    def revertir_cadena(self):
        cadena = self.cadena.split()
        resultado = " ".join(cadena[::-1])
        return resultado

revertir = RevierteCadena("Hola Pythonista, seguimos adelante")
print(revertir.revertir_cadena())