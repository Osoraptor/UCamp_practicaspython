### <<m_retosemanal.py>>

def agreagar_elements(numero, elemento):
    '''
    Esta función recibe el número de listas y los elementos que contendrá una lista.
    Posteriormente, se agragan los elementos a una lista temporal.
    A esta última se le hace un insert() con la lista y su número en formato string.
    Después esta lista hace un append() de su contenido a la lista de listas.
    Finalmente se hace un clear de la lista temporal para poder volver a usar mientras el while se cumpla.
    '''
    
    lista_elementos = []
    lista_de_listas = []

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



# def agreagar_elementos(lista, valor):
#     '''
#     Función que agrega un dato a una lista especificada.
#     '''
#     if valor == '':
#         valor = 'No especificado.'  
#     lista.append(valor)
#     return lista


def quitar_nombresDuplicados(lista, valor):
    '''
    Función que quita nombres duplicados de la lista 1 que se encuentren en la lista 2.
    '''
    if valor == '':
        valor = 'No especificado.'  
    lista.append(valor)
    return lista