len_dia = 'dd'
len_dia_lista = list(len_dia)
len_mes = 'mm'
len_mes_lista = list(len_mes)
len_año = 'aaaa'
len_año_lista = list(len_año)

formato = 'dd/mm/aaaa'
formato_lista = list(formato)


dia = []
mes = []
año = []


def verificar_formato(dia, mes, año):
    dia = int(input('Introduzca un dia: '))
    mes = int(input('ingrese un mes:'))
    año = int(input('ingrese un año:'))
    formato_lista = (dia + mes + año)
    if formato_lista == len(formato_lista[8]):
        print('Formato valido')
    elif formato_lista != len(formato_lista[8]):
        print('error')
        while len_dia_lista == len(len_dia_lista[2]):
            print('Comprobacion de dato dia correcto')
        if len_dia_lista != (len_dia_lista[2]):
            print('El formato en dia no es correcto, dd.')
            dia = int(input('Introduzca un dia: '))
            return
        elif len_mes_lista == len(len_mes_lista[2]):
            print('Comprobacion de dato mes correcta')
        elif len_mes_lista != len(len_mes_lista[2]):
            print('El formato en mes no es correcto, mm')
            mes = int(input('Introduzca un mes: '))
            return
        elif len_año_lista == len(len_año_lista[4]):
            print('Comprobacion de dato año correcta')
        elif len_año_lista != len(len_año_lista[4]):
            print('El formato en año no es correcto, aaaa')
            año = int(input('Introduzca el año: '))
            return


verificar_formato(dia, mes, año)

'''
def calculo_dia(dia):
    if dia < 28:
        print('dia no valido')
    elif dia >= 28 and dia <= 31:
        print('dia valido')
    else:
        print('dia no valido')


def calcular_mes(mes):
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


def calculo_año(año):
    if año <= 0 and año >= 3000:
        print('no te pases')
    else:
        print('año valido')


def calculo_bisiesto():
    if año % 4 == 0:
        print('es año bisiesto')
    elif año % 4 % 100 == 0:
        print('es año bisiesto')
    elif año % 100 % 400 == 0:
        print('es año bisiesto')
    else:
        print('es un año normal')
'''
