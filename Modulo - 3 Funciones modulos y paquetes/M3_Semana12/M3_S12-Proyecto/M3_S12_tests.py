import numpy as NP
import random
from matplotlib import pyplot as PLT


numero_canicas = 3_000 #Número de canicas
niveles = 12 # Número de niveles
probabilidad_izquierda = -1.0 # Probabilidad de ir a la izquierda
probabilidad_derecha = 1.0 # Probabilidad de ir a la derecha


inicio = []


### Calcular resultados ###

def calcular_resultados(canicas, bids):

    

    for _ in range(canicas): # Este es el loop por el número de canicas

        posicion = 0 # Este es el origen de donde salen las canicas. \ Asi que hay probalidad del extremo izquierdo que es -12 al derecho que es +12

        for _ in range(bids): # Este es el loop por le número de niveles

            prob = [-1.0, 1.0]
            posicion += random.choice(prob) # Se utiliza random.choice para escoger un elemento de la lista al azar.


        inicio.append(posicion)




calcular_resultados(numero_canicas, niveles)

#############################################################


def graficacion_histog(resultado):

    PLT.title('Simulación de la Máquina de Galton')
    PLT.xlabel('Distribución de canicas')
    PLT.ylabel('Cantidad de canicas')

    print(resultado)
    PLT.hist(resultado)

    PLT.show()


print('A continuación se grafica los resultados: ')

graficacion_histog(inicio)



