class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.__nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def imprimir_datos(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.edad)
        print("Ciudad:", self.ciudad)


class Empleado(Persona):
    def __init__(self, nombre, edad, ciudad):
        super().__init__(nombre, edad, ciudad)
        self.sueldo = self.pedir_sueldo()

    def pedir_sueldo(self):
        while True:
            try:
                sueldo = float(input("Ingrese el sueldo del empleado: "))
                return sueldo
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")

    def impuesto(self):
        if self.sueldo > 5500:
            return self.sueldo * 0.09
        else:
            return 0


def manejo_diccionario(empleados):
    diccionario = {}
    for empleado in empleados:
        diccionario[empleado._Persona__nombre] = {
            "edad": empleado.edad,
            "sueldo": empleado.sueldo,
            "impuesto": empleado.impuesto()
        }
    return diccionario


def generar_archivo_empleado(empleados):
    try:
        with open("empleados.txt", "a") as archivo:
            for empleado in empleados:
                archivo.write(f"{empleado._Persona__nombre},"
                              f"{empleado.sueldo},{empleado.impuesto()}\n")
        print("Archivo generado exitosamente.")
    except IOError:
        print("Error al generar el archivo.")


def mostrar_empleados_registrados():
    try:
        with open("empleados.txt", "r") as archivo:
            print("Empleados registrados:")
            for linea in archivo:
                nombre, sueldo, impuesto = linea.strip().split(",")
                print("Nombre:", nombre)
                print("Sueldo:", sueldo)
                print("Impuesto:", impuesto)
    except IOError:
        print("Error al abrir el archivo.")


empleados = []

while True:
    print("=== Registro de Empleados ===")
    nombre = input("Ingrese el nombre del empleado (o 'q' para salir): ")
    if nombre == 'q':
        break
    edad = int(input("Ingrese la edad del empleado: "))
    ciudad = input("Ingrese la ciudad del empleado: ")

    empleado = Empleado(nombre, edad, ciudad)
    empleados.append(empleado)
    print("Empleado registrado exitosamente.")

generar_archivo_empleado(empleados)
mostrar_empleados_registrados()

diccionario_empleados = manejo_diccionario(empleados)
print("Diccionario de empleados:")
print(diccionario_empleados)
