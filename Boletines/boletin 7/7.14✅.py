# Escribir unha función que reciba unha cadea que conten un número entero longo e devolte unha cadea co número
# e as separacións de miles. Por exemplo, se recibe 1234567890, debe devoltar 1.234.567.890.

numero = '1234567890'
lista = list(numero)
print(lista)
nueva = ''

for n in lista:
    nueva = nueva+n
    if n in lista[::3]:
        nueva = nueva + '.'

print(nueva)
