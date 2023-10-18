# Parametros de tipo TUBLA, *args

def promedio (*numeros):
    '''
    Recibe sólo parametro de tipo tupla, de valores númericos
    y se imprime su promedio
     '''
    promedio = sum(numeros) / len(numeros)
    print('El promedio es: ', promedio)


promedio(4)
promedio(4, 5, 6)
promedio(1, 2, 3, 4, 5, 6, 7, 8, 9)



def es_numero(titulo, *serie):
    '''
    Imprime titulo.
    Verifica si el caracter de tipo tupla es un numero o no.
    '''
    print(titulo)
    for algo in serie:
        if type(algo) == int or algo.isdigit():
            print(f'{algo} es numero')
        else:
            print(f'{algo} no es numero')


es_numero('Numeros', '1', '2', '3')
es_numero('Letras', 'a', 'b', 'c')


nombre = 'Mezcla'
lista_varios = ['a', '2', 3, 'f', 5]
es_numero(nombre, *lista_varios) # Se tiene que agregar el * a la variable que se va a usar en la función que tiene parametros de tipo TUPLA.



#########################################################

#### Parametros tipo diccionario **kwargs

def area(**dato): # **dato es una variable que recibe un diccionario
    '''
    Calcula el área de una figura geométrica y la imprime en pantalla.
    '''
    
    #si el diccionario tiene una clave llamada 'figura' se evalua el valor de la clave

    if dato['figura']=='Rectángulo': # Si el valor de la clave es 'Rectángulo' imprime el valor de la clave 'base'
        print(dato['base'] * dato['altura'])
    elif dato['figura']=='Triángulo':
        print(dato['base'] * dato['altura'] / 2)
    elif dato['figura']=='Circulo':
        print(3.141593 * dato['radio'] **2)
    else:
        print('Figura desconocida')


area(figura = 'Triángulo', base = 10, altura = 5)
area(figura = 'Circulo', radio = 10, color = 'Rojo')
area(figura = 'Dodecágono', lado = 10)
