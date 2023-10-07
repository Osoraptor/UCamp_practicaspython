
palabra = input("Introduce una palabra: ")

if len(palabra) < 4:
    print(f'Hacen falta letras. Solo tiene {len(palabra)} letras')
elif len(palabra) > 8:
    print(f'Sobran letras. Tiene {len(palabra)} letras')
else:
    print('La palabra es correcta!')