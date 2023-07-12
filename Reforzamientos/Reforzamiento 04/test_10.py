"""10. Crear una función donde se permitirá guardar el nombre, apellido y edad de un usuario en un fichero (agenda.txt),
cada usuario tiene que estar guardado en una línea diferente y cada dato de una persona
tiene que estar separados por comas."""

def agregar_usuario_agenda():
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    edad = input("Ingrese la edad del usuario: ")

    with open("agenda.txt", "a") as archivo:
        usuario = f"{nombre},{apellido},{edad}\n"
        archivo.write(usuario)

    print("El usuario ha sido agregado a la agenda correctamente.")

agregar_usuario_agenda()
