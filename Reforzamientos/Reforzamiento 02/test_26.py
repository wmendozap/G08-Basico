"""Crear un diccionario con 6 departamentos en el país
- Borrar cualquier departamento (uno) usando la palabra reservada del
- Comprobar que no existe este departamento borrado dentro del diccionario"""
departamentos = {
    "Amazonas": "Chachapoyas",
    "Áncash": "Huaraz",
    "Apurímac": "Abancay",
    "Arequipa": "Arequipa",
    "Ayacucho": "Ayacucho",
    "Cajamarca": "Cajamarca"
}

departamento_borrado = "Arequipa"
if departamento_borrado in departamentos:
    del departamentos[departamento_borrado]
    print(f"Se ha eliminado el departamento {departamento_borrado}.")
else:
    print(f"El departamento {departamento_borrado} no existe en el diccionario.")

if departamento_borrado not in departamentos:
    print(f"El departamento {departamento_borrado} no se encuentra en el diccionario.")
