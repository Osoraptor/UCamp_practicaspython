### Requisitos ###
### Simulación de una máquina de Galton de 3000 canicas
### En total tendrá 12 niveles de obstáculos -deberás decidir si va a caer a un lado o al otro 12 veces.
### El resultado final será un histograma que represente la cantidad de canicas en cada contenedor. No olvides colocar nombre a los ejes y un título al gráfico.
### Emplear dos funciones, una para calcular los resultados de las canicas y la segunda para la graficación del histograma.


import numpy as NP
import random
from matplotlib import pyplot as PLT


numero_canicas = 3_000 #Número de canicas
niveles = 12 # Número de niveles
probabilidad_izquierda = 0.5 # Probabilidad de ir a la izquierda
probabilidad_derecha = 0.5 # Probabilidad de ir a la derecha


# start = NP.empty(numero_canicas)
# start[0] = 0
#posicion = 0

inicio = []

start = 0 # Este es el origen de donde salen las canicas. \ Asi que hay probalidad del extremo izquierdo que es -12 al derecho que es +12


#def calcular_resultados():


    # posicion = 0
    # canica_rdn = NP.random.random(3000)
    # izquierda =  canica_rdn < probabilidad_izquierda
    # derecha =  canica_rdn > probabilidad_derecha

for canicaP in range(numero_canicas): # Este es el loop por el número de canicas

    posicion = 0

    for canicaN in range(niveles): # Este es el lopp por le número de niveles

        prob = [-1.0, 1.0]
        posicion += random.choice(prob)
        #posicion += random.randint(-1.0, 1.0)

        # azar = random.randint(0, 1) # Probabilidad aleatoria entre 0 y 1
        # '''
        # Utilizar el randint (-1,1) para que asi se salte los ifs! WoWWWWWWWWW!!!!!!!!!!
        # Esto se hace por 12 veces
        # '''
        # if azar > 0 and azar <  probabilidad_izquierda:
        #     posicion = posicion - 1.0 # moverse a la izquirda
        # elif azar > probabilidad_derecha and azar < 1.0:
        #     posicion = posicion + 1.0 # moverse a la derecha

    inicio.append(posicion)

    #start[canicaP] = posicion





#def graficacion_histog():

#n_bins = ( 2 * niveles + 1)

# x = range(niveles + 1)
# y = numero_canicas
# PLT.bar(x, y)

PLT.title('Simulación de la Máquina de Galton')
PLT.xlabel('Distribución de canicas')
PLT.ylabel('Cantidad de canicas')

print(inicio)
PLT.hist(inicio)

# PLT.hist(inicio, bins = range(int(start - niveles), int(start + niveles)))
# print(int(start - niveles))
# print(int(start + niveles))

#PLT.hist(inicio, bins = range(niveles * 2 + 1)) # revisar documentación bins =

PLT.show()



