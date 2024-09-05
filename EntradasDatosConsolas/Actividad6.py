# Generador de ID Unico
from random import randint
print('*** Sistema de Generador de ID Unico ***')

nombre = input('Indicame tu Nombre: ')
apellido = input('Indiame tu Apellido: ')
fecha = input('Indicame Año de Nacimiento: ')

#Normalizar Valores
nombre1 = nombre.upper()[0:2]
apellido1 = apellido.upper()[0:2]
fecha1 = fecha[2:]
aleatorio = randint(1000, 9999) # el valor aleatorio de 4 digitos siempre se debe marcar segun el rango de dijitos a generar

#generar el Id Unico
id = f'{nombre1}{apellido1}{fecha1}{aleatorio}'

print (f'''\nHola {nombre}
      Tu Nuevo Id de Identificacion (ID) Generado por el Sistema es:
      {id}
      Felicidades!''')

