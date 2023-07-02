"""3. Crear una clase que contenga dos métodos, uno que pida ingresar un nombre y apellido,
un método para pedir su edad y otro método que lo imprima ambos resultados, pero estarán contenidos en un diccionario
Comprobar ambos métodos instanciado la clase respectivamente
Considerar en el constructor los valores necesarios"""

class Persona:
    def __int__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = ""
    def ingresar_nombre_apellido(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
    def ingresar_edad(self):
        self.edad = input("Ingrese su edad: ")
    def imprimir_datos(self):
        persona = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Edad": self.edad
        }
        print("Datos de la persona:")
        for clave, valor in persona.items():
            print(clave + ": " + valor)
persona = Persona()
persona.ingresar_nombre_apellido()
persona.ingresar_edad()
persona.imprimir_datos()