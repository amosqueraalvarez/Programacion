# Escribir funcións que dada unha cadea de caracteres:
# Devolva soamente as letras consonantes. Por exemplo, se recibe ‘algoritmos’ ou ‘logaritmos’ debe devolver ‘lgrtms’.

lista_consonates = 'bcdfghjklmñnpqrstvwxyz'
texto = 'algoritmos ou logaritmos'
so_consonantes = ''

for char in texto:
    if char in lista_consonates:
        so_consonantes = so_consonantes + char

print(so_consonantes)

# Devolva soamente as letras vogais. Por exemplo, se recibe ‘sen 	consonantes’ debe devoltar ‘e ooae’.

lista_vogais = 'aeiou'
texto1 = 'sen consonantes'
so_vogais = ''

for char in texto1:
    if char in lista_vogais:
        so_vogais = so_vogais + char

print(so_vogais)


# Substitúa cada vogal pola súa seguinte vogal. Por exemplo, se recibe ‘vestiario’ debe devoltar ‘vostoerou’.
