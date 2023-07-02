class Gato:
    def sonido(self):
        print("Miua")

class Perro:
    def sonido(self):
        print("Gua")

class Vaca:
    def sonido(self):
        print("Mu")


def bulla(animales):
    for animal in animales:
        animal.sonido()

gato = Gato()
perro = Perro()
vaca = Vaca()

lista_animales = [gato, perro, vaca]
bulla(lista_animales)