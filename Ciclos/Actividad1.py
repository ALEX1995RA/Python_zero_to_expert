# Suma los primeros 5 Numeros
print('*** Suma Acumulativa ***')
Maximo = 5
Minimo = 1
acomulador_suma = 0

while Minimo <= Maximo:
# Impresion de Valores a Gestionar

    acomulador_suma += Minimo
    Minimo += 1
    print(f'(acomulador_suma + Minimo)->{acomulador_suma} + {Minimo}')

    print(f' \nResultado suma Acomulativa: {acomulador_suma}')