from datetime import datetime


class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.nacionalidad = "Peruana"

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        while True:
            try:
                self.edad = int(input("Ingrese su edad: "))
                break
            except ValueError:
                print("Error: La edad debe ser un número entero."
                      "Inténtelo nuevamente.")

    def cumpleaños(self):
        self.edad += 1

    def obtener_fecha_registro(self):
        now = datetime.now()
        fecha_registro = now.strftime("%d/%m/%Y %H:%M")
        return fecha_registro


persona = Persona()

persona.solicitar_datos()
persona.cumpleaños()
persona.cumpleaños()

print("Edad actualizada:", persona.edad)

fecha_registro = persona.obtener_fecha_registro()
print("Fecha de registro:", fecha_registro)
