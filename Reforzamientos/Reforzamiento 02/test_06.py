"""6. Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista) dentro de la lista"""
lista_1 = [
    "GESTIÓN DEL CONOCIMIENTO",
    "GESTIÓN DE LA INFORMACIÓN DIGITAL",
    "GESTIÓN DE PROYECTOS DE TI",
    "TRANSFORMACIÓN DIGITAL",
    "DIRECCIÓN DE TESIS I",
    "SEMINARIO DE INVESTIGACIÓN I"
]
lista_1.append("GESTIÓN DEL CONOCIMIENTO")
lista_1.append("TRANSFORMACIÓN DIGITAL")
lista_1.append("GESTIÓN DEL CONOCIMIENTO")
print("Cantidad de veces que se repite el curso de GESTIÓN DEL CONOCIMIENTO: {}".format(lista_1.count("GESTIÓN DEL CONOCIMIENTO")))