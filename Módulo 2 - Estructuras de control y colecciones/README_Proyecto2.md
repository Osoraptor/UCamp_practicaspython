# Notas Generales

Este repo contiene todos los archivos y programas creados dentro del bootcamp Fundamentos de Python.

Módulos:

•	Módulo 2: Estructuras de control y colecciones.


# Módulo 2: Estructuras de control y colecciones / Proyecto 2 - Longitud de una frase & Encuentra el cuadrante

Archivo de proyecto:

  - proyecto2_Longitud_Frase.py .  
  - OSWALDO_MARTINEZ_proyecto2.py .  

Para la elaboración del proyecto **Longitud de una frase**, decidí hacerlo por separado en otro archivo ya este lo encontré de un carácter sencillo ya que se valida el **input** del usuario primero con la función **len**, esto para determinar de cuantos caracteres es la frase, y posteriormente con los validadores **if**, **elif** y el **else** para determinar si la frase es correcta dentro de los parámetros del ejercicio o si esta le faltan o sobran caracteres.

Para la elaboración del proyecto **Encuentra el cuadrante**, la prioridad fue enfocarse en las validaciones de que los campos **input** para que estos solo permitieran números incluidos en lista, la cual contenía ya los que son negativos; y por otro lado verificar que en el contenido de los **input** no se encontrarán “*letras*”. Esto se logró gracias al uso del **while True:** y las validaciones como **str. isalpha()** y **str.startswith()** .

Lo más difícil fue hacer la validación de revisar si el contenido de los **input** contenía “*letras*”. Para esto en específico se utilizó el ciclo “*for*” para revisar cada elemento del input y al encontrar el primer valor alfabético, volvía la validación de **str. isalpha()** en “*True*” lo cual le devuelve un mensaje al usario de que el valor ingresado no debe de contener letras.

Ahora bien, para poder hacer las validaciones de a que cuadrante correspondían los números ingresados por el usuario, primero las variables se convirtieron a “*enteros*”, esto para que se pudieran lograr operaciones matemáticas con los operadores menor que (<)  y el mayor que (>).

Para determinar el cuadrante, se hizo uso de las validaciones **if** junto con la comparación de los operadores matemáticos, lo cual permitió de una sencilla de terminar los cuadrantes al validar los valores contra el 0, esto es si eran menores a 0 o mayores a 0. Con esto se llegó a los siguientes validadores:

  - if X > 0 and Y > 0 = cuadrante I.
    
  - if X < 0 and Y > 0 = cuadrante II.

  - if X < 0 and Y < 0 = cuadrante III.

  - if X > 0 and Y < 0 = cuadrante IV.

¨Por último, se imprime los valores de cada eje, el de la **X** y el de la **Y** y se imprime a que cuadrante pertenece.
