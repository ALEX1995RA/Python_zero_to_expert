# Inmutabilidad en Cadenas
cadena1 = 'Hola Mundo'
# cadena1[0] = 'h' # Genera Error al imprir
cadena2 = cadena1
cadena1 = 'Adios'
print(cadena1)
print(cadena2)
