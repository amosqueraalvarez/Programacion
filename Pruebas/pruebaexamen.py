'''
cadea = 'esto es una prueba de un texto'
vocales = 'aeiou'
for i in cadea:
    if i == i in vocales:
        cadea = cadea.replace(i, ',')
        print(i)
print(cadea)

n = int(input('Ingrese un numerico: '))
factorial = 1
for i in range(n+1):
    if i > 0:
        factorial = factorial*i
print(factorial)



def quitar_espacios(cadea):
    inicio = 0
    final = len(cadea)
    espacios_inicio = 0
    espacios_final = 0
    while inicio < final and cadea[inicio] == ' ':
        inicio += 1
        espacios_inicio += 1
    while final > inicio and cadea[final - 1] == ' ':
        final -= 1
        espacios_final += 1
    return cadea[inicio:final], 'se quitaron espacios de inicio', espacios_inicio, 'se quitaron espacios del final', espacios_final


limpiar = quitar_espacios(
    '  esto es una cadena con espacios en las esquinas    ')
print(limpiar)

diccionario = {'nombre': 'Adrian',
               'edad': '33',
               'estudia': 'dam'}

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

for titulo, dato in diccionario.items():
    if titulo == 'nombre':
        print(titulo)
    if dato == 'Adrian':
        print(dato)
    else:
        print(titulo)

for i in range(8):
    if i == 3:
        continue
    if i == 5:
        continue
    print(i)

compras = ['melocotones', 'peras', 'manzanas', 'queso']
for cosa in compras:
    if cosa == 'queso':
        compras.remove(cosa)
print(compras)
'''

numero = float(input('Ingrese un numero : '))

raiz = numero ** 0.5
print(raiz)
raiz_entera = round(raiz)
print(raiz_entera)
resto = numero - (raiz_entera ** 2)
print(resto)
