### Reto Semana 10 ###

### Requisitos ###

### Se podrán crear varias listas; el usuario del programa especificará cuántas
### La longitud de cada lista la definirá el usuario (¿Cuantos elementos?)
### Imprimir las listas e indicar que son las originales.
### Se eliminarán los elementos de una lista que estén también en las listas posteriores.
### Imprimir las listas indicando que se eliminaron los elementos que estaban, también, en las listas posteriores.

import m_retosemanal as MR

### Validaciones ###

while True:

    numero_listas = input('¿Cuantas listas se van a crear? ')

    if numero_listas.isdigit():
        numero_listas = int(numero_listas)
        if numero_listas == 0:
            print('El valor no puede ser 0. Intente nuevamente por favor')
        elif numero_listas <= 5:
            break
        else:       
            print('El limite máximo es 5. Intente nuevamente por favor.')


    else:
        print('Opción invalida. Ingrese un número por favor.')
        

while True:

    elementos_listas = input('¿Cuantos elementos tendrán las listas? ')

    if elementos_listas.isdigit():
        elementos_listas = int(elementos_listas)
        if elementos_listas == 0:
            print('El valor no puede ser 0. Intente nuevamente por favor')
        elif elementos_listas <= 5:
            break
        else:       
            print('El limite máximo es 5. Intente nuevamente por favor.')


    else:
        print('Opción invalida. Ingrese un número por favor.')


print(f'Número de listas: {numero_listas}.')
print(f'Número de elementos por lista: {elementos_listas}.')
 

MR.agreagar_elements(numero_listas, elementos_listas)


### Lista de referencia para borrado de duplicados ###


while True:

    lista_referencia = input('¿Que lista quiere usar como referencia? ')

    if lista_referencia.isdigit():
        lista_referencia = int(lista_referencia)
        if lista_referencia == 0:
            print('El valor no puede ser 0. Intente nuevamente por favor')
        elif lista_referencia <= 5:
            break
        else:       
            print('El limite máximo es 5. Intente nuevamente por favor.')

    else:
        print('Opción invalida. Ingrese un número por favor.')


MR.remover_duplicados(lista_referencia, elementos_listas)

lista_super = []



    