# https://pokeapi.co/api/v2/pokemon/charizard
import requests

res = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
print(res.status_code)
# print(res.headers)

json = res.json()
print(json)
