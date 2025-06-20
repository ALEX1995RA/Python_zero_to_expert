print('*** Funciones en Python ***')

# Definir una funcion para mandar a saludar
def saludar():  # Firma del metodo
    # Cuerpo de la funcion
    print('Saludos desde una función...')

# Programa principal, llamamos a la funcion
saludar()
saludar()
saludar()

# Definir Parametros sobre la funcion
def saludar(mensaje):  # Firma del metodo
    print(f'Mensaje recibido: {mensaje}')
saludar('Hola a todos!')


