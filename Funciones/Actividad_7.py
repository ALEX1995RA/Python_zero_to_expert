print("**** Termostato inteligente ****")

# Definición de la función
def termostato(temperatura):
    if  temperatura < 15:
        return "Encender calefacción"
    elif 15 <= temperatura < 32:
        return "Temperatura ideal"
    else:
        return "Encender aire acondicionado"

# programa principal
def main():
    temperatura = float(input('Ingrese la temperatura actual: '))
    accion = termostato(temperatura)
    print(f'la temperatura actual es: {temperatura}°C')
    print(f'Accion recomendada: {accion}')

# Ejecutar la función principal
if __name__ == '__main__':
    main()

 
