
import module_proyectoM3 as MP

numero_canicas = 3_000 #Número de canicas
niveles = 12 # Número de niveles
probabilidad_izquierda = -1.0 # Probabilidad de ir a la izquierda
probabilidad_derecha = 1.0 # Probabilidad de ir a la derecha


print(f'Con {numero_canicas} canicas y {niveles} niveles se procedera a graficar una simulación de la Máquina de Galton.')

MP.calcular_resultados(numero_canicas, niveles)

print('Fin del programa.')



