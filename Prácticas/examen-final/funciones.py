import random
import math


def crear_fichero():
    archivo = open("notas.txt", "w")
    archivo.close()


def llenar_lista(tamano):
    lista = []
    for _ in range(tamano):
        lista.append(random.randint(1, 100))
    return lista


def escribir_lista_en_fichero(lista):
    archivo = open("notas.txt", "a")
    for numero in lista:
        archivo.write(str(numero) + "\n")
    archivo.close()


def calcular_raiz_cuadrada(lista):
    raices = [math.sqrt(numero) for numero in lista]
    return raices


def escribir_raices_en_fichero(raices):
    archivo = open("notas.txt", "a")
    for raiz in raices:
        archivo.write(str(raiz) + "\n")
    archivo.close()
