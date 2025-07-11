# Definición de la clase
class Calculadora:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2

    def multiplicacion(self):
        return self.operando1 * self.operando2

    def division(self):
        if self.operando2 == 0:
            return 'Error: división por cero'
        return self.operando1 / self.operando2

# Código principal
if __name__ == '__main__':
    print("*** Calculadora Aritmética con clases y objetos ***")

    # Primer objeto con sus propios operandos
    op1 = float(input('Ingresa el primer operando para calc1: '))
    op2 = float(input('Ingresa el segundo operando para calc1: '))
    calc1 = Calculadora(op1, op2)

    print("\nResultados con primer objeto:")
    print(f'Suma: {calc1.suma()}')
    print(f'Resta: {calc1.resta()}')
    print(f'Multiplicación: {calc1.multiplicacion()}')
    print(f'División: {calc1.division()}')

    # Segundo objeto con operandos diferentes
    op3 = float(input('\nIngresa el primer operando para calc2: '))
    op4 = float(input('Ingresa el segundo operando para calc2: '))
    calc2 = Calculadora(op3, op4)

    print("\nResultados con segundo objeto:")
    print(f'Suma: {calc2.suma()}')
    print(f'Resta: {calc2.resta()}')
    print(f'Multiplicación: {calc2.multiplicacion()}')
    print(f'División: {calc2.division()}')

