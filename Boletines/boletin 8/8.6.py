# 6.Dada unha lista de números enteiros, escribir unha función que:
# Devolte unha lista con tódolos que sexan primos.
# Devolte o sumatorio e o promedio dos valores.
# Devolte unha lista co factorial de cada un de eses números.


# Devolte o sumatorio e o promedio dos valores.
'''
lista_numeros = [1, 3, 4, 5, 6]
suma = 0
for numero in lista_numeros:
    suma += numero
calculo = suma/(len(lista_numeros))
print(calculo)
'''
# Devolte unha lista co factorial de cada un de eses números.
import math
lista_numeros = [1, 3, 4, 5, 6]
for numero in lista_numeros:
    factorial = math.factorial(numero)
    print(factorial)
