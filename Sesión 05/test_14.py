var_1 = int(input("Ingrese primer valor numérico: "))
var_2 = int(input("Ingrese segundo valor numérico: "))
var_3 = int(input("Ingrese tercer valor numérico: "))

def media (x, y, z):
    promedio = (x + y + z) / 3
    return promedio
print(media(var_1, var_2, var_3))
