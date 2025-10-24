

dia = int(input('ingrese un dia: '))
mes = int(input('ingrese un mes:'))
año = int(input('ingrese un año:'))


if dia < 28:
    print('dia no valido')
elif dia >= 28 and dia <= 31:
    print('dia valido')
else:
    print('dia no valido')

if mes == 1:
    print('enero')
elif mes == 2:
    print('febrero')
elif mes == 3:
    print('marzo')
elif mes == 4:
    print('abril')
elif mes == 5:
    print('mayo')
elif mes == 6:
    print('junio')
elif mes == 7:
    print('julio')
elif mes == 8:
    print('agosto')
elif mes == 9:
    print('septiembre')
elif mes == 10:
    print('octubre')
elif mes == 11:
    print('noviembre')
elif mes == 12:
    print('dicembre')
elif mes > 12:
    print('mes no valido')

if año <= 0 and año >= 3000:
    print('no te pases')
else:
    print('año valido')


if año % 4 == 0:
    print('es año bisiesto')
elif año % 4 % 100 == 0:
    print('es año bisiesto')
elif año % 100 % 400 == 0:
    print('es año bisiesto')
else:
    print('es un año normal')
