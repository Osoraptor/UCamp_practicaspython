import requests

latitud = 21.882758138096047
longitud = -102.32755526764123

api_key = '0b1bc3ac045fb78648b53b8b40427341'

url_destino = f'https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&lang=es&appid={api_key}'

respuesta = requests.get(url_destino)

if respuesta.status_code != 200:
    print('Ha ocurrido un error. Intenta nuevamente.')
    exit()

datos = respuesta.json()
ciudad = datos['name']

datos_clima = datos ['weather']
clima = datos_clima[0]['description']

print(f'El clima en {ciudad} es {clima}.')
