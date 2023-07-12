"""4. Crear una función y dentro la respectiva excepción para el siguiente bloque de código para que tu programa
no se bloquee y además imprime un mensaje al usuario la causa y/o solución:
string = "Hello Pythonista"
print(string/0)
"""

def division_cero():
    try:
        string = "Hello Pythonista"
        resultado = string / 0
        return resultado
    except TypeError:
        mensaje = "Se produjo un error: no se puede realizar la división entre un string y cero."
        print(mensaje)
    except ZeroDivisionError:
        mensaje = "Se produjo un error: división por cero."
        print(mensaje)

division_cero()
