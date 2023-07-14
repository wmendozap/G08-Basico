import manejo_listas as ml

lista_aleatoria = ml.generar_lista_aleatoria()

numeros_no_repetidos = ml.obtener_numeros_no_repetidos(lista_aleatoria)

lista_ascendente, lista_descendente = ml.ordenar_listas(numeros_no_repetidos)

mayor_numero = ml.obtener_mayor_numero(numeros_no_repetidos)
