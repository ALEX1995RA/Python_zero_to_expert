# SISTEMA DE RESERVA DE HOTEL
print(f'*** Sistema de R eserva ***')

nombre = input('Ingrese el nombre de Registro: ')
dias_estadia = int(input('Cuantos dias desea de Reserva: '))
cuarto_al_mar = input('Desea cuarto con vista al mar (Si/No): ')
costo_cvmar = 190.50
costo_svmar = 150.50

if cuarto_al_mar.strip().lower() == 'si':
    print(f'Cuaro con vista al mar: {cuarto_al_mar}')
    costo_total = costo_cvmar * dias_estadia
    print(f'El valor de la reserva por {dias_estadia} dias con habitación con vista al mar es de ${costo_total:.2f}')
else:
    print(f'Cuaro con vista al mar: {cuarto_al_mar}')
    costo_total = costo_svmar * dias_estadia
    print(f'El Valor de la reserva por {dias_estadia} dias en habitacion sin vita al mar es ${costo_total:.2f}')

