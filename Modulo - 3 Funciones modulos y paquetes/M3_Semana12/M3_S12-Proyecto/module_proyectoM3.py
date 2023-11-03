
import numpy as NP
import random
from matplotlib import pyplot as PLT


inicio = []


def calcular_resultados(canicas, niveles):
    '''
    das
    '''
    
    print(canicas)
    print(niveles)

    #inicio = []

    for _ in range(canicas): # Este es el loop por el número de canicas

        posicion = 0

        for _ in range(niveles): # Este es el lopp por le número de niveles

            prob = [-1.0, 1.0]
            posicion += random.choice(prob)
    
   

    inicio.append(posicion)
    
    #return inicio


    print(inicio)
    graficacion_histog(inicio)
    # return inicio


def graficacion_histog(data):

    PLT.title('Simulación de la Máquina de Galton')
    PLT.xlabel('Distribución de canicas')
    PLT.ylabel('Cantidad de canicas')

    print(data)
    PLT.hist(data)


#inicio = []