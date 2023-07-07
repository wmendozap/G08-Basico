from json import loads
jsonData = '{"Nombre": "Python", "Tipo": "Backend", "Paradigma": "POO"}'
jsonToPython = loads(jsonData)
print(jsonToPython)
print(type(jsonToPython))