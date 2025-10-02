# Escribir un programa que tome unha cantidade m de valores ingresados polo usuario, a cada un lle calcule o factorial
# e imprima o resultado xunto co número de orden correspondiente.

print('''
Bienvenido, a continuacion ingrese
3 cantidas para realizar el 
calculo e imprimirlo''')

cantidad1 = int(input('Ingrese la primera cantidad: '))
cantidad2 = int(input('Ingrese la segunda cantidad: '))
cantidad3 = int(input('Ingrese la tercera cantidad: '))


def operaciones(cantidad1, cantidad2, cantidad3):
    sumar = cantidad1 + cantidad2 + cantidad3
    return sumar


l = operaciones
operaciones()
print(l)
# pendiente
