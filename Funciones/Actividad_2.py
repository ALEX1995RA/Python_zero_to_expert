print("*** Potencia número usando funciones recursivas ***")

# Definimos la funcion potencia recursiva
def potencia(base, exponente):
    # Caso base, cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    else: # Caso recursivo
        return base * potencia(base, exponente - 1)

# Probamos la función
base = int(input("Ingresa la base sobre la cual se calculará la potencia: "))
exponente = int(input("Indica el exponente a cual quiere elevar la base: "))
resultado = potencia(base, exponente)
print(f'La potencia de {base} elevado a {exponente} es: {resultado}')