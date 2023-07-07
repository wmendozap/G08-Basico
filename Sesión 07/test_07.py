from datetime import datetime
strFecha = "4/7/2023"
conversion = datetime.strptime(strFecha, "%d/%m/%Y")
print(conversion)
print(type(conversion))

conversionMes = datetime.strftime(conversion, "%d %b del %Y")
print(conversionMes)