# Utilizar al menos 2 funciones
# Preguntar cuantos alumnos se registrarán en caso de no ingresar una cantidad, se asume que se registrarán 3 alumnos
# Preguntará el nombre y 2 calificaciones
# Mostrar el nombre en pantalla en mayuscula y promedio
# Al finalizar el programa mostrará una lista con el nombre de cada alumno y sus calificaciones

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

def promedio(nombre, calificacion1, calificacion2):
    '''
    Función que calcula el promedio de un alumno y lo despliega por medio de un mensaje.
    Recibe como parametros el nombre y 2 calificaciones del alumno.
    '''
    promedio = (calificacion1 + calificacion2) / 2
    print(f'El promedio de {nombre} es: {promedio}')


numero_alumnos = input('¿Cuantos alumnos desea registrar? ')

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else: 
    captura_alumnos()