entrada = input('Hola! Introduce tu edad: ')

edad = 0

if entrada.isnumeric(): # .isnumeric si la entrada es numerica, esto es un booleano, FALSE o TRUE
    edad = int(entrada)
else:
    print('Dato incorrecto. Debes introducir un número.')
    exit() # Nota: Se usa exit() para terminar la ejecución del programa.

if edad <= 0:
    print('WOOOOOWWWWW!! Que joven eres. Pero, lo siento, eso no es posible.') # Validacion: que no sea negativo
elif edad > 115:
    print('VAYA!!!! ¿Cómo le haces para vivir tanto? No te creo, mejor intenta de nuevo.') # Validacion que no sea mayor a 115 años
elif edad < 18:
    print('Eres menor de edad así que no puedes compra tu vaina!') # Validación que no sea menor de edad, en este caso menor a 18 años.
else:
    print('Eres mayor de edad. Aquí tienes tu bicho!')
