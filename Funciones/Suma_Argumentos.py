print('*** Suma de argumentos ***')

def suma(*args):
   total = 0
   for numero in args:
       total += numero
   return total

print(suma(1, 2, 3))
print(suma(5, 10, 15, 20))
