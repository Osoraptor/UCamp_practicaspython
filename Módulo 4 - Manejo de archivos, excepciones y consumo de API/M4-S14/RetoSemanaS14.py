# El programa te mostrará en la pantalla la información de los contactos guardados numerada.
# Preguntará de cuál de los contactos se desea modificar la información.
# Se podrá modificar el nombre, el teléfono y el correo. 
# Se debe actualizar la información en el archivo.
# El programa no debe interrumpirse al ingresar mal los datos o las opciones.





def modificar_registro(ID):
    print(ID) 
    print(personas[ID])

        # with open('agenda.txt', 'w') as f_archivo: # se sobrescribe el archivo.
        #     f_archivo.writelines(personas)

    '''
    Esta función tiene como finalidad modificar atributos de una persona.
    Este menú cuenta con las siguientes opciones:
        ● Modificar Nombre (1).
        ● Modificar Telefono (2).
        ● Modificar Correo. (3).
        ● Regresar al menu principal (M).
    '''
    while True:


        print('''
        
        ¿Qué información desea modificar?
        
        1. Modificar Nombre.
        2. Modificar Telefono.
        3. Modificar Correo.
        M. Regresar al menu principal.
        ''')
        
        menu_cambios = input('Ingrese una opción. ')

        # print(menu) # Validación contenido
        # print(type(menu)) # Validación typo de contenido

        if menu_cambios == '':
            print('El valor no puede estar vacio.', '\n')
        elif menu_cambios == '1':
            break
        elif menu_cambios == '2':
            break
        elif menu_cambios == '3':
            break
        elif menu_cambios == 'm' or menu_cambios == 'M':
            break
        else:
            print('Opción invalida. Intente nuevamente', '\n')

    if menu_cambios == '1':
        print()
    elif menu_cambios == '2':
        print()
    elif menu_cambios == '3':
        print()
    elif menu_cambios == 'm' or menu_cambios == 'M':
        menu_inicio()

#####################################################

def menu_inicio():

    contactos = 0

    while True:
        print('''
        1. Agregar persona a la agenda.
        2. Guardar datos en el archivo.
        3. Ver registros en el archivo.
        4. Modificar registros.
        7. Salir.
        ''')
        opcion = input('Ingrese una opción. ')

        if opcion == '1':

            contacto = []

            while True:
                nombre = input('Introduce tu nombre: ').upper()
                apellido = input('Introduce tu apellido: ').upper()
                if nombre == '':
                    print('No has introducido tu nombre.')
                elif apellido == '':
                    print('No has introducido tu apellido.')
                else:
                    contacto.append(nombre)
                    contacto.append(apellido)
                    break

            while True:
                try:
                    edad = int(input('Introduce tu edad: '))
                    contacto.append(edad)
                    break # en caso de que se introdusca un integer, se hace un break
                except ValueError:
                    print('Debes introducir un número.')


            correo = input('Introduce tu correo: ')
            contacto.append(correo)

            while True:
                try:
                    telefono = input('Introduce tu teléfono: ')
                    int(telefono)
                    contacto.append(telefono)
                    break
                except ValueError:
                    print('Debes introducir un número.')

            contactos += 1
            contacto.insert(0, ('ID: ' + str(contactos)))
            personas.append(contacto)

        elif opcion == '2':
            with open('agenda.txt', 'w') as f_agenda:
                for persona in personas:
                    f_agenda.write(f' {persona[0]}. Nombre: {persona[1]} {persona[2]}. Edad: {persona[3]}. Correo: {persona[4]}. Telefono: {persona[5]}.\n')
                print('Datos guardados en agenda.txt.')
                #break
        elif opcion == '3':
            
            with open('agenda.txt', 'r') as f_lectura: 
                contenido = f_lectura.read()
                print(f'''***
                \n{contenido}\n***
                ''')
            
            #print(personas)

        elif opcion == '4':
            
            print(personas) # Validación: Se revisa que hay en la lista de personas.



            if personas == []:
                print('\nAún no hay registros.\n')
                
            else: 
                
                while True:
                    try:
                        persona_ID = input(print('¿Que persona quiere modificar sus atributos?'))
                        int(persona_ID)
                        print(f'Ha seleccionado a la persona # ', persona_ID)
                    except ValueError:
                        print('Debes introducir un número.')
                
                
                
                
                
            # persona_ID = input(print('¿Que persona quiere modificar sus atributos?'))
            # print(f'Ha seleccionado a la persona # ', persona_ID)


        elif opcion == '7':
            print('Fin del programa.', '\n', 'Bye!')
            with open('agenda.txt', 'w') as f_archivo: # Se borran los contenidos del archivo.
              pass
            exit()
            
        else:
            print('Opción no valida.')
            print('Volver a intentar.')


personas = []


print('A continuación le presentamos las opciones del programa: ', '\n')
menu_inicio()




