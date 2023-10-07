### Encuentrar el cuadrante ###


while True:

    X = input('Ingrese el valor de X como línea horizontal: ')
    X_validacion = X.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9'))

    X_valid2 = [palabra for palabra in X if palabra.isalpha() == True]

    if X_valid2[:1] == []:
        if X_validacion == True:
            break
    elif X_valid2[0].isalpha() == True:
        print('El dato ingresado debe ser númerico y no igual a 0.')
    else:
        print('Intente nuevamente.')

while True:

    Y = input('Ingrese el valor de Y como línea vertical: ')
    Y_validacion = Y.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9'))

    if Y_validacion == True:
        #print(f'El valor de Y es: {Y}') # print validacion de Y
        break
    else:
        print('El dato ingresado debe ser númerico y no igual a 0')

X = int(X)
Y = int(Y)

print(f'El valor de X es: {X}')
print(f'El valor de Y es: {Y}')


if X > 0 and Y > 0:
    print('El punto se encuentra en el cuadrante I.')
if X < 0 and Y > 0:
    print('El punto se encuentra en el cuadrante II.')
if X < 0 and Y < 0:
    print('El punto se encuentra en el cuadrante III.')
if X > 0 and Y < 0:
    print('El punto se encuentra en el cuadrante IV.')