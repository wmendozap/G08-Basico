def funcionDecoradora(funcionParametro):
    def funcionInterna(*args):
        print("Antes de la ejecución\n")
        resultado = funcionParametro(*args)
        print("Después de la ejecución\n")
        return resultado
    return funcionInterna

@funcionDecoradora
def suma(a, b, c, d, e):
    return a + b + c + d + e

print(suma(10, 25, 40, 5, 2))

@funcionDecoradora
def saludar(name, lastname, age):
    print("Bienvenido/a: {}, {}, {}".format(name, lastname, age))

nombres = input("Ingrese nombres: ")
apellidos = input("Ingrese apellidos: ")
edad = input("Ingrese edad: ")

saludar(nombres, apellidos, edad)
