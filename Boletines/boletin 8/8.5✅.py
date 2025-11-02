# 5.Modificar as funcións anteriores para que teñan en conta o xénero do destinatario, para elo,
#  deberán recibir unha tupla de tuplas, contendo o nome e o xénero, adaptando a mensaxe con ‘don’ ou ‘dona’ dependendo deste.

lista_nomes = ['Homes', ['Paco', 'Ramon', 'Jose'],
               'Mulleres', ['Maria', 'Julia', 'Paula']]


def saudoXenero(lista):
    homes = lista[1]
    mulleres = lista[3]
    for i in homes:
        print('Don: ', i)
    for i in mulleres:
        print('Dona: ', i)


saudoXenero(lista_nomes)
