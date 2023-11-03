### Graficas con NUMPY ###

import numpy as NP
import matplotlib.pyplot as PLT

NP.random.seed(0) # para plantar una semill y tener numeros seudo-aleatorio

numeros = NP.random.rand(5) # cuantos valores se van a generar random



#NP.random.normal(media_distribucion, desviacion_estandar, tamano_muestras)

print(numeros)

PLT.plot(numeros)
PLT.show()
