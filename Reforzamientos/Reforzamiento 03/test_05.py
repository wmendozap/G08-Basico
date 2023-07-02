"""5. Crear una clase llamada círculo que contenga radio en su constructor y que contenga un método área que devuelva
el área de un círculo. Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios."""


class Circulo:
    def __init__(self, radio):
        if not isinstance(radio, (int, float)):
            raise TypeError("El radio debe ser un número.")

        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.radio

try:
    radio1 = float(input("Ingresa el radio del primer círculo: "))
    circulo1 = Circulo(radio1)
    area1 = circulo1.calcular_area()
    perimetro1 = circulo1.calcular_perimetro()
    print("Primer círculo")
    print("Área: ", area1)
    print("Perímetro: ", perimetro1)

    radio2 = float(input("\nIngresa el radio del segundo círculo: "))
    circulo2 = Circulo(radio2)
    area2 = circulo2.calcular_area()
    perimetro2 = circulo2.calcular_perimetro()
    print("Segundo círculo")
    print("Área: ", area2)
    print("Perímetro: ", perimetro2)
except ValueError:
    print("El valor ingresado no es numérico")
except TypeError as e:
    print(str(e))