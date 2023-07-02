cadena_1 = "Conexión a base de datos con Python"
cadena_2 = cadena_1.replace(cadena_1[0:6], "ppp")
print(cadena_2)
cadena_3 = "Conexión a base de datos con Python         "
cadena_4 = cadena_3.rstrip()

print(cadena_4)
cadena_5 = "         Conexión a base de datos con Python"
cadena_6 = cadena_5.lstrip()
print(cadena_6)