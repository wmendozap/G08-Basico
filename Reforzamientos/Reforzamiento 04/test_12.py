"""12. Crear una función decoradora que dará los buenos días antes de ejecutar una función a ser decorada
y luego de ser ejecutada lanzará un mensaje diciendo “Hasta luego”. La función a decorar pedirá el nombre
de una persona y retornará el mensaje “Soy ‘nombre’”"""

def saludo_decorator(func):
    def wrapper():
        print("Buenos días!")
        func()
        print("Hasta luego!")
    return wrapper

@saludo_decorator
def saludar():
    nombre = input("Ingrese su nombre: ")
    print(f"Soy '{nombre}'.")

saludar()
