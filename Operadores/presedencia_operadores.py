# 1. Paréntesis (): Los paréntesis tienen la mayor precedencia
# 2. Exponente **: Este operador calcula la potencia de un número.
# 3. Unario +, -: Estos operadores realizan operaciones unarias de positivo y negativo
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Suma +, Resta -: Estos operadores realizan operaciones aritméticas.
# 6. Comparaciones (==, !=, >, <, >=, <=)
# 7. Operadores lógicos not, and, or
# 8. Asignación (=, +=, -=, *=, /=, entre otros)

# Ejemplo de precedencia de operadores
resultado = 12/3+2*3-1
print(f'Resultado: {resultado}')
#Alteracion de orden por parentesis
resultado1 = 12/(3+2)*3-1
print(f'El Nuevo resultado es: {resultado1}')
#Alteracion a entero //
resultado2 = 12//3+2*(3-1)
print(f'Resultado: {resultado2}')