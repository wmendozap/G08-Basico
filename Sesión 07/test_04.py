def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error, división entre cero")
    else:
        print(result)

division(40, 0)
division(1000, 70)
