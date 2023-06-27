"""11. Crear una lista (entre floats y bools, 6 elementos mínimo) donde imprimas el penúltimo y último valor (por índice)"""
lista_4 = [
    152.60,
    895.01,
    False,
    True,
    True,
    2563.12
]
print("Penúltimo valor de la lista: {}".format(lista_4[len(lista_4) - 2]))
print("Último valor de la lista: {}".format(lista_4[len(lista_4) - 1]))