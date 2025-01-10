# SISTEMA DE AUTENTICACION

print('*** SISTEMA DE  AUTENTICACION ***')
usuario_val = 'Admin'
pasword_val = '123'

usuario = input('Ingrese el Usuario: ')
pasword = input('Ingrese su Pasword: ')

if usuario == usuario_val.strip().lower() and pasword == pasword_val:
    print('Bienvenidos al Sistema')
elif usuario == usuario_val.strip().lower():
    print('Pasword incorrecto, Vuelva a intentarlo...')
elif pasword == pasword_val:
    print('Usuario incorrecto Vuelva a intentarlo...')
else:
    print('Usuario y pasword invalido, Vuelva a intentarlo.....')