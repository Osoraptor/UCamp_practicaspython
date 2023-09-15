
### While ###

print('Impares menores a 10')
x = 1
while x <= 10:
    print(x)
    x += 2 # nota: el signo += agrega valores con base a lo que se pone despues de el mismo.

### Factorial ### 

factorial = 5
contador = factorial - 1
while contador > 0:
    factorial *= contador
    contador -= 1

print('El factorial de 5 es: ', factorial)


### Ciclo FOR ### # Nota: para cada valor en "X"


for i in 1, 2, 3 :
    print(i)

for i in range(5): # range cuenta desde el 0 como primer valor.
    print(i)

for i in ['Ale', 'Ivan', 'Monse', 'Luis', 'Rafa', 'Luca']:
    print(i)

for i in 'Hola Mundo':
    if i == 'M' :
        pass
    else:
        print(i, end=' ') # Nota: end='' agrega algo despues de cada ejecución, en este caso de print()
 

