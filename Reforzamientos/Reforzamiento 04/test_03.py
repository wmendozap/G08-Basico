"""3. Crear una función y dentro la respectiva excepción para el siguiente bloque de código para que tu programa
no se bloquee y además imprime un mensaje al usuario la causa y/o solución:
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']"""

def obtener_valor(diccionario, clave):
    try:
        valor = diccionario[clave]
        return valor
    except KeyError:
        mensaje = "Se produjo un error: la clave '{}' no existe en el diccionario.".format(clave)
        print(mensaje)

persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
valor = obtener_valor(persona, 'profesion')

if valor is not None:
    print(valor)
