# Escribir unha función que dada unha cadea de caracteres, devolte:
# A primeira letra de cada palabra. Por exemplo, 	si recibe Universal Serial Bus debe devoltar USB.

texto1 = 'Universal Serial Bus'
letras_mayusculas = 'ABCDEFGHIJKLMÑNOPQRSTUVWXYZ'
abreviatura = ''
for char in texto1:
    if char in letras_mayusculas:
        abreviatura = abreviatura + char

print(abreviatura)


# Unha cadea coa primeira letra de cada palabra en maiúsculas. Por exemplo, se recibe república arxentina,
# debe devoltar, República Argentina.
texto = 'republica arxentina'
print(texto.title())

# As palabras que comecen coa letra A. Por exemplo, si recibe Antes de abrir, debe devoltar, Antes abrir.
