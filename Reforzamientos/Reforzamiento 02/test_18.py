"""18. Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes repetidos
(los cuales son impares dentro del rango indicado y que no sea el último impar)
- Empezando desde 1 y no 0.
- Agregar una cadena en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del."""

numeros_impares = [i for i in range(1, 31) if i % 2 != 0][:15]

flotantes_repetidos = [3.3, 5.5, 7.7]
numeros_impares.extend(flotantes_repetidos)
numeros_impares.insert(2, "MENDOZA")

print(numeros_impares)
del numeros_impares[2]
print(numeros_impares)

