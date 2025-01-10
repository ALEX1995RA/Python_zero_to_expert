# SISTEMA DE CALIFICACIONES
print('*** Sistemas de Calificaciones ***')

usuario = float(input('Ingrese la Calificacion Obtenida de (0 a 10): '))
calificacion = None

if 9 <= usuario <= 10:
    calificacion = 'A'
elif 8 <= usuario < 9:
    calificacion = 'B' 
elif 7 <= usuario < 8:
    calificacion = 'C'
elif 5 <= usuario < 7:
    calificacion = 'D'
elif 0 <= usuario < 5:
    calificacion = 'F'
else:
    calificacion = 'Valor Incorecto no se denomina Calificacion'

print(f'\nTu calificacion es: {calificacion}')

# SISTEMA DE ENVIOS A NIVEL NACIONAL E INTERNACIONAL

print('**** SISTEMA DE ENVIOS ***')

tarifa_Nal = 10
tarifa_inter = 20

destino = input('Engresa el lugar de destino del paquete (Nacional o Internacional):')
peso = float(input('Ingrese el peso del  paquete (Kg):'))

costo = None
destino = destino.strip().lower()
if destino == 'nacional':
    costo = peso * tarifa_Nal
elif destino == 'internacional':
    costo = peso * tarifa_inter
else:
    print('Destino no Valido.\nIngresa el valor nancional o internacional')
if costo  is not None:
    print(f'El costo del envio del paquete es ${costo:.2f}')
