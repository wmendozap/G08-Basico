"""6. Crear una clase llamada Alumno que tenga como atributos el nombre, edad y la nota final del alumno.
Crear los métodos para inicializar sus atributos, otro para imprimirlos y un método para mostrar un mensaje con
el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el alumno.
Instanciar la clase por lo menos 3 veces (3 alumnos)"""


class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir_informacion(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota final: ", self.nota_final)

    def mostrar_resultado(self):
        if self.nota_final >= 11:
            print("Alumno {} ha aprobado".format(self.nombre))
        else:
            print("Alumno {} no ha aprobado".format(self.nombre))

alumno1 = Alumno("Antonio", 18, 14)
print("Información del alumno 1")
alumno1.imprimir_informacion()
alumno1.mostrar_resultado()

alumno2 = Alumno("María", 17, 9)
print("\nInformación del alumno 2")
alumno2.imprimir_informacion()
alumno2.mostrar_resultado()

alumno3 = Alumno("William", 19, 12)
print("\nInformación del alumno 3")
alumno3.imprimir_informacion()
alumno3.mostrar_resultado()