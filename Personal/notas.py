suma = 0
for i in range(5):
    notas = int(input('Ingrese un numero: '))
    if notas < 0:
        print('error')
        break
    suma += notas
print(suma/5)
