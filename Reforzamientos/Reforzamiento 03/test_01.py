"""1. Escribir una clase en python que contenga un método que convierta un número entero en su cubo
y contenga otro método que obtenga el cuadrado de ese resultado. El valor inicial de resultado deberá estar creado
en el constructor. Considerar un método en la cual le pedirá al usuario ingresar un valor numérico"""

class CalculadoraCubos:
    def __int__(self):
        self.resultado = 0
    def obtener_valor(self):
        num = input("Ingresa valor numérico: ")
        try:
            num = int(num)
            return num
        except:
            print("Error: el valor ingresado no es numérico")
            return None
    def valor_cubo(self):
        num = self.obtener_valor()
        if num is not None:
            self.resultado = num ** 3
    def valor_cuadrado(self):
        self.valor_cubo()
        num = self.resultado ** 2
        return num

calculadora = CalculadoraCubos()
result = calculadora.valor_cuadrado()
print("El resultado al cuadrado del cubo es: ", result)