# Actividad numero Mayor

print('*** El Numero Mayor seleccionado ***')
numero1 = int(input('Ingresa el Primer Numero: '))
numero2 = int(input('Ingresa el Segundo Numero: '))

if numero1 > numero2:
    print(f'El primer numero {numero1} es mayor que el segundo {numero2}')
else:
    print(f'El segundo numero {numero2} es mayor que el primero {numero1}')

# Estaciones del Año

print('*** Selecion de Estaciones del Año ***')
usuario = int(input('Proporciona el el valor numerico del mes (1 a 12): '))
estacion = None

if usuario == 1 or usuario == 2 or usuario == 12:
    estacion = 'Invierno'
elif usuario == 3 or usuario == 4 or usuario == 5:
    estacion = 'Primavera'
elif usuario == 6 or usuario == 7 or usuario == 8:
    estacion ='Verano'
elif usuario == 9 or usuario == 10 or usuario == 11:
    estacion = 'Otoño'
else:
   estacion = 'Temporada no encontrada vuelva a intentarlo'
print(f'La estacion para el mes {usuario} es {estacion}')


