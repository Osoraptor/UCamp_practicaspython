### <<m_alumnos.py>>

'''
Este módulo contiene la función captura que solicita la información de los
alumnos y la función promedio que calcula el promedio de cada alumno.
'''

def promedio(nombre, calificacion1, calificacion2):
    '''
    Función que calcula el promedio de un alumno y lo despliega por medio de un mensaje.
    Recibe como parametros el nombre y 2 calificaciones del alumno.
    '''
    promedio = (calificacion1 + calificacion2) / 2
    print(f'El promedio de {nombre} es: {promedio}')


def captura_alumnos(numero = 3):
    '''
    Una funcion que registra alumnos y 2 calificaciones.
    Recibe como parametro la cantidad de alumnos a registrar.
    Si no se especifica el número de alumnos, se registrarán 3.
    '''
    lista_alumnos = []
    for i in range(numero):
        nombre = input(f'{i + 1}.- Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificación de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificación de {nombre}: '))
        lista_alumnos.append([nombre, calificacion1, calificacion2])
        promedio(nombre, calificacion1, calificacion2)
    print(f'Las calificaiones de los alumnos son: ', lista_alumnos)




numero_alumnos = input('¿Cuantos alumnos desea registrar? ')

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else: 
    captura_alumnos()