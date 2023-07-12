"""9. Crear una función que pida al usuario un número entero entre 1 y 20 y guarde en un fichero (que no existe)
con el nombre tabla.txt la tabla de multiplicar de ese número, done n es el número introducido."""

def guardar_tabla_multiplicar():
    numero = int(input("Ingrese un número entero entre 1 y 20: "))

    if numero < 1 or numero > 20:
        print("El número debe estar entre 1 y 20.")
        return

    with open("tabla.txt", "w") as archivo:
        archivo.write(f"Tabla de multiplicar del {numero}:\n\n")
        for i in range(1, 11):
            resultado = numero * i
            archivo.write(f"{numero} x {i} = {resultado}\n")

    print("La tabla de multiplicar ha sido guardada en el archivo tabla.txt.")

# Ejemplo de uso
guardar_tabla_multiplicar()
