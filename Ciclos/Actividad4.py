print('*** Sistema de  Calculadora ***')
Operando1 = Opoerando2 = Resultado = 0
salir = False
while not salir:
    print(f''' Operaciones a Realizar
    1. Suma 
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Elija la operacion a relizar: '))
    if 1 <= opcion <= 4: 
        Operando1 = float(input('Ingrese el primer valor: '))
        Opoerando2 = float(input('Ingrese el segundo Valor: '))
    # Suma de Datos
    if opcion == 1:
        Resultado = Operando1 + Opoerando2
        print(f'El resultado a la suma es: {Resultado:.2f}\n')
# Resta de Datos    
    elif opcion == 2:
        Resultado = Operando1 - Opoerando2
        print(f'El resultado a la resta es: {Resultado:.2f}\n')
# Multiplicacion
    elif opcion == 3:
        Resultado = Operando1 * Opoerando2
        print(f'El resultado a la Multiplicacion es: {Resultado:.2f}\n')
# Division
    elif opcion == 4:
        Resultado = Operando1 / Opoerando2
        print(f'El resultado a la Divicion es: {Resultado:.2f}\n')
# Salir
    elif opcion ==  5:
        print(' Saliendo de la Calculadora')
        salir = True
# Opcion Invalida    
    else:
        print(' Opcion Invalida vuelve a intentarlo ')



    