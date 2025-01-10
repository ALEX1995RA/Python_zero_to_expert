print('*** Dibujando un Triangilo asimetrico *** ')
numero_filas = int(input('Proporcian la cantidad de filas: '))
for fila in range(1, numero_filas + 1):
    espacios = ' ' * (numero_filas - fila)
    asterisco = '*' * (2 * fila - 1)
    print(f'{espacios}{asterisco}')