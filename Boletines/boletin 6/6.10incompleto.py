'''
10. Escribir un programa que almacene as matrices


a =         (1,2,3)                                  b =         (-1,0)
                    (4,5,6)                                        (0,1)
                                                                (1,1)
nunha lista e mostre por pantalla o seu produto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila nunha tupla
'''

matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [-1, 0],
    [0, 1],
    [1, 1]
]

print(matriz1)
print(matriz2)


calculo = sum(x for x in zip(matriz1, matriz2))
print(calculo)
