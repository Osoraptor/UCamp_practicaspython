### Reto Semana 10 ###

### Que permita crear dos listas de distintas longitudes.
### Que la longitud y los elementos de cada lista sean especificados por el usuario.
### Que imprima las listas indicando que son las listas originales.
### Que elimine de la primera lista los nombres de la segunda.
### Que imprima la primera lista indicando que se han eliminado los elementos que estaban también en la segunda


def agreagar_nombres(lista, valor):
    '''
    Función que agrega un dato a una lista especificada.
    '''
    if valor == '':
        valor = 'No especificado.'  
    lista.append(valor)
    return lista


def quitar_nombresDuplicados(lista, valor):
    '''
    Función que quita nombres duplicados de la lista 1 que se encuentren en la lista 2.
    '''
    if valor == '':
        valor = 'No especificado.'  
    lista.append(valor)
    return lista


lista_nombres1 = []
lista_nombres2 = []
lista_nombresSinDuplicados = []


elementos_lista = int(input('Cuantos nombres tendrán las listas? '))

for elemtento in range(elementos_lista):
    nombre1 = input(f'Para la primera lista, Ingrese el nombre de la persona {elemtento+1}: ').title()
    elementos_lista1 = agreagar_nombres(lista_nombres1, nombre1)
    

for elemtento in range(elementos_lista):
    nombre2 = input(f'Para la segunda lista, Ingrese el nombre de la persona {elemtento+1}: ').title()
    elementos_lista2 = agreagar_nombres(lista_nombres2, nombre2)

print(f'Los nombres de la primera lista son: {lista_nombres1}')

print(f'Los nombres de la segunda lista son: {lista_nombres2}')


elementos = [elemento for elemento in lista_nombres1 if elemento not in lista_nombres2]
lista_nombresSinDuplicados = quitar_nombresDuplicados(lista_nombresSinDuplicados, elementos)

print(f'La primera lista sin dulicados de la segunda lista es: {lista_nombresSinDuplicados}')