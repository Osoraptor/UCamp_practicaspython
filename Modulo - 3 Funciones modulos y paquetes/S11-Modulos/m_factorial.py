# Módulo m_factorial (m_factorial.py)

'''
Módulo que contiene la función recursiva del factorial.

'''

def factorial(num):
    '''
    Calcular el factorial de un número
    '''
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

    
    