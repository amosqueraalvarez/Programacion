# 1.Escribir un ciclo definido para imprimir por pantalla tódolos números entre	10 e 20

t = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

for i in t:
    print(i)


# 2.Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius.
# Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

temperatura = float(input('Ingrese una temperatura en grados Fahrenheit: '))
conversion = (9/5 * temperatura) + 32
print('Su temperatura en Celsius es: ' + str(conversion))


# 3.Utiliza o programa anterior para xerar unha táboa de conversión
# de temperaturas, dende 0º F ata 120º F, de 10 en 10.


temperatura = 0
t = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)

for i in (t):
    conversion = (9/5 * temperatura) + 32
    temperatura += 10
    print(conversion)


# 4.Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario


numero = float(input('Ingrese un numero: '))
numero2 = float(input('Ingrese otro numero: '))
diferencia = int(numero - numero2)
print('La diferencia es: ' + str(diferencia))

for i in range(0, diferencia+1, 2):
    if diferencia % 2 == 0:
        print(i)
        i += 1
    else:
        diferencia % 2 != 0
        i += 1
        print(i)

print('No se porque funciona pero funciona')


# 5.Escribir un programa que reciba un número n por parámetro e imprima os primeiros n números triangulares,
# xunto co seu índice. Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n.
# É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:
'''
n = int(input('Ingrese un numero: '))
n_triangulares = n*(n+1)/2
print(n_triangulares)


 corregir MAL
n = int(input('Ingrese un numero: '))

for i in range(0, n, 1):
    if n != i:
        suma = n + (n-i)
        print(suma)
        i += 1

'''

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
