# Escribir funcións que dada unha cadena de caracteres:

texto = 'Hola mundo'
# Imprima os dous primeiros caracteres.
print(texto[:2])

# Imprima os tres últimos caracteres.
print(texto[-3:])

# Imprima dita cadea cada dous caracteres. Ex.: recta debería imprimir rca
print('recta'[::2])

# Imprima a cadea nun sentido e en sentido inverso. Ex: reflexo imprime reflexooxelfer.

texto1 = 'reflexo'
texto2 = texto1[::-1]

print(texto1+texto2)
