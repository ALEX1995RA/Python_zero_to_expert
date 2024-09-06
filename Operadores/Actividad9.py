#Sistema de Prestamo de Libros
distancia = 3
credencia_estudiantil = input(f'Cuenta con Credecial Estudiantil: (Si/No) ')
distanciakm = int(input('A cuantos KM vives de la Biblioteca? '))
elegible_prestamo = credencia_estudiantil.strip().lower() == 'si' or distanciakm <= distancia
print(f'Eres elegible para el Prestamo del Libro: {elegible_prestamo}')