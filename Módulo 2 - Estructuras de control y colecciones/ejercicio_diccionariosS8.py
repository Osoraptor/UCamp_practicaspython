
colores_diccionario_IN = {'rojo': 'red',  'naranja':'orange', 'amarillo':'yellow', 'verde':'green', 'azul':'blue', 'violeta':'violet'}
colores_diccionario_JP = {'rojo': 'aka',  'naranja':'orenji', 'amarillo':'kiiro', 'verde':'midori', 'azul':'ao', 'violeta':'baioretto'}

frase = input('Escribe una frase: ')
frase = frase.lower()
palabras = frase.split()

respuesta= ''

opcion = input('Traducir en inglés (1) o japonés (2): ')


    
if opcion == '1':
    for palabra in palabras:
        if palabra in colores_diccionario_IN:
            respuesta = respuesta + colores_diccionario_IN[palabra] + ' '
            
        else:
            respuesta = respuesta + palabra + ' '
            
    print(respuesta)
    
elif opcion == '2':
    for palabra in palabras:
        if palabra in colores_diccionario_JP:
            respuesta = respuesta + colores_diccionario_JP[palabra] + ' '
            
        else:
            respuesta = respuesta + palabra + ' '
            
    print(respuesta)
        
else:
    print('La opcón ingresada no es correcta. Intente nuevamente')



    