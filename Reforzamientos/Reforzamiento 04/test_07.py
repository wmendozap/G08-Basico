"""7. Creando un archivo principal (main.py) donde importará a un módulo (operaciones.py) el cuál
contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y 100, que muestre en pantalla esta lista.
- Otra función que ordene los valores de una lista y volver a mostrarla."""

from operaciones import generar_numeros_aleatorios, ordenar_lista

numeros_aleatorios = generar_numeros_aleatorios()
print("Lista generada:", numeros_aleatorios)

numeros_ordenados = ordenar_lista(numeros_aleatorios)
print("Lista ordenada:", numeros_ordenados)
