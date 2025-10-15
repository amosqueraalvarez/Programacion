# 9. Calcula a cantidade de números negativos, positivos e ceros que hai nun grupo de 10 números enteiros.

numeros = [0, -3, 7, -3, 5, 0, 2, -3, 0, 20]

contador_negativos = 0
contador_positivos = 0
contador_ceros = 0

for i in numeros:
    if i == 0:
        contador_ceros += 1
    if i < 0:
        contador_negativos += 1
    if i > 0:
        contador_positivos += 1

print('Los numeros positivos son: ', contador_positivos)
print('Los numeros negativos son: ', contador_negativos)
print('Los cero son: ', contador_ceros)
