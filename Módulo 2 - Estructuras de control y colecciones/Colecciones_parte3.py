### TUPLAS ###

# vocales = ('a', 'e', 'i', 'o', 'u')

# print(vocales[2])

# ERROR vocales[2] = 'I' # Python no permite modificar valores en una tupla y devuelve el error: tuple' object does not support item assignment

# print(vocales[:3] + vocales[2:]) # aquí se concatena la tupla

# el prumer indice es hasta y el segundo desde. Cuando se deja en blanco algo es el contenido total.

# nota en los indices, el de la izquiera si se toma en cuenta su propio valor mientras que el de la izquierda hay que restarle 1 ya que este no se toma en cuenta.

# print(vocales.index('o'))

# Nota: para poder modificar una tupla se puede hacer por medio de una lista, despues se convierta de lista a tupla

# lista_vocales = list(vocales) # la funcion lista nos permite traer una lista a partir de una tupla

# lista_vocales[2] = 'I'

# print(lista_vocales)

# tupla_vocales = tuple(lista_vocales)

# print(tupla_vocales)

# ERROR tupla_vocales[2] = 'W' # no se puede modificar una tupla


### CONJUNTOS ###

# Nota: Los conjuntos no tienen orden ni indice y no se puede repetir valores

# canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'platano'}

# print(canasta)

# print('manzana' in canasta)
# print('melón' in canasta)

# vocales = ['a', 'e', 'i', 'o', 'u', 'a']
# print(vocales)

# vocales = list(set(vocales)) # primero se convierta a conjunto y luego a lista
# print(vocales)

# vocales1 = {'a', 'e', 'i', 'o', 'u', 'a'}

# vocales2 = {'e', 'i', 'o'}

# print(vocales2.issubset(vocales1)) # Nota: El método issubset() nos permite saber si un conjunto esta dentro de otro conjunto

# vocales1 = {'a', 'e', 'i', 'o', 'u'}
# vocales2 = {'A', 'E', 'I', 'O', 'U', 'u'}

# print(vocales1 - vocales2) # la diferencia de ambos conjuntos

# print(vocales1 | vocales2) # Nota: El simbolo | agrega los valores de un conjunto a otro conjunto

# print(vocales1 & vocales2) # Nota: El simbolo & verifica si un valor esta en ambos conjuntos

# print(vocales1 ^ vocales2) # Nota: El simbolo ^ nos permite que valores no estan en ambos (en este caso la u no se ve)



### CONJUNTOS ###

# Los diccionarios es una colección sin un orden ni índice, en lugar del índice usa llaves, (llave / valor)
# Las llaves le dan un identificador a cada elemento del diccionario
# Los diccionarios no permiten las llaves duplicadas y si pueden ser modificables
# Permite mapeo entre 2 colecciones distintas
# Las llaves deben ser únicas dentro de un diccionario

tiempos = {
    'Hamilton': '1:49.8',
    'Bottas': '1:56.4',
    'Perez': '1:53.8',
    'Jago': '1:53.8'
}

#print(tiempos)

#print(tiempos.items()) # Nota: El método items nos permite traer una lista de tuplas por cada llave y su valor

#print(tiempos.keys()) # Nota: devulve todas las llaves contenidas en un diccionario (lista)

#print(tiempos.values()) # Nota: devulve todos los valores contenidos en un diccionario (lista)

print(tiempos.get('Hamilton')) # Nota: para obtener el valor especifico de una llave, se usa el método get() y se introduce dentro de sus parentesis la llave a la cual se le buscará su valor.

print(tiempos.get('mamilton', 'No encontrado')) # Si no se encuentra la llave dentro del diccionario, se puede agregar otro argumento dentro del get para poner un mensaje por ejemplo.






