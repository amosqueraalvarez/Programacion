hora_gratis = 2
tarifa_1 = 2
tarifa_2 = 3
extra_hora_2a4 = 4
time = int(input('ingrese un numero:'))


if time <= 2:
    print('no tiene que pagar nada')
elif time > 2 and time <= 4:
    calculo_tiempo = (time - hora_gratis)
    calculo_pago = (calculo_tiempo * tarifa_1)
    print(' el importe a pagar es: ', calculo_pago)
elif time > 4:
    calculo_tiempo_2 = time - 4
    calculo_pago_2 = calculo_tiempo_2 * tarifa_2
    calculo_total = calculo_pago_2 + extra_hora_2a4
    print('el importe total a pagar es: ', calculo_total)
