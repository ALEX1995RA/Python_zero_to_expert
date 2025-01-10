print(' *** Repeticion de Mensajes *** ')
mensaje = input('Ingrese el Mensaje a Repetir: ')
repetición = int(input('Cuantas Veses desea repetir el mensaje: '))
for i in range(repetición):
    print(f'{i} - {mensaje}')

