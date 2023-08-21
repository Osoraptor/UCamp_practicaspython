#Ejemplos de la función print()

print('Hola mundo')
print('Hola mundo', 'otra vez') # Cuando usamos la ',' se agrega un espacio entre parametros
print('Son las', 9, 'de la mañana')
print('El resultado de 3 * 4 es:', 3 * 4)

#Ejemplo de cadenas formateadas

print('El número 15 en sistema decimal es %d, en sistema octal es %o, en el sistema hexadecimal es %x' %(15, 15 , 15))

pi = 3.141592
r = 5
print(f'El radio de un circulo es {r} y el área de ese circulo es {pi * r ** 2 : .2f}')

#Impresion de caracteres especiales

print('La letra beta es: \n\t \u03B2') # \n es para salta de linea / \t es para dar salto de tabulación / \formatoAski para caracteres especiales

#Caracteres de escape ESC key

print('Hola mundo', end = ' ')
print('otra vez', end = '\t')
print('y otra vez')



