tecnologiasBackend = [
    "Python",
    "Java",
    "Ruby",
    "NodeJS"
]

tecnologiasFrontend = [
    "Angular",
    "JavaScript",
    "React JS",
    "Bootstrap"
]

file = open("text.txt", "a+")
file.writelines(tecnologiasBackend)
file.writelines(tecnologiasFrontend)

file = open("text.txt", "r")
print(file.read())

file.close()