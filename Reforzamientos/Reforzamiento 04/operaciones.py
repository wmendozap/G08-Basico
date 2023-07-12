# operaciones.py

import random
import math

def cargar_numero():
    try:
        numero = int(input("Ingrese un número entero: "))
        return numero
    except ValueError:
        raise ValueError("Debe ingresar un número entero válido.")

def sumar_valores(a, b):
    try:
        suma = a + b
        return suma
    except TypeError:
        raise TypeError("Los valores proporcionados no se pueden sumar.")

def generar_numeros_aleatorios():
    numeros = []
    for _ in range(30):
        numero = random.randint(0, 100)
        numeros.append(numero)
    return numeros

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

def mostrar_raiz_cuadrada(valor):
    try:
        raiz_cuadrada = math.sqrt(valor)
        print("La raíz cuadrada de {} es: {:.2f}".format(valor, raiz_cuadrada))
    except ValueError:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")

def mostrar_cuadrado_cubo(valor):
    cuadrado = valor ** 2
    cubo = valor ** 3
    print("El cuadrado de {} es: {}".format(valor, cuadrado))
    print("El cubo de {} es: {}".format(valor, cubo))
