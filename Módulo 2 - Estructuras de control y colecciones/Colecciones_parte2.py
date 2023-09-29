
vocales = ['a', 'e', 'i', 'o', 'u']

vocales[1:4] = ['E', 'I', 'O'] # el 1 se toma en cuenta despues del 0 y el 4 representa antes de ese número, por lo que se cambia desd

vocales[1:4] = [] # aquí como no hay nada se elimina el rango que se estipuló, del 1 al antes del 4

print(vocales, len(vocales))

vocales[1:2] = ['e', 'i', 'o', 'u'] #aqui se agregan datos en lugar de la posición 1 anterior, que en este caso es 'u'

print(vocales, len(vocales))

vocales.extend(['i', 'i']) # se incrementa la lista al final de ella con los nuevos valores

print(vocales, len(vocales))

print(vocales.index('i')) # nos regresa el primer lugar donde aparece el valor dentro de la lista

print(vocales.count('i')) # nos cuenta el numero de veces que el valor aparece en la lista.

print(vocales.index('i', 4)) # el metodo index nos permite espicificar a partir de que posición se toma en cuenta el index

vocales.reverse() # se trae la list al revés.

print(vocales, len(vocales))

vocales.sort() # El método sort() ordena lo valores de manera ascendente

print(vocales, len(vocales))

## Nota: En Python se comienza a contar desde el 0 !!!


### ejemplos lista ###

carros = ['Audi', 'Ford', 'BMW', 'VW']

carros.sort(key=len) # aquí se ordenan los elementos según su longitud y los ordena alfabeticamente

print(carros)

listas = [[0, 1], [2, 3, 4], [5,6]]

print(listas[0], listas[1:3]) # aquí se especifica desde que posición de la lista se imprime

print(listas[2][1]) # aqui se defina cual lista imprimir y que elemento se de esa lista se tomará en cuenta

x = [3, 2.5, 6, 6.3] # esto se guarda en la memoria del programa (casillero)


### memoria en listas ###

vocales1 = ['a', 'e', 'i', 'o', 'u']

vocales2 = vocales1 # se hace una copia o duplicado del contenido de la variable

print(vocales1, vocales2)

print(id(vocales1), id(vocales2)) # se le asigna el mismo ID a la segunda variable ya que python asi optimiza memoria.

vocales3 = vocales1.copy() # el método copy hace una copia del valor y se guarda en un nuevo ID, el del 3. 

print(id(vocales1), id(vocales3))

print(id(vocales1[2]), id(vocales2[2])) # aquí se puede ver que cada valor es un objeto en Python y por ende tiene su propio ID

print(id(vocales1[2]), id(vocales3[2])) # es el mismo ID de objeto pero en diferente casillero

del vocales1[2]
print(vocales2, vocales3) # aquí se ve que la eliminación sucede a nivel de la primera variable pero no sobre la copia que se le hizo

print(id(vocales1[2]), id(vocales3[3])) # los valores tienen el mismo ID ya que son al final el mismo objeto

