# Sistema de Empleados
print('**Sistema de empleados**')

nombre_empleado = input('Ingresa Tu Nombre: ')
edad_empleado = int(input('Ingresa tu edad: '))
salario = float(input('Ingresa tu Salario: ')) 
director = input('Es jefe de departemento (Si/No)')
director = director.lower() == 'si'

print(f'\nNombre del emplado: {nombre_empleado}')
print(f'Edad del Emplado: {edad_empleado}')
print(f'Salario del Empleado: {salario}') #Para agregar mas decimales se debe anexar .2f
print(f'Es Jefe de Departamento: {director}')

# Receta de Cocina

print('\n***Receta de Cocina***')

nombre = input('Ingresa el Nombre de la Receta: ')
ingredientes = input('Ingrese los ingredientes necesarios: ')
tiempo = int(input('Tiempo de Coccion:  '))
preparacion = input('Facil - Medio - Dificil: ')

print(f'\nNombre de la Receta: {nombre}')
print(f'Ingredientes base: {ingredientes}')
print(f'Tiempo estimado de Preparacion: {tiempo} Minutos')
print(f'Dificultad del Plato: {preparacion}')