texto_variado = 'Palabra 123 +-* #%&'
print(type(texto_variado))

# Nota: El uso de triple "" para poder imprimir lo que escribamos tal cual en una cadena.
# También se usa el simbolo \ para poder decirle a Python que meta lo que viene despues en la misma linea


print("""
Funcionamiento de \
programa: (opciones)
    -1 para acceder a opcines
        -2 para salir
""")

### Subscripting e indexado

texto = 'Python'

print(texto[0])
print(texto[5])
print(texto[-1])
print(texto[-6])

# Nota: los elementos negativos se comienzan del elemento a la izquierda, en este caso desde el estecho derecho o la última letra.

print(texto[6]) # esto es un error de fuera del rango, posición que no existe (string index out of range)
print(texto[-7]) # esto es un error de fuera del rango, posición que no existe (string index out of range)

letra = texto[0]
print(letra)

texto[0] = 'p' # error: no se puede modificar una cadena ('str' object does not support item assignment)

letra = 'p'
print(letra)

texto_compuesto = letra + texto[1] # Concatenacion en cadenas de texto
print(texto_compuesto)


################################################################################

### Slicing o Substringing

texto = 'Python'
print(texto[0:3]) # al segundo numero se le resta 1 en la consideración
print(texto[0:-3])
print(texto[0:-2])
print(texto[2:]) # Al no poner un numero y dejarlo en blanco se impre hasta el final de la cadena
print(texto[:3])

print(texto[-3::-1]) # se agregan los incrementos o saltos

print(texto[::-1])
print(texto[1:50]) #Nota: no da error, pero llega al limite de la cadena
print(texto[2:2]) # no se impreme ya el alcance sobrescribe el resultado ya que se excluye


#################################################################################

### Cadenas y formatos

texto = 'Hola mundo! Buenastardes'
print(texto.lower()) #.lower() pone todo en minusculas
print(texto.upper()) #.upper() pone todo en mayusculas
print(texto.capitalize()) # SOLO La primera letra de toda la cadena la hace mayuscula
print(texto.title()) # La inicial de cada palabra sea mayuscula
print(texto.swapcase()) #intercambia las mayusculas por las minusculas


texto = texto.upper() #Solo al cambiar el valor de la variables es que puede cambiar la cadena
print(texto)

### formatos de print y cadenas

print('{} + {} = {}'.format(2, 3, 2+3))
print('{} + {} = {}'.format('Hola', 'mundo', 'Hola mundo'))
print('{:.3f} + {:.4f} = {}'.format(2, 3, 2+3)) # .3f agrega decimales al numero
print('{1} + {0} = {2}'.format(2, 3, 2+3)) # los numeros dentro de los {} indican los indices del formato
print('{2} + {0} = {1}'.format('Hola', 'mundo', 'Hola mundo'))
print('{:d} = {:b} = {:o} = {:x}'.format(15, 15, 15, 15)) # se pone el tipo de impresion de numero, decimal, hexa, binario, etc




