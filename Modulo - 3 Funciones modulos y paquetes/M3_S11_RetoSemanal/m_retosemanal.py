### <<m_retosemanal.py>>

lista_de_listasX = []
elementos_listas = []
lista_referencia = []

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

    lista_de_listasX.extend(lista_de_listas)

### Remover duplicados ###

def remover_duplicados(lista_referencia, elementos_listas):
    '''
    Esta función toma como parametros la lista de referencia a tener en cuenta. Los elementos de esta se usarán para remover duplicados.
    Se crea una lista temporal donde se guardan los elementos de la lista de referencia.
    Se hace un loop con los elementos de la lista de referencia y con su index se borran los duplicados de la lista maestra.
    Se hace un extend a la lista de refencia con la lista temporal para tener todo en contexot.
    Se imprime la lista con las lista sin los elementos duplicados y los valores originales de la lista de referencia.
    '''
    print(f'Lista de referencia: ', lista_de_listasX[lista_referencia - 1]) #Nota: Validación del Valor original de la lista de listas.

    elementos_borrar = []
    eduplicados = elementos_listas
    lista_RX = lista_referencia
    

    for item in lista_de_listasX[lista_RX - 1]:
        elementos_borrar.append(item)

    vueltas = 0


    while vueltas <= eduplicados:


        for duplicado in lista_de_listasX:

            if vueltas > eduplicados:
                break

            try:
                duplicado_index = duplicado.index(elementos_borrar[vueltas])
                
            except ValueError:
                pass
            else:
                del duplicado[duplicado_index]
        
        vueltas += 1


    #print(lista_de_listasX) #Nota: Validación de listas sin duplicados borrando todos los elementos de la lista de referencia.
   
    print(f'Se borraron todos los duplicados y elementos de la lista {elementos_borrar[lista_RX - 1]}')

    lista_de_listasX[0].extend(elementos_borrar)
    print(f'Las listas sin los elementos duplicados son:', lista_de_listasX)

