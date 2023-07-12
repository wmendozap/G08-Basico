"""14. Crear un decorador donde imprimirá la cantidad de argumentos que tiene la función a decorar usando
*args y **kwargs. Mensaje previo “La cantidad de argumentos que tiene la función es”
mensaje post “La función decoradora terminó de ejecutarse correctamente”

Ejemplo: Al usar una función suma que creamos y usamos
suma(4, 1, 10, 2, 50, 64)
El decorador determinará la cantidad de argumentos que tiene la función al decorarla.
Salida:
“La cantidad de argumentos que tiene la función es”
5
“La función decoradora terminó de ejecutarse correctamente” """

def imprimir_cantidad_argumentos_decorator(func):
    def wrapper(*args, **kwargs):
        print("La cantidad de argumentos que tiene la función es:", len(args) + len(kwargs))
        resultado = func(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado
    return wrapper

@imprimir_cantidad_argumentos_decorator
def suma(*args):
    return sum(args)

resultado = suma(4, 1, 10, 2, 50, 64, -1)
print("Resultado:", resultado)
