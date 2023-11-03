
import matplotlib.pyplot as PLT

def diagrama_barras_calificaciones(notas, color, alumno):
    '''
    Dibujar la grafica de barras con las calificaciones.
    '''

    PLT.bar(notas.keys(), notas.values(), color=color)
    PLT.title('Calificaciones de: ' + alumno)

calificaciones = {
    'Programación': 9,
    'Español': 6.5,
    'Cálculo': 4,
    'Historia': 8,
    'Biologia': 10
}

alumno = input('Nombre del alumno: ')

diagrama_barras_calificaciones(calificaciones, 'green', alumno)

PLT.show()