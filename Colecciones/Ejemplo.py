print('*** Playlist de Canciones ***')

# Creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deseas agregar? '))

# iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)


#Orden alfabeticos de la lista
lista_reproduccion.sort()
lista_reproduccion.sort(reverse=True)

#lista de Canciones
print(f'\nLista de reproduccion en orden alfabatico: ')
print(lista_reproduccion)

# Mostar la lista lista iterando sus elementos
# print('\nIteramos el playlist')
#for cancion in lista_reproduccion:
#   print(f'- {cancion}')

# Agregar Canciones
#lista_reproduccion.append('Hotel california - Eagles')
#lista_reproduccion.append('Staying alive - Bee Gees')
#lista_reproduccion.append('Dream on Aerosmith')


