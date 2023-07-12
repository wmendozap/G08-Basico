"""15. Queremos consumir un JSON que se encuentra alojado en la nube el cual nos traerá los datos de una persona
como la id, nombre, nombre usuario, correo, nombre de compañía y dirección web de la compañía en donde trabaja.
La url a consumir usando Python es la siguiente:

https://jsonplaceholder.typicode.com/users

Obtener respectivamente los valores necesarios para formar la siguiente oración:
Bienvenido “id”, “nombre”, con nombre usuario “nombre usuario”. El correo que nos proporcionó es “correo” y la compañía
actual donde trabaja se llama “nombreCompañía”. Dentro de sus datos también encontramos un website que es: “nombreWeb”

Finalmente, agregar un usuario al json obtenido, pero solo con los datos de id, nombre, nombreUsuario, correo,
nombreCompañía y nombreWeb. Finalmente, mostrarlo en consola (solo ese usuario nuevo)"""

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

id = data[0]["id"]
nombre = data[0]["name"].split()[0]
nombreUsuario = data[0]["username"]
correo = data[0]["email"]
nombreCompañía = data[0]["company"]["name"]
nombreWeb = data[0]["website"]

oracion = f"Bienvenido/a {id}, {nombre}, con nombre de usuario {nombreUsuario}.\n" \
          f"El correo que nos proporcionó es {correo} y la compañía actual donde trabaja se llama {nombreCompañía}.\n" \
          f"Dentro de sus datos también encontramos un website que es: {nombreWeb}\n"

print(oracion)

nuevo_usuario = {
    "id": 11,
    "name": "Liam",
    "nombreUsuario": "Liam98",
    "email": "liam@msn.com",
    "company": {
        "name": "MSN Perú"
    },
    "website": "beerus.info"
}
data.append(nuevo_usuario)

print(data[-1])
