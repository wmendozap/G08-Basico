"""13. Elimina ahora todos los elementos de la lista creada previamente y mostrar en consola el estado de la lista """
lista_4 = [
    152.60,
    895.01,
    False,
    True,
    True,
    2563.12
]
lista_4.clear()

# len(lista_4) == 0
if not bool(lista_4):
    print("Lista vacía")
else:
    print("Longitud de la lista: {}".format(len(lista_4)))