import datetime

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        while True:
            try:
                self.edad = int(input("Ingrese su edad: "))
                break
            except ValueError:
                print("Error: La edad debe ser un número entero.")

    def cumpleaños(self):
        self.edad += 1

    def obtener_fecha_registro(self):
        now = datetime.datetime.now()
        fecha_registro = now.strftime("%d/%m/%Y %H:%M")
        return fecha_registro

class Cliente(Persona):
    def __init__(self, nombre, edad, nacionalidad, saldo):
        super().__init__(nombre, edad, nacionalidad)
        self.__saldo = saldo

    def mostrar_saldo(self):
        print("Saldo actual:", self.__saldo)

    def transferencia(self, persona2, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
            persona2.__saldo += monto
            print("Transferencia realizada.")
        else:
            print("Saldo insuficiente. No se puede realizar la transferencia.")

cliente1 = Cliente("William Antonio", 30, "Peruana", 2510)
cliente2 = Cliente("Tammy Lucia", 25, "Peruana", 0)

monto_transferencia = 100
cliente1.transferencia(cliente2, monto_transferencia)

cliente1.mostrar_saldo()
cliente2.mostrar_saldo()
