"""8. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario
- Mostrar en consola los valores de su variable final (ya sea diccionario o lista)"""
empleado = {
    "nombre": "William",
    "edad": 37,
    "salario": 3562.25,
    "dni": "43197591",
    "carrera": "Ingeniería en Sistemas"
}

lista_valores = list(empleado.values())

for i in range(len(lista_valores)):
    print(lista_valores[i])