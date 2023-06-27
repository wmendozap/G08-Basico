"""5. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene"""
empleado = {
    "nombre": "William",
    "edad": 37,
    "salario": 3562.25
}
lista_claves = list(empleado.keys())
print("lista_claves: {}".format(lista_claves))

lista_valores = list(empleado.values())
print("lista_valores: {}".format(lista_valores))

lista_pares = list(empleado.items())
print("lista_pares: {}".format(lista_pares))

for i in range(len(lista_valores)):
    print(type(lista_valores[i]))