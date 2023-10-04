
lista = []

alumnos = 0
#calificaciones = 0

total_alumnos = int(input('¿Cuantos alumnos tiene en total? ')) 

while alumnos <= total_alumnos - 1: # Se agrega el -1 para salir del 0 al inicio.
    opcion = input('Agregar alumno (1) o terminar (2): ')
    if opcion == '1':
        
        nombre = input('Ingrese el nombre del alumno: ').capitalize() # El método capitalize pone en mayuscula la primera letra.
        
        calificaciones = 0

        while calificaciones <= 3:
            # opcionC = input('Agregar calificacio (1) o terminar (2): ')

            if calificaciones == 0: 
                calificacion1 = int(input(f'Ingrese la primera calificación de {nombre}: '))

                #calificaciones += 1
            
            elif calificaciones == 1:
                opcionC = input('Agregar segunda calificación (1) o terminar (2): ')

                if opcionC == '1':
                    calificacion2 = int(input(f'Ingrese la segunda calificación de {nombre}: '))

                    #calificaciones += 1
                
                elif opcionC == '2':
                    print('Solo se ingreso una calificación.')

                    calificacion2 = 0
                    calificacion3 = 0

                    break
                else:
                    print('Se ha ingresado una opción invalida.')
                    continue

            elif calificaciones == 2:
                opcionC2 = input('Agregar tercera calificación (1) o terminar (2): ')

                if opcionC2 == '1':
                    calificacion3 = int(input(f'Ingrese la tercera calificación de {nombre}: '))

                    #calificaciones += 1
                
                elif opcionC2 == '2':
                    print('Solo se ingreso dos calificaciones.')

                    
                    calificacion3 = 0

                    break
                else:
                    print('Se ha ingresado una opción invalida.')
                    continue



                
            calificaciones += 1
        
        #int((calificacion1 + calificacion2 + calificacion3)) / 3
        
        promedio = 0

        if calificacion2 == 0:
            promedio += calificacion1
        elif calificacion3 == 0:
            promedio += int((calificacion1 + calificacion2)) / 2
        else:
            promedio += int((calificacion1 + calificacion2 + calificacion3)) / 3

        pf = 'Promedio: ' + str(promedio)

        alumno = [nombre, calificacion1, calificacion2, calificacion3, pf]
        lista.append(alumno)
        

        alumnos += 1
    elif opcion == '2':
        print(f'El programa ha terminado con {alumnos} alumnos.')
        break
    else:
        print('Se ha ingresado una opción invalida.')
        continue

print('La lista de alumnos es: ')
print(lista)