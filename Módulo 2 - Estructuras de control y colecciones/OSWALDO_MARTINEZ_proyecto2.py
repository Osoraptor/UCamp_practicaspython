### Encuentrar el cuadrante ###

# EJE X
while True:

    X = input('Ingrese el valor de X como línea horizontal: ')
    X_validacion = X.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9'))

    X_valid2 = [palabra for palabra in X if palabra.isalpha() == True] # Aquí se valida si hay letras dentro del input. Se usa Comprensión de listas.

    if X_valid2[:1] == []:
        if X_validacion == True: # En esta validación se revisa que empiece con un número de la lista.
            break
    elif X_valid2[0].isalpha() == True:
        print('El dato ingresado debe ser númerico y no igual a 0.')
    else:
        print('Intente nuevamente.')

# EJE Y
while True:

    Y = input('Ingrese el valor de Y como línea vertical: ')
    Y_validacion = Y.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9'))

    Y_valid2 = [palabra for palabra in Y if palabra.isalpha() == True] # Aquí se valida si hay letras dentro del input. Se usa Comprensión de listas.

    if Y_valid2[:1] == []:
        if Y_validacion == True: # En esta validación se revisa que empiece con un número de la lista.
            break
    elif Y_valid2[0].isalpha() == True:
        print('El dato ingresado debe ser númerico y no igual a 0.')
    else:
        print('Intente nuevamente.')

# Nota: convertir variables en enteros para validación de cuadrantes.
X = int(X)
Y = int(Y)

# Se imprime los valores de ambos ejes.
print(f'El valor de X es: {X}')
print(f'El valor de Y es: {Y}')

#Se determina en que cuadrante queda.
if X > 0 and Y > 0:
    print('El punto se encuentra en el cuadrante I.')
if X < 0 and Y > 0:
    print('El punto se encuentra en el cuadrante II.')
if X < 0 and Y < 0:
    print('El punto se encuentra en el cuadrante III.')
if X > 0 and Y < 0:
    print('El punto se encuentra en el cuadrante IV.')