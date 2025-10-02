# 4.Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario


numero = float(input('Ingrese un numero: '))
numero2 = float(input('Ingrese otro numero: '))
diferencia = int(numero - numero2)
print('La diferencia es: ' + str(diferencia))

for i in range(0, diferencia+1, 2):
    if diferencia % 2 == 0:
        print(i)
        i += 1
    else:
        diferencia % 2 != 0
        i += 1
        print(i)

print('No se porque funciona pero funciona')
