# Probando ámbitos

titulo = 'probando ámbitos'
suma = 10.5

def sumar():
    suma = 2 + 2
    #titulo = titulo + ' mundo'
    print(titulo)
    print('Suma en ambito local', suma,id(suma))

print('Antes de llamar a la función')
print('Suma el ambito global', suma,id(suma))
sumar()
print('Suma el ambito global', suma,id(suma))