import random

def tiro_dado(num_tiros):
    for dado in range(num_tiros) :
        print('El dado ' + str(dado + 1) + ' dió: ' + str(random.randint(1, 6)))


tiro_dado(5)

print('El dado dio: ' + str(random.randint(1, 6))) #randint requiere 2 valores, el primero es el numero inferior y el segundo el superior (limite)

test = [-1.0, 1.0]


#test = random.randint(-1.0, 1.0)
print(random.choice(test))
