
def sumar(parametro1, parametro2):
    '''Funcion que suma 2 parametros y los imprime en pantalla'''
    print('Suma:', parametro1 + parametro2)

argumento1 = 5
argumento2 = 7

# Invocando a la función por medio de parametros variables
sumar(argumento1, argumento2)

# Invocando a la función por medio de parametros de valor

sumar('mundo!', 'Hola ')
sumar('Hola ', 'mundo!')

# sumar('hola!') # Nota: Aquí da error ya que la función se definió con 2 parametros.

####################################

### Parametros opcionales ###

def muestra_alumno(nombre, edad = 18, sexo = 'F'):

    '''
    Es una funcion que muestra en pantalla el nombre, la edad y el sexo de un alumno.
    Recibe 3 parametros.
    1.- Nombre
    2. Edad = 18
    3. Sexo 0 'F'
    '''

    print(f'Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}' )

# Ejecución de función con parametro obligatorio
muestra_alumno('Maria')

# Ejecución de función con parametro obligatorio y uno opcional
muestra_alumno('Maria', 22)

# Ejecución de función con el primer y el último
muestra_alumno('Juan', sexo = 'M')