nombres_apellidos = input("Ingrese sus nombres y apellidos: ")
# print("{} {}".format(nombres_apellidos.split()[-2], nombres_apellidos.split()[-1]))
for items in nombres_apellidos.split()[2:4]:
    print(items)
