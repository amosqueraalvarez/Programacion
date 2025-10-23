cajas = [['Caja1', [[10, 2], [5, 1], [1, 2]]],
         ['Caja2', [[10, 1], [5, 31], [1, 5]]],
         ['Caja3', [[10, 11], [5, 3], [1, 22]]]]


def bienvenida():
    print('Bienvenido al supermercado, a continuacion te mostrare las cajas que puedes consultar')
    for caja in cajas:
        nombre_caja = caja[0]
        print('Hoy esta abierta la: ', nombre_caja)


def cuentas_caja(nombre):
    for caja in cajas:
        nombre_caja = caja[0]
        efectivo = caja[1]
        if nombre == nombre_caja:
            print('En la caja ', nombre_caja, 'hay: ')
            total_caja = 0
            for i, u in efectivo:
                total_caja = total_caja + i*u
                print('De:', i, '€', 'una cantidad de:',
                      u, 'y hace un total de:', i*u, '€')
            print('Y tiene un total de: ', total_caja, '€')


def total_cajas():
    total = 0
    for caja in cajas:
        dinero = caja[1]
        for i, u in dinero:
            total += (i*u)
    print('Hay un total de: ', total, '€', 'entre las cajas de hoy')


def total_cajas_recuento():
    total10 = 0
    total5 = 0
    total1 = 0
    for caja in cajas:
        dinero = caja[1]
        for i, u in dinero:
            if i == 10:
                total10 += u
            if i == 5:
                total5 += u
            if i == 1:
                total1 += u
    print('De 10€ hay:', total10, 'De 5€ hay:',
          total5, 'De 1€ hay:', total1, 'entre todas las cajas del supermercado')


total_cajas_recuento()
bienvenida()
cuentas_caja('Caja2')
total_cajas()
