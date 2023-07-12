def paciente(**kwargs):
    nombre = kwargs.get('nombre')
    ciudad = kwargs.get('ciudad')
    fecha_alta = kwargs.get('fecha_alta')

    return f"Paciente {nombre}, es de la ciudad {ciudad} y le dieron de alta el {fecha_alta}"

print(paciente(nombre="William", ciudad="Lima", fecha_alta="15/07/2023"))
