# 6. Escribir un programa que pida o usuario unha palabra e mostre por pantalla si é un palíndromo.


palabra = str(input('Ingrese una palabra: '))
caracteres_lista = list(palabra)
caracteres_lista.append

print(caracteres_lista)

caracteres_lista.reverse()
print(caracteres_lista)

if caracteres_lista == caracteres_lista[::-1]:
    print('La palabra es un palindromo')
else:
    print('No es un palindromo')
