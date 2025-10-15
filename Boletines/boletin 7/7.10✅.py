# 10. Tenta escribir un método, que dado un obxecto da clase str conte diferentes tipos de caracteres.
# En particular, o método deberá imprimir o número de letras,
# díxitos e espazos en branco da cadea.
# Tenta facer un programa que escriba o cálculo da cadea: «Ola, son alumno de DAM1, e son programador desde o 2025».
'''
texto = 'Ola, son alumno de DAM1, e son programador desde o 2025'
for i in range(len(texto)):
    print(texto[i])
'''
texto = 'Ola, son alumno de DAM1, e son programador desde o 2025'
texto = texto.lower()

l = '1234567890'

l2 = 'bcdfghjklmnpqrstvwxyz'
l3 = 'aeiou'
l4 = '.,_-!"·$%&/()'

contador_num = 0
contador_nom = 0
contador_vocales = 0
contador_sig = 0

for i in texto:
    if i in l:
        contador_num += 1
    if i in l2:
        contador_nom += 1
    if i in l3:
        contador_vocales += 1
    if i in l4:
        contador_sig += 1

print(contador_sig)
print(contador_vocales)
print(contador_nom)
print(contador_num)
