tecnologiasBackend = [
    "Python\n",
    "Java\n",
    "Ruby\n",
    "NodeJS"
]

file = open("test_05.txt", "a+")
file.writelines(tecnologiasBackend)

file = open("test_05.txt", "r")
for item in file:
    # print(item)
    if item.find("Python"):
        print("Python encontrado")
    else:
        print("Python no encontrado")

file.close()
