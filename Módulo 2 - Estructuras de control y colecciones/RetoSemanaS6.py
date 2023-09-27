


for i in range (3, 0, -1):
    
    pwd1 = input('Ingrese una contraseña: ')
    pwd1_valid = pwd1.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))

    if pwd1_valid == True:
        

        for i in range (3, 0, -1):
            pwd2 = input('Ingrese la contraseña nuevamente: ')
            #pwd2_valid = pwd2.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))

            if pwd1 == pwd2:
                break
            else:
                print('Las contraseñas no coinciden.')
        if i == 1:
            break

    else:
        print('La contraseña debe comenzar con un número.')

if i == 1:
    print('Intentos agotados. Fin del programa')

else:
    print('Contraseña correcta!')
    print('Fin del programa.')



    # pwd2 = input('Ingrese la contraseña nuevamente: ')
    # pwd2_valid = pwd2.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))


    




### WHILE LOOP ###

# while True:

#     pwd1 = input('Ingrese una contraseña: ')
#     pwd1_valid = pwd1.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
    
#     if not pwd1:
#         print("El valor se mando vacio. Por favor vuelva a intentar.")

#     elif pwd1_valid == True:
        
#        while True:

#          pwd2 = input('Ingrese la contraseña nuevamente: ')
#          pwd2_valid = pwd1.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))  

#          if not pwd1:
#             print("El valor se mando vacio. Por favor vuelva a intentar.")

#          elif pwd1 == pwd2:
#             print('Contraseña correcta')
#             print('Fin del programa')
#             break


#     else:
#         print('La contraseña debe comenzar con un número.')
    
    
    
#     print(pwd1_valid)