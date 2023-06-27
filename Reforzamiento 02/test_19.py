"""19. Crea una lista vacía (con 10 posiciones), pide sus valores y devuelve la suma y la media de los números"""
lista = [0] * 10

for i in range(10):
    lista[i] = int(input("Ingresa el valor {}: ".format(i + 1)))

suma = sum(lista)
media = suma / len(lista)

print("Suma: {}".format(suma))
print("Media: {}".format(media))