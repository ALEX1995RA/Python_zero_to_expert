# Validacion Positivo

print('*** Revision del Valor Positivo ***')
numero = int(input('Proporciona un Numero: '))

if numero >0:
    print(f'Espositivo: {numero}')
elif numero <0:
    print(f'Es Negativo: {numero}')
else:
    print(f'El valor es Cero: {numero}')
    10
    
# Sistema Bancario

print("*** Bienvenidos al Sistma Bancario****")
salir_txt = input('Desea Salir del Sistema (Si/No) ')
salir = salir_txt.strip().lower() =='si'
if not salir:
    print('Continuando dentro del Sistema')
else:
    print('Saliendo del sistema')

# Casa de espejos

print('*** Bienvenidos a la casa de los espejos ***')
edad = int(input('Cual es tu Edad: '))
tienes_miedo = input('Tienes Miedo a la Oscuridad (Si/No)')
miedo_oscuridad = tienes_miedo.strip().lower() == 'si'
if not miedo_oscuridad and edad >= 10:
    print('Puedes entrar a la casa de los Espejos')
else:
    print('Lo siento, la casa de los espejos te hara morir del Susto')

# Aplicacion Fitm¿nes

print('*** Aplicacion de Salud Fitnes ***')
# Constantes
Meta_Diaria = 10000
Calorias_paso = 0.04
# Valores a Solicitar
usuario = input('Ingrese su Usuario: ')
Pasos = int(input('Cuantos pasos realizaste: '))
#Verificación
Meta_Final = Pasos >= Meta_Diaria
Meta_Final_txt = 'Si' if Meta_Final else 'No'
# Calcular calorias Quemadas
Calorias_Quemadas = Pasos * Calorias_paso
#Mostrar Información
print(f'\nUsuario: {usuario}')
print(f'Numero de pasos dados: {Pasos}')
print(f'Calorias quemadas por caminar: {Calorias_Quemadas}')
print(f'La meta de pasos diarios es: {Meta_Diaria} pasos')
