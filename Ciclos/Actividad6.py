from random import randint

print(' *** Juego de Adivinanza *** ')
Numero_Oculto = randint(1, 50)
Intento = 0
Adivinanza = None
Maximos = 5
while Adivinanza != Numero_Oculto and Intento < Maximos:
    Adivinanza = int(input('Adivina el Numero Oculto (1 a 50): '))
    if Adivinanza < Numero_Oculto:
        print('El numero Oculto es mayor ')
    elif Adivinanza > Numero_Oculto:
        print('El numero Oculto es menor')
    Intento += 1
if Adivinanza == Numero_Oculto:
    print(f'Felicidades acabas de encontrar el numero oculto en {Intento} intentos.... ')
else:
    print(f'Lo sentimos agotaste todos los intentos solo tienes {Maximos}')
    print(f'El numero Secreto es {Numero_Oculto} ')