### continue & break ###

# Uso de la setencia continue en un ciclo for.

for numero in range(1, 11): # Entre el 1 y el 10. En range se le resta 1 al numero de alcance.
    if numero % 2 == 1:
        continue
    print(f'{numero} es un numero par.')


# Uso de la sentencia continue en un ciclo while

numero = 0

while numero < 11:
    numero += 1
    if numero % 2 == 0:
        continue
    print(f'{numero} es un numero inpar.')

# Nota aquí si se pudo terminar un ciclo WHILE con una condicional de numeros, en este caso hasta el 10.

################################

# Uso de la sentencia break #

# Programa adivinar el numero de un input y mostrar cuantos intentos #

numero = int(input('Ingrese un digito: '))
limite_inferior = 0
limite_superior = 10
buscado = 5
intentos = 0

while True:
    intentos += 1
    if numero == buscado:
        print(f'El numero {numero} fue encontrado en {intentos} intentos.')
        break
    elif numero < buscado:
        limite_superior = buscado
        buscado = (buscado + limite_inferior) // 2 #Nota division de piso devuelve el máximo numero de enteros divididos por enteros.
    else:
        limite_inferior = buscado
        buscado = (buscado + limite_superior) // 2

print('Fin del programa.')

##############################

# uso de la función exit() #

numero = int(input('Ingrese un digito: '))
limite_inferior = 0
limite_superior = 10
buscado = 5
intentos = 0

while True:
    intentos += 1
    if numero == buscado:
        print(f'El numero {numero} fue encontrado en {intentos} intentos.')
        exit()
    elif numero < buscado:
        limite_superior = buscado
        buscado = (buscado + limite_inferior) // 2 #Nota division de piso devuelve el máximo numero de enteros divididos por enteros.
    else:
        limite_inferior = buscado
        buscado = (buscado + limite_superior) // 2

print('Fin del programa.')
print('Impresión después del uso de la sentencia break.')
print('Impresión después del uso de la función exit().')

# # Nota: La función exit() cierra el programa por completo.

intentos = 0

while True:
    intentos += 1
    print(f'Inteno {intentos}')
    if intentos == 20:
        print('Fin del programa')
        exit()

print('Impresión después del uso de la función exit().')