# Escribir funcións que dada unha cadea e un caracter:

# Reemplace tódolos espazos polo caracter. Ex: ‘meu arquivo de texto.txt’ e ‘\_’ debería devoltar ‘meu\_arquivo\_de\_texto.txt’

texto = 'meu arquivo de texto.txt'
print(texto.replace(' ', '.'))

# Inserte o caracter entre cada letra da cadea. Ex: ‘separar’ e ‘,’ debería devolver s,e,p,a,r,a,r

texto1 = 'separar'
texto2 = ''
for char in range(len(texto1)):
    texto2 = texto2 + (texto1[char])+(',')
print(texto2)


# Reemplace tódolos díxitos na cadea polo caracter. Ex: súa clave é: 1540 e ‘X’ debería devotar súa clave é: XXXX

texto3 = 'súa clave é: 1540'
print(texto3.replace('1540', 'XXXX'))
numeros = '1234567890'
texto4 = ''

for char in texto3:
    if char in numeros:
        texto4 = texto4 + 'X'
    else:
        texto4 = texto4 + char

print(texto4)

# Inserte o caracter cada 3 díxitos na cadea. Ex. 2552552550 e ‘.’ debería devoltar 255.255.255.0

numeros2 = '2552552550'
numeros3 = numeros2[0:3] + '.' + numeros2[3:6] + \
    '.' + numeros2[6:9]+'.' + numeros2[9:]

print(numeros3)
