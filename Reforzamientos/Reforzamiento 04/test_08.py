"""8. Creando un archivo principal (main.py) donde importará a un módulo (operaciones.py)
el cuál contendrá las siguientes funciones:
- Una función que realizará la carga de un valor entero.
- Una función que mostrará por pantalla la raíz cuadrada de dicho valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho número.
- Utilizar el módulo math de python."""

from operaciones import cargar_numero, mostrar_raiz_cuadrada, mostrar_cuadrado_cubo

valor = cargar_numero()

mostrar_raiz_cuadrada(valor)

mostrar_cuadrado_cubo(valor)
