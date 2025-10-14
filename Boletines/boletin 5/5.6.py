# Escribir un programa que tome unha cantidade m de valores ingresados polo usuario, a cada un lle calcule o factorial
# e imprima o resultado xunto co número de orden correspondiente.

import math
print('''
Bienvenido, a continuacion ingrese
3 cantidas para realizar el 
calculo e imprimirlo''')

cantidad1 = int(input('Ingrese la primera cantidad: '))


def calculo_factorial(cantidad1):
    factorial = math.factorial(cantidad1)
    return factorial


resultado = calculo_factorial(cantidad1)
print(resultado)
