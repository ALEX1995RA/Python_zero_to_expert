print('*** Aplicación Bancaria ***')

Saldo = 10000
Salir = False
while not Salir:
    print(f'''Operaciones a Realizar
    1. Consiltar Saldo
    2. Retirar
    3. Consignación
    4. Salir ''')
    Opcion = int(input('Ingrese la Opcion Requerida: '))
    if Opcion == 1:
        print(f'Tu saldo Actual es de: ${Saldo}') 
    elif Opcion == 2:
        Retiro = float(input('Ingrese Saldo a Retirar: '))
        if Retiro <= Saldo:
            Saldo -= Retiro
            print(f'Tu nuevo Saldo es: ${Saldo:.2f}\n')
        else:
            print(f'Saldo Insuficiente por favor ingrese el nuevo valor a retirar. Saldo actual: ${Saldo:.2f}\n')
    elif Opcion == 3:
        Deposito = float(input('Ingresa el Valor de la Consignación: '))
        Saldo += Deposito
        print(f'Tu nuevo saldo es: {Saldo:.2f}\n')
    elif Opcion == 4:
        print(f'Saliendo del sistema Bancario')
        Salir = True
    else:
        print('Opcion Invalida Vuelva a intentarlo\n')



