# Modificar as funcións anteriores, para que reciban un parámetro que indique a cantidade máxima de reemplazos
#  ou insercións a realizar.

numero = '1234567890'
lista = list(numero)
nueva = ''

for n in lista:
    nueva = nueva+n
    if n in lista[::3]:
        if len(nueva) < 6:
            nueva = nueva + '.'

print(nueva)
