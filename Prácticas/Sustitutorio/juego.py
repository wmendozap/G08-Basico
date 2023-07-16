import random
import datetime


def obtener_numero_aleatorio():
    return random.randint(1, 40)


def validar_numero_ingresado(numero):
    try:
        numero = int(numero)
        if 0 < numero < 100:
            return numero
        else:
            print("El número ingresado debe ser mayor a 0 y menor a 100.")
    except ValueError:
        print("El valor ingresado no es un número entero válido.")


def adivina():
    numero_aleatorio = obtener_numero_aleatorio()
    print("Bienvenido a 'Acierta el número'!")

    while True:
        numero_ingresado = input("Ingresa un número: ")
        numero_validado = validar_numero_ingresado(numero_ingresado)

        if numero_validado is not None:
            if numero_validado == numero_aleatorio:
                fecha_actual = datetime.datetime.now()
                print("¡Has ganado!")
                print("Fecha y hora actual:", fecha_actual)
                break
            elif numero_validado < numero_aleatorio:
                print("El número es mayor. Intenta nuevamente.")
            else:
                print("El número es menor. Intenta nuevamente.")
