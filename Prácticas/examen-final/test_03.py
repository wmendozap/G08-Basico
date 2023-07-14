import time


def calcular_tiempo_y_sumar(funcion):
    def wrapper(**kwargs):
        start_time = time.time()
        resultado = funcion(**kwargs)
        end_time = time.time()
        tiempo_ejecucion = end_time - start_time
        suma = sum(kwargs.values())
        print("Resultado de la suma: ", suma)
        print("Tiempo de ejecución: {:.6f} segundos".format(tiempo_ejecucion))
        return resultado
    return wrapper


@calcular_tiempo_y_sumar
def multiplicacion(**numeros):
    resultado = 1
    for num in numeros.values():
        resultado *= num
    return resultado


resultado1 = multiplicacion(num1=5, num2=6)
print("Resultado 1:", resultado1)

resultado2 = multiplicacion(num1=2, num2=3, num3=4)
print("Resultado 2:", resultado2)

resultado3 = multiplicacion(num1=7, num2=8, num3=9, num4=10)
print("Resultado 3:", resultado3)
