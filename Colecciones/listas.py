print(' *** Manejo de Listas ***')
mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} -> Lasta original')

# Largo de la lista
print(f'El largo de la lista {len(mi_lista)} ')

#Acceder alo elementos de la lista por Indice
print(f'Acccedemos al indice 4 de la lista {mi_lista[4]}')
print(f'Accedemos al indice final de la lista {mi_lista[-1]}')

# Modifocar los elementos de la lista
mi_lista [1] = 10
print(f'Modificamos el indice 1: {mi_lista[1]}')

# Agregar nuevos elementos al final de la lista
mi_lista.append (6)
print(f'{mi_lista} -> Se agrego el el elemento numero 6')

# Añadir un nuevo elemento en un indice especifico
mi_lista.insert(2, 15)
print(f'{mi_lista} -> Se añadió el valor de 15 en el índice 2')

# Eliminar elementos de una lista
# usando el metodo remove
mi_lista.remove(5)
print(f'{mi_lista} -> Se removió el valor 5')

# Removemos por indice con el metodo pop
mi_lista.pop(1) # Remueve el elemento del indice 1
print(f'{mi_lista} -> Se eliminó el índice 1')

# Eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista} -> Se eliminó el índice 2')

# Obtener sublistas
sublista = mi_lista[1:3]  # genera una sublista del indice 1 al 2 (3 no se incluye)
print(f'Sublista [1:3]: {sublista}')


