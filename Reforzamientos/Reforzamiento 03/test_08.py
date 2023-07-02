"""8. Realizar una clase que administre una agenda. Se debe almacenar en un diccionario dentro de una lista para cada
contacto el nombre, el teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)"""


class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email, dni):
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'dni': dni
        }
        self.contactos.append(contacto)
        print("Contacto añadido correctamente...")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("No hay contactos en la agenda")
        else:
            print("Lista de contactos")
            for contacto in self.contactos:
                print("Nombre: ", contacto['nombre'])
                print("Teléfono: ", contacto['telefono'])
                print("Email: ", contacto['email'])
                print("DNI: ", contacto['dni'])
                print("->")

    def buscar_contacto_por_dni(self, dni):
        for contacto in self.contactos:
            if contacto['dni'] == dni:
                print("Contacto encontrado!!!")
                print("Nombre: ", contacto['nombre'])
                print("Teléfono: ", contacto['telefono'])
                print("Email: ", contacto['email'])
                print("DNI: ", contacto['dni'])
                return
        print("No se encontró ningún contacto con DNI: {}".format(dni))

agenda = Agenda()

agenda.añadir_contacto("William Antonio", "985325419", "liam@gmail.com", "43985682")
agenda.añadir_contacto("Gladis Elida", "923658961", "glad@hotmail.com", "4456585")
agenda.añadir_contacto("Tammy Lucia", "902543659", "lucia15@outlook.com", "78562541")

agenda.mostrar_contactos()
agenda.buscar_contacto_por_dni("43985682")