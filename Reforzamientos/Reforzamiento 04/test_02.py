"""2. Crear una función y dentro la respectiva excepción para el siguiente bloque de código para que tu programa
no se bloquee y además imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]"""

def obtener_elemento(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        mensaje = "Se produjo un error: el índice está fuera del rango válido."
        print(mensaje)

lista = [2, 6, 10, 4, 5, 23, 1]
elemento = obtener_elemento(lista, 10)

if elemento is not None:
    print(elemento)
