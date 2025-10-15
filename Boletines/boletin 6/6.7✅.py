# 7. Escribir un programa que pida o usuario unha palabra e mostre por pantalla o número de veces que conten cada vogal.


palabra = (str(input('Introducta una palabra: ')))
lista_palabra = list(palabra)


vocales = ['a', 'e', 'i', 'o', 'u']

for indice in range(len(lista_palabra)):
    if lista_palabra[indice] in vocales:
        print('La vocal', lista_palabra[indice], 'esta dentro de la palabra')


contador = 0
for i in range(len(lista_palabra)):
    if lista_palabra[i] in vocales:
        contador += 1
        print('Se suma la letra ', lista_palabra[i])

print(contador)
