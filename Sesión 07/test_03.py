valor = True
while valor:
    try:
        x = int(input("Ingrese valor numérico: "))
        break
    except:
        print("Error")
