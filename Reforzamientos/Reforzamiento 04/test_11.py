"""11. Crear una función que creará el archivo calificaciones.txt que contiene las calificaciones de un curso.
Escribir un programa que contenga las siguientes funciones:
- Una función que guarde el nombre, 2 notas y el promedio (el promedio lo calculará la función antes de escribirlo
en el fichero)
- Y una función que leerá el fichero anterior y dirá si el alumno X, aprobó o no, tener en cuenta que si tiene un
promedio mayor a diez tendrá un mensaje de “Alumno X, aprobado” de lo contrario “Alumno X, desaprobado”"""

def guardar_calificaciones():
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    promedio = (nota1 + nota2) / 2

    with open("calificaciones.txt", "a") as archivo:
        linea = f"{nombre},{nota1},{nota2},{promedio}\n"
        archivo.write(linea)

    print("Las calificaciones han sido guardadas correctamente.")


def verificar_aprobacion(alumno):
    nombre_buscar = alumno.lower()
    aprobado = False

    with open("calificaciones.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            nombre = datos[0].lower()
            promedio = float(datos[3])

            if nombre == nombre_buscar:
                aprobado = promedio >= 10.0
                break

    if aprobado:
        print(f"Alumno {alumno}, aprobado.")
    else:
        print(f"Alumno {alumno}, desaprobado.")


guardar_calificaciones()
verificar_aprobacion("Gladis")
