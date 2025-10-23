# dada unha lista onde hay varias caixas e cada caixa teñen cartos en efectivo
# cada caixa ten os cartos en efectivo e moedas
# eso esta almacenado en unha lista


'''
('caixa2', (500, 1), (200, 2), (100, 1), (50, 4), (20, 8), (10, 2), (5, 30), (2, 15),
 (1, 10), (0.5, 21), (0.2, 2), (0.1, 2), (0.05, 4), (0.02, 21), (0.01, 8)),
('caixa3', (500, 3), (200, 0), (100, 0), (50, 2), (20, 5), (10, 2), (5, 10), (2, 2),
 (1, 5), (0.5, 1), (0.2, 3), (0.1, 13), (0.05, 4), (0.02, 21), (0.01, 51))
'''
lista_cajas = ['1', '2']

efectivo2 = [[500, 1], [200, 1], [100, 1], [50, 2], [20, 10], [10, 20], [5, 2],
             [2, 31], [1, 15], [0.5, 11], [0.2, 22], [0.1, 1], [0.05, 0], [0.02, 21], [0.01, 5]]
efectivo1 = [[500, 0], [200, 0], [100, 2], [50, 5], [20, 10], [10, 20], [5, 20],
             [2, 31], [1, 15], [0.5, 11], [0.2, 22], [0.1, 6], [0.05, 40], [0.02, 2], [0.01, 5]]


total_caja = 0


if lista_cajas[0]:
    print('La caja: ', lista_cajas[0])
    for i, e in efectivo1:
        print('De : ', i, 'hay: ', i*e, 'y hay: ', e, 'de ', i)
        total_caja = total_caja + i*e
if lista_cajas[1]:
    print('La caja: ', lista_cajas[1])
    for i, e in efectivo2:
        print('De : ', i, 'hay: ', i*e, 'y hay: ', e, 'de ', i)
        total_caja = total_caja + i*e


print('El total de la caja es: ', total_caja)
