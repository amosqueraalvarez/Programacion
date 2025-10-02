# 9. Escribir un programa que almacene os vectores (1,2,3) e (-1,0,2) en duas listas e mostre por pantalla o seu producto escalar.

vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

producto_escalar = sum(x*y for x, y in zip(vector1, vector2))

print(producto_escalar)
