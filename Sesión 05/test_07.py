"""Usando las propiedades de cadenas
Requisitos:
- Ingresar tu nombre y apellido por consola (cada valor en una variable diferente)
- Concatenar ambos valores en una sola variable y luego imprimirlas
- Obtener el tamaño de tu nombre completo
- Imprimir el resultado final y que todo esté en mayusculas
- Indicar mediante condicional el tamaño del nombre, es mayor o no al apellido"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nombre_apellido = nombre + " " + apellido
print("Nombre y apellido: {}".format(nombre_apellido))
print("Longitud del nombre: {}".format(len(nombre)))
print("A mayusculas: {}".format(nombre_apellido.upper()))
if len(nombre) > len(apellido):
    print("El tamaño del nombre es mayor")
else:
    print("El tamaño del nombre es menor")
