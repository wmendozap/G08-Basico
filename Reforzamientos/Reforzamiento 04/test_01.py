"""1. Crear una función para encontrar el error en el siguiente bloque de código. Crea una excepción para evitar
que tu programa se bloquee y además imprime un mensaje al usuario la causa y/o solución:
suma = 80 + “Hola Pythonista”"""

def suma_excepcion():
    try:
        suma = 80 + "Hola Pythonista"
        return suma
    except TypeError as e:
        mensaje = "Se produjo un error de tipo: {}. ".format(type(e).__name__)
        mensaje += "\nAsegúrate de sumar dos valores del mismo tipo."
        print(mensaje)

suma_excepcion()
