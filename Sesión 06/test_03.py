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

carro_1 = Carro("Negro", 90)
print("Velocidad: {}".format(carro_1.velocidad))
carro_1.acelerar()
carro_1.acelerar()
print(carro_1.velocidad)

carro_1.acelerar()
carro_1.acelerar()

carro_1.frena()
carro_1.frena()
carro_1.frena()
carro_1.frena()

print(carro_1.velocidad)