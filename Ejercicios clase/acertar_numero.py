import random

n = random.randint(0, 100)
contador = 7

print(n)

while contador > 0:
    numero = int(input('Ingrese un numero: '))
    if numero == n:
        print('Enhorabuena, has acertado. El numero es: ', n)
    if numero < n:
        print('El numero es mas pequeño')
        contador = contador - 1
    if numero > n:
        print('El numero es mayor')
        contador = contador - 1
    if contador == 0:
        print('Lo siento has perdido')
