efectivo = [['2', [50, 4], [20, 5], [0.5, 6]],
            ['1', [20, 15], [10, 5], [0.2, 5], [0.1, 4]],
            ['3', [20, 12], [5, 6], [0.02, 5]]]


def mostrarContidoUnhaCaixa(caixa, totalEfectivoCaixas):
    for contidoCaixa in totalEfectivoCaixas:
        if contidoCaixa[0] == caixa:
            print('O contido da ', caixa, 'e:')
            for i in range(1, len(contidoCaixa)):
                if contidoCaixa[i][0] > 2.0:
                    print(contidoCaixa[i][1], 'billetes de ',
                          contidoCaixa[i][0], 'euros')
                else:
                    print(contidoCaixa[i][1], 'moedas de ',
                          contidoCaixa[i][0], 'euros')


mostrarContidoUnhaCaixa('1', efectivo)
