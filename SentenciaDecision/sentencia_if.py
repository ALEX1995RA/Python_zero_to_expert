# Linea de proceso Sentencia If

print(f'*** Sentencia if ***')
edad= 30
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años')

# Sentencia else

print(f'*** Sentencia else ***')
edad= 10
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años')
else:
    print(f'Eres menor de edad, tienes {edad} años')
 
 #Sentencia elif

print(f'*** Sentencia elif ***')
edad= 15
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años')
elif 13 <= edad < 18:
    print(f'Eres un adolecente. Tienes {edad} años')
else:
    print(f'Eres menor de edad, tienes {edad} años')