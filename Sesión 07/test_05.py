"""Manejo de errores"""
"""
- Crear una función aplicando excepciones donde no se pueda realizar una suma de diferentes tipos de datos
"""


def operacion(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Error: No se puede sumar diferentes tipos de datos")
        return None


resultado1 = operacion(4, "Hola Python")
print(resultado1)

resultado2 = operacion(50, 100)
print(resultado2)
