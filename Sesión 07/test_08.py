from datetime import datetime
fecha_1 = datetime(2023, 7, 13)
fecha_2 = datetime(2023, 7, 30)

if fecha_1 == fecha_2:
    print("Valores iguales")
elif fecha_1 > fecha_2:
    print("Fecha 1 mayor que fecha 2")
else:
    print("Fecha 2 mayor que fecha 1")
