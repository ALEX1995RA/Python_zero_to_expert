print(" *** Combinacion de listas y Diccionarios *** ")

# Definir una lista de diccionarios
Personas = [
    {
        "Nombre": "Regina",
        "Apellido": "Flores",
        "Edad": 21,
    },
    {
        "Nombre": "Alejandro",
        "Apellido": "Reyes",
        "Edad": 25
    },
]
print("Lista de Personas: {Personas}")

# Acceder a los elementos de la lista de diccionarios
print(f'''Detalle del primer elemento de la lista:
    Nombre: {Personas[0].get('Nombre')}
    Apellido: {Personas[0].get('Apellido')}
    Edad: {Personas[0].get('Edad')}''')

# Recorrer los elementos de la lista
print()
for contador, persona in enumerate(Personas):

# Imprimir el contador y el diccionario de la persona
    print(f'{contador} - Persona: {persona}')
    
# Imprimir los detalles de la persona    
    print(f'Detalle: Nombre: {persona.get('Nombre')}, Apellido: {persona.get('Apellido')}, Edad: {persona.get('Edad')}')