# Volers Aleatorios con la funcion es randint

# import random/ Una de las formas para importar el modulo Random tambien hay que anexar las especificaciones de la funcion

from random import randint

#Generar un numero aleatorio entre 1 y 10
numero = randint(1,10)
print(f'Numero aleatorio entre 1 y 10: {numero}')

# Simular Un dado de 6 caras
dado = randint(1,6)
print(f'El valor aleatorio del Dado: {dado}')

