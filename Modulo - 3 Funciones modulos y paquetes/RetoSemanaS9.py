# Caracteristicas del programa:
# un bucle infinito solicite al usuario una letra
# especificar al usuario la condición para terminar el programa
# una función que imprima en la pantalla la letra siguiente en el alfabeto y la letra anterior a la ingresada
# El programa debe continuar en el bucle hasta que el usuario decida salir del programa

# 

import string # Se importa string para poder hacer uso del alfabeto

lista_abc = list(string.ascii_lowercase)
print(lista_abc) #NOta: validación de lista del alfabeto




def letras_abc(letra_user):
    for letra in lista_abc:
        if letra == letra_usuario:
            print(f'Esta es la letra: {letra}')
            break
        else:
            print('La letra no se encuentra en nuestro alfabeto.')
            break



while True:

    choice = input('Ingresar letra (1) o terminar programa (7): ')

    if choice == '1':
        letra_usuario = input('Ingrese una letra por favor: ').lower()
        print(letra_usuario)
        letras_abc(letra_usuario)
    elif choice == '7':
        print('Cierre de programa.')
        exit()
    else:
        print('Opción invalida. Vuelva a intentar por favor.')

