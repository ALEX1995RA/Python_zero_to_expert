# Inicializamos el inventario como una lista
inventario = [
    {"Id": "1", "Nombre": "Camisa", "Precio": 25.99, "Cantidad": 50},
    {"Id": "2", "Nombre": "Pantalon", "Precio": 39.99, "Cantidad": 30},
    {"Id": "3", "Nombre": "Zapatos", "Precio": 49.99, "Cantidad": 20}
]

# Mostrar inventario
def mostrar_inventario():
    print("\n📦 Inventario actual:")
    for producto in inventario:
        print(f'ID: {producto["Id"]}')
        print(f'Nombre: {producto["Nombre"]}')
        print(f'Cantidad: {producto["Cantidad"]}')
        print(f'Precio: {producto["Precio"]}\n')

# Agregar productos
def agregar_productos():
    while True:
        id_producto = input('Ingrese el Id de producto: ').strip()
        nombre_producto = input('Ingrese el nombre del producto: ').strip()
        cantidad_producto = int(input('Ingresa la cantidad del producto: ').strip())
        precio_producto = float(input('Ingresa el valor del producto: ').strip())
        inventario.append({
            "Id": id_producto,
            "Nombre": nombre_producto,
            "Cantidad": cantidad_producto,
            "Precio": precio_producto
        })
        print(f'✅ Producto "{nombre_producto}" agregado con éxito.\n')  
        mostrar_inventario()
        continuar = input("¿Desea agregar otro producto? (Y/N): ").strip().lower()
        if continuar != 'y':
            break

# Buscar producto por ID
def buscar_producto():
    while True:
        id_producto = input('🔍 Ingrese el ID del producto a buscar: ').strip()
        encontrado = False
        for producto in inventario:
            if producto["Id"] == id_producto:
                print("\n✅ Producto encontrado:")
                print(f'ID: {producto["Id"]}')
                print(f'Nombre: {producto["Nombre"]}')
                print(f'Cantidad: {producto["Cantidad"]}')
                print(f'Precio: {producto["Precio"]}\n')
                mostrar_inventario()
                encontrado = True
                break
        if not encontrado:
            print("❌ Producto no encontrado.\n")
        
        continuar = input("¿Desea buscar otro producto? (Y/N): ").strip().lower()
        if continuar != 'y':
            break

# Eliminar producto por ID
def eliminar_productos():
    while True:
        id_producto = input('🗑️ Ingrese el ID del producto a eliminar: ').strip()
        encontrado = False
        for producto in inventario:
            if producto["Id"] == id_producto:
                inventario.remove(producto)
                print(f'✅ Producto con ID {id_producto} eliminado con éxito.\n')
                mostrar_inventario()              
                encontrado = True
                break
        if not encontrado:
            print(f'❌ No se encontró el producto con el ID {id_producto}.\n')
        
        continuar = input("¿Desea eliminar otro producto? (Y/N): ").strip().lower()
        if continuar != 'y':
            break

# Bucle del sistema
print("*** Sistema de inventario por funciones ***")

while True:
    print("\n📋 Menú de opciones:")
    print("1. Mostrar inventario actual")
    print("2. Agregar producto al inventario")
    print("3. Buscar un producto por Id")
    print("4. Eliminar un Artículo del inventario")
    print("5. Salir del sistema")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_productos()
    elif opcion == "5":
        print("👋 Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("❗ Opción no válida. Intenta nuevamente.")

    seguir = input('¿Desea realizar otra operación? (Y/N): ').strip().lower()
    if seguir != 'y':
        print('👋 Gracias por usar el sistema. ¡Hasta pronto!')
        break


