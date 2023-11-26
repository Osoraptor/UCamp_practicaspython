import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

pokemon = input('Pon un pokémon: ')

url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon

respuesta = requests.get(url)

if respuesta.status_code != 200:
    print('Pokémon no encontrado')
    exit()

datos = respuesta.json()

try :
    url_imagen = datos['sprites']['front_default']
    imagen = Image.open(urlopen(url_imagen))
except:
    print('El pokémon no tiene imagen.')
    exit()

plt.title(datos['name']) # para acceder a su nombre
imgplot = plt.imshow(imagen)
plt.show() 