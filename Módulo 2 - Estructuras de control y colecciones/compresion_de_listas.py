
### crear lista de cuadrados hasta el 9.

cuadrados = []

for numero in range(10):
    numero = numero **2
    cuadrados.append(numero)

print(cuadrados)
print(numero)

# lista compresa #

cubos = [cubo **3 for cubo in range(10)]
print(cubos)
# print(cubo) #Nota la variable cubo no esta definida ya que no se le ha asignado un espacio en memoria! WOW!!!



#######################################
# Crear un diccionario por medio de la compresión de listas.

cubos = {numero : numero **3 for numero in range(10)}
print(cubos) # WoW!!!!!!! 

### Lista con condicionales

pares = [numero for numero in range(1,11) if numero % 2 == 0]
impares = [numero for numero in range(1,11) if numero % 2 != 0]
print(pares)
print(impares)

#########################################

# Método para cambiar valores de una lista

nombres = ['ana', 'fernando', 'carlos', 'priscila']
print(nombres)
nombres = [nombre.capitalize() for nombre in nombres] # Tipo de lista compresa
print(nombres)



