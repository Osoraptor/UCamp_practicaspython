
personas = []

while True:
    print('''
    1. Agregar persona a la agenda.
    2. Guardar datos en un archivo.
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

        personas.append(contacto)

    elif opcion == '2':
        with open('agenda.txt', 'w') as f_agenda:
            for persona in personas:
                f_agenda.write(f'# {personas.index(persona)}: {persona[0]} {persona[1]}. Edad: {persona[2]}. Correo: {persona[3]}. Telefono: {persona[4]}.\n')
            print('Datos guardados en agenda.txt.')
            break
    
    else:
        print('Opción no valida.')
        print('Volver a intentar.')





