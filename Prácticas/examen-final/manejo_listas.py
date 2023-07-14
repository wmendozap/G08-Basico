import random


def generar_lista_aleatoria():
    lista = []
    for _ in range(10):
        lista.append(random.randint(1, 10))
    print("Lista aleatoria generada:")
    print(lista)
    return lista


def obtener_numeros_no_repetidos(lista):
    numeros_no_repetidos = list(set(lista))
    print("Números no repetidos:")
    print(numeros_no_repetidos)
    return numeros_no_repetidos


def ordenar_listas(numeros_no_repetidos):
    lista_ordenada_ascendente = sorted(numeros_no_repetidos)
    lista_ordenada_descendente = sorted(numeros_no_repetidos, reverse=True)
    print("Lista ordenada de forma ascendente:")
    print(lista_ordenada_ascendente)
    print("Lista ordenada de forma descendente:")
    print(lista_ordenada_descendente)
    return lista_ordenada_ascendente, lista_ordenada_descendente


def obtener_mayor_numero(lista):
    mayor_numero = max(lista)
    print("Mayor número de la lista:")
    print(mayor_numero)
    return mayor_numero
