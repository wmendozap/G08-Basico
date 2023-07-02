class Carro:
    ruedas = 4
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

carro_1 = Carro("Negro", 50)
print("Color: {}".format(carro_1.color))
print("Aceleracion: {}".format(carro_1.aceleracion))
print("Ruedas: {}".format(carro_1.ruedas))

carro_1.marchas = 500
print(carro_1.marchas)

carro_2 = Carro("Rojo", 550)
print(carro_2.marchas)