### Grafico de campana GAUS ###

import numpy as NP
import matplotlib.pyplot as PLT

datos = NP.random.normal(0, 1.0, 1000)

PLT.hist(datos) # esto genera un histograma
PLT.show()
