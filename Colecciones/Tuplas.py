print("*** Manejo de Tuplas ***")
Mi_Tupla = (1, 2, 3, 4, 5) 
print("Mi_Tupla:", Mi_Tupla)
# No se puede Modificar una Tupla
# Mi_Tupla[0] = 10 # Esto generará un error
# Mi_Tupla.append(6) # Esto también generará un error

# Iteracion de una Tupla
for i in Mi_Tupla:
    print(i, end=" ")

# Crear una tupla para cordenadas x, y,
Coordenadas = (3, 5)
# Acceso a los elementos de la tupla
print("\nCoordenadas: en el eje X", Coordenadas[0])
print("Coordenadas: en el eje Y", Coordenadas[1])

# Tupla con un solo elemento
Tupla_Solitaria = (10,)  # Nota la coma al final    
print("Tupla con un solo elemento:", Tupla_Solitaria)

# Tupla vacía
Tupla_Vacia = ()
print("Tupla vacía:", Tupla_Vacia)

# Tupla anidada
Tupla_Anidada = (1, 2, (3, 4), (5, 6))
print("Tupla anidada:", Tupla_Anidada)
print("Elemento anidado:", Tupla_Anidada[2][3])  # Acceso al elemento 6 de la tupla anidada