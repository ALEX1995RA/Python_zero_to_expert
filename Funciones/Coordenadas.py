print("*** Obtenr coordenadas de un punto ***")
# Definicion de la funcion
def coordenadas_punto():
    x,y, z = 10, 20, 30
    return(x, y, z)

# Llamada a la funcion
resultado = coordenadas_punto()
print(resultado)

#Unpacking de la tupla
x1, y1, z1 = resultado
print(f'Coordenada x = {x1}, Coordenada y = {y1}, Coordenada z = {z1}')



