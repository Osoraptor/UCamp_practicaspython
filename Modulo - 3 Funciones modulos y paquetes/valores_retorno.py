# Valores de retorno sentencia RETURN

# def promedio (*numeros):
#     '''
#     Recibe sólo parametro de tipo tupla, de valores númericos
#     y se regresa su promedio
#      '''
#     return sum(numeros) / len(numeros) # La sentencia return termina la secuencia de la iteración como la sentencia BREAK

# x = promedio(4, 5, 6)
# print(x)

###########################

# def area(**dato): # **dato es una variable que recibe un diccionario
#     '''
#     Calcula el área de una figura geométrica y la imprime en pantalla.
#     '''
    
#     #si el diccionario tiene una clave llamada 'figura' se evalua el valor de la clave

#     if dato['figura']=='Rectángulo': # Si el valor de la clave es 'Rectángulo' imprime el valor de la clave 'base'
#         return(dato['base'] * dato['altura'])
#     elif dato['figura']=='Triángulo':
#         return(dato['base'] * dato['altura'] / 2)
#     elif dato['figura']=='Circulo':
#         return(3.141593 * dato['radio'] **2)
#     else:
#         print('Figura desconocida')


# triangulo = area(figura = 'Triángulo', base = 10, altura = 8)
# print(f'El área del triángulo es: {triangulo}')


# circulo = area(figura = 'Circulo', radio = 10, color = 'Rojo')
# print(f'El área del circulo es: {circulo}')

# dodecagono = area(figura = 'Dodecágono', lado = 10)
# print(f'El área del dodecágono es: {dodecagono}')


#########################################################

### Recursividad de funciones en python

# def factorial(numero, intentos = 0):
#     if numero == 0:
#         return 1
#     else:
#         intentos += 1
#         print(intentos)
#         return numero * factorial(numero - 1, intentos)
    
# print('El factorial de 0 es (0!):', factorial(0))
# print('El factorial de 1 es (1!):', factorial(1))
# print('El factorial de 3 es (3!):', factorial(3))
###print('El factorial de -1 es (-1!):', factorial(-1))

#################################################################

### Funciones lambda o funciones anónimas ###

# suma = lambda x, y : x + y

# print(suma('Hola ', 'mundo!'))
# print(suma(2, 5))

# lista_numeros = [1, 0, -2]
# lista_numeros = sorted(lista_numeros, key = lambda n: abs(n))
# print(lista_numeros)


################################################################

### Funcion zip

paises = ['Kenia', 'Francia', 'México', 'Japón']
capitales = ['Nairobi', 'Paris', 'Ciudad de México', 'Tokio']
poblacion = [54, 66, 130]

for elemento in zip (paises, capitales, poblacion):
    print(elemento)

# Usar multiples elementos en un solo paso, como listas de personas con sus atributos (nombre, edad, trabajo) y se requiere emparejarlos a un solo elemento