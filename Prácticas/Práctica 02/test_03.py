def ingresar_datos():
    while True:
        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Ingrese solo números enteros.")


def division(num1, num2):
    try:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")


def evaluar_suma(num1, num2):
    try:
        resultado = num1 + num2
        print("El resultado de la suma es:", resultado)
    except TypeError:
        print("Error: Los datos ingresados no son válidos para realizar la suma.")


num1, num2 = ingresar_datos()
division(num1, num2)

while True:
    try:
        evaluar_suma(num1, num2)
        break
    except TypeError:
        print("Error: Los datos ingresados no son válidos para realizar la suma.")
        num1, num2 = ingresar_datos()
