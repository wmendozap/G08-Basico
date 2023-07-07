from json import dumps
jsonData = '{"Nombre": "Python", "Tipo": "Backend", "Paradigma": "POO"}'
jsonToPython = dumps(jsonData)
print(jsonToPython)
print(type(jsonToPython))
