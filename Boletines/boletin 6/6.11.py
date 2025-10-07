# 11. Escribir un programa que pregunte por unha mostra de números, separados por comas, os garde nunha
# lista e mostre por pantalla a súa media e desviación típica.


lista_numeros = []

for i in range(5):
    numeros_lista = (int(input('Ingrese un numero: ')))
    lista_numeros.append(numeros_lista)

print(lista_numeros)
suma = sum(lista_numeros)
print(suma)
media = sum(lista_numeros) / len(lista_numeros)

print('La media es: ', media)


for numero in range(len(lista_numeros)):
    resta = (lista_numeros[numero]) - media
    print('La desviacion tipica en: ', lista_numeros[numero], 'es: ', resta)
