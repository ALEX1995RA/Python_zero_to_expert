# Sistema Generador de Emails
nombres = input('Ingresa tus Nombres: ')
apellidos = input('Ingresa tus Apellidos: ')
empresa = input('Indica la Empresa: ')
extencion = '.com.co'
 
 #normalizacion de datos
usuario1 = nombres.lower().strip().replace(' ','.')
usuario2 = apellidos.lower().strip().replace(' ','.')
usuario3 = empresa.lower().strip().replace(' ','')

 # Ejecución de la actividad
print(f'*** Generador De  Emails ***')
print(f'''\nHola {nombres} {apellidos} 
    Tu Email Asignado es: {usuario1}.{usuario2}@{usuario3}{extencion}
    Gracias por tu Tiempo! ''' )