

### Validaciones ###

# while True:

#     numero_listas = input('¿Cuantas listas se van a crear? ')

#     if numero_listas.isdigit():
#         numero_listas = int(numero_listas)
#         if numero_listas == 0:
#             print('El valor no puede ser 0. Intente nuevamente por favor')
#         elif numero_listas <= 5:
#             break
#         else:       
#             print('El limite máximo es 5. Intente nuevamente por favor.')


#     else:
#         print('Opción invalida. Ingrese un número por favor.')
        

# while True:

#     elementos_listas = input('¿Cuantos elementos tendrán las listas? ')

#     if elementos_listas.isdigit():
#         elementos_listas = int(elementos_listas)
#         if elementos_listas == 0:
#             print('El valor no puede ser 0. Intente nuevamente por favor')
#         elif elementos_listas <= 5:
#             break
#         else:       
#             print('El limite máximo es 5. Intente nuevamente por favor.')


#     else:
#         print('Opción invalida. Ingrese un número por favor.')


# print(f'Número de listas: {numero_listas}.')
# print(f'Número de elementos por lista: {elementos_listas}.')


### Recorrido FOR ###

# lista_elementos = []
# lista_de_listas = []


# numero = 2
# elemento = 2

# vueltas = 1

# while vueltas <= numero:
    
#     for elementoX in range(elemento):
#         elementoB = input(f'Para la lista {vueltas}, Ingrese el elemento {elementoX+1}: ').title()
#         lista_elementos.append(elementoB)
#     print(f'Elementos de la lista {vueltas}: ',lista_elementos)
#     lista_elementos.insert(0, f'Lista {vueltas}') # Se inserta al inicio de la lista la lista en cuestion (la lista y su número como string).
#     lista_de_listas.append(lista_elementos) # Se hace un append de esta lista a la lista maestra.
#     lista_elementos = [] # Se borra la lista o un clear de la lista para poder volver a usarla.
#     vueltas += 1


# print(f'Las listas son: ', lista_de_listas)


### Ubicar listas ###

lista_test = [['Lista 1', 'Rojo', 'Sapo', 'Avion'], ['Lista 2', 'Rojo', 'Carro', 'Sope']]

print(lista_test[1][1]) # Agarrar la lista que se va a usar para borrar duplicados

print(type(lista_test[1][1]))

#lista_referencia = int(input('¿Que lista quiere usar como referencia? '))
# print(f'Las lista que seleccionada es la: {lista_test[lista_referencia - 1][0]}')
# print('Los elementos de esta lista se tomarán en cuenta para borrarlos de otras listas \
# si estos se encuentran en las otras listas (duplicados).')



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

print(f'Las lista que seleccionada es la: {lista_test[lista_referencia - 1][0]}')
print('Los elementos de esta lista se tomarán en cuenta para borrarlos de otras listas \
si estos se encuentran en las otras listas (duplicados).')

# for duplicado in lista_test[lista_referencia - 1]:
#     #print(duplicado)
#     if duplicado in lista_test:
#         print(duplicado)
#         # if duplicado in lista_test[lista_referencia - 1]:
#         #     continue
#         # else:
#         #     print(lista_test)

deduplicated_list = [['Lista 1', 'Rojo', 'Sapo', 'Avion'], ['Lista 2', 'Rojo', 'Carro', 'Sope']]
elementos_borrar = []

for item in lista_test[lista_referencia - 1]:
    elementos_borrar.append(item)

print(elementos_borrar)
print(elementos_borrar[1])

eduplicados = 3
vueltas = 0


while vueltas <= eduplicados:


    for duplicado in deduplicated_list:

        if vueltas > eduplicados:
            break

        try:
            duplicado_index = duplicado.index(elementos_borrar[vueltas])
            print(elementos_borrar[vueltas])
            #vueltas += 1
            
        except ValueError:
            pass
        else:
            del duplicado[duplicado_index]
    
    vueltas += 1




print(deduplicated_list)
print(f'Se borraron todos los duplicados y elementos de la lista {lista_test[lista_referencia - 1]}')

deduplicated_list[0].extend(elementos_borrar)
print(deduplicated_list)




