# Caracteristicas del programa:
# un bucle infinito solicite al usuario una letra
# especificar al usuario la condición para terminar el programa
# una función que imprima en la pantalla la letra siguiente en el alfabeto y la letra anterior a la ingresada
# El programa debe continuar en el bucle hasta que el usuario decida salir del programa

# 

import string # Se importa string para poder hacer uso del alfabeto list(string.ascii_uppercase)

lista_abc = list(string.ascii_uppercase)
#print(lista_abc) #Nota: validación de lista del alfabeto




def letras_abc(letraIngresada):
    '''
    En esta funcion se revisa lo siguiente:
    El index de la letra ingresada por el usuario dentro de la lista del alfabeto.
    Con base a ese index se le resta 1 y se suma 1 para poder hacer el print de la letra anteriror y siguiente.
    '''
    letraIngresadaID = lista_abc.index(letraIngresada) # Nota: Se utiliza el método .index para sacar la posición de la letra dentro de la lista.

    letraAnterior = lista_abc[letraIngresadaID - 1]
    print(f'La letra anterior es: ' + letraAnterior)

    letraSiguiente = lista_abc[letraIngresadaID + 1]
    print(f'La letra siguiente es: ' + letraSiguiente)
    


while True:

    choice = input('Ingresar letra (1) o terminar programa (7): ')

    if choice == '1':
        letra_usuario = input('Ingrese una letra por favor: ').upper()

        if letra_usuario in lista_abc:
            print(f'La letra ingresada es: {letra_usuario}')
            letras_abc(letra_usuario)
            
        else:
            print('La letra no se encuentra en nuestro alfabeto.')
            
    elif choice == '7':
        print('Cierre del programa.')
        exit()
    else:
        print('Opción invalida. Vuelva a intentar por favor.')

