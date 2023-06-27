"""4. Elimina el key edad tipo de tu diccionario, incluyendo su valor"""
empleado = {
    "nombre": "William",
    "edad": 37,
    "salario": 3562.25
}
del empleado["edad"]
print(empleado)