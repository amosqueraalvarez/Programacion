
def menu_principal():
    print('''
[1] Superficie de triangulo
[2] Superficie de cuadrado
[3] Superficie del circulo
[4] Salir''')


def pedir_datos(dato):
    dato = (float(input('Ingrese un dato: ')))
    return dato


def calculo_opciones():
    if opcion == 1:
        dato = pedir_datos
        area_triangulo = (dato * dato)/2
        print('El area del triangulo es: ', area_triangulo)
    else:
        if opcion == 2:
            dato = pedir_datos
            area_cuadrado = dato * dato
            print('El area del cuadrado es: ', area_cuadrado)
        else:
            if opcion == 3:
                dato = pedir_datos
                pi = 3.14
                area_circulo = (pi * (dato**2))
                print('El area del circulo es: ', area_circulo)
            else:
                if opcion == 4:
                    print('Hasta otra')
                else:
                    if opcion > 4:
                        print('No es una opcion valida')


menu_principal()
opcion = int(input('Elija una opcion: '))
calculo_opciones()
