



def agreagar_datos(lista, valor):
    '''
    Función que agrega un dato a una lista especificada.
    '''
    if valor == '':
        valor = 'No especificado.'  
    lista.append(valor)
    return lista


nombres = []
edades = []
sexos = []

personas = int(input('Cuantas personas se quiere registrar? '))

for persona in range(personas):
    nombre = input(f'Ingrese el nombre de la persona {persona+1}: ').title()
    nombres = agreagar_datos(nombres, nombre)

for persona in range(personas):
    edad = input(f'Ingrese la edad de {nombres[persona]}: ')
    edades = agreagar_datos(edades, edad)

for persona in range(personas):
    sexo = input(f'¿Cual es el sexo de {nombres[persona]}? ')
    sexos = agreagar_datos(sexos, sexo)

for persona in zip(nombres, edades, sexos):
    print(persona)

