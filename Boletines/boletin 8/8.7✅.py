# 7.Dada unha lista de números enteiros e un enteiro k, escribir unha función que:
# Devolte tres listas, unha cos menores, outra cos maiores e outra cos iguais a k.
# Devolte unha lista con aqueles que son múltiplos de k.

lista = [3, 5, 7, 8, 10, 14, 20, 2]
numero_k = 7
lista_menores = []
lista_maiores = []
lista_iguais = []
for numero in lista:
    if numero < numero_k:
        lista_menores.append(numero)
    elif numero > numero_k:
        lista_maiores.append(numero)
    elif numero == numero_k:
        lista_iguais.append(numero)

print(lista)
print(lista_iguais)
print(lista_maiores)
print(lista_menores)


# Devolte unha lista con aqueles que son múltiplos de k.
lista_multiplos = []
lista_no_multiplos = []
for numero in lista:
    if numero % numero_k == 0:
        lista_multiplos.append(numero)
    else:
        lista_no_multiplos.append(numero)

print(lista_no_multiplos)
print(lista_multiplos)
