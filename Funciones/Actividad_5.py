print('*** Calculadora de funciones ***')
# Asignacion de funciones
def suma(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return 'Error division por cero'
    return a / b

# Asignación del Menu
def menu():
    print(''' 
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir ''')

# Programa inicial
def calcular(opcion, a, b):
    if opcion == 1:
        return suma(a, b)
    elif opcion == 2:
        return restar(a,b)
    elif opcion == 3:
        return multiplicar(a, b)
    elif opcion == 4:
        return division(a,b)
    elif opcion == 5:
        return 'Saliendo del programa...'
    else:
        print('Opcion incorrecta intente de nuevo')

# Función principal que ejecuta el programa
def main():
    while True:
        menu()
        opcion = int(input('Seleccion la operacion a realizar: '))
        if opcion == 5:
            print(calcular(opcion, 0, 0))
            break
        a = float(input('Indica el primer valor: '))
        b = float(input('Indica el Segundo Valor: '))
        resultado = calcular(opcion, a, b)
        print(f'El resultado a la opercion asignada es: {resultado}')
        if resultado == 'Error division por cero':
            print('No se puede dividir entre Cero')

# Ejecutar la función principal
if __name__ == '__main__':
    main()
    