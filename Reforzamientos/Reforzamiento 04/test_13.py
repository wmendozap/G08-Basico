"""13. Haciendo el uso de *args y **kwargs aplicarlo debidamente para usar decorar una función que recibirá 4 argumentos
los cuales se multiplicaran entre ellos. Mensaje previo al usar el decorador “Está por ejecutarse la función” y mensaje
luego de usar el decorador “La función ha sido ejecutado correctamente”"""

def mensaje_decorator(func):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = func(*args, **kwargs)
        print("La función ha sido ejecutada correctamente")
        return resultado
    return wrapper

@mensaje_decorator
def multiplicar(a, b, c, d):
    return a * b * c * d

resultado = multiplicar(2, 3, 4, 5)
print("Resultado:", resultado)
