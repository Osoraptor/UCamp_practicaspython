
for i in range(2, 100):
    primo = True
    for j in range(2, i):
        if i == j:
            break
        elif i % j == 0 : # Nota: El simbolo % es modulo y regresa el residuo de una división entera.
            primo = False
        else:
            continue
    
    if primo == True:
        print(i, end=' ')
