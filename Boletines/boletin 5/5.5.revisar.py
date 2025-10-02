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