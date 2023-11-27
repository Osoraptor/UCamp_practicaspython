# Notas Generales

Este folder/repo contiene archivos y programas creados dentro del bootcamp Fundamentos de Python.

Módulos:

•	Módulo 4: Manejo de archivos, excepciones y consumo de API.


# Módulo 4: Manejo de archivos, excepciones y consumo de API.

Archivos del proyecto:

  - Oswaldo_Martinez_proyectoM4.py .  

Para la elaboración del proyecto **Construye una Pokédex**, se trabajó en 3 funciones principales:

  - def info_pokemon .
  - def pokemon_json_file .
  - def imagen_pokemon .

En la primera función, **def info_pokemon(data)**, se obtiene los datos del pokémon que el usuario desea buscar. Recibe como parametro la respuesta.json() del API 'https://pokeapi.co/api/v2/pokemon/' + 'pokemon_a_buscar'.

Se obtienen los siguientes datos del pokémon:

    ● Nombre.
    ● Peso.
    ● Tamaño.
    ● Movimientos.
    ● Habilidades.
    ● Tipos.
    ● Imagen.

Al final se manda a llamar la función def pokemon_json_file para generar el archivo JSON pasandole como parametro el diccionario generado en esta función.

En la segunda función, **def pokemon_json_file(pokedict)**, esta función crea un archivo JSON con base a un diccionario heredado. Recibe como parametro el diccionario generado en la función def info_pokemon. En este paso o proceso, se hizo uso de **json.dump** por parte del modulo “*JSON*” para poder crear un archivo JSON con base a un diccionario en python.

En la tercera función, **def imagen_pokemon(data_img)**, esta función genera una imagen con base a los datos pasados como parametro. Recibe como parametro los datos de respuesta.json(). Posteriormente se adentra a “*'sprites'*” luego “*'front_default'*” para obtener la imagen. En esta función en particular se hace uso del modulo **“*matplotlib.pyplot*”** para poder generar la imagen.

