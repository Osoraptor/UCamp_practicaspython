
palabra = input("Introduce una palabra: ")

if len(palabra) < 4: # Validación menor a 4 palabras
    print(f'Hacen falta letras. Solo tiene {len(palabra)} letras')
elif len(palabra) > 8: # Validación mayor a 8 palabras
    print(f'Sobran letras. Tiene {len(palabra)} letras')
else:
    print('La palabra es correcta!')