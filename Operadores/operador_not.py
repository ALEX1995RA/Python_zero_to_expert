#Aplicacion del operador Not
condicion = False
resultado = not condicion
print(f'El operador Not sobre {condicion}: {resultado}')

# mcambio de valores
condicion = True
resultado = not condicion
print(f'\nEl operador Not sobre {condicion}: {resultado}')

#Cadena vacia
nombre = ''
cadena = not nombre
print(f'\nLa Variable no tiene ningun Valor es: {cadena}')

#Revisar si nop hay valor asignado
variable = None
sin_valor = not variable
print(f'\nEs variable sin valor {sin_valor}')

#Con valor  Asignado
variable = 10
sin_valor = not variable
print(f'\nEs variable sin valor {sin_valor}')

#Revisar si hay una variable dentro del rango

dato = int(input('Proporcian un valor '))
rango = 1 <= 10
cumple = 1 <= dato <= 10
print(f'La Variable esta dentro del Rango 1 a 10 {cumple}')

#Logica Inversa
dato = int(input('Proporcian un valor '))
rango = 1 <= 10
cumple = not 1 <= dato <= 10
print(f'La Variable esta fuera del Rango 1 a 10 {cumple}')