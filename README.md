# Notas Generales

Este repo contiene todos los archivos y programas creados dentro del bootcamp Fundamentos de Python.

Módulos:

•	Módulo 1: Variables, operadores y cadenas de texto.


# Módulo 1: Variables, operadores y cadenas de texto / Proyecto 1 - Calculadora de Índice de masa corporal

Archivo de proyecto: proyecto1.py .

Para la elaboración de este proyecto, la prioridad fue enfocarse en las validaciones de que los campos no estuvieran vacíos o que fueran entregados con la tecla de espacio “*space*”. Esto se logró gracias al uso del **while True:** y las validaciones como **str. isalpha()** y **str.isnumeric()** .
Esto se usó principalmente para la obtención de los datos:

  - Nombre  
  - Apellido Paterno  
  - Apellido materno  
  - Edad

Por otro lado, fue un tanto más complicado las validaciones para los campos que requerían información decimal o en este caso flotante. Para esto se usó validaciones con el **while True:** con la adición de **try:** , **except ValueError:** y la valición de los flotantes con **isinstance(varibale, float)** . 

Para el calculo del IMC, se hizo uso de las validaciones con el **if**, **elif** y el **else**; junto con el operador menor o igual que (<=).
Finalmente, al introducir todos los datos, se imprimé toda la información junto con la condición en la que se encuentra la persona con base al IMC obtenido.

Menor a 18.9   = peso bajo

18.50 a 24.99   = peso normal

25.00 a 29.99   = sobrepeso

30.00 a 34.99   = obesidad leve

35.00 a 39.99   = obesidad media

Mayor a 40.0   = obesidad mórbida

