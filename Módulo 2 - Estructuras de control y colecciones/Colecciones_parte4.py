## Cast tupla a un diccionario ##

tiempos = dict(
    Hamilton = '1:49.8',
    Bottas = '1:56.4',
    Perez = '1:53.8',
    Jago = '1:53.8'
)

print(tiempos)

tiempos1 = {
    'Hamilton': '1:49.8',
    'Bottas': '1:56.4',
    'Perez': '1:53.8',
    'Hamilton': '1:53.8'
}

print(tiempos1)

#Nota: Un diccionario no puede tener claves (llave) duplicadas. Cuando se usa la clase dict() no se puede tener una llave duplicada, pero si en un diccionario aparte donde se toma el último valor como referencia.

### PILAS ###
# Nota: esquema last in first out (LIFO). Los últimos elementos en entrar en la lista serán los primero en salir de ella.
# Las pilas tienen un esquema FIFO (First IN First OUT), los primero elementos en entrar son los primeros en salir.

pila = [3, 6, 7]

while len(pila) >= 3:
    if pila[-1] % 3 :
        extraido = pila.pop()
        pila.append(extraido + 1)
        print(pila)
    else: 
        print('Todos los elementos de la pila son multiplos de 3.')
        break


