
#X_valid2 = [palabra for palabra in X if palabra.isalpha() == True]

lista1 = ['A', 'B', 'C']
lista2 = ['D', 'B', 'F']

listaX = []

# for elemento in lista2:
#     if elemento not in lista1:
#         listaX.append(elemento)



listaX = [
    listaX.append(elemento) for elemento in lista2 if elemento not in lista1
]

print(listaX)
