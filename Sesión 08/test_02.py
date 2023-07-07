file = open("sample.txt", "w")
file.write("@ Caracteristicas de Python\n")
file.write("@ Lenguaje multiplataforma\n")
file.write("@ Basodo en POO\n")
file.write("@ Lenguaje intuitivo")

file = open("sample.txt", "r")

print(file.read())
file.close()
