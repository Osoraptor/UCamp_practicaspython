# Status:
    #PESO
    #Tamaño
    #Movimientos
    #Habilidades
    #Tipos

import requests
import matplotlib.pyplot as plt
import json
from PIL import Image
from urllib.request import urlopen



while True:
    pokemon = input('¿Que pokémon deseas conocer? ')
    if pokemon == '':
        print('No has introducido un nombre.')
    else:
        break


url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon

respuesta = requests.get(url)


if respuesta.status_code != 200:
    print('Pokémon no encontrado')
    exit()


pokemon_dict = {
    'Nombre': '',
    'Peso': '',
    'Tamaño': '',
    'Movimientos': [],
    'Habilidades': [],
    'Tipos': []

}


datos = respuesta.json()


nombre = datos['name']
nombre = nombre.upper()
pokemon_dict['Nombre'] = nombre



peso = datos['weight']
peso = str(peso)
peso_format = peso[:(len(peso)-1)] + "." + peso[(len(peso)-1):] + ' kg'
pokemon_dict['Peso'] = peso_format


tamagno = datos['height']
tamagno = str(tamagno)
tamagno_format = tamagno[:(len(tamagno)-1)] + "." + tamagno[(len(tamagno)-1):] + ' metros'
pokemon_dict['Tamaño'] = tamagno_format




movimientos = datos['moves']

for move in range(int(len(movimientos))): # se hace in for por el rango de la cantidad de movimientos.
    movimiento = movimientos[move] ['move'] ['name']
    pokemon_dict['Movimientos'].append(movimiento)


habilidades = datos['abilities']

for ability in range(int(len(habilidades))): # se hace in for por el rango de la cantidad de habilidades.
    habilidad = habilidades[ability] ['ability'] ['name']
    pokemon_dict['Habilidades'].append(habilidad)


tipos = datos['types']

for type in range(int(len(tipos))): # se hace in for por el rango de la cantidad de tipos.
    tipo = tipos[type] ['type'] ['name']
    pokemon_dict['Tipos'].append(tipo)



### Validaciones print ###

# print(nombre)
# print(peso)
# print(tamagno)

################################


print(pokemon_dict)





########## JSON file ############




with open('pokemon.json', 'w') as f_pokemon:
    json.dump(pokemon_dict, f_pokemon)


with open('pokemon.json', 'r') as f_pokemon:
    data = json.load(f_pokemon)

# Validación de lectura de la data del JSON file.

print(f'''\n***
\n {data} \n*** 
''')

#print(data)



############ IMAGEN ###########


try :
    url_imagen = datos['sprites']['front_default']
    imagen = Image.open(urlopen(url_imagen))
except:
    print('El pokémon no tiene imagen.')
    exit()

plt.title(datos['name']) # para acceder a su nombre
imgplot = plt.imshow(imagen)
plt.show() 