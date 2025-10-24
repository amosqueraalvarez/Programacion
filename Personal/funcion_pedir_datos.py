

def pedir_datos():
    dia = str(input('Introduzca un dia: '))
    mes = str(input('ingrese un mes:'))
    año = str(input('ingrese un año:'))
    return dia, mes, año


dia, mes, año = pedir_datos()
formato = str(dia+'/'+mes+'/'+año)
print(formato)


def verificar_datos():
    if formato == 10:
        print('correcto')
    else:
        print('error')


verificar_datos()
