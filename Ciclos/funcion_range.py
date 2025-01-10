print('*** Función range ***')


# inicio = 0 (opcional)
# fin = 5 - 1 = 4
# incremento = 1 (opcional)
print('Secuencia del 0 al 4: ')
for i in range(5):  
    print(i, end=' ')

# incremento = 1 (default y es opcional)
print('\n\nSecuencia del 10 al 20:')
for i in range(10, 20 + 1):
    print(i, end=' ')


print('\n\nSecuencia del 20 al 30 de 2 en 2: ')
for i in range(20, 30 + 1, 2):
    print(i, end=' ')