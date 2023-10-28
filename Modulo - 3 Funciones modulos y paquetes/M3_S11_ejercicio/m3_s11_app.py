import m_alumnos as M3

numero_alumnos = input('Cuantos alumnos desea registrar?')

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    M3.captura_alumnos(numero_alumnos)

else:
    M3.captura_alumnos()