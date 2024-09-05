# Crea Un Generador de Email
print('***Generador de Emails***')

nombre = 'Ubaldo Acosta Soto'
empresa = 'Global Mentory'
dominio = '.com.mx'
print(f'Datos para el Email: \nNombre: {nombre} \nCorporacion: {empresa} \nConectividad: {dominio}')
      
#Remplazar espácios en Blanco
usuario = nombre.replace(' ', '.')
entidad = empresa.replace(' ','')

# Convertir todo aa minusculas
usuario = usuario.lower() 
entidad = entidad.lower()
print(f'Email Asignado: {usuario}@{entidad}{dominio}')
