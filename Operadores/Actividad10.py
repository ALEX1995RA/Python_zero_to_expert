#Sistema de Prestamo de Libros
distancia = 3
credencia_estudiantil = input(f'Cuenta con Credecial Estudiantil: (Si/No) ')
distanciakm = int(input('A cuantos KM vives de la Biblioteca? '))
elegible_prestamo = credencia_estudiantil.strip().lower() == 'si' or distanciakm <= distancia
print(f'Eres elegible para el Prestamo del Libro: {elegible_prestamo}')

# Tiquetera de Venta

leche = float(input('Precio de la Lache: '))
pan = float(input('Precio del Pan: '))
lechuga = float(input('Precio de la Lechuga: '))
platano = float(input('Precio del Platano: '))
descuento = int(input('Aplicar descuento (%) '))

# Calculo de totales sin impuesto 
subtotal = lechuga + leche + pan + platano

# Aplicar descuento 
descuento1 = subtotal * (descuento / 100)

# Aplicar descuento
subdescuento = subtotal - descuento1

#impuesto con descuento
impudescuento = subdescuento * 0.19

# Calculo de impuesto 19%
impuesto = subtotal * 0.19

# Costo final
valor = subtotal + impuesto
valor1 = subdescuento + impudescuento

print('\n**** Tiquet de Compra ***')
print(f'''\n Articulos Valor Unitario
      Leche.... {leche}
      Pan...... {pan}
      Lechuga.. {lechuga}
      Platanos. {platano}
      -----------------
      Subtotal *** {subtotal:.2f}
      Impu. 19% ** {impuesto:.2f}
      Sub.Desc *** {subdescuento}
      Impu.Des.*** {impudescuento}   
      Des. Aplicar* {descuento}%
      ------------------
      VALOR TOTAL DE LA COMPRA
          {valor:.3f}
      VALOR CON DESCUENTO
          {valor1}    
   \n*** GRACIAS POR LA COMPRA ***''')