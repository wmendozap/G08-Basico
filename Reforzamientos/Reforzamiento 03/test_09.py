"""9. Crear una clase Persona que contenga dos atributos: nombre y edad
- Nombre y edad se ingresarán por teclado en el constructor
- Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre
si debe pagar impuestos (10% de su sueldo-encapsulamiento) (sueldo superior a 4000)
- Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto debe pagar de impuesto"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.__sueldo = sueldo

    def obtener_sueldo(self):
        return self.__sueldo

    def calcular_impuesto(self):
        if self.__sueldo > 4000:
            impuesto = self.__sueldo * 0.1
            return impuesto
        else:
            return 0

nombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
sueldo = float(input("Ingrese el sueldo del empleado: "))

empleado = Empleado(nombre, edad, sueldo)

print("Sueldo del empleado:", empleado.obtener_sueldo())
print("Impuesto a pagar:", empleado.calcular_impuesto())