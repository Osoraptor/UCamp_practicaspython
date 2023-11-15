
# f_archivo = open('archivo1.txt', 'w') # 'w' = (write) significa que es modo de escritura o sobrescritura
# print(f_archivo)
# f_archivo.write('Hola mundo!') # variable.write('xxxxx) permite escribir sobre el archivo
# f_archivo.close()

# f_archivo = open('archivo1.txt', 'w')
# f_archivo.write('Este es mi primer archivo.') # En este caso sobrescribe la información
# f_archivo.close()

# f_lectura = open('archivo1.txt', 'r') # la 'r' = (read) solo deja leer el archivo.
# print(f_lectura.read()) # aqui se imprime el contenido del archivo en modo lectura.
# f_lectura.close()

# print(f_archivo)
# print(f_lectura)

####################################################

### Sentencias with & as ###

# f_lectura = open('archivo1.txt', 'r')
# print(f_lectura.closed) # esto para ver si el archivo esta cerrado o no. Si es FALSE es que el archivo esta abierto.
# f_lectura.close()
# print(f_lectura.closed)

# with open('archivo1.txt', 'r') as f_lectura: # en el as: se usa el mismo nombre de la variable de uso del archivo.
#     print(f_lectura.closed) # mientras se este en el bloque del with el archivo esta "abierto". Al salir del bloque se cierra automaticamente.
# print(f_lectura.closed)

# with open('archivo1.txt', 'a') as f_archivo: # la 'a' = (append / agregar) sirve para agregar datos al archivo.
#     f_archivo.write('\nEste es mi primer archivo 2.')
#     f_archivo.write('Este es mi primer archivo 3.')
#     f_archivo.write('\n')
#     f_archivo.write('\tEste es mi primer archivo 4.')

# with open('archivo1.txt', 'r') as f_lectura: # al final de la sentencia del with se define el nombre de la variable que se va a usar para trabajar con el archivo.
#     contenido = f_lectura.read()
#     print(f'****{contenido}****')
#     contenido = f_lectura.read() # en este caso ya se leyó el archivo y esta en su final del mismo. Por eso la lectura esta vacia ya que esta en el final del archivo.
#     print(f'****{contenido}****')


###########################################

### Lectura de archivo línea a línea ###

# with open('archivo1.txt', 'r') as f_lectura:

#     numero_de_lineas = 0
#     for linea in f_lectura:
#         numero_de_lineas += 1
#         print(f'Línea {numero_de_lineas}: {linea}')
#     print(f'El archivo tiene {numero_de_lineas} líneas.')



# Creando una lista a partir de un archivo

with open('archivo1.txt', 'r') as f_archivo:
    lista_archivo = f_archivo.readlines() # el método readlines asigna a una lista cada elemento de un archivo.
    print(lista_archivo)

#print(lista_archivo)

lista_archivo[1] = 'Este es mi primer archivo 2.\n'
lista_archivo.insert(2, 'Este es mi primer archivo 3.\n')
print(lista_archivo)

with open('archivo1.txt', 'w') as f_archivo: # se sobrescribe el archivo.
    f_archivo.writelines(lista_archivo) # writelines escribe los elementos de una lista en un archivo.


