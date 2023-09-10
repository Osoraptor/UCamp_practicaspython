print('Hola! Vamos a conocer cual es tú indice de masa corporal según el ISSSTE.\n')

# nombre = input('¿Cómo te llamas? ')
# nombre_validacion_Digito = nombre.isalnum()
# nombre_validacion_Letras = nombre.is
#x = '0123456789' in nombre

# x = input('Pon algo')
# print(type(x))




while True:
    
    nombre = input('¿Cual es tu nombre? ')
    nombre_validacion_Digito = nombre.isalnum()

    # if nombre_validacion_Digito == True:
    #     apellido = input('¿Cual es tu apellido? ')
    #     break
    
    # if not nombre or nombre_validacion_Digito == True:
    #     print("Yeah")
    #     break

    # else:
    #     print('Ingrese solo letras.')





    
    if not nombre:
        print("El valor esta vacio")

    elif nombre_validacion_Digito == False:
        #apellido = input('¿Cual es tu apellido? ')
        break
    else:
        print('Ingrese solo letras.')

print(nombre)

### PESO Option 1 ###

while True:
    
    peso = float(input('¿Cual es tu peso? (en kilos con decimales) '))
    peso_validacion_Digit = isinstance(peso, float)
    
    ValueError: print('error')

    if not peso:
        print("El valor se mando vacio. Por favor vuelva a intentar.")

    elif peso == ' ':
        print('El dato debe ser númerico.')  
    
    elif peso_validacion_Digit == True:
        break
    else:
        print('Por favor solo ingrese números. Vuelva a ingresar sus datos.')








# while nombre_validacion_Digito == True or nombre != "":
#     nombre = input('Ingrese solo letras.')


# if nombre == '' or nombre_validacion_Digito == True:
#     nombre = print(input('Ingrese solo letras por favor'))




#print(nombre_validacion_Digito)
# print('1234567809' in nombre)
# print(x)
