### Grafico de dispersión ###

import random
import matplotlib.pyplot as PLT

eje_x = [random.randint(1, 100) for n in range (100)]

eje_y = [random.randint(1, 100) for n in range (100)]

PLT.scatter(eje_x, eje_y)

PLT.title('Gráfica de dispersión')

PLT.show() # este comando muestra la grafica en una nueva ventana

