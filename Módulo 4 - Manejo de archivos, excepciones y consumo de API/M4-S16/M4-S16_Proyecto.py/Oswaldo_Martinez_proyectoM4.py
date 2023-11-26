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
#nombre = nombre.upper()
#pokemon_dict['Nombre'].append(nombre)

peso = datos['weight']
tamagno = datos['height']


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


print(nombre)
print(peso)
print(tamagno)


print(pokemon_dict)

#print(movimientos)
# print(habilidades)
# print(tipos)



########## JSON file ############




# with open('agenda.txt', 'w') as f_agenda:
#     for persona in personas:
#         f_agenda.write(f' {persona[0]}. Nombre: {persona[1]} {persona[2]}. Edad: {persona[3]}. Correo: {persona[4]}. Telefono: {persona[5]}.\n')
#     print('Datos guardados en agenda.txt.')
#     #break




############ IMAGEN ###########


# try :
#     url_imagen = datos['sprites']['front_default']
#     imagen = Image.open(urlopen(url_imagen))
# except:
#     print('El pokémon no tiene imagen.')
#     exit()

# plt.title(datos['name']) # para acceder a su nombre
# imgplot = plt.imshow(imagen)
# plt.show() 