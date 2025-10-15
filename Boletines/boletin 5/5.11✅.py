# 11. Codifica un programa que solicite un número e visualice a táboa de multiplicar dese número.
# O programa seguirá pedindo números ata que o usuario pulse o número cero.

numero = int(input('Ingrese un numero del 1 al 9: '))
numero2 = 11

while numero > 0 and numero < 10:
    for i in range(numero2):
        multiplicar = i * numero
        print(i, '*', numero, '=', multiplicar)
        i += 1
    if i == 11:
        numero = int(input('Ingrese un numero del 1 al 9: '))
