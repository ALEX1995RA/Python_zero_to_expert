print(" *** Gestor de Inventario *** ")

# Definir una lista de diccionarios para el inventario
Inventario = [
    {"Id": 1,
     "Nombre": "Camisa",
     "Precio": 25.99,
     "Cantidad": 50
    },
    {"Id": 2,
     "Nombre": "Pantalon",
     "Precio": 39.99,
     "Cantidad": 30
    },
    {"Id": 3,
     "Nombre": "Zapatos",
     "Precio": 49.99,
     "Cantidad": 20
    }
]
print("Inventario actual:\n")
for producto in Inventario:
    print(f"Id: {producto['Id']}")
    print(f"Nombre: {producto['Nombre']}")
    print(f"Precio: ${producto['Precio']}")
    print(f"Cantidad: {producto['Cantidad']}")
    print("-" * 30)

print("\n Seleccione la opcion a realizar: ")
print("1. Agregar nuevo producto ")
print("2. Actualizar un producto existente ")
print("3. Eliminar un producto del inventario ")
print("4. Buscar producto en el inventario ")
print("5. Salir del gestor de inventario ")
Opcion = input("Indica la opcion deseada: ").strip()
if Opcion == "1":
    print("**** Agregar nuevo producto al inventario ****")
    while True:
        Id = int(input("Indica el Id del producto: "))
        Nombre = input("Indica el Nombre del producto: ")
        Precio = float(input("Indica el precio del producto: "))
        Cantidad = int(input("Indica la cantidad del producto: "))
        Producto = {"Id": Id, "Nombre": Nombre, "Precio": Precio, "Cantidad": Cantidad}
        Inventario.append(Producto)
        print("✅ Producto agregado al inventario\n")
        continuar = input("¿DESEA AGREGAR OTRO PRODUCTO? (1. Sí / 2. No): ").strip()
        if continuar != "1":
         break
    print("\n📦 Inventario actualizado:\n")
    for producto in Inventario:
        print(f"Id: {producto['Id']}")
        print(f"Nombre: {producto['Nombre']}")
        print(f"Precio: ${producto['Precio']}")
        print(f"Cantidad: {producto['Cantidad']}")
        print("-" * 30)

elif Opcion  == "2":
    print(" **** Actualiza un producto existente en el inventario ****")
    while True:
        Id = int(input("Indica el Id a actualizar: "))
        for producto in Inventario:
            if producto["Id"] == Id:
                producto["Nombre"] = input("Indica el nombre a actualizar: ")
                producto["Precio"] =float(input("Indica el precio a actualizar: "))
                producto["Cantidad"] = int(input("Indica la catidad a actualizar: "))
                print("✅ Producto actualizado en el inventario")
                break
        continuar = input("¿DESEA ACTUALIZAR OTRO PRODUCTO? (1. Si / 2. No): ").strip().lower()
        if continuar != "1":
            break
    print("\n📦 Inventario actualizado:\n")
    for producto in Inventario:
        print(f"Id: {producto['Id']}")
        print(f"Nombre: {producto['Nombre']}")
        print(f"Precio: ${producto['Precio']}")
        print(f"Cantidad: {producto['Cantidad']}")
    else:
        print("❌ Producto no encontrado en el inventario")
    print(f"Inventario actualizado: {Inventario}")

elif Opcion == "3":
     print(" **** Eliminar un producto existente en el inventario ****")
     while True:
        Id = int(input("Indica el Id a actualizar: "))
        for producto in Inventario:
            if producto["Id"] == Id:
                producto["Nombre"] = input("Indica el nombre a actualizar: ")
                producto["Precio"] =float(input("Indica el precio a actualizar: "))
                producto["Cantidad"] = int(input("Indica la catidad a actualizar: "))
                print("✅ Producto actualizado en el inventario")
                break
        continuar = input("DESEA ELIMINAR OTRO PRODUCTO? (1. Si / 2. No): ").strip().lower()
        if continuar != "1":
            break
     print("\n📦 Inventario actualizado:\n")
     for producto in Inventario:
        print(f"Id: {producto['Id']}")
        print(f"Nombre: {producto['Nombre']}")
        print(f"Precio: ${producto['Precio']}")
        print(f"Cantidad: {producto['Cantidad']}")
     else:
        print("⚠️  Producto no encontrado en el inventario")
     print(f"Inventario actualizado: {Inventario}")

elif Opcion == "4":
    print("🔍 Buscar producto en el inventario por Id")
    while True:
        Id = int(input("Ingrese el Id del producto que desea buscar: "))
        encontrado = False
        for producto in Inventario:
            if producto["Id"] == Id:
                print("\n✅ Producto encontrado:")
                print(f"Id: {producto['Id']}")
                print(f"Nombre: {producto['Nombre']}")
                print(f"Precio: ${producto['Precio']}")
                print(f"Cantidad: {producto['Cantidad']}")
                print("-" * 30)
                encontrado = True
                break
        if not encontrado:
            print("❌ Producto no encontrado.")
        continuar = input("¿Desea buscar otro producto? (1. Sí / 2. No): ").strip()
        if continuar != "1":
            break
elif Opcion == "5":
    print("👋  Saliendo del gestor de inventario")
else:
    print("❌ Opcion no valida, por favor intente de nuevo")
