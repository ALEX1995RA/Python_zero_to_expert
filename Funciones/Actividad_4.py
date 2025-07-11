# Definimos la lista de snacks inicial
snacks = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]
# Lista de productos 
productos = []
def mostrar_snacks():
    print('*** Snacks Disponibles ***')
    for snack in snacks:
        print(f"ID: {snack['id']}, Nombre: {snack['nombre']}, Precio: {snack['precio']}")   
def comprar_snack():
    id_snack = int(input('Ingresa el ID del snack que deseas comprar: '))
    snack_encontrado = next((snack for snack in snacks if snack['id'] == id_snack), None)
def mostrar_ticket():
    if not productos:
        print('No has comprado ningún snack.')
        return
    print('*** Ticket de Compra ***')
    total = 0
    for producto in productos:
        print(f"Snack: {producto['nombre']}, Precio: {producto['precio']}")
        total += producto['precio']
    print(f'Total a pagar: {total}')

# Programa principal
if __name__ == '__main__':
    print('*** Sistema de Snacks ***')

# Creamos el menu
    while True:
        print(f'''Menú:
        1. Mostrar Snacks
        2. Comprar Snack
        3. Mostrar ticket
        4. Salir''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Regresa pronto!')
            break
        else:
            print('Opción inválida, proporciona otra opción!')