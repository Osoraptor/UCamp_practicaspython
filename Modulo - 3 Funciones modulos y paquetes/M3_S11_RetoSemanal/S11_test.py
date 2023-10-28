

### Validaciones ###

# while True:

#     numero_listas = input('¿Cuantas listas se van a crear? ')

#     if numero_listas.isdigit():
#         numero_listas = int(numero_listas)
#         if numero_listas == 0:
#             print('El valor no puede ser 0. Intente nuevamente por favor')
#         elif numero_listas <= 5:
#             break
#         else:       
#             print('El limite máximo es 5. Intente nuevamente por favor.')


#     else:
#         print('Opción invalida. Ingrese un número por favor.')
        

# while True:

#     elementos_listas = input('¿Cuantos elementos tendrán las listas? ')

#     if elementos_listas.isdigit():
#         elementos_listas = int(elementos_listas)
#         if elementos_listas == 0:
#             print('El valor no puede ser 0. Intente nuevamente por favor')
#         elif elementos_listas <= 5:
#             break
#         else:       
#             print('El limite máximo es 5. Intente nuevamente por favor.')


#     else:
#         print('Opción invalida. Ingrese un número por favor.')


# print(f'Número de listas: {numero_listas}.')
# print(f'Número de elementos por lista: {elementos_listas}.')


### Recorrido FOR ###

lista_elementos = []
lista_de_listas = []


numero = 2
elemento = 2

vueltas = 1

while vueltas <= numero:
    
    for elementoX in range(elemento):
        elementoB = input(f'Para la lista {vueltas}, Ingrese el elemento {elementoX+1}: ').title()
        lista_elementos.append(elementoB)
    print(f'Elementos de la lista {vueltas}: ',lista_elementos)
    lista_elementos.insert(0, f'Lista {vueltas}') # Se inserta al inicio de la lista la lista en cuestion (la lista y su número como string).
    lista_de_listas.append(lista_elementos) # Se hace un append de esta lista a la lista maestra.
    lista_elementos = [] # Se borra la lista o un clear de la lista para poder volver a usarla.
    vueltas += 1


print(f'Las listas son: ', lista_de_listas)






# x = 1

# while x <= 10:
#     print(x)
#     x+=2

