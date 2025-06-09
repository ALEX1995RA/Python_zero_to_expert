print("*** Operaciones de tipo set ****")

# Definir dos conjuntos de números
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#Definir la union de los conjuntos A y B
union = A | B
print(f"Union de A y B: {union}")

# Definir la intersección de los conjuntos A y B
interseccion = A & B
print(f"Intersección de A y B: {interseccion}") 

# Definir la diferencia de los conjuntos A y B
diferencia = A - B
print(f"Diferencia de A y B: {diferencia}")

# Definir la diferencia simétrica de los conjuntos A y B
diferencia_simetrica = A ^ B
print(f"Diferencia simétrica de A y B: {diferencia_simetrica}")     

