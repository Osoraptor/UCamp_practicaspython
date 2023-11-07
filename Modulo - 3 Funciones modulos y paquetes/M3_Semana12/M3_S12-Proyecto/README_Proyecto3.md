# Notas Generales

Este folder/repo contiene archivos y programas creados dentro del bootcamp Fundamentos de Python.

Módulos:

•	Módulo 3: Funciones, módulos y paquetes.


# Módulo 3: Funciones, módulos y paquetes / Proyecto 3 - Gráfica de datos aleatorios

Archivos del proyecto:

  - module_proyectoM3.py .  
  - OSWALDO_MARTINEZ_proyectoM3_app.py .  

Para la elaboración del proyecto **Gráfica de datos aleatorios**, se trabajó en 2 programas, uno donde se contienen las funciones como modulo y el otro como programa principal el cual importa las funciones del programa modulo.

Posteriormente se procede a trabajar con las 2 funciones que vienen como requisito del proyecto.

La primera función toma como referencia el número de canicas como el número de niveles que se pasan del programa principal. Se usan 2 “*for loops*”, uno para el número de canicas y otro para el número de niveles. Para el tema de la probabilidad se usa una lista **[-1.0, 1.0]** con **random.choice()** para determinar que tanto a la izquierda o derecha terminan las canicas. Posteriormente se manda a llamar a la función **graficacion_histog()** para proceder a graficar los resultados.

La segunda función grafica los resultados obtenidos de la función **calcular_resultados()**. Se agrega el título y las etiquetas de los ejes “*X*” e “*Y*”. Finalmente se grafica en formato histograma.

Por último, se imprime “*fin del programa*” una vez que se cierra la ventana de la gráfica.