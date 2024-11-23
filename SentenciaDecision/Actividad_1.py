# Sistema Descuento de tienda
print(f'*** SISTEMA DESCUENTOS EN LINEA ***')
aplicadescu = 1000
compra =int(input('Proporciona un el valor de la compra: '))
miembro = input('Eres miebro de la tienda (Si/No) ')
descuento = 0

# Verificación de  ingreso de datos

if compra >= aplicadescu and miembro.strip().lower() == 'si':
    descuento = 0.1  #Descuento del 10%
elif miembro.strip().lower() =='si':
    descuento = 0.5 #Descuento del 5%
elif compra >= aplicadescu:
    descuento = 0.3 #Aplica deescuento 3%
else: 
    descuento = 0

# Calculo final
if descuento != 0:
    descuentotal = compra * descuento
    total = compra - descuentotal
    print(f'\nFelicidades has obtenido un descuento de {descuento * 100:.0f}%' )
    print(f'Monto de la compra: ${compra:.2f}')
    print(f'Monto del descuento: ${descuentotal:.2f}')
    print(f'Monto final de la compra con descuento: ${total:.2f}')

else:
    print('\nNo obtuviste descuento')
    print('Te invitamos a hacerte miembro de la tienda')
    print(f'Monto total de la compra: ${compra:.2f}')