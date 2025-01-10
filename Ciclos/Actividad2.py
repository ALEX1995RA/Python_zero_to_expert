print('*** Sistema de Administración de Cuentas ***')
salir = False
while not salir:
    print(f'''Menu:
          1. Crear Cuenta
          2. Eliminar Cuenta
          3. salir''')
    opcion = int(input('Selecione la opcion requerida: '))
    if opcion == 1:
        print('Creando nueva cuenta ... \n')
    elif opcion == 2:
        print('Eliminando Cuenta ... \n')
    elif opcion == 3:
        print('Saliendo del sistema, hasta pronto.... \n')
        salir = True
    else:
        print('Opcion incorrecta vuelve a intentarlo ....')
else:
    print('Terminando ejecucion del programa')