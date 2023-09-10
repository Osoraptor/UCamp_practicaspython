print('Hola! Vamos a conocer cual es tú indice de masa corporal según el ISSSTE.\n')

### Nombre ###

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


### Apellido Paterno ###

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


### Apellido Materno ###

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


### Edad ###

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

### PESO ###


while True:
    
    try:
        peso = float(input('¿Cual es tu peso? (en kilos con decimales) '))
        peso_validacion_Digit = isinstance(peso, float)
    
        if peso_validacion_Digit == True:
            break
        
    except ValueError:
        print('El valor ingresado esta vacio o incorrecto. Por favor ingrese solo numeros con sus respectivos decimales.')


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


# Se imprime la información de la persona

print('\n')

print('Nombre: ' + nombre)
print('Apellido Paterno: ' + apellidoP)
print('Apellido Materno: ' + apellidoM)
print('Tienes: ' + str(edad) + ' años')
print('Peso: ' + str(peso) + ' kilos')
print('Estatura: ' + str(estatura) + ' metros')


# Calculo de IMC con la formula: (peso) ÷ (estatura al cuadrado) = IMC

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



### FIN ###