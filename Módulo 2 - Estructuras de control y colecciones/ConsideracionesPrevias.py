
### if / elif /  else ###

animal = input('Dime un animal: ')
if animal == 'perro':
    print('-guau')
elif animal == 'gato':
    print('-Miau')
elif animal == 'vaca':
    print('-Muu')
else:
    print('No conozco su sonido.')

print('Conozco pocos animales')

# nota: se usa pass cuando queremos que un bloque de codigo no haga nada


num = int(input('Ingrese un entero: '))
if num < 0:
    num = -num
print('Su valor absoluto es', num)


######################

### while ###

print('Impares menores a 10')

x = 1

while x <= 10:
    print(x)
    x+=2

# Nota: aquí se impreme el resultado hasta antes del 10 ya que previo a ello el while era FALSE.

factorial = 5

contador = factorial -1

while contador > 0:

    factorial *= contador
    contador -= 1

# Nota: revisar ejemplo con print!

#####################################

### FOR ###

for i in 1,2,3:
    print(i)

for i in range(5): # Nota; dentro del parentesis se pone el rango, que es la catidad de veces que se ejecutará el codigo).
    print(i) # En este ejemplo, a recordar que en Python el 0 se cuenta como 1 para conteo.

for i in ['Ale', 'Ivan', 'Monse', 'Luis', 'Rafa', 'Luca']: # Esta es una lista con el sigo [].
    print(i)

for i in 'Hola Mundo':

    if i == 'M':
        pass # ejemplo del pass donde el FOR no considera esta parte.

    else:
        print(i, end='')
