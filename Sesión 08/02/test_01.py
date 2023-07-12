def funcionA(funcionB):
    def funcionC():
        print("1. Antes de ejecutar la función a decorar\n")
        funcionB()
        print("2. Después de ejecutar la función a decorar\n")

    return funcionC()

@funcionA
def saludar():
    return print("Hola Python\n")
