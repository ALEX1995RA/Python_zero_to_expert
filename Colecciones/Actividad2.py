print( " *** Lista de Suscriptores ***" )

# Definir el set inicial
suscriptores= set() # Crear un conjunto vacío para almacenar los suscriptores
numer_suscriptores = int(input("Ingresa el numero de suscriptores iniciales: "))
for _ in range(numer_suscriptores):
    suscriptores.add(input("Digita el nuevo Suscriptor (Email): "))

# Mostrar la lista de suscriptores 
#suscriptores = {"luisa@mail.com", "carlos@mail.com", "maria@mail.com", "elena@mail.com"}
print(f"Lista de suscriptores: {suscriptores}")

#Verificar si un nuevo suscriptor está en la lista
#nuevo_suscriptor = "ana@mail.com"
nuevo_suscriptor = input("Ingresa el nuevo suscriptor (Email): ")
if nuevo_suscriptor in suscriptores:
    print(f"El nuevo suscriptor ya se encuentra en la lista {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"El nuevo suscriptor {nuevo_suscriptor} se ha añadido a la lista")
print(f"Lista de suscriptores actualizada: {suscriptores}")

# Eliminar un suscriptor de la lista
#suscriptor_eliminar = "maria@mail.com"
suscriptor_eliminar = input("Ingresa el suscriptor a eliminar (Email): ")
suscriptores.remove(suscriptor_eliminar)
print(f"El suscriptor {suscriptor_eliminar} se ha eliminado de la lista")
print(f"Lista de suscriptores actualizada: {suscriptores}")

# Verificar la cantidad de suscriptores
print(f"La cantidad total de suscriptores es: {len(suscriptores)}")

# Iterar sobre la lista de suscriptores
print("---- Lista de suscriptores ----")
for suscriptor in suscriptores: 
    print(f" - {suscriptor}")