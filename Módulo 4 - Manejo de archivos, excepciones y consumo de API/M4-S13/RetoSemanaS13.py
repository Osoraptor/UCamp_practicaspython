### 

# menú con las siguientes opciones:
    # ● Agregar un nuevo alumno (1).
    # ● Ver los alumnos y las calificaciones (2).
    # ● Salir (S).
#corroborar que el nombre del alumno no esté en blanco
#Preguntar cuántas calificaciones se quiere agregar
#Después de agregar la información de un alumno, volver al menú principal.
#Si se selecciona la opción 2, mostrar en la pantalla la información de cada alumno y el promedio de sus calificaciones. 
    #Ejemplo: “Laura Ramírez: Promedio 9.5


print('Programa Calificaciones Alumnos.', '\n')

def agregar_alumno():
    '''
    Esta funcion registra a un alumnos y el número de calificaciones deseadas.
    Se hacen validaciones del nombre.
        - Tanto que no contenga números por medio de isdigit(), como que este tampoco venga vacio.
    Se hace un for loop por el número de calificaciones espeficiado anteriormente.
    Se hace un append a una lista de calificaciones por cada calificación registrada dentro del loop.
    Posteriormente se manda a llamar otra función para calcular el promedio.
    Se hace un append tanto del nombre del alumno al inicio de la lista como su promedio al final de la misma.
    Por último, se hace un append de la información del alumno en la lista de alumnos del programa.

    '''  

    while True:

        nombre_alumno = input('Ingrese el nombre del alumno: ').capitalize()
        
        nombre_digit_valid = any(chr.isdigit() for chr in nombre_alumno)
 
        #print(nombre_digit_valid) # Validación si contiene números el string.

        if nombre_alumno == '':
            print('El valor no puede estar vacio.')
        elif nombre_digit_valid is True:
            print('El nombre no puede contener números')     
        else:
            break
    
    while True:
        try:
            calificaciones_num = int(input(f'¿Cuántas calificaciones quiere agregar para {nombre_alumno}? (el valor máximo es 5) '))
            int(calificaciones_num)
            if calificaciones_num <= 5:
                break
        except ValueError:
            print('Debes introducir un número.')
        
    calificaciones_alumno = []
    
    for calificacion in range(calificaciones_num):
        
        while True:
            try:
                calificacion = int(input(f'Ingrese la calificación #{calificacion + 1} de {nombre_alumno}: '))
                int(calificacion)
                if calificacion > 10:
                    print('La calificación no puede ser mayor a 10')
                if calificacion < 0:
                    print('La calificación no puede ser menor a 0')
                elif calificacion <= 10:
                    break
            except ValueError:
                print('Debes introducir un número.')



        
        
        calificaciones_alumno.append(calificacion)
    
    print(calificaciones_alumno)

    promedio(nombre_alumno, calificaciones_alumno)

    calificaciones_alumno.insert(0, nombre_alumno) 
    print(f'Las calificaciones de {nombre_alumno} son: ', calificaciones_alumno) #Validación alumnos    
    lista_alumnos.append(calificaciones_alumno)
    menu_inicio()


def promedio(nombre, list_calif):
    '''
    Función que calcula el promedio de un alumno.
    Recibe como parametros el nombre y la lista de sus calificaciones.
    Al final de la función se hace una cocatenación para poder hacer un append del promedio junto con un mensaje string.
    '''
    #print(list_calif) # Nota: Validación de lista obtenida
    promedio = round((sum(list_calif)) / len(list_calif),2)
    print(f'El promedio de {nombre} es: {promedio}')
    promedio_str = 'Promedio: ' + str(promedio)
    #print(promedio_str) #Nota: Validación de cocatenación para el promedio.
    list_calif.append(promedio_str)
        

    



def menu_inicio():
    '''
    Esta función tiene como finalidad ser el menú de opciones del programa.
    Este menú cuenta con las siguientes opciones:
        ● Agregar un nuevo alumno (1). Por medio de la función def agregar_alumno().
        ● Ver los alumnos y las calificaciones (2). Aquí se hace un print de la lista de alumnos del programa.
        ● Salir (S). Se sale del programa y se termina la ejecución del mismo.
    '''
    while True:


        menu = input('''Menu: 
            ● Agregar un nuevo alumno (1). 
            ● Ver los alumnos y las calificaciones (2).
            ● Salir (S).

    Opción: ''')

        # print(menu) # Validación contenido
        # print(type(menu)) # Validación typo de contenido

        if menu == '':
            print('El valor no puede estar vacio.', '\n')
        elif menu == '1':
            break
        elif menu == '2':
            break
        elif menu == 's' or menu == 'S':
            break
        else:
            print('Opción invalida. Intente nuevamente', '\n')

    if menu == '1':
        agregar_alumno()
    elif menu == '2':
        print(lista_alumnos)
        menu_inicio()
    elif menu == 's' or menu == 'S':
        print('Fin del programa.', '\n', 'Bye!')
        exit


lista_alumnos = []
numero_alumnos = 0

limite_calificaciones_ciclo = 5
limite_alumnos_beta = 5


print('A continuación le presentamos las opciones del programa: ', '\n')
menu_inicio()












