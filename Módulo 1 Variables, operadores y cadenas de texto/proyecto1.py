print('Hola! Vamos a conocer cual es tú indice de masa corporal según el ISSSTE.\n')


while True:
    
    nombre = input('¿Cual es tu primer nombre? ')
    nombre_validacion_Digito = nombre.isalpha()
    
    if not nombre:
        print("El valor se mando vacio. Por favor vuelva a intentar.")

    elif nombre == ' ':
        print('El dato debe empezar con una letra.')  
    
    elif nombre_validacion_Digito == True:
        break
    else:
        print('Por favor solo ingrese letras. Vuelva a ingresar sus datos.')


while True:
    
    apellidoP = input('¿Cual es tu apellido paterno? ')
    apellidoP_validacion_Alpha = apellidoP.isalpha()
    
    if not apellidoP:
        print("El valor se mando vacio. Por favor vuelva a intentar.")

    elif apellidoP == ' ':
        print('El dato debe empezar con una letra.')  
    
    elif apellidoP_validacion_Alpha == True:
        break
    else:
        print('Por favor solo ingrese letras. Vuelva a ingresar sus datos.')


while True:
    
    apellidoM = input('¿Cual es tu apellido materno? ')
    apellidoM_validacion_Alpha = apellidoM.isalpha()
    
    if not apellidoM:
        print("El valor se mando vacio. Por favor vuelva a intentar.")

    elif apellidoM == ' ':
        print('El dato debe empezar con una letra.')  
    
    elif apellidoM_validacion_Alpha == True:
        break
    else:
        print('Por favor solo ingrese letras. Vuelva a ingresar sus datos.')


while True:
    
    edad = input('¿Cuantos años tienes? ')
    edad_validacion_Digit = edad.isnumeric()
    
    if not edad:
        print("El valor se mando vacio. Por favor vuelva a intentar.")

    elif edad == ' ':
        print('El dato debe ser númerico.')  
    
    elif edad_validacion_Digit == True:
        break
    else:
        print('Por favor solo ingrese números. Vuelva a ingresar sus datos.')

# edad = int(input('Introduce tu edad: '))

#print(type(edad)) # Validación de tipo de edad que sea string

### PESO Opción 1 ###

# while True:
    
#     peso = float(input('¿Cual es tu peso? (en kilos con decimales) '))
#     peso_validacion_Digit = isinstance(peso, float)
    
#     ValueError: print('error')

#     if not peso:
#         print("El valor se mando vacio. Por favor vuelva a intentar.")

#     elif peso == ' ':
#         print('El dato debe ser númerico.')  
    
#     elif peso_validacion_Digit == True:
#         break
#     else:
#         print('Por favor solo ingrese números. Vuelva a ingresar sus datos.')

### PESO Opción 2 ###


while True:
    
    try:
        peso = float(input('¿Cual es tu peso? (en kilos con decimales) '))
        peso_validacion_Digit = isinstance(peso, float)
    
        if peso_validacion_Digit == True:
            break
        
    except ValueError:
        print('El valor ingresado esta vacio o incorrecto. Por favor ingrese solo numeros.')


    else:
        print('Vuelva a intentar nuevamente.')


### Estatura ###

while True:
    
    try:
        estatura = float(input('¿Cual es tu estatura? (en metros con decimales) '))
        estatura_validacion_Digit = isinstance(peso, float)
    
        if estatura_validacion_Digit == True:
            break
        
    except ValueError:
        print('El valor ingresado esta vacio o incorrecto. Por favor ingrese solo numeros.')


    else:
        print('Vuelva a intentar nuevamente.')


print('\n')

print('Nombre: ' + nombre)
print('Apellido Paterno: ' + apellidoP)
print('Apellido Materno: ' + apellidoM)
print('Tienes: ' + str(edad) + ' años')
print('Peso: ' + str(peso) + ' kilos')
print('Estatura: ' + str(estatura) + ' metros')

#print(nombre_validacion_Digito)

print('\n')

imc = round(peso / (estatura ** 2), 2) # se redondea al segundo decimal.

if imc <= 19: # Nota: decidí dejarlo en 19 ya que se me hace raro los números del ISSSTE.
  print(f"Tu IMC es {imc}, tienes el peso bajo.")
elif imc <= 25:
  print(f"Tu IMC es {imc}, tienes el peso normal.")
elif imc <= 30:
  print(f"Tu IMC es {imc}, tienes sobrepeso.")
elif imc <= 35:
  print(f"Tu IMC es {imc}, tienes obesidad leve.")
elif imc <= 40:
  print(f"Tu IMC es {imc}, tienes obesidad media.")
else:
  print(f"Tu IMC es {imc}, tienes obesidad mórbida.")








# while nombre_validacion_Digito == True or nombre != "":
#     nombre = input('Ingrese solo letras.')


# if nombre == '' or nombre_validacion_Digito == True:
#     nombre = print(input('Ingrese solo letras por favor'))




#print(nombre_validacion_Digito)
# print('1234567809' in nombre)
# print(x)
