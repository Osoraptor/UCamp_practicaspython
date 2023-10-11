import string # Se importa string para poder hacer uso del alfabeto

lista_abc = list(string.ascii_uppercase)
print(lista_abc) #NOta: validación de lista del alfabeto


def letras_abc(fname):
    
    prueba = lista_abc.index(fname)
    #prueba = int(prueba)
    print(prueba)
    # print(type(prueba))

    pruebaB = lista_abc[prueba - 1]
    print(f'La letra anterior es: ' + pruebaB)

    pruebaC = lista_abc[prueba + 1]
    print(f'La letra siguiente es: ' + pruebaC)


letra_usuario = input('Ingrese una letra por favor: ').upper()

if letra_usuario in lista_abc:
    print('yeah')
else:
    print('error')


# for letra in lista_abc:
#     if letra == letra_usuario:
#         print(f'La letra ingresada es: {letra}')
#         letras_abc(letra_usuario)
#         break
#     else:
#         print('error')
    

#letras_abc(letra_usuario)


#def letras_abc(letraIngresada):
    

# print(lista_abc[prueba - 1]) # Nota validacion -1

################### TEST 2 ##################

# def letras_abc(fname):
 
#     prueba = lista_abc.index(fname)
#     #prueba = int(prueba)
#     print(prueba)
#     # print(type(prueba))

#     pruebaB = lista_abc[prueba - 1]
#     print(f'La letra anterior es: ' + pruebaB)

#     pruebaC = lista_abc[prueba + 1]
#     print(f'La letra siguiente es: ' + pruebaC)

