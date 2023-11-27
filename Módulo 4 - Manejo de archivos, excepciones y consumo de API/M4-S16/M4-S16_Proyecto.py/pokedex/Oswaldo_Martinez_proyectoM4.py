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




def info_pokemon(data):

    '''
    Esta función genera la información del pokemón que el usuario desea buscar.
    Recibe como parametro la respuesta.json() del API 'https://pokeapi.co/api/v2/pokemon/' + 'pokemon_a_buscar'.
    Se obtienen los siguientes datos del pokémon:
        ● Nombre.
        ● Peso.
        ● Tamaño.
        ● Movimientos.
        ● Habilidades.
        ● Tipos.
        ● Imagen.
    Al final se manda a llamar la función def pokemon_json_file para generar el archivo JSON pasandole como parametro el diccionario generado en esta función.
    '''

    pokemon_dict = {
    'Nombre': '',
    'Peso': '',
    'Tamaño': '',
    'Movimientos': [],
    'Habilidades': [],
    'Tipos': [],
    'Imagen': ''

    }

    ### NOMBRE ###
    nombre = data['name']
    nombre = nombre.upper()
    pokemon_dict['Nombre'] = nombre


    ### PESO ###
    peso = data['weight']
    peso = str(peso)
    peso_format = peso[:(len(peso)-1)] + "." + peso[(len(peso)-1):] + ' kg'
    pokemon_dict['Peso'] = peso_format

    ### TAMAÑO###
    tamagno = data['height']
    tamagno = str(tamagno)
    tamagno_format = tamagno[:(len(tamagno)-1)] + "." + tamagno[(len(tamagno)-1):] + ' metros'
    pokemon_dict['Tamaño'] = tamagno_format



    ### MOVIMIENTOS ###
    movimientos = data['moves']

    for move in range(int(len(movimientos))): # se hace in for por el rango de la cantidad de movimientos.
        movimiento = movimientos[move] ['move'] ['name']
        pokemon_dict['Movimientos'].append(movimiento)


    ### HABILIDADES ###
    habilidades = data['abilities']

    for ability in range(int(len(habilidades))): # se hace in for por el rango de la cantidad de habilidades.
        habilidad = habilidades[ability] ['ability'] ['name']
        pokemon_dict['Habilidades'].append(habilidad)


    ### TIPOS ###
    tipos = data['types']

    for type in range(int(len(tipos))): # se hace in for por el rango de la cantidad de tipos.
        tipo = tipos[type] ['type'] ['name']
        pokemon_dict['Tipos'].append(tipo)


    ### IMAGEN ###
    imagen = data['sprites']['front_default']
    imagen_format = f'URL: ' + imagen
    pokemon_dict['Imagen'] = imagen_format

    print(pokemon_dict)

    pokemon_json_file(pokemon_dict)


    ### Validaciones print ###

    # print(nombre)
    # print(peso)
    # print(tamagno)

################################



########## JSON file ############

def pokemon_json_file(pokedict):

    '''
    Esta función crea un archivo JSON con base a un diccionario heredado.
    Recibe como parametro el diccionario generado en la función def info_pokemon.
    '''

    with open('pokemon.json', 'w') as f_pokemon:
        json.dump(pokedict, f_pokemon)


    with open('pokemon.json', 'r') as f_pokemon:
        data = json.load(f_pokemon)

    # Validación de lectura de la data del JSON file.

    print(f'''\n***
    \n {data} \n*** 
    ''')

    

    #print(data)



############ IMAGEN ###########

def imagen_pokemon(data_img):

    '''
    Esta función genera una imagen con base a los datos pasados como parametro.
    Recibe como parametro los datos de respuesta.json().
    Posteriormente se adentra a 'sprites' luego 'front_default' para obtener la imagen.
    '''

    try :
        url_imagen = data_img['sprites']['front_default']
        imagen = Image.open(urlopen(url_imagen))
    except:
        print('El pokémon no tiene imagen.')
        exit()

    plt.title(data_img['name']) # para acceder al nombre del pokemon
    imgplot = plt.imshow(imagen)
    plt.show() 


#################################


print('Hola futuro maestro pokémon!')

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


datos = respuesta.json()

info_pokemon(datos)

imagen_pokemon(datos)