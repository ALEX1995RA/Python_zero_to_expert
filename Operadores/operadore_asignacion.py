# Operadores de Asignacion
# Tipo Numerico
numero = 5
print(f'El valor del Operador asignado es:{numero}')

# Tipo Cadena
cadena = 'Saludos desde Pyton'
print(f'El valor asigando a la Variable es: {cadena}')

#Asignacion Multiplii
variable, variable1, variable2, variable3 = 1, 2, 3, 4
print(f'Los valores asignados son: {variable}, {variable1}, {variable2}, {variable3}') 

# Asignacion en cadena
contador = contador1 = contador2 = 5
print(f'Los valores de los operadores son: {contador}, {contador1}, {contador2}')

# Intercambios de Valores sin Temporales
a, b, = 3, 6
print(f'Valores iniciales de a:{a} y b:{b}')

# Aplicando concepto basico de Intercambio
a,b = b,a 
print(f' Invertir los Valores Asignados a {a} y b {b}')

# Ingreso de multiples Valores por digitacion de usuario
nombre, apellido = input('Ingresa tu nombre y apellido separado por coma: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip( )} ')