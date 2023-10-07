
# X = '-5aAc'
# Y = '-5'
# Z = 'ext'

# print(X.islower())
# print(X.isupper())
# print(Y.islower())
# print(Z.islower() or Z.isupper())

# X = X.lower
# print(X)

# if X.islower() == True:
#     print('El dato ingresado debe ser númerico y no igual a 0')


#print(x.isalpha())


# while True:

#     X = input('Ingrese algo: ')
#     X_validacion = X.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9'))
    
#     for palabra in X:
#         if palabra.isalpha() == True:
#             print({palabra})
#             break
#     if X_validacion == True:
#         print('Done!')
#         break
#     else:
#         print('again')

# X = input('Ingrese algo: ')

# if palabra for palabra in X if palabra.isalpha() == True:
#     print(palabra)

X = input('Ingrese algo: ')

X_valid2 = [palabra for palabra in X if palabra.isalpha() == True]

print(X_valid2[:1])

if X_valid2[:1] == []:
    print('nada')
elif X_valid2[0].isalpha() == True:
    print('yeah')
else:
    print('done')

