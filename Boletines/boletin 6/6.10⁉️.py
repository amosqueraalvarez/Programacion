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


producto_matrices = (((matriz1[0][0])*(matriz2[0][0]))+((matriz1[0][1])*(matriz2[1][0]))+((matriz1[0][2])*(matriz2[2][0])))-(
    ((matriz1[1][0])*(matriz2[0][1]))+((matriz1[0][1])*(matriz2[1][0]))+((matriz1[0][2])*(matriz2[2][0])))
