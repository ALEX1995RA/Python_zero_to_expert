print('*** Calculo Area y Perimetro de un rectangulo ***')
base = float(input('Ingresa la base del Rectangulo: '))
altura = float(input('Ingresa la altura del Rectangulo: '))
# Realizemos los calculos
area = base * altura
perimetro = 2 * (base+altura)  #Presedencia de Opoeradores
print(f'El area del Rectangulo es: {area}')
print(f'El Perimetro del rectangulo es: {perimetro}')
