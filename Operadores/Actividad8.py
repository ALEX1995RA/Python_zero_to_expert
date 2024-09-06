# Sistema descuento VIP
print('*** Sistema de Descuentos VIP ***')
no_descuento = 10
cantidad_productos = int(input('Cuantos productos compraste hoy? '))
membresia = input('Tiene Membresia: (Si/No)')
aplica_descuento = cantidad_productos >= no_descuento and membresia.strip().lower() == 'si'
print(f'Tienes acceso al descuento VIP: {aplica_descuento}')
