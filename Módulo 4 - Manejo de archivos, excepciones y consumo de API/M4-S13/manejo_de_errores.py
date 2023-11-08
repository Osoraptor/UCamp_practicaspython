# numerador = 10
# denominador = 0
# cadena = '3'
# numerico = 5

#print(numerador / denominador) # Error 1
#print(cadena + numerico) # Error 2

# try :
#     print(numerador / denominador)
    
# except ZeroDivisionError: # Nota: Se puede usar una tupla para tener una lista de posibles errores.
#     print('Ha ocurrido una división entre 0.')


# try :
#     print(cadena + numerico)

# except TypeError: # Nota: Se puede usar una tupla para tener una lista de posibles errores.
#     print('Ha ocurrido un error de tipo.')

# print('Fin del programa.')


# Error 1 = ZeroDivisionError
# Error 2 = TypeError: can only concatenate str (not "int") to str


### Varios except en un solo TRY ###

# try:
#     print(10 / 0)
# except TypeError:
#     print('Ha ocurrido un error de tipo.')
# except:
#     print('Ha ocurrido un error desconocido.')


#####################################################

### Manejo de errores con excepciones y ciclos ###


while True: # Se usa while True para poder lograr el TRY y se seguira pidiendo la información hasta que se cumpla.
    
    try: 

        dividendo = int(input('Ingrese el dividendo: '))
        divisor = int(input('Ingrese el divisor: '))
        print('El resultado es: ', dividendo / divisor)
        break

    except ValueError:
        print('Debe ingresarse un número.')
    except ZeroDivisionError:
        print('No se puede dividir entre cero.')


print('Fin del programa.')

# Error ValueError: invalid literal for int()

