print(" *** Sets ***")
# Definir un conjunto de números
numeros = {1, 2, 3, 4, 5, 4}
# Imprimir el conjunto
print("Conjunto de números:", numeros)

#agregar un elemento al Set
numeros.add(6)
numeros.add(7)

# Imprimir el conjunto después de agregar elementos
print("Conjunto de números después de agregar elementos:", numeros)

#Agrgar un elemento duplicado al Set
numeros.add(3)  

#eliminar un elemento del Set
numeros.remove(2)

#Iteración sobre el Set
for numero in numeros:
    print("Número:", end=" ")

# Verificar si un elemento está en el Set
if 3 in numeros:
    print("El número 3 está en el conjunto.")
else:
    print("El número 3 no está en el conjunto.")

#Obtener la longitud del Set
print("Longitud del conjunto:", {len(numeros)})
