"""4. Crea una función que al ingresar dos números por parámetro mostrará todos los cuadrados de los números
que hay entre ellos (Usar la función una vez y mostrar el resultado por consola).
Los números serán ingresados y solicitados por consola"""

def mostrar_cuadro(numero1, numero2):
    for num in range(numero1 + 1, numero2):
        cuadrado = num ** 2
        print(cuadrado)

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

mostrar_cuadro(numero1, numero2)