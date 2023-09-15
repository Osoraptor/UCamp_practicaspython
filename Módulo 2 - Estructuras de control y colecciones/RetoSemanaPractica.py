agno = input('Hola! Introduce el año actual: ')

if agno.isnumeric(): #validación numerica
    agno = int(agno)
else:
    print('Dato incorrecto. Debes introducir un número.')
    exit()

if agno != 2023: # Validación del año actual.
    
    print('Dato incorrecto. Ese no es el año actual.')
    exit()

# else:
#     print(agno)

agno2 = input('Introduce otro año para calcular: ')

if agno2.isnumeric(): #validación numerica
    agno2 = int(agno2)
else:
    print('Dato incorrecto. Debes introducir un número.')
    exit()



if agno == agno2:
    print('Has introducido el mismo año que el actual.')
    exit()
elif agno2 == agno + 1:    
    print('Para llegar al ' + str((agno + 1)) + ' hace falta 1 año.')
    exit()
elif agno2 == agno - 1:
    print('Desde el año ' + str(agno2) + ' ha pasado 1 año.')
    exit()
elif agno > agno2:
    print('Han pasado ' + str((agno - agno2)) + ' desde el año que has introducido.')
    exit()
else:
    print('Faltan ' + str((agno2 - agno)) + ' años para llegar al año que has introducido.')
    exit()

# print(agno2)