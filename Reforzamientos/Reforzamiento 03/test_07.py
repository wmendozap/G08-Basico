"""7. Crear una clase Persona con los siguientes requerimientos. La clase tendrá como atributos el nombre, edad
y sueldo de una persona. Implementar los métodos necesarios para inicializar los atributos (constructor),
un método para mostrar los datos e indicar si la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo. Instanciar por lo menos la clase con 2 diferentes personas."""


class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Sueldo: ", self.sueldo)

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def bonificacion(self):
        bono = self.sueldo * 0.2
        return self.sueldo + bono


persona1 = Persona("Liam", 25, 2000)
print("Datos de la persona 1")
persona1.mostrar_datos()
print("La persona 1 es mayor de edad: ", persona1.es_mayor_de_edad())
print("Sueldo con bonificación de la persona 1: ", persona1.bonificacion())


persona2 = Persona("Tammy", 17, 1500)
print("\nDatos de la persona 2")
persona2.mostrar_datos()
print("La persona 2 es mayor de edad: ", persona2.es_mayor_de_edad())
print("Sueldo con bonificación de la persona 2: ", persona2.bonificacion())