
import numpy as NP
import random
from matplotlib import pyplot as PLT


inicio = []

### Calcular resultados ###

def calcular_resultados(canicas, bids):
    '''
    Esta función toma como referencia el número de canicas como el numero de niveles que se pasan del programa principal.
    Se usan 2 for loops, uno para el número de canicas y otro para el número de niveles.
    Para el tema de la probabilidad se usa una lista [-1.0, 1.0] con random.choice() para determinar que tanto a la izquierda o derecha terminan las canicas.
    Posteriormente se manda a llamar a función graficacion_histog() para proceder a graficar los resultados.
    '''
    #print(canicas) # Validación de canicas   
    #print(bids) # Validación de niveles

    for _ in range(canicas): # Este es el loop por el número de canicas

        posicion = 0 # Este es el origen de donde salen las canicas. \ Asi que hay probalidad del extremo izquierdo que es -12 al derecho que es +12

        for _ in range(bids): # Este es el loop por le número de niveles

            prob = [-1.0, 1.0]
            posicion += random.choice(prob) # Se utiliza random.choice para escoger un elemento de la lista al azar.


        inicio.append(posicion)
        
    #print(f'resultado: ', inicio) # Prueba dentro de la función calcular_resultados
    graficacion_histog(inicio)
    

    

### Graficar resultados ###

def graficacion_histog(resultado):
    '''
    Esta función grafica los resultados obtenidos de la función calcular_resultados().
    Se agrega el titulo y las etiquetas de los ejes X e Y.
    Finalmente se grafica en formato histograma.
    '''
    PLT.title('Simulación de la Máquina de Galton')
    PLT.xlabel('Distribución de canicas')
    PLT.ylabel('Cantidad de canicas')

    #print(f'Test ', resultado) # Prueba dentro de la función graficacion_histog
    PLT.hist(resultado)

    PLT.show()


