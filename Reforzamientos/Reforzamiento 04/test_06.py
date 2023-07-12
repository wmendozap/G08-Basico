"""6. Creando un archivo principal donde llamará a un módulo (operaciones.py) el cuál contendrá las siguientes funciones.
- La primera función cargará un número entero que pedirá al usuario que ingrese por consola un valor.
- La segunda función solamente sumará dos valores.
- Desde el archivo principal importar al módulo y sumar dos valores usando las funciones anteriormente creadas en el módulo"""

from operaciones import cargar_numero, sumar_valores

numero = cargar_numero()
resultado = sumar_valores(numero, 5)

print("El resultado de la suma es: ", resultado)
