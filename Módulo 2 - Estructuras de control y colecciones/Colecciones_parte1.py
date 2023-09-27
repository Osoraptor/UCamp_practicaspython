
### Listas ###

mix = [0, 1.0, 'dos', 3 + 4j]

for i in mix:
    print(f'{i:6} - Tipo: {type(i)}')

print(len(mix))

sin_dos = mix[:2] + mix[3:]
print(mix, sin_dos)

duplicado = mix * 3
print(duplicado)

### otras operaciones de listas ###

cuadrados = [0, 1, 4, 9, 16, 25]
for i in range(len(cuadrados)):
    
    print(f'{i}**2 = {cuadrados[i]}')
    print([cuadrados[i]])
    cuadrados[i] = cuadrados[i] * i
    print(f'Ahora están al cubo {cuadrados[i]}')
    
cuadrados.append(7 ** 3)

cuadrados.insert(6, 6 ** 3) # el primer digito señala a que lugar se inserta el dato, empenzado con el 0

cuadrados.extend([27, 1000, -1]) # se agraga una lista al FINAL de otra lista

cuadrados.extend(range(-1, -4, -1)) # se agragan datos al final del rango (esta en negativo)

del cuadrados[9:] # se borran datos desde el índice 9 empezando desde el 0

cuadrados.remove(27) # se remueve el primer valor al cual encuentra la primera coincidencia

valor_removido = cuadrados.pop(2) # remueve el valor por indice

print(valor_removido)
print(cuadrados)

cuadrados.clear() # la lista se limpia o queda vacia
print(cuadrados)


### Pueden contener varios tipos de datos
### Se puede usar el metodo (len) para saber la cantidad de elementos

