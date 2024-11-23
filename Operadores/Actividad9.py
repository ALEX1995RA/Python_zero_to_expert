# Sistema de Atenticación
usuario_valido = 'admin'
clave_valida = '123'

# Ingreso de datos
usuario = input('Ingrese el Usuario: ')
clave = input('Ingresa la clave: ')

# Ejecucion de la autenticacion
datos_correcto = usuario.strip().lower() == usuario_valido.lower() and clave.strip() == clave_valida

print(f''' Sistema de Autenticación ***
      \nDatos Ingresados 
      Usuario: {usuario}
      Clave: {clave}
      Los datos son correctos: {datos_correcto}''')

# Valor dentro de Rango
minimo = 0
maximo = 5

# Solictar datos al Usuario
valor_rango = int(input('Ingresa un Numero de 0 a 10: '))

#Validar el Rango
dato = valor_rango >= minimo and valor_rango <= maximo
print(f'''\n*** Valor Dentro de Rango ***
      \nEl valor asignado esta en rango: {dato}''')