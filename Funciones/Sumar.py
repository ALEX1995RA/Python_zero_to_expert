#Importe de un modulo
import modulo_funcion

from modulo_funcion import sumar

# Imprimir mensaje de inicio
print('*** Función sumar ***')

# Definimos la funcion
##def sumar(a, b):
    #resultado_suma = a + b
    #return resultado_suma

# Llamar a la funcion
resultado_funcion = sumar(8, 5)
print(f'Resultado función sumar: {resultado_funcion}')

resultado_funcion = modulo_funcion.sumar(10, 20)
resultado_funcion = sumar(10, 20)

# Llamar a la funcion del modulo
print(f'Resultado función sumar: {resultado_funcion}')
print(__name__)

