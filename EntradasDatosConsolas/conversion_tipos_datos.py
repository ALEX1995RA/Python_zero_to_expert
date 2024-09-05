# Conversion de tipos de Datos

#Convertire de Cadena  Numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numerico en Cadena: {numero_cadena}')
print(f'Cadena a Entero: {numero_entero}')

#Convertir de Cadena a Flotante
numero_cadena = '3.141'
numero_flotante = float(numero_cadena)
print(f'Cadena a Flotante: {numero_flotante}')

#Convertir de Numero a Cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Numero a Cadena: {numero_cadena}')

#Convertir a Booleano
#tipo boll es falso en los siguientes casos
# Si el valor es 0,o None regresa a False
#Regresa Verdadero, siempre el valor sea distinto a 0 si es distinto a cadena vacia o None

#Caso Falso
numero_entero = 0
booleno = bool(numero_entero)
print(f'Valor booleno de 0 es : {booleno}') #false

# Caso Verdadero
numero_entero = 5
booleno = bool(numero_entero)
print(f'Valor booleno de 5 es : {booleno}') #true

#cadena Vacia = 0
cadena = ''
booleno = bool(cadena)
print(f'El valor booleano de la Cadena Vacia es: {booleno}') # False

#Cadena con Valor 
cadena = '5'
booleno = bool(cadena)
print(f'El valor booleano de la Cadena asignada es: {booleno}') # True

#Variable tipo None
Variable = None
booleno = bool(Variable)
print(f'El valor Boolenao de None: {booleno}') #False