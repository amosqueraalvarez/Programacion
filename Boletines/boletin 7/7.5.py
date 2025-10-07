# 5. Conta as vocais e as consoantes do String “Python Python Python”. Ollo cos espazos!

texto = 'Python Python Python'

print(texto.count('a'))
print(texto.count('e'))
print(texto.count('i'))
print(texto.count('o'))
print(texto.count('u'))

# forma fea

consonantes = 'bcdfghjklmnñpqrstvwxyz'
lista_consonantes = list(consonantes)
print(lista_consonantes)


contador = 0
for letra in lista_consonantes:
    if letra in texto:
        contador += 1

print(contador)

# prueba
