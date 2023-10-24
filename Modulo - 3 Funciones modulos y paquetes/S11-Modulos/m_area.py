### Módulo m_area (m_area.py)
'''
Módulo que contiene la función área
'''
def area(**dato):
    '''
    Recibe como parametro un diccionario con los datos de una figura.
    Calculo los datos de una figura.
    '''
    if dato['figura']=='Rectángulo':
        return (dato['base'] * dato['altura'])
    elif dato['figura']=='Triángulo':
        return (dato['base'] * dato['altura'] / 2)
    elif dato['figura']=='Circulo':
        return (3.141593 * dato['radio'] **2)
    else:
        print('Figura desconocida')