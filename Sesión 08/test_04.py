titulo_1 = "Tecnologias Backend\n"
tecnologiasBackend = [
    "Python\n",
    "Java\n",
    "Ruby\n",
    "NodeJS"
]

lista = list(titulo_1) + tecnologiasBackend

file = open("test_04.txt", "a+")
file.writelines(lista)

file = open("test_04.txt", "r")
print(file.read())

file.close()
