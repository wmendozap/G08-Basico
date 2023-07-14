import funciones as func

func.crear_fichero()
tamano_lista = int(input("Ingrese el tamaño de la lista: "))
lista = func.llenar_lista(tamano_lista)

func.escribir_lista_en_fichero(lista)

raices = func.calcular_raiz_cuadrada(lista)
func.escribir_raices_en_fichero(raices)
