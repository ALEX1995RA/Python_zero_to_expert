# Combinación de Listas y Tuplas
print("*** Combinación de Listas y Tuplas ***")
#Definir la lista que almacena tuplas
Productos= [
    ("p001", "Camiseta", 10.50), 
    ("p002", "Pantalón", 20.75),
    ("p003", "Zapatos", 30.00)
]
precio_total = 0
# Calcular el precio total de los productos
print("Infoarmación de los productos: ")
for producto in Productos:
    id_producto, nombre_producto, precio = producto
    print(f"ID: {id_producto}, Nombre: {nombre_producto}, Precio: {precio}")   

    # Sumar el precio de cada producto al total
    precio_total += precio  

# Imprimir la lista de productos y el precio total
print("Precio total: $", precio_total)

Tupla = (4, 5, 6)
Combinacion = Productos + [Tupla]

# Imprimir la combinación de lista y tupla
print("Productos:", Productos)
print("Combinación de Lista y Tupla:", Combinacion)