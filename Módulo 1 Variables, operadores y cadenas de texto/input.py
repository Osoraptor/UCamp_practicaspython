nombre = input('¿Cómo te llamas? ')
print('Hola ' + nombre)

edad = input('¿Cuantos años tienes? ')
print(type(edad))
print(f'{nombre} tiene {edad} años')

# Programa que pide 2 numeros al usuario y los suma / aquí usamos el cast para poder sumar con intergers

numero1 = int(input('Introduce un número por favor: '))
numero2 = int(input('Introduce otro número por favor: '))
numero3 = numero1 + numero2

print(f'El resultado de la suma es {numero3}')
