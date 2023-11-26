# import requests

# NOMBRE_VARIABLE = requests.VERBO_HTTP('URL_DESTION', DATOS)

#######################

import requests

url = 'https://pokeapi.co/api/v2/pokemon/ho-oh'

try:
    respuesta = requests.get(url, timeout=10)
except requests.Timeout:
    print('El tiempo de espera ha terminado.')


respuesta = requests.get(url)

if respuesta.status_code != 200:
    print('Pokémon no encontrado')
else:
    print(respuesta)

datos = respuesta.json()
nombre = datos['name'] #llave nombre
#nombre = datos['species']['name'] # Aquí se agregan [] para ingresar a las capas del API, en este caso  llave nombre de la especie


print('Movimientos de ' + nombre + ': ')

movimientos = datos['moves']
for move in range(int(len(movimientos))): # se hace in for por el rango de la cantidad de los movimientos.
    movimiento = movimientos[move] ['move'] ['name']
    print(movimiento)