print('***  Creación y validacion de Contraseña *** ')
Contraseña =input ('Ingrese la contraseña: ')
while len (Contraseña) < 6:
    print('Contraseña invalida, debe tener minimo 6 Caracteres')
    Contraseña = input('Digite la nueva contraseña: ')
else:
    print('Contraseña Valida registro terminado. ')