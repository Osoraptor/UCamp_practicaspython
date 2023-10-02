
### Programa de alumnos con listas y ciclos ###

lista = []

alumnos = 0

while alumnos <= 5:
    opcion = input('Agregar alumno (1) o terminar (2): ')
    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno: ').capitalize() # El método capitalize pone en mayuscula la primera letra.
        calificacion1 = int(input(f'Ingrese la primera calificación de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificación de {nombre}: '))
        alumno = [nombre, calificacion1, calificacion2]
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