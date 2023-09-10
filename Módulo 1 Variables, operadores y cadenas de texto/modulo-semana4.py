
### Error de ejecución

numHuevos = 12

print('Tengo ' + numHuevos + ' huevos') # Error: can only concatenate str (not "int") to str

#Opcion 1

print('Tengo ' +str(numHuevos) + ' huevos')

#Option 2

print('Tengo %s huevos' %(numHuevos))


### Error de lógica ###

# calcular la superficieo área de un cuadrado

lado = int(input('Ingrese la medida del lado del cuadrado: '))
superficie = lado * lado #* lado # Aqui el issue es que el área de un cuadrado es lado por lado, no por 3 lados.
print('La superficie del cuadrado es: ' + str(superficie))


#### Ejercicio  ####

nombre = input('Introduce tu nombre: ')
apellido = input('Introduce tu apellido: ')
edad = int(input('Introduce tu edad: ')) # int transforma el input de cadena a entero
correo = input('Introduce tu correo electrónico: ')
telefono = input('Introduce tu telefono: ') # esto no se convierte en INT ya que el 0 se lo comería

print('Nombre: ' + nombre)
print('Apellido: ' + apellido)
print('Tengo: ' + str(edad) + 'años')
print('Correo: ' + correo)
print('Teléfono: ' + telefono)





