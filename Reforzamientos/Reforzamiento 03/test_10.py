"""10. Crear un módulo y un archivo principal (donde llamará las funciones del módulo) el módulo tendrá una función
para ingresar nombres y apellidos, una función para pedir el tipo de seguro que tiene y otra función para indicar
si es mayor de edad o no (pedir la edad desde consola)"""

# archivo_principal.py
import modulo

nombre, apellido = modulo.ingresar_nombre_apellido()
tipo_seguro = modulo.pedir_tipo_seguro()
es_mayor = modulo.es_mayor_de_edad()
print("Nombre completo: ", nombre, apellido)
print("Tipo de seguro: ", tipo_seguro)
if es_mayor:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")